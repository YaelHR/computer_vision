import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import roc_auc_score, average_precision_score
from sklearn.preprocessing import label_binarize
from sklearn.utils.class_weight import compute_class_weight

## Fijar pseudoaleatoriedad
SEED = 42
np.random.seed(SEED)
tf.random.set_seed(SEED)

## =========================
## Cargar dataset
## =========================
df = pd.read_csv(r"C:\Users\ejoji\Downloads\datasets2\Predicción de ingresos por marketing y ventas de comercio electrónico\test.csv")

print("Shape del dataset:", df.shape)
print("Columnas:", df.columns)

## =========================
## Preprocesamiento
## =========================

# Eliminar filas con NaN en la columna target
df = df.dropna(subset=[df.columns[-1]])

# Separar variables (última columna como target)
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# Convertir categóricas si existen
X = pd.get_dummies(X)

# Si tu variable es continua (como ingresos), convertir en clases para clasificación multiclase
# Por ejemplo, en 5 bins iguales
num_classes = 5
y_class = pd.qcut(y, q=num_classes, labels=False)

# Codificar clases
le = LabelEncoder()
y_encoded = le.fit_transform(y_class)
class_names = [f"Clase_{i}" for i in range(len(np.unique(y_encoded)))]

# Convertir a numpy
X = X.values.astype(np.float32)
y_encoded = y_encoded.astype(np.int32)

print("\nClases:", class_names)
print("Shape de X:", X.shape)
print("Shape de y:", y_encoded.shape)

## =========================
## División del dataset
## =========================

X_train, X_temp, y_train, y_temp = train_test_split(
    X, y_encoded,
    test_size=0.3,
    random_state=SEED,
    stratify=y_encoded
)

X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp,
    test_size=0.5,
    random_state=SEED,
    stratify=y_temp
)

print("\nShape del dataset")
print("Train:", X_train.shape, y_train.shape)
print("Val:", X_val.shape, y_val.shape)
print("Test:", X_test.shape, y_test.shape)

## =========================
## Escalado
## =========================

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)
X_test = scaler.transform(X_test)

## =========================
## Class Weights
## =========================

classes = np.unique(y_train)
weights = compute_class_weight(class_weight="balanced", classes=classes, y=y_train)
class_weights = dict(zip(classes, weights))
print("\nClass weights:", class_weights)

## =========================
## Modelo
## =========================

def build_model(input_dim, num_classes):
    inputs = tf.keras.Input(shape=(input_dim,))
    x = tf.keras.layers.Dense(64, activation="relu")(inputs)
    x = tf.keras.layers.Dropout(0.3)(x)
    x = tf.keras.layers.Dense(32, activation="relu")(x)
    x = tf.keras.layers.Dropout(0.2)(x)
    x = tf.keras.layers.Dense(16, activation="relu")(x)
    outputs = tf.keras.layers.Dense(num_classes, activation="softmax")(x)
    return tf.keras.Model(inputs, outputs)

model = build_model(X_train.shape[1], len(class_names))

## =========================
## Compilación
## =========================

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(),
    metrics=["accuracy"]
)

print("\nResumen del modelo")
model.summary()

## =========================
## Callbacks
## =========================

callbacks = [
    tf.keras.callbacks.EarlyStopping(
        monitor="val_loss",
        patience=10,
        restore_best_weights=True
    )
]

## =========================
## Entrenamiento
## =========================

history = model.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),
    epochs=300,
    batch_size=32,
    class_weight=class_weights,
    verbose=1
)

## =========================
## Evaluación TEST
## =========================

test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)

print("\n=== RESULTADOS TEST ===")
print(f"Loss     : {test_loss:.4f}")
print(f"Accuracy : {test_acc:.4f}")

## =========================
## Predicciones
## =========================

y_prob = model.predict(X_test, verbose=0)
y_pred = np.argmax(y_prob, axis=1)

print("\n=== MATRIZ DE CONFUSIÓN ===")
print(confusion_matrix(y_test, y_pred))

print("\n=== REPORTE DE CLASIFICACIÓN ===")
print(classification_report(y_test, y_pred, target_names=class_names))

## =========================
## ROC-AUC y PR-AUC
## =========================

y_test_bin = label_binarize(y_test, classes=np.unique(y_encoded))

roc_auc = roc_auc_score(y_test_bin, y_prob, multi_class="ovr")
pr_auc = average_precision_score(y_test_bin, y_prob)

print("\n=== MÉTRICAS AVANZADAS ===")
print(f"ROC-AUC: {roc_auc:.4f}")
print(f"PR-AUC : {pr_auc:.4f}")

## =========================
## Gráficas
## =========================

plt.figure(figsize=(10, 4))
plt.plot(history.history["loss"], label="Train loss")
plt.plot(history.history["val_loss"], label="Val loss")
plt.title("Evolución de la pérdida")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 4))
plt.plot(history.history["accuracy"], label="Train accuracy")
plt.plot(history.history["val_accuracy"], label="Val accuracy")
plt.title("Evolución de la exactitud")
plt.legend()
plt.grid(True)
plt.show()