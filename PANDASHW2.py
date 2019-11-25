import pandas as pd
x = pd.read_csv('cars.csv')
a = x.loc[:4,['mpg','disp','drat','qsec','am','carb']]
b = x[x['Model']=='Mazda RX4']
c = x.loc[x['Model']=='Camaro Z28',['cyl']]
d = x.loc[[1,28,18],['Model','cyl','gear']]