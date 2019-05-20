from pandas import read_csv
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import sys; sys.path.append('./scripts')
import quality
# previsao com dataset test
# inicialmente não foi possível fazer o treinamento pois  apos a etapa de  one hot encoding
#  as matrizes ficaram de tamanhos diferentes.
# retreinei os modelos apenas com os preditores semelhantes entre os 
# dataframes.
le = LabelEncoder()
scaler = StandardScaler()

df_val = read_csv('./data/call_data_VAL_ML.csv')
df_val['Event Clearance Description'] = le.fit_transform(df_val['Event Clearance Description'])

df = read_csv("./data/call_data_ML.csv")
df['Event Clearance Description'] = le.fit_transform(df['Event Clearance Description'])
classe = df['Event Clearance Description'].values

lista_df =  list(df.columns)
lista_val = list(df_val.columns)
colunas_val = list(filter(lambda x: x in lista_df, lista_val))
colunas_df = list(filter(lambda x: x in lista_val, lista_df))

classe_val = df_val['Event Clearance Description'].values
preditores_val = df_val[colunas_df].drop(columns=['Event Clearance Description'])

preditores = df[colunas_val].drop(columns=['Event Clearance Description'])
preditores = scaler.fit_transform(preditores)

rfc = RandomForestClassifier(n_estimators=100, random_state=100)
rfc.fit(preditores, classe)
quality.validaModelo(df_val, preditores_val.columns,'Event Clearance Description',\
    rfc, scaler, quality.accuracy_score)
#0.7563544568245125

lr = LogisticRegression(solver='newton-cg', multi_class='multinomial')
lr.fit(preditores, classe)
quality.validaModelo(df_val, preditores_val.columns, 'Event Clearance Description',\
   lr, scaler, quality.accuracy_score)
#0.7598798746518106   
