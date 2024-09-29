def hitung_selisih_waktu(jam_mulai, menit_mulai, jam_selesai, menit_selesai):
    # Mengubah jam dan menit mulai dan selesai menjadi total menit
    waktu_mulai = jam_mulai * 60 + menit_mulai
    waktu_selesai = jam_selesai * 60 + menit_selesai
    
    # Menghitung selisih waktu
    selisih_menit = waktu_selesai - waktu_mulai
    
    # Jika waktu selesai lebih kecil dari waktu mulai, berarti waktunya melewati tengah malam
    if selisih_menit < 0:
        selisih_menit += 24 * 60

    # Menghitung jumlah jam dan menit dari selisih waktu
    selisih_jam = selisih_menit // 60
    sisa_menit = selisih_menit % 60
    
    return selisih_jam, sisa_menit


def main():
    while True:
        # Input waktu mulai
        jam_mulai = int(input("Masukkan jam mulai    : "))
        menit_mulai = int(input("Masukkan menit mulai  : "))
        
        # Input waktu selesai
        jam_selesai = int(input("Masukkan jam selesai  : "))
        menit_selesai = int(input("Masukkan menit selesai: "))
        
        # Hitung selisih waktu
        selisih_jam, sisa_menit = hitung_selisih_waktu(jam_mulai, menit_mulai, jam_selesai, menit_selesai)
        
        # Menampilkan hasil
        if selisih_jam == 0:
            print(f"Selisih waktu di antara kedua waktu tersebut adalah {sisa_menit} menit.")
        elif sisa_menit == 0:
            print(f"Selisih waktu di antara kedua waktu tersebut adalah {selisih_jam} jam.")
        else:
            print(f"Selisih waktu di antara kedua waktu tersebut adalah {selisih_jam} jam dan {sisa_menit} menit.")
        
        # Tanya apakah mau melakukan perhitungan lain
        pilihan = input("Apakah anda mau melakukan perhitungan yang lain (Y/T) ? ").lower()
        if pilihan != 'y':
            print("Terima kasih telah menggunakan program saya byee (Programmer)")
            break

# Menjalankan program utama
main()

