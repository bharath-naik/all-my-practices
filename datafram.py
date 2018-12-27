import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

web_stats = {
             'Day':[1,2,3,4,5,6,],
             'visitors':[43,54,56,76,87,63],
             'bounce_Rate':[67,67,89,56,66,72]
             }

df = pd.DataFrame(web_stats)
print(df.set_index('Day'))
print("its completed")
print(df.head())
print("it's head from above")
print(df.tail(2))
print("it is the tail from above")

#print(df['visitors'])
#print(df.visitors)
#print(df.bounce_Rate)
print(np.array(df[['visitors','bounce_Rate']]))
 
