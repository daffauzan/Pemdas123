import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# Hitung peningkatan gaji sebesar 5% untuk setiap karyawan menggunakan loop for dan lambda
for index, row in df.iterrows():
    df.at[index, 'Gaji'] = (lambda x: x + x * 0.05)(row['Gaji'])

# Tampilkan DataFrame yang sudah diperbarui
print("DataFrame setelah peningkatan gaji 5%:")
print(df)

# Berikan peningkatan tambahan sebesar 2% untuk karyawan yang usianya di atas 30
for index, row in df.iterrows():
    if row['Usia'] > 30:
        df.at[index, 'Gaji'] = (lambda x: x + x * 0.02)(row['Gaji'])

# Tampilkan DataFrame yang sudah diperbarui setelah peningkatan gaji tambahan
print("\nDataFrame setelah peningkatan gaji tambahan 2% untuk usia di atas 30:")
print(df)

# Ringkasan hasil
total_peningkatan_5_percent = sum(df['Gaji'] * 0.05)
print("\nRingkasan Perubahan:")
print("Total Karyawan: ", len(df))
print("Total Peningkatan Gaji 5%: ", total_peningkatan_5_percent)



# ---------------------------- #
# Buat Branch Baru pada repository github berikut dengan format KELAS_NRP_NAMA
# https://github.com/diashfirdaus-cyber/Pemdas_Itenas.git
# ---------------------------- #

# Catatan:

# Gunakan loop for dan fungsi lambda untuk mengimplementasikan operasi yang diminta.
# Pastikan untuk menyimpan hasil perubahan pada DataFrame.
# Tampilkan hasil dan ringkasan dengan jelas.
# Jangan lupa untuk menyesuaikan persentase peningkatan gaji sesuai dengan cerita.