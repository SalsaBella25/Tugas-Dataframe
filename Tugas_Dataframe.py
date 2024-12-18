import pandas as pd

#Pengerjaan no 1
df_dataSampahJabar = pd.read_csv('jumlah_produksi_sampah_berdasarkan_kabupatenkota_data.csv')
df_dataSampahJabar

#Pengerjaan no 2
print('jumlah data sampah di tahun 2018')
dataSampah_2018 = 0
for index,row in df_dataSampahJabar.iterrows():
  if(row['tahun']==2018):
    dataSampah_2018 += row['jumlah_produksi_sampah']

df_dataSampahThn2018 = pd.DataFrame({'tahun':'2018','Jumlah Sampah':[dataSampah_2018]})
df_dataSampahThn2018.to_csv('data sampah pada tahun 2018.csv',index=False)
df_dataSampahThn2018.to_excel('data sampah pada tahun 2018.xlsx',index=False)
print(df_dataSampahThn2018)

#Pengerjaan no 3
print('jumlah data sampah pertahun di jawa barat')
datasampahPertahun = {}
for index,row in df_dataSampahJabar.iterrows():
  tahun = row['tahun']
  jumlah = row['jumlah_produksi_sampah']
  if tahun in datasampahPertahun:
    datasampahPertahun[tahun] += jumlah
  else:
    datasampahPertahun[tahun] = 0

df_sampahPertahun = pd.DataFrame(datasampahPertahun.items(),columns=['tahun','total sampah'])
df_sampahPertahun.to_csv('sampah pertahun.csv',index=False)
df_sampahPertahun.to_excel('sampah pertahun.xlsx',index=False)
print(df_sampahPertahun )

#Pengerjaan no 4
print('jumlah data perkota pertahunnya')
sampahPerkota = {}
for index,row in df_dataSampahJabar.iterrows():
  nama_Kota = row['nama_kabupaten_kota']
  tahun = row['tahun']

  if nama_Kota not in sampahPerkota:
    sampahPerkota[nama_Kota]={}
  if tahun not in sampahPerkota[nama_Kota]:
    sampahPerkota[nama_Kota][tahun] = 0
  
  sampahPerkota[nama_Kota][tahun] += row['jumlah_produksi_sampah']

df_JumlahsampahPerkota = pd.DataFrame(sampahPerkota)
df_JumlahsampahPerkota.to_csv('sampah perkota.csv',index=False)
print(sampahPerkota)

