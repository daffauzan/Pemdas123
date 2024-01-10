# Pemdas123

import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

for index, row in df.iterrows():
    df.at[index, 'Gaji'] = (lambda x: x + x * 0.05)(row['Gaji'])

print("DataFrame setelah peningkatan gaji 5%:")
print(df)

for index, row in df.iterrows():
    if row['Usia'] > 30:
        df.at[index, 'Gaji'] = (lambda x: x + x * 0.02)(row['Gaji'])

print("\nDataFrame setelah peningkatan gaji tambahan 2% untuk usia di atas 30:")
print(df)

total_peningkatan_5_percent = sum(df['Gaji'] * 0.05)
print("\nRingkasan Perubahan:")
print("Total Karyawan: ", len(df))
print("Total Peningkatan Gaji 5%: ", total_peningkatan_5_percent)
