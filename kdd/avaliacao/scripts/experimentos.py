from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from pandas import read_csv
from pandas import DataFrame
import sys; sys.path.append('./scripts')
import quality

le = LabelEncoder()
df = read_csv('./data/call_data_ML.csv')
df['Event Clearance Description'] = le.fit_transform(df['Event Clearance Description'])

classe = df['Event Clearance Description'].values
preditores = df.drop(columns=['Event Clearance Description'])

scaler = StandardScaler()
preditores = scaler.fit_transform(preditores)

X_train, X_test, y_train, y_test = train_test_split(preditores,\
   classe, test_size=0.3, random_state=100)

rfc = RandomForestClassifier(n_estimators=100, random_state=100)   
rfc_trained = quality.analise_modelo(rfc, X_train, y_train, X_test, y_test)
#              precision    recall  f1-score   support
#
#           0       0.69      0.77      0.73      3827
#           1       0.95      0.89      0.92      1311
#           2       0.71      0.69      0.70      5068
#           3       0.77      0.56      0.65      2575
#           4       0.91      0.90      0.90       918
#           5       0.84      0.93      0.88     11256
#           6       0.60      0.46      0.52      3037
#
#   micro avg       0.78      0.78      0.78     27992
#   macro avg       0.78      0.74      0.76     27992
#weighted avg       0.77      0.78      0.77     27992
#
#[{'Acuracy Score': 0.7776150328665333},
# {'RMSE': 1.386573122591324}, 
# {'R2': 0.5179588711139703}, 
# {'MAE': 0.5624821377536439}]
#  {'Confusion Matrix': array([
# [ 2963,     2,   575,    11,     6,    64,   206],
# [   11,  1167,    13,     5,     2,    63,    50],
# [  851,     5,  3478,    87,    44,   244,   359],
# [   63,     2,   278,  1438,     8,   735,    51],
# [    8,     2,    46,    13,   823,    18,     8],
# [   26,    10,   233,   249,    17, 10440,   281],
# [  367,    34,   272,    72,     8,   873,  1411]])}] 

fi = quality.featureImportances(rfc_trained,\
df.drop(columns=['Event Clearance Description']).columns)

lr = LogisticRegression(solver='newton-cg', multi_class='multinomial')
lr_trained = quality.analise_modelo(lr, X_train, y_train, X_test, y_test)
#              precision    recall  f1-score   support
#
#           0       0.66      0.86      0.75      3827
#           1       0.95      0.89      0.92      1311
#           2       0.74      0.65      0.69      5068
#           3       0.77      0.62      0.68      2575
#           4       0.91      0.89      0.90       918
#           5       0.86      0.92      0.89     11256
#           6       0.62      0.48      0.54      3037
#
#   micro avg       0.79      0.79      0.79     27992
#   macro avg       0.79      0.76      0.77     27992
#weighted avg       0.78      0.79      0.78     27992
#
# [{'Acuracy Score': 0.7855815947413547}, 
# {'RMSE': 1.3597372524967386}, 
# {'R2': 0.5364372487435647}, 
# {'MAE': 0.5443698199485567}, 
# {'Confusion Matrix': array(
# [[ 3305,     2,   400,     4,     6,    48,    62],
#  [    9,  1172,    14,     6,     1,    50,    59],
#  [ 1109,     5,  3302,    86,    39,   160,   367],
#  [   69,     1,   205,  1585,    10,   643,    62],
#  [   14,     4,    52,    11,   818,    10,     9],
#  [   31,    14,   221,   286,    20, 10337,   347],
#  [  457,    37,   273,    89,     4,   706,  1471]])}]


# validacao cruzada e acuracia dos modelos

valida_rf = quality.KFoldEstratificado(rfc, preditores, classe, 10, quality.accuracy_score)
#[['accuracy_score', 0.7785226433011777],
# ['cross_val_score', 0.7683305920264262]]
valida_lr = quality.KFoldEstratificado(lr, preditores, classe, 10, quality.accuracy_score)
#[['accuracy_score', 0.7847171182312669],
# ['cross_val_score', 0.7832486651217272]]


# GridSearch 
params_rfc = { 
    'n_estimators': [100,200, 500],
    'max_features': ['auto', 'sqrt', 'log2'],
    'max_depth' : [4,5,6,7,8],
    'criterion' :['gini', 'entropy']
}
CV_rfc = GridSearchCV(estimator=rfc, param_grid=params_rfc, cv= 10)
CV_rfc.fit(X_train, y_train)
#best params
#{'criterion': 'entropy',
# 'max_depth': 8,
# 'max_features': 'auto',
# 'n_estimators': 100}

params_lr = {"C":np.logspace(-3,3,7),
 "penalty":["l1","l2"]}
CV_lr = GridSearchCV(estimator=lr, param_grid=params_lr, cv= 10)
CV_lr.fit(X_train, y_train)
#best params
# {'C': 1.0, 'penalty': 'l1'}

# previsao com dataset test
# inicialmente não foi possível fazer o treinamento pois 
# apos o one hot encoding as matrizes ficaram de tamanhos diferentes.
# retreinei os modelos apenas com os preditores semelhantes entre os 
# dataframes.
lista_df =  list(df.columns)
lista_val = list(df_val.columns)
colunas_val = list(filter(lambda x: x in lista_df, lista_val))
colunas_df = list(filter(lambda x: x in lista_val, lista_df))

df_val = read_csv('./data/call_data_VAL_ML.csv')
df_val['Event Clearance Description'] = le.fit_transform(df_val['Event Clearance Description'])
classe_val = df_val['Event Clearance Description'].values
preditores_val = df_val[colunas_df].drop(columns=['Event Clearance Description'])

df = pd.read_csv("./data/call_data_ML.csv")
df['Event Clearance Description'] = le.fit_transform(df['Event Clearance Description'])
classe = df['Event Clearance Description'].values
preditores = df[colunas_val].drop(columns=['Event Clearance Description'])
preditores = scaler.fit_transform(preditores)

rfc = RandomForestClassifier(n_estimators=100, random_state=100)
rfc.fit(preditores, classe)
validaModelo(df_val, preditores_val.columns,'Event Clearance Description',\
    rfc, scaler, quality.accuracy_score)
#0.7563544568245125

lr = LogisticRegression(solver='newton-cg', multi_class='multinomial')
lr.fit(preditores, classe)
validaModelo(df_val, preditores_val, 'Event Clearance Description',\
   lr, scaler, quality.accuracy_score)
#   
