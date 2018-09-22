# Example of code, first code
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.datasets as dts

def get_iris_df():
    ds = dts.load_iris()
    df = pd.DataFrame(ds['data'], columns = ds['feature_names'])
    code_species_map = dict(zip(range(3), ds['target_names']))
    df['species'] = [code_species_map[c] for c in ds['target']]
    return df
df = get_iris_df()
# print(df)

# Making pie chart
sums_by_species = df.groupby('species').sum()
var = 'sepal width (cm)'
sums_by_species[var].plot(kind='pie', fontsize=15)
plt.ylabel(var, horizontalalignment = 'left')
plt.title('Example for: ' + var, fontsize=30)
plt.show()
plt.savefig('iris_pie_chart.jpg')
plt.close()

#page 63

