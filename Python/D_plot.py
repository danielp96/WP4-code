import pandas as pd
import matplotlib.pyplot as plt

var = pd.read_excel("D_ejemplo.xlsx")
print(var)
x = list(var['X values'])
y = list(var['Y values'])

plt.figure(figsize=(10,10))
plt.style.use('seaborn')
plt.scatter(x,y,marker="*",s=100,edgecolors="black",c="yellow")
plt.title("Excel sheet to Scatter Plot")
plt.show()
