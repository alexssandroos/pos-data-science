from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from numpy import logspace
from pandas import read_csv

rfc = RandomForestClassifier()
lr = LogisticRegression()

le = LabelEncoder()
df = read_csv('./data/call_data_ML.csv')
df['Event Clearance Description'] = le.fit_transform(df['Event Clearance Description'])

classe = df['Event Clearance Description'].values
preditores = df.drop(columns=['Event Clearance Description'])

scaler = StandardScaler()
preditores = scaler.fit_transform(preditores)

X_train, X_test, y_train, y_test = train_test_split(preditores,\
   classe, test_size=0.3, random_state=100)


# GridSearch 
params_rfc = { 
    'n_estimators': [100,200, 500],
    'max_features': ['auto', 'sqrt', 'log2'],
    'max_depth' : [4,5,6,7,8],
    'criterion' :['gini', 'entropy']
}
CV_rfc = GridSearchCV(estimator=rfc, param_grid=params_rfc,cv= 10, n_jobs=3)
CV_rfc.fit(X_train, y_train)
#best params
#{'criterion': 'entropy',
# 'max_depth': 8,
# 'max_features': 'auto',
# 'n_estimators': 100}

params_lr = {"C":logspace(-3,3,7),
 "penalty":["l1","l2"]}
CV_lr = GridSearchCV(estimator=lr, param_grid=params_lr, cv= 10, n_jobs=3)
CV_lr.fit(X_train, y_train)
#best params
# {'C': 1.0, 'penalty': 'l1'}