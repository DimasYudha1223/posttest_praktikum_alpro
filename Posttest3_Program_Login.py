print("""Selamat Datang Di Blog IT Unmul Silakan Masukkan Akun Anda Atau Membuat Akun Jika Belum Memiliki
A. Membuat Akun Baru
B. Masuk Ke Akun Yang Sudah Ada
C. Keluar Dari Akun
""")
nama_awal = "dimas"
sandi_awal = "098"
data_akun = []
beranda = str(input("Pilih Pilihan Berikut : "))
maksimal_kesalahan = 3
while maksimal_kesalahan>=1: 
    if beranda == "A" :
        nama_pengguna = input("Silakan Masukkan Nama Akun Anda : ")
        sandi = input("Silakan Masukkan Sandi Akun Anda : ")
        data_akun = [nama_pengguna, sandi]
        print("Daftar Berhasil")
        beranda = str(input("Pilih Pilihan Berikut : "))
    elif beranda == "B" :
        nama_akun = input("Masukkan Nama Pengguna Anda :")
        sandi_akun = input("Masukkan Sandi Anda :")
        if nama_akun == nama_awal or nama_akun == (data_akun[0]):
            if sandi_akun == sandi_awal or sandi_akun == (data_akun[1]):
                print ("Akun Berhasil Masuk")
                print ("Selamat Datang Di Blog Ini")
                print ("Semoga Bermanfaat")
                beranda = str(input("Pilih Pilihan Berikut : "))
            else :
                maksimal_kesalahan -= 1
                print("Masukan Salah, Batas Kesalahan Adalah :", maksimal_kesalahan )
        else :
            maksimal_kesalahan-=1
            print("Masukan Salah, Batas Kesalahan Adalah :", maksimal_kesalahan )
    else :
        beranda == "C"
        print("Sampai Jumpa Lagi Semoga Bermanfaat.....")
        break