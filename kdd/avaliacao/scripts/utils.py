from pandas import concat, get_dummies

def FiltraDataFrame(df, col , setfilter):
  return df.loc[df[col].isin(setfilter)]

def RelacionaColuna(df, colName, col1, col2, operador):
  df[colName] = operador(col1,col2)
  return df

def ColunaTransformada(df, colName, groupby, col, operation ):
  df[colName] = df.groupby(groupby)[col].transform(operation)
  return df

def TrataNA(df, col, use):
  df[col] = df[col].fillna(use)
  return df

def onInterval(vMin, vMax, value):
    if value >= vMin and value <= vMax:
        return 0
    return 1

def setOutlier(df, colName, col):
    iqr = df[colName].quantile(.75) - df[colName].quantile(.25)
    inf_limit = df[colName].quantile(.25) - (iqr*1.5)
    sup_limit = df[colName].quantile(.75) + (iqr*1.5)
    df[col] = df[colName].apply(lambda x: onInterval(inf_limit, sup_limit, x))
    return df

def aplicaFuncao(df, colName, col, function):
  df[colName] = df[col].apply(function)
  return df

def set_onehotencoding(dataframe, coluna, prefixo):
    cols = get_dummies(dataframe[coluna], prefix=prefixo)
    dataframe.drop(columns=[coluna], inplace=True)
    return concat([dataframe,cols],axis=1)  