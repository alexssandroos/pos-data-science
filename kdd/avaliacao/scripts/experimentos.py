from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
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


def rfFeatureImportances(Dataframe, rfInstance, X_train_columns):
   feature_importance = Dataframe(rfInstance.feature_importances_,\
      index = X_train_columns, columns=['importance'])\
         .sort_values('importance', ascending=False)
   return feature_importance   

fi = rfFeatureImportances(DataFrame, rfc_trained,\
df.drop(columns=['Event Clearance Description']).columns)

svm = SVC(gamma='scale')
svm_trained = quality.analise_modelo(svm, X_train, y_train, X_test, y_test)