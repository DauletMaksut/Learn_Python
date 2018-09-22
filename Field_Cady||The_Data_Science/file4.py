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
colors = ["r", "g", "b"]
markers = [".", "*", "^"]
fig, ax = plt.subplots(1, 1)
for i, spec in enumerate(df['species'].unique()):
    dff = df[df['species'] == spec]
    dff.plot(kind='scatter', x="sepal width (cm)", y = "sepal length (cm)", 
            alpha = .5, ax = ax, s = 50, color = colors[i],
            marker = markers[i], label = spec)
plt.legend()
plt.show()