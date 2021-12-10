import pandas as pd

df = pd.DataFrame({'first_name':['Jason','Alice'], 'last_name':['Houston','Cooper'], 'age':[29, 21], 'gender':['male',
         'female'], 'hobby':['video games', 'None'], 'job':['None', 'sofware engineer']})


df.to_excel('./status.xlsx', sheet_name='first_name', index=False)








