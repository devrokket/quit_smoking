import pandas
import numba

data = {'col1':[1,2,3,4],'col2':[3,7,5,6]}
idx = ['row1','row2','row3','row4']
df = pd.DataFrame(data = data, index = idx)
print(df)