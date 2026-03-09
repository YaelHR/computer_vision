import numpy as np
import tensorflow as tf

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.utils.class_weight import compute_class_weight
from sklearn.metrics import roc_auc_score, average_precision_score
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt

#para saber si tenemos CPU y GPU
print(tf.config.list_physical_devices())

#Para tener siempre una misma semilla de aleatoriedad
SEED = 42
np.random.seed(SEED)
tf.random.set_seed(SEED)

#Cargar el dataset
data = load_breast_cancer()
X = data.data.astype(np.float32)
y = (data.target == 0).astype(np.int32)

# Division de mi dataset
X_train, X_temp, y_train, y_temp = train_test_split(
    X,y,
    test_size=0.3,
    stratify=y,
    random_state=SEED)

X_val,  X_test, y_val, y_test = train_test_split(
    X_temp,y_temp,
    test_size=0.5,
    stratify=y_temp,
    random_state=SEED)

#Scaling
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_val_s = scaler.transform(X_val)
X_test_s = scaler.transform(X_test)

#Balance de clases
classes = np.array([0, 1])
cw = compute_class_weight(class_weight="balanced", classes=classes, y=y_train)
class_weight = {0:float(cw[0]), 1: float(cw[1])}

#Modelo
def build_model(input_dim):
  inputs = tf.keras.Input(
      shape=(input_dim,))
  x = tf.keras.layers.Dense(64,
      activation="relu",
      kernel_regularizer=tf.keras.regularizers.l2(1e-4)
      )(inputs)
  x = tf.keras.layers.Dropout(0.25)(x)
  x = tf.keras.layers.Dense(32, activation="relu",
      kernel_regularizer=tf.keras.regularizers.l2(1e-3))(x)
  x = tf.keras.layers.Dropout(0.20)(x)
  outputs = tf.keras.layers.Dense(1, activation="sigmoid")(x)
  return tf.keras.Model(inputs, outputs)

model = build_model(X_train_s.shape[1])

#Metricas
metrics = [
    tf.keras.metrics.AUC(curve="ROC", name="auc_roc"),
    tf.keras.metrics.AUC(curve="PR", name="auc_pr"),
    tf.keras.metrics.Recall(name="Recall"),
    tf.keras.metrics.Precision(name="Precision"),
]

#Compilar modelo
lr=1e-3
model.compile(
    optimizer=tf.optimizers.Adam(lr),
    loss="binary_crossentropy",
    metrics=metrics
)

#CallBacks - EarlyStopping
callbacks = [
    tf.keras.callbacks.EarlyStopping(
        monitor="val_auc_roc",
        mode="max",
        patience=20,
        restore_best_weights=True)
]

history=model.fit(
    X_train_s, y_train,
    validation_data=(X_val_s, y_val),
    epochs=300,
    batch_size = 32,
    class_weight=class_weight,
    verbose=1,
    callbacks=callbacks,
    )

#Graficar
plt.figure()
plt.plot(history.history["loss"])
plt.plot(history.history["val_loss"])
plt.title("Perdida")
plt.legend(["Train", "validation"])
plt.show()

#Evaluacion con datos de testing
testing_data_results = model.evaluate(X_test_s, y_test, verbose=1)
print(testing_data_results)

#Eleccion del umbral
y_est_prob = model.predict(X_test_s).ravel()
y_est_bin = (y_est_prob>=0.5).astype(int)

#Matriz de confusion
print(classification_report(y_test, y_est_bin))
confusion_matrix_table = confusion_matrix(y_test, y_est_bin)
print(confusion_matrix_table)