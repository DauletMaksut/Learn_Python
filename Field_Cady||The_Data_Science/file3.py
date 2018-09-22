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
rgb = (0.1, .1, .1)
for spec in df['species'].unique():
    for_spec = df[df['species'] == spec]
    for_spec['petal length (cm)'].plot(kind='hist', alpha=0.6,subplots=True, label = spec, edgecolor='black', color=rgb )
    tmp = list(rgb)
    tmp[0] += .3
    rgb = tuple(tmp)
plt.legend(loc='upper right')
plt.suptitle('Should be overlapping')
plt.savefig('iris_hist_1.jpg')

