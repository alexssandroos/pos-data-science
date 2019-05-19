from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from pandas import read_csv
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
quality.analise_modelo(rfc, X_train, y_train, X_test, y_test)

