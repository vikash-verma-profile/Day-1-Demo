import pandas as pd
import time

start = time.time()
df = pd.read_csv('hw_200.csv')
print(df.shape)
print("Full load time:", time.time() - start)
