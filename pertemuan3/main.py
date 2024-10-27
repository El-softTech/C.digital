
nama = input("Nama Mahasiswa: ")
uts = float(input("Nilai UTS (30%): "))
ujian_akhir = float(input("Nilai Ujian Akhir (40%): "))
tugas = float(input("Nilai Tugas (20%): "))
pertemuan_hadir = int(input("Jumlah Pertemuan yang Dihadiri (maksimal 14): "))


presensi = (pertemuan_hadir / 14) * 100


nilai_akhir = (uts * 0.3) + (ujian_akhir * 0.4) + (tugas * 0.2) + (presensi * 0.1)


if nilai_akhir >= 85:
  grade = "A"
elif nilai_akhir >= 70:
  grade = "B"
elif nilai_akhir >= 55:
  grade = "C"
elif nilai_akhir >= 40:
  grade = "D"
else:
  grade = "E"


print("\n--- Hasil Perhitungan ---")
print("Nama Mahasiswa:", nama)
print("Nilai Akhir:", nilai_akhir)
print("Grade:", grade)