# Memanggil File Gempa dan Import Semua Method/Fungsi
from Gempa import * 
# Membuat objek gempa argumen 
gempa1 = Gempa("banten", 1.2)


# Informasi Gempa 
print('## Info Gempa maseh ##')
print()
gempa1.dampak()

gempa2 = Gempa("palu", 6.1)
print('## Info Gempa maseh ##')
print()
gempa2.dampak()

gempa3 = Gempa("cianjur", 5.1)
print(' ada berita gempa nih bree ')
print()
gempa3.dampak()

gempa4 = Gempa("jayapura", 3.3)
print('## ada berita gempa nih bree ##')
print()
gempa4.dampak()

gempa5 = Gempa("Garut", 3.3)
print('## ada berita gempa nih bree ##')
print()
gempa5.dampak()

