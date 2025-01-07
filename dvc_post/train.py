import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Cargar el dataset
data = pd.read_csv('data/dataset.csv')

# Separar las características y el target
X = data[['income', 'credit_score', 'loan_amount']]
y = data['approved']

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar un modelo
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluar el modelo
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

# Guardar el modelo
import joblib
joblib.dump(model, 'model.pkl')

# Guardar las métricas
with open('metrics.json', 'w') as f:
    f.write(f'{{"accuracy": {accuracy}}}')

