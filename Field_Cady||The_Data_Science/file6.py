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
df.plot(kind="hexbin", x="sepal width (cm)", y="sepal length (cm)")
plt.show()
