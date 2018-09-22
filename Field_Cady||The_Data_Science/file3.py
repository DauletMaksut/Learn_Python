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
for spec in df['species'].unique():
    for_spec = df[df['species'] == spec]
    for_spec['petal length (cm)'].plot(kind='hist', alpha=0.8,subplots=True, label = spec)
plt.legend(loc='upper right')
plt.suptitle('Should be overlapping')
plt.savefig('iris_hist_1.jpg')
# df.plot(kind='hist', subplots=True, layout=(2,2))
# plt.suptitle('Histogram for iris data')
# plt.show()

