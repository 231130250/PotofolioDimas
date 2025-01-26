import random

nama_user = input("Masukkan nama anda: ")

print("=" * 100)
print(f"Selamat Datang di Goa Berhantu {nama_user}")
print("=" * 100)

gosth_position = random.randint(1, 5)

while True:
    print('''
    Tugas anda adalah memilih salah satu dari ke 5 goa ini manakah goa yang terdapat hantu nya
    Apakah goa 
    |_| |_| |_| |_| |_| 
    1/  2/  3/  4/  5 ?
    ''')
    pilihan = int(input("Masukkan pilihan anda: "))

    if pilihan == gosth_position:
        print(f"Selamat, Anda telah memilih goa yang terdapat hantu nya!")
        print(f"Pilihan Anda: Goa ke {pilihan}")
        print(f"Posisi hantu: Goa ke {gosth_position}")
        break
    else:
        print(f"Maaf, Anda telah memilih goa yang tidak terdapat hantu nya")
        print(f"Pilihan Anda: Goa ke {pilihan}")
        print(f"Posisi hantu: Goa ke {gosth_position}")
        jawaban = input("Apakah anda ingin memilih lagi? (y/n): ")
        if jawaban.lower() == "y":
            continue 
        elif jawaban.lower() == "n":
            print("Terima kasih telah bermain!")
            break