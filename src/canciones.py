import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf 

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import roc_auc_score, average_precision_score
from sklearn.preprocessing import label_binarize

## Fijar pseudoaleatoriedad
SEED = 42
np.random.seed(SEED)
tf.random.set_seed(SEED)

## =========================
## Cargar dataset
## =========================
df = pd.read_csv(r"C:\Users\ejoji\Downloads\datasets2\canciones\songs_normalize.csv")

print("\n=== DATASET INFO ===")
print(df.info())
print(df.head())

## =========================
## Preprocesamiento
## =========================

# Eliminar columnas no útiles
df = df.drop(columns=["song", "artist"])

# Variable objetivo
target_col = "genre"

y = df[target_col]
X = df.drop(columns=[target_col])

# Codificar etiquetas
le = LabelEncoder()
y = le.fit_transform(y)

# One-hot encoding variables categóricas
X = pd.get_dummies(X)

# Convertir a numpy
X = X.values.astype("float32")
y = y.astype("int32")

## 🔴 ELIMINAR CLASES RARAS
counts = pd.Series(y).value_counts()
valid_classes = counts[counts > 1].index

mask = np.isin(y, valid_classes)
X = X[mask]
y = y[mask]

print("\nClases después de limpieza:", len(np.unique(y)))

## =========================
## División del dataset
## =========================

# ✔️ PRIMER SPLIT (con stratify)
X_train, X_temp, y_train, y_temp = train_test_split(
    X, y,
    test_size=0.3,
    random_state=SEED,
    stratify=y
)

# ✔️ SEGUNDO SPLIT (SIN stratify)
X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp,
    test_size=0.5,
    random_state=SEED,
    stratify=None
)

print("\n=== SHAPES ===")
print("Train:", X_train.shape, y_train.shape)
print("Val:", X_val.shape, y_val.shape)
print("Test:", X_test.shape, y_test.shape)

## =========================
## Escalamiento
## =========================
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)
X_test = scaler.transform(X_test)

## =========================
## Construcción del modelo
## =========================

def build_model(input_dim, num_classes):

    inputs = tf.keras.Input(shape=(input_dim,))
    
    x = tf.keras.layers.Dense(
        32, activation="relu",
        kernel_regularizer=tf.keras.regularizers.l2(1e-4)
    )(inputs)
    x = tf.keras.layers.Dropout(0.2)(x)

    x = tf.keras.layers.Dense(
        16, activation="relu",
        kernel_regularizer=tf.keras.regularizers.l2(1e-4)
    )(x)
    x = tf.keras.layers.Dropout(0.2)(x)

    x = tf.keras.layers.Dense(8, activation="relu")(x)

    outputs = tf.keras.layers.Dense(
        num_classes,
        activation="softmax"
    )(x)

    return tf.keras.Model(inputs, outputs)

num_classes = len(np.unique(y))
model = build_model(X_train.shape[1], num_classes)

## =========================
## Compilación
## =========================

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(),
    metrics=["accuracy"]
)

print("\n=== RESUMEN DEL MODELO ===")
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
    callbacks=callbacks,
    verbose=1
)

## =========================
## Evaluación
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
print(classification_report(y_test, y_pred))

## =========================
## ROC-AUC y PR-AUC
## =========================

y_test_bin = label_binarize(y_test, classes=range(num_classes))

roc_auc = roc_auc_score(y_test_bin, y_prob, multi_class="ovr")
print("\nROC-AUC:", roc_auc)

pr_auc = average_precision_score(y_test_bin, y_prob)
print("PR-AUC:", pr_auc)

## =========================
## Ejemplos
## =========================

print("\n=== EJEMPLOS ===")
for i in range(min(5, len(X_test))):
    print(f"Muestra {i+1}:")
    print(f"  Clase real     : {y_test[i]}")
    print(f"  Clase predicha : {y_pred[i]}")
    print(f"  Probabilidades : {y_prob[i]}")
    print()

## =========================
## Gráficas
## =========================

plt.figure(figsize=(10,4))
plt.plot(history.history["loss"], label="Train loss")
plt.plot(history.history["val_loss"], label="Val loss")
plt.title("Evolución de la pérdida")
plt.xlabel("Época")
plt.ylabel("Loss")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10,4))
plt.plot(history.history["accuracy"], label="Train acc")
plt.plot(history.history["val_accuracy"], label="Val acc")
plt.title("Evolución del accuracy")
plt.xlabel("Época")
plt.ylabel("Accuracy")
plt.legend()
plt.grid(True)
plt.show()

