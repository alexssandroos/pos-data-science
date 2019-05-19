from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
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

lr = LogisticRegression(solver='lbfgs', multi_class='multinomial')
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

