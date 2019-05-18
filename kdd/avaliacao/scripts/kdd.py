from pandas import read_csv
import matplotlib.pyplot as plt
import seaborn as sns
import sys; sys.path.append('./scripts')
import utils
from pandas import Timestamp


flatui = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]
sns.color_palette(flatui)
plt.style.use('tableau-colorblind10')  
#pd.options.display.float_format = '{:,.2f}'.format


df = read_csv('./data/train_call_data_v1.csv', 
              usecols=[2,3,4,5,6,7,8,9,10,11],
              parse_dates=['Original Time Queued', 'Arrived Time'])

df.dropna(inplace=True)

plt.title("Classe")
sns.countplot(y='Event Clearance Description',data=df)

df['Event Clearance Description'].value_counts()/len(df)*100

# Existe um desbalanceamento das classes, onde das 7 possíveis
# classes 40% estão relacionadas ao relatorio escrito sem crime.

# Regioes West e North somam mais de 55% das ocorrencias
df['Precinct'].value_counts()/len(df)*100
plt.title("Registros por area")
sns.countplot(y='Precinct',data=df)

plt.title("Registros por tipo de ligação")
sns.countplot(y='Call Type',data=df)

# Apenas 5% dos registros foram corretamente tipados
df[df['Final Call Type']== df['Initial Call Type']].info()

df.pipe(utils.aplicaFuncao,'MonthOfOriginal',\
  'Original Time Queued', lambda x: Timestamp(x).month)\
  .pipe(utils.aplicaFuncao,'DayOfOriginal',\
  'Original Time Queued', lambda x: Timestamp(x).day)\
  .pipe(utils.aplicaFuncao,'DayWeekOfOriginal',\
  'Original Time Queued', lambda x: Timestamp(x).dayofweek)\
  .pipe(utils.aplicaFuncao,'HourOfOriginal',\
  'Original Time Queued', lambda x: Timestamp(x).hour)  

#Quase não há registros para os meses de janeiro e maio
# dezembro possui menos de 50% da média dos meses restantes.
df['MonthOfOriginal'].value_counts()

#sabado é o dia com menor incidencia de ocorrencias
df['DayWeekOfOriginal'].value_counts()

#ocorrencias estao concentradas em horarios acima das 8 da manha
df['HourOfOriginal'].value_counts()

cols_to_ohe = ['Call Type', 'Priority','Initial Call Type',\
   'Final Call Type', 'Precinct', 'Sector', 'Beat']

for col in cols_to_ohe:
    df = utils.set_onehotencoding(dataframe=df, coluna=col, prefixo=col)
cols_to_remove = [ 'Original Time Queued','Arrived Time']

df.drop(columns=cols_to_remove, inplace=True)

corr = df.corr()
sns.heatmap(corr, 
            xticklabels=corr.columns.values,
            yticklabels=corr.columns.values)

df.to_csv('./data/call_data_ML.csv', index=False)            