input_ulang_data = "y"
while input_ulang_data == "y":
    print("==========>>>Data Mahasiswa<<<==========") 
    print(" ")
    nama=str(input("Tulis Nama Lengkap Mahasiswa : ")) 
    umur=int(input("Tulis Umur Mahasiswa Saat ini (Bentuk Angka) : "))
    fakultas=str(input("Tulis Asal Fakultas : "))
    nim=int(input("Tulis Nim Mahawsiswa (Contoh:210606060) : "))
    ipk=float(input("Tulis IPK Mahasiswa (Contoh: 3.0) : "))

    Data=[] 
    Data.append(nama)
    Data.append(umur)
    Data.append(fakultas)
    Data.append(nim)
    Data.append(ipk)
    print(" ")
    print("=======>>>Data Mahasiswa<<<=======") 
    print(" ")
    print(f"Nama) :          {Data[0]} ")
    print(f"Umur) :          {Data[1]} Tahun ")
    print(f"Fakultas) :      {Data[2]} ")
    print(f"Nim) :           {Data[3]} ")
    print(f"IPK) :           {Data[4]} ")
    print(" ")
    input_ulang_data = str(input("Isi Lagi? (y/t) : "))
print("Terima Kasih Sudah Mengisi Data")