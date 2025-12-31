import pandas as pd
import numpy as np

df_laptops = pd.read_csv('dataset/laptop_price.csv')

conditions = [
    df_laptops['Price_euros']> 3000,
    (df_laptops['Price_euros']> 2000) & (df_laptops['Price_euros']<= 3000),
    (df_laptops['Price_euros']> 800) & (df_laptops['Price_euros']<= 2000),
    df_laptops['Price_euros']<= 800
]

values = ['Very Expensive', 'Expensive', 'Affordable', 'Cheap']
df_laptops['level_price'] = np.select(conditions, values, default='Unknown')

print("Primeras 10 filas:")
print(df_laptops[['Price_euros', 'level_price']].head(10))
print("\nÚltimas 5 filas:")
print(df_laptops[['Price_euros', 'level_price']].tail(5))
print("\nValores únicos:")
print(df_laptops['level_price'].unique())

