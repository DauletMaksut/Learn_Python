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
sums_by_species[var].plot(kind='bar', fontsize=15, rot=20)
plt.title('Sepal width', fontsize=15)
# plt.show()
plt.savefig('iris_bar_1.jpg')
plt.close()
sums_by_species = df.groupby('species').sum()
sums_by_species.plot(kind='bar', subplots=True, fontsize=12)
plt.suptitle("Worked lol")
# plt.show()
plt.savefig('iris_bar_2.jpg')
plt.close()
#page 63

