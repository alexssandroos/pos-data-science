import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score
from sklearn.metrics import homogeneity_score
from sklearn.metrics import v_measure_score
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
import seaborn as sns
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'scripts'))
    print(os.getcwd())
except:
    pass


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


df = pd.read_csv('../data/customers.csv')

df.drop(columns=['Channel', 'Region'], inplace=True)

df.pipe(setOutlier, 'Fresh', 'outFresh')\
    .pipe(setOutlier, 'Milk', 'outMilk')\
    .pipe(setOutlier, 'Grocery', 'outGrocery')\
    .pipe(setOutlier, 'Frozen', 'outFrozen')\
    .pipe(setOutlier, 'Delicatessen', 'outDelicatessen')\
    .pipe(setOutlier, 'Detergents_Paper', 'outDetergents_Paper')  

outliers_columns = df.columns[df.columns.str.startswith('out')].values
df['out_total'] = df[outliers_columns].sum(axis=1)
df.drop(df[df['out_total'] > 3].index, inplace=True)
df.drop(columns=df.columns[df.columns.str.startswith('out')].values, inplace=True)


scaler = MinMaxScaler()
X = scaler.fit_transform(X=df.values)

kmean = KMeans(n_clusters=5, random_state=0)
kmean.fit(X)


pca = PCA(n_components=2)
components = pca.fit_transform(X)


# plot
# https://nikkimarinsek.com/blog/7-ways-to-label-a-cluster-plot-python

plt.rc('font', size=16)
sns.set_style('white')
customPalette = ['#630C3A', '#39C8C6', '#D3500C', '#FFB139']
sns.set_palette(customPalette)
sns.palplot(customPalette)

df_plot = pd.DataFrame(components, columns=['x', 'y'])
df_plot['classe'] = kmean.labels_
sns.lmplot(data=df_plot, x='x', y='y', hue='classe',
           fit_reg=False, legend=True, legend_out=True)


# Otimizaçao de K
distortions = []
K = range(1,10)
for k in K:
    kmeanModel = KMeans(n_clusters=k).fit(X)
    kmeanModel.fit(X)
    distortions.append(sum(np.min(cdist(X, kmeanModel.cluster_centers_, 'euclidean'), axis=1)) / X.shape[0])

# Plot the elbow
plt.plot(K, distortions, 'bx-')
plt.xlabel('k')
plt.ylabel('Distortion')
plt.title('O gráfico roxeda pro K otimizado')
plt.show()


dbScan = DBSCAN(min_samples=10, algorithm='kd_tree',
                metric='manhattan')
dbScan.fit(X)
dbScan.labels_


print('silhouette_score', silhouette_score(X=X, labels=kmean.labels_))
print('homogeneity_score', homogeneity_score(kmean.labels_, dbScan.labels_))
print('v_measure_score',v_measure_score(kmean.labels_, dbScan.labels_))


# https://www.kaggle.com/typewind/draw-a-radar-chart-with-python-in-a-simple-way

df_labels = df.columns.values
df_stats = df[387:388].values

angles = np.linspace(0, 2*np.pi, len(df_labels), endpoint=False)

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.plot(angles, df_stats[0], 'o-', linewidth=2)
ax.fill(angles, df_stats[0], alpha=0.25)
ax.set_thetagrids(angles * 180/np.pi, df_labels)
ax.set_title('Cliente 398')
ax.grid(True)
