from pandas import read_csv
from pandas import Timestamp
import sys; sys.path.append('./scripts')
import utils


df = read_csv('./data/test_call_data.csv', 
              usecols=[2,3,4,5,6,7,8,9,10,11],
              parse_dates=['Original Time Queued', 'Arrived Time'])

df.dropna(inplace=True)

df.pipe(utils.aplicaFuncao,'MonthOfOriginal',\
  'Original Time Queued', lambda x: Timestamp(x).month)\
  .pipe(utils.aplicaFuncao,'DayOfOriginal',\
  'Original Time Queued', lambda x: Timestamp(x).day)\
  .pipe(utils.aplicaFuncao,'DayWeekOfOriginal',\
  'Original Time Queued', lambda x: Timestamp(x).dayofweek)\
  .pipe(utils.aplicaFuncao,'HourOfOriginal',\
  'Original Time Queued', lambda x: Timestamp(x).hour)  

cols_to_ohe = ['Call Type', 'Priority','Initial Call Type',\
   'Final Call Type', 'Precinct', 'Sector', 'Beat']

for col in cols_to_ohe:
    df = utils.set_onehotencoding(dataframe=df, coluna=col, prefixo=col)
cols_to_remove = [ 'Original Time Queued','Arrived Time']

df.drop(columns=cols_to_remove, inplace=True)

df.to_csv('./data/call_data_VAL_ML.csv', index=False)    