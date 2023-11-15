import pandas as pd

data_thread={'District':['Belagavi','Bagalkot','Vijaypura','Kalburgi','Bidar'],
             'Cities Towns Urban':[31,17,15,11,7],
             'Inhabited Villages':[1263,613,679,871,595],
             'Un-Inhabited':[12,11,13,47,25],
             'Total Villages':[1275,624,692,918,620],
             }
df=pd.DataFrame(data_thread)
df.scale=0.2
df.offset=2.0
df.info()
print(df.columns)
print(df.describe())