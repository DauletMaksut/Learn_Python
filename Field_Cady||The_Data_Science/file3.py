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

# Calculate mean, stdev, median and quatiles

col = df['petal length (cm)']
print("Average is:", col.mean())
print("StandDev is:", col.std())
print("Median is:", col.quantile(.5))
print("q.25 is:", col.quantile(.25))
print("q.75 is:", col.quantile(.75))
print("Number of data is:", len(col))
print()

# delete upper .75 and lower .25 in quantile
p_25 = col.quantile(.25)
p_75 = col.quantile(.75)
col = col[(col>p_25)&(col<p_75)]
print("Average is:", col.mean())
print("StandDev is:", col.std())
print("Median is:", col.quantile(.5))
print("q.25 is:", col.quantile(.25))
print("q.75 is:", col.quantile(.75))
print("Number of data is:", len(col))
print()

p_25 = col.quantile(.25)
p_75 = col.quantile(.75)
col = col[(col>p_25)&(col<p_75)]
print("Average is:", col.mean())
print("StandDev is:", col.std())
print("Median is:", col.quantile(.5))
print("q.25 is:", col.quantile(.25))
print("q.75 is:", col.quantile(.75))
print("Number of data is:", len(col))
print()

