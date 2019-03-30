import pandas as pd
url = "wine.data"
wine = pd.read_csv(url, names = ["Cultivator", "Alchol", "Malic_Acid", "Ash", "Alcalinity_of_Ash", "Magnesium", "Total_phenols", "Falvanoids", "Nonflavanoid_phenols", "Proanthocyanins", "Color_intensity", "Hue", "OD280", "Proline"])
wine.head()
wine.describe().transpose()
wine.shape
X = wine.drop('Cultivator',axis=1)
y = wine['Cultivator']
from sklearn.model_selection import train_test_split
#dados para treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y)
#padronizacao dos dados
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
StandardScaler(copy=True, with_mean=True, with_std=True)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
#Escolher um classificador
from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(hidden_layer_sizes=(13,13,13),max_iter=500)
mlp.fit(X_train,y_train)
import pickle
pickle.dump(mlp,open('modelo_mlp.sav','wb'))
predictions = mlp.predict(X_test)
from sklearn.metrics import classification_report,confusion_matrix
print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))
