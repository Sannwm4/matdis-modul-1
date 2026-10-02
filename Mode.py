# Pilihan Mode-XOR

mode_pesawat = True
mode_gaming = True

# Model logika
mode = mode_pesawat ^ mode_gaming 

# Output hasil seleksi
if mode:
    print("Mode pesawat/Mode gaming akif") 
else:
    print("kedua mode tidak aktif") 

