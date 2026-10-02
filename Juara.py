# Juara Umum-AND

keaktifan = False
nilai_tinggi = True
perasyaratan = False
pengalaman = True
sertifikat = True

# Model logika
Juara = keaktifan and nilai_tinggi and perasyaratan 
Uang = pengalaman and sertifikat

# Output hasil seleksi
if Juara:
    print("Peserta juara 1 Nasional") 
else:
    print("Peserta gagal meraih juara") 

if Uang:
    print("Peserta mendapat uang 10 juta")
else: 
   print("Peserta tidak mendapat uang")