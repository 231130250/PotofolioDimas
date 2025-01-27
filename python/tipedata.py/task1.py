import random

print("=" * 50)
print(f"   ======Selamat Datang di Goa Berhantu======")
print("=" * 50)

nama_user = input("Masukkan nama anda: ")

gosth_position = random.randint(1, 5)

while True:
    print(f''' Halo {nama_user}
    Tugas anda adalah memilih salah satu dari ke 5 goa ini manakah goa yang terdapat hantu nya
    Apakah goa 
    |_| |_| |_| |_| |_| 
     1   2   3   4  5 ?
    ''')
    pilihan = int(input("Masukkan pilihan anda: "))
    jawaban = input("apakah anda sudah yakin dengan jawaban anda (y/n)? : ")
    if jawaban.lower() == "y" :
        if pilihan == gosth_position:
            print(f"Selamat, Anda telah memilih goa yang terdapat hantu nya!")
            print(f"Pilihan Anda: Goa ke {pilihan}")
            print(f"Posisi hantu: Goa ke {gosth_position}")
            break
        else:
            print(f"Maaf, Anda telah memilih goa yang tidak terdapat hantu nya")
            print(f"Pilihan Anda: Goa ke {pilihan}")
            print(f"Posisi hantu: Goa ke {gosth_position}")
            jawaban1 = input("Apakah anda ingin memilih lagi? (y/n): ")
            if jawaban1.lower() == "y":
                continue 
            elif jawaban1.lower() == "n":
                print("Terima kasih telah bermain!")
            break
    elif jawaban.lower() == "n":
        jawaban2 = input("Apakah anda ingin memilih lagi? (y/n): ")
        if jawaban2.lower() == "y":
            continue
        elif jawaban2.lower() == "n":
            print("Terima kasih telah bermain!")
        else: 
            print("Maaf, jawaban anda tidak valid. Silakan masukkan jawaban yang benar")
    else: 
        print("Maaf, jawaban anda tidak valid. Silakan masukkan jawaban yang benar")
    