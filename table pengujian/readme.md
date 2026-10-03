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

## 4. Pilihan Transportasi - OR

| Bus | Kereta | Ojek | Hasil |
|---|---|---|---|
| False | False | False | TRANSPORTASI TIDAK TERSEDIA |
| True | False | False | TRANSPORTASI TERSEDIA |
| False | True | False | TRANSPORTASI TERSEDIA |
| False | False | True | TRANSPORTASI TERSEDIA |
| True | True | False | TRANSPORTASI TERSEDIA |

## 5. Juara Umum - AND

| Keaktifan | Nilai Tinggi | Persyaratan | Pengalaman | Sertifikat | Hasil |
|---|---|---|---|---|---|
| False | False | False | MEDIA PENYIMPANAN TIDAK TERSEDIA |
| True | False | False | MEDIA PENYIMPANAN TERSEDIA |
| False | True | False | MEDIA PENYIMPANAN TERSEDIA |
| False | False | True | MEDIA PENYIMPANAN TERSEDIA |
| True | True | False | MEDIA PENYIMPANAN TERSEDIA |

## 6. Mode Kipas - XOR

| Level 1 | Level 2 | Level 3 | Hasil |
|---|---|---|---|
| False | False | True | Kipas Dapat Menyala |
| True | False | True | Kipas Dapat Menyala |
| False | True | false | Kipas Dapat Menyala |
| True | True | True | Kipas Tidak Dapat Menyala |

## 7. Mode Kehadiran - XOR

| Hadir Online | Hadir Offline | Hasil |
|---|---|---|
| False | False | MODE KEHADIRAN TIDAK VALID |
| True | False | MODE KEHADIRAN VALID |
| False | True | MODE KEHADIRAN VALID |
| True | True | MODE KEHADIRAN TIDAK VALID |

## 8. Jenis Keanggotaan - XOR

| Anggota Reguler | Anggota Premium | Hasil |
|---|---|---|
| False | False | KEANGGOTAAN TIDAK VALID |
| True | False | KEANGGOTAAN VALID |
| False | True | KEANGGOTAAN VALID |
| True | True | KEANGGOTAAN TIDAK VALID |
