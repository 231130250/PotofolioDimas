print("="*45)
print("===Selamat datang Di Kalkulator saya===")
print("="*45)

print('''Pilih Opsi yang ingin kamu lakukan: 
      1. Tambah 
      2. Kurang 
      3. Kali
      4. Bagi''')
pilihan = input("Masukkan pilihan kamu (1/2/3/4): ")
if pilihan == "1":
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))
    rumus = angka1 + angka2
    print(f"Hasil dari {angka1} + {angka2} = {rumus}")
elif pilihan == "2":
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))
    rumus = angka1 - angka2
    print(f"Hasil dari {angka1} - {angka2} = {rumus}")
elif pilihan == 3:
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))
    rumus = angka1 * angka2
    print(f"Hasil dari {angka1} * {angka2} = {rumus}")
elif pilihan == 4:
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))
    if angka2 != 0:
        print("tidak bisa di bagi dengan 0")
    rumus = angka1 / angka2
    print(f"Hasil dari {angka1} / {angka2} = {rumus}")
else:
    print("silahkna masukkan angka yang sesuai")
    
