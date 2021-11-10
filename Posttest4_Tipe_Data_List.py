import string
import random


def id_menu(size=6, chars=string.ascii_uppercase + string.digits):
  return ''.join(random.choice(chars) for _ in range(size))

menu_yang_tersedia = [
  [id_menu(), "Gorengan Tempe", 2000, "jenis_makanan"],
  [id_menu(), "Burger", 10000, "jenis_makanan"],
  [id_menu(), "Nasi Goreng", 15000, "jenis_makanan"],
  [id_menu(), "Kopi Original", 5000, "jenis_minuman"],
  [id_menu(), "Kopi Boba", 8000, "jenis_minuman"],
]

def print_pilihan_menu():
  print("""
1. Menu
2. Menambah Menu
3. Mengubah Menu
4. Menghapus Menu
5. Keluar dari menu
""")




def print_pilihan():
  makanan = []
  minuman = []
  for menu_kafe in menu_yang_tersedia:
    if menu_kafe[3] == "jenis_makanan":
      makanan.append(menu_kafe)
    else:
      minuman.append(menu_kafe)
  print("""
Menu Makanan
""")
  for index, jenis_makanan in enumerate(makanan):
    print(f"{index + 1}. [{jenis_makanan[0]}] {jenis_makanan[1]} - Rp. {jenis_makanan[2]}")
  print("""
\nMenu Minuman
""")
  for index, jenis_minuman in enumerate(minuman):
    print(f"{index + 1}. [{jenis_minuman[0]}] {jenis_minuman[1]} - Rp. {jenis_minuman[2]}")
  input()


def cari_menu_pesananan(menu, id):
  return next((menu for menu in menu if menu[0] == id), None)

def simpan_menu(menu, data, is_append=True):
  if is_append:
    menu.append(data)
  else:
    midpoint = len(menu)//2 
    menu.insert(midpoint, data)
  return menu

def menghapus_menu(menu, id):
  menu_kafe = cari_menu_pesananan(menu, id)
  if menu_kafe != None:
    if menu_kafe[3] == "makanan":
      del menu_kafe
    else:
      menu.remove(menu_kafe)


def dapatkan_makanan(info):
  print(f"""
{info}
1. Makanan
2. Minuman
  """)
  choice = input("Silakan Pilih : ")
  return choice == "1"
  

# MAIN
choice = "0"
while choice != "5":
  print_pilihan_menu()
  choice = input("Silakan Ingin Memilih Apa: ")
  if choice == "1":
    print_pilihan()
  elif choice == "2":
    menu_makanan = dapatkan_makanan("Silakan Menambahkan")
    jenis_menu = "jenis_makanan" if menu_makanan else "jenis_minuman"
    id_dari_menu = id_menu()
    nama_menu = input("\nTentukan Nama Menu : ")
    harga_menu = input("Tentukan Harganya : ")
    menu_baru = [id_dari_menu, nama_menu, int(harga_menu), jenis_menu]
    menu_append =  input("Apa Anda Ingin Menampatkan Menu Di Tengah (y/n) : ") == "n"
    simpan_menu(menu_yang_tersedia, menu_baru, menu_append)
    print("Menu Baru Berhasil Dimasukkan")
    input()

  elif choice == "3":
    id = input("Input ID Dari Menu : ")
    menu_baru = cari_menu_pesananan(menu_yang_tersedia, id)
    if menu_baru != None:
      print(f"""
ID Menu: {menu_baru[0]}
Nama Menu: {menu_baru[1]}
Harga: Rp. {menu_baru[2]}\n""")
      menu_baru[1] = input("Tetukan Nama Menu Baru : ")
      menu_baru[2] = input("Tentukan Harga Menu Baru : ")
      print("Menu Berhasil Diubah")
    else:
      print("Menu Tidak Ditemukan Silakan Cek Ulang")
    input()

  elif choice == "4":
    id = input("Input ID Menu Yang Ingin Dipilih : ")
    menu_baru = cari_menu_pesananan(menu_yang_tersedia, id)
    if menu_baru != None:
      print(f"""
ID Menu: {menu_baru[0]}
Nama Menu: {menu_baru[1]}
Harga Menu: Rp. {menu_baru[2]}\n""")
      menu_confirmed = input("Anda Yakin Ingin Menghapus Menu Ini? (y/n) : ") == "y"
      if menu_confirmed:
        menghapus_menu(menu_yang_tersedia, id)
        print("Menu Telah Dihapus")
    else:
      print("Menu Tidak Ada Silakan Pilh Lagi")
    input()
  else:
    print("Terima Kasih Atas Kunjungannya Datang Lagi Ya.....")
    exit()