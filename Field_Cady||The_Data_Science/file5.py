import pandas as pd
import sklearn.datasets as ds
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
bs = ds.load_boston()
df = pd.DataFrame( bs.data, columns = bs.feature_names)
df['MEDV'] = bs.target

df.plot(x='CRIM', y='MEDV', kind='scatter', logx=True)
plt.title('Boston example')
plt.show()
plt.close()