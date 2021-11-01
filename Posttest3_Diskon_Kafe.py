import datetime
pesan_lagi="y"
while pesan_lagi=="y":
    print("""
    A. Gorengan Tempe : Rp 2.000
    B. Burger         : Rp 10.000
    C. Nasi Goreng    : Rp 15.000
    D. Kopi Original  : Rp 5.000
    E. Kopi Boba      : Rp 8.000
    """)
    menu=str(input("Silakan Pilih Menu Yang Tersedia ="))
    jumlah_makanan=int(input("Jumlah Makanan ="))
    if menu == "a":
        nama_menu = "Gorengan Tempe"
        harga_menu = 2000
        diskon_menu = 10 if jumlah_makanan >= 3 else 0
        total_harga_menu = (harga_menu*jumlah_makanan)
    elif menu == "b":
        nama_menu = "Burger"
        harga_menu = 10000
        diskon_menu = 10 if jumlah_makanan >= 3 else 0
        total_harga_menu = (harga_menu*jumlah_makanan)
    elif menu == "c":
        nama_menu = "Nasi Goreng"
        harga_menu = 15000
        diskon_menu = 10 if jumlah_makanan >= 3 else 0
        total_harga_menu = (harga_menu*jumlah_makanan)
    elif menu == "d":
        nama_menu = "Kopi Original"
        harga_menu = 5000
        diskon_menu = 5 if jumlah_makanan >= 2 else 0
        total_harga_menu = (harga_menu*jumlah_makanan)
    elif menu == "e":
        nama_menu = "Kopi Boba"
        harga_menu = 8000
        diskon_menu = 5 if jumlah_makanan >= 2 else 0
        total_harga_menu = (harga_menu*jumlah_makanan)
    else:
        nama_menu = " "
        harga_menu = " "
        diskon_menu = " "
        total_harga_menu = " "
        pesan_lagi = input("Menu Yang Dipilih Sedang Kosong Silakan Pilih Yang Lain y/t =")
    pilihan_pembayaran = input("Pembayaran Dengan Kartu ATM Bukan Tabungan Daerah? (y/n)")
    diskon_pelanggan = 5 if pilihan_pembayaran == "y" else 0
    diskon_sesuai_hari = 10 if datetime.datetime.today().weekday() < 5 else 5
    diskon_keseluruhan = diskon_menu + diskon_pelanggan + diskon_pelanggan
    harga_akhir = total_harga_menu - (diskon_keseluruhan * total_harga_menu / 100)
    print("Menu :",nama_menu)
    print("Jumlah Pesan :", jumlah_makanan)
    print("Harga :", harga_menu)
    print("Diskon :", diskon_keseluruhan)
    print("Jumlah Bayar :", harga_akhir)
    pesan_lagi = input("Ada Lagi Yang Ingin Dipesan? y/t =")