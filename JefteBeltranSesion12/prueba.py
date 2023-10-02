
import pandas as pd

data = pd.read_csv('Sesion12/auto-mpg.csv')
print(data)
print(data['horsepower'].mean())
print(data['horsepower'].sum())




import  matplotlib.pyplot as plt
plt.figure()
plt.hist(data['horsepower'])
plt.show()





