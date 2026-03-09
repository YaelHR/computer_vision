import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.utils.class_weight import compute_class_weight
from sklearn.metrics import (
    roc_auc_score,
    average_precision_score,
    confusion_matrix,
    classification_report,
    roc_curve,
    precision_recall_curve
)

print(tf.config.list_physical_devices())

seed = 42
np.random.seed(seed)
tf.random.set_seed(seed)

# ================================
# Cargar dataset
# ================================

df = pd.read_csv(
r"C:\Users\ejoji\Downloads\Datasets\Potabilidad de agua\water_potability.csv"
)

# ================================
# Manejo de valores faltantes
# ================================

df = df.fillna(df.mean())

# separar variables
X = df.drop(columns=["Potability"]).values.astype(np.float32)
y = df["Potability"].values.astype(np.int32)

print(np.bincount(y))

# ================================
# Split 70 / 15 / 15
# ================================

X_train, X_temp, y_train, y_temp = train_test_split(
    X,y,
    test_size=0.30,
    stratify=y,
    random_state=seed
)

X_val, X_test, y_val, y_test = train_test_split(
    X_temp,y_temp,
    test_size=0.50,
    stratify=y_temp,
    random_state=seed
)

# ================================
# Escalamiento
# ================================

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)
X_test = scaler.transform(X_test)

# ================================
# Balanceo de clases
# ================================

classes = np.array([0,1])

weights = compute_class_weight(
    class_weight="balanced",
    classes=classes,
    y=y_train
)

class_weight = {0:float(weights[0]),1:float(weights[1])}

# ================================
# Modelo MLP
# ================================

def create_model(input_dim):

    inputs = tf.keras.Input(shape=(input_dim,))

    x = tf.keras.layers.Dense(
        64,
        activation="relu",
        kernel_regularizer=tf.keras.regularizers.l2(1e-4)
    )(inputs)

    x = tf.keras.layers.Dropout(0.25)(x)

    x = tf.keras.layers.Dense(
        32,
        activation="relu",
        kernel_regularizer=tf.keras.regularizers.l2(1e-4)
    )(x)

    x = tf.keras.layers.Dropout(0.20)(x)

    outputs = tf.keras.layers.Dense(1,activation="sigmoid")(x)

    return tf.keras.Model(inputs,outputs)

model = create_model(X_train.shape[1])

metrics = [
    tf.keras.metrics.AUC(curve="ROC",name="auc_roc"),
    tf.keras.metrics.AUC(curve="PR",name="auc_pr"),
    tf.keras.metrics.Recall(name="recall"),
    tf.keras.metrics.Precision(name="precision")
]

model.compile(
    optimizer=tf.keras.optimizers.Adam(1e-3),
    loss="binary_crossentropy",
    metrics=metrics
)

callbacks = [
    tf.keras.callbacks.EarlyStopping(
        monitor="val_auc_roc",
        mode="max",
        patience=20,
        restore_best_weights=True
    )
]

# ================================
# Entrenamiento
# ================================

history = model.fit(
    X_train,
    y_train,
    validation_data=(X_val,y_val),
    epochs=300,
    batch_size=32,
    class_weight=class_weight,
    callbacks=callbacks,
    verbose=1
)

# ================================
# Evaluación TEST
# ================================

pred_test = model.predict(X_test).ravel()

auc_roc = roc_auc_score(y_test,pred_test)
auc_pr = average_precision_score(y_test,pred_test)

print("AUC ROC:",auc_roc)
print("AUC PR:",auc_pr)

# ================================
# Análisis de threshold
# ================================

thresholds = np.linspace(0.05,0.95,50)

def evaluate_threshold(t):

    y_pred = (pred_test>=t).astype(int)

    cm = confusion_matrix(y_test,y_pred)

    tn,fp,fn,tp = cm.ravel()

    recall = tp/(tp+fn+1e-12)
    precision = tp/(tp+fp+1e-12)

    return cm,precision,recall

target_recall = 0.90

best_threshold = 0.5
best_precision = -1

for t in thresholds:

    cm,precision,recall = evaluate_threshold(t)

    if recall>=target_recall and precision>best_precision:

        best_precision = precision
        best_threshold = t

cm,precision,recall = evaluate_threshold(best_threshold)

print("Best threshold:",best_threshold)
print("Confusion Matrix:\n",cm)

y_pred = (pred_test>=best_threshold).astype(int)

print(classification_report(y_test,y_pred))