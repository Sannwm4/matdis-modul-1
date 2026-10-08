# TABEL PENGUJIAN

Tabel pengujian digunakan untuk menguji setiap studi kasus dengan beberapa kombinasi kondisi True dan False.

## 1. Orang Sakit - AND

| Istirahat | Minum Obat| Healing | Hasil |
|---|---|---|---|
| True | True | True | Orangnya Akan Sembuh |
| False | True | True | Orangnya Tidak Akan Sembuh |
| True | False | True | Orangnya Tidak Akan Sembuh |
| False | False | False | Orangnya Tidak Akan Sembuh|

## 2. Motor Rusak - AND

| Bensin | Ban | Mesin | Hasil |
|---|---|---|---|
| True | True | True | Motor Dapat Menyala Dan Berjalan |
| False | True | True | Motor Tidak Dapat Menyala Dan Berjalan |
| True | True | False | Motor Tidak Dapat Menyala Dan Berjalan|
| False | False | False | Motor Tidak Dapat Menyala Dan Berjalan |

## 3. Alaram Kemanan - OR

| Pintu | Jendela | Pintu Loteng | Hasil |
|---|---|---|---|
| False | False | False | Alaram Keamanan Tidak Aktif |
| True | False | False | Alaram Keamanan Aktif |
| False | True | False | Alaram Keamanan Aktif |
| False | False | True | Alaram Keamanan Aktif |

## 4. Pilihan Mode - XOR

| Mode Pesawat | Mode Gaming | Hasil |
|---|---|---|
| False | False | Kedua Mode Tidak Aktif |
| True | False | Mode Pesawat/Mode Gaming Aktif |
| False | True | Mode Pesawat/Mode Gaming Aktif |
| True | True | Kedua Mode Tidak Aktif  |

## 5. Juara Umum - AND

| Keaktifan | Nilai Tinggi | Persyaratan | Pengalaman | Sertifikat | Hasil |
|---|---|---|---|---|---|
| False | False | False | False | False | Peserta Gagal Meraih Juara, Peserta Tidak Mendapat Uang |
| True | False | False | True | True | Peserta Gagal Juara, Peserta Mendapat Uang 10 Juta |
| True| True | True | False | True | Peserta Juara 1 Nasional, Peserta Tidak Mendapat Uang |
| False | False | True | True | True | Peserta Gagal Meraih Juara, Peserta Mendapat Uang 10 Juta |
| True | True | True | True | True | Peserta Juara 1 Nasional, Peserta Mendapat Uang 10 Juta |

## 6. Mode Kipas - XOR

| Level 1 | Level 2 | Level 3 | Hasil |
|---|---|---|---|
| False | False | True | Kipas Dapat Menyala |
| True | False | True | Kipas Dapat Menyala |
| False | True | false | Kipas Dapat Menyala |
| True | True | True | Kipas Tidak Dapat Menyala |

## 7. Lampu Otomatis - AND

| Saklar A | Saklar B | Saklar C | Hasil |
|---|---|---|---|
| False | False | True | Lampu Otomatis Tidak Menyala |
| True | False | True | Lampu Otomatis Tidak Menyala |
| False | True | False | Lampu Otomatis Tidak Menyala |
| True | True | True | Lampu Otomatis Menyala |

## 8. Seleksi Ujian - AND

| Saklar A | Saklar B | Saklar C | Hasil |
|---|---|---|---|
| False | False | True | Lampu Otomatis Tidak Menyala |
| True | False | True | Lampu Otomatis Tidak Menyala |
| False | True | False | Lampu Otomatis Tidak Menyala |
| True | True | True | Lampu Otomatis Menyala |
