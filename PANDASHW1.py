import pandas as pd
x = pd.read_csv('cars.csv')
y = pd.DataFrame(x, index=[0,1,2,3,4,5,27,28,29,30,31])