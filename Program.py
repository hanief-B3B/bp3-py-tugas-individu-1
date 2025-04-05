# Tugas Individu

from datetime import date

nama = input("Masukkan nama Anda: ")
tahun_lahir = int(input("Masukkan tahun lahir Anda: "))

tahun_sekarang = date.today().year

umur = tahun_sekarang - tahun_lahir

print(f"Hai! {nama}, umur Anda sekarang adalah {umur} tahun.")
