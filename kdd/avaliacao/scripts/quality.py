from sklearn.metrics import confusion_matrix, accuracy_score, f1_score
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score
from numpy import sqrt , mean 


def analise_modelo(model_instance, x_train, y_train, x_test, y_test):
  model_instance.fit(x_train, y_train)
  y_pred = model_instance.predict(x_test)
  results = []
  results.append({"Acuracy Score": accuracy_score(y_test, y_pred)})
  results.append({"RMSE": sqrt(mean_squared_error(y_test, y_pred))})
  results.append({"R2": r2_score(y_test, y_pred)})
  results.append({"MAE": mean_absolute_error(y_test, y_pred)})
  #results.append({"Confusion Matrix": confusion_matrix(y_test, y_pred)})
  #results.append({"F1 Score": f1_score(y_test, y_pred)})
  #results.append({"AUC ROC": roc_auc_score(y_test, y_pred)})
  #print(classification_report(y_test, y_pred))
  print(results)
  return model_instance

def KFoldEstratificado(Modelo, Previsores, Classe, Folds, Metrica):
  stratifiedFolds = StratifiedKFold(n_splits=Folds, shuffle=True, random_state=100) 
  score_cruzado = cross_val_score( Modelo, Previsores, Classe, cv=Folds)
  results = []
  for index_train, index_test in stratifiedFolds.split(Previsores, Classe, Classe):
      Modelo.fit(Previsores[index_train], Classe[index_train])
      predict = Modelo.predict(Previsores[index_test])
      metric = Metrica(Classe[index_test], predict)
      results.append(metric)
  return [[Metrica.__name__ , mean(results) ], [cross_val_score.__name__, mean(score_cruzado)]]

def validaModelo(df, X_cols, Y_col, Modelo, Scaler, Metrica):
  X = Scaler.fit_transform(df[X_cols])
  y = df[Y_col].values
  y_predict = Modelo.predict(X)
  return Metrica(y, y_predict)  