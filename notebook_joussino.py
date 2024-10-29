import pandas as pd 
import numpy as np
df=pd.read_csv('donnees.csv', header =96)
df2=df.disc_facility
df2
mask=(df2=="Xinglong Station")
print(mask.value_counts())
