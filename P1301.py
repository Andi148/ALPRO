

# Data barang
data_barang = [
    {"ID": "E01", "Nama": "Laptop", "Spesifikasi": "Lenovo ThinkPad X1", "Stok": 10, "Satuan": "Unit", "Harga": 15000000},
    {"ID": "E02", "Nama": "Handphone", "Spesifikasi": "Samsung Galaxy S21", "Stok": 15, "Satuan": "Unit", "Harga": 10000000},
    {"ID": "E03", "Nama": "Kamera", "Spesifikasi": "Canon EOS 5D Mark IV", "Stok": 7, "Satuan": "Unit", "Harga": 50000000},
    {"ID": "E04", "Nama": "Printer", "Spesifikasi": "Epson L3150", "Stok": 20, "Satuan": "Unit", "Harga": 3000000},
    {"ID": "E05", "Nama": "Televisi", "Spesifikasi": "LG OLED55C1PUB", "Stok": 5, "Satuan": "Unit", "Harga": 15000000},
    {"ID": "E06", "Nama": "Speaker", "Spesifikasi": "JBL Flip 5", "Stok": 25, "Satuan": "Unit", "Harga": 2000000},
    {"ID": "E07", "Nama": "Mouse", "Spesifikasi": "Logitech MX Master 3", "Stok": 30, "Satuan": "Unit", "Harga": 1500000},
    {"ID": "E08", "Nama": "Keyboard", "Spesifikasi": "Razer BlackWidow V3 Pro", "Stok": 20, "Satuan": "Unit", "Harga": 3000000},
    {"ID": "E09", "Nama": "Charger", "Spesifikasi": "Anker PowerPort III Nano", "Stok": 50, "Satuan": "Unit", "Harga": 300000},
    {"ID": "E10", "Nama": "Headset", "Spesifikasi": "Sony WH-1000XM4", "Stok": 15, "Satuan": "Unit", "Harga": 4000000},
    {"ID": "E11", "Nama": "Webcam", "Spesifikasi": "Logitech C922 Pro", "Stok": 10, "Satuan": "Unit", "Harga": 1500000},
    {"ID": "E12", "Nama": "Flashdisk", "Spesifikasi": "Sandisk Ultra Flair 64GB", "Stok": 40, "Satuan": "Unit", "Harga": 200000},
    {"ID": "E13", "Nama": "SSD", "Spesifikasi": "Kingston A2000 NVMe PCIe M.2 1TB", "Stok": 15, "Satuan": "Unit", "Harga": 2000000},
    {"ID": "E14", "Nama": "HDD", "Spesifikasi": "Seagate BarraCuda 2TB", "Stok": 10, "Satuan": "Unit", "Harga": 1000000},
    {"ID": "E15", "Nama": "RAM", "Spesifikasi": "Corsair Vengeance LPX 16GB DDR4", "Stok": 20, "Satuan": "Unit", "Harga": 1000000}
    
    # Tambahkan data lainnya sesuai kebutuhan
]

# nama_pss = [
#     {"Nama": "Andi", "pss":"sononamidawo123"}
# ]


total_pembelian = 0

# Menampilakan Tabel barang

def tampilkan_data():
    print("{:<8} {:<15} {:<37} {:<13} {:<13} {:<8}".format("ID","Merek", "Tipe", "Stok", "Satuan", "Harga"))
    for barang in data_barang:
        print("{:<8} {:<15} {:<37} {:<13} {:<13} {:<8}".format(barang["ID"], barang["Nama"], barang["Spesifikasi"], barang["Stok"], barang["Satuan"], barang["Harga"]))
        
        # Fungsi untuk membeli barang dan mencetak total pembelian
def beli_barang(id):
    global total_pembelian
    for barang in data_barang:
        if barang['ID'] == id and barang['Stok'] > 0 and jlbarang <= barang["Stok"]:
            barang["Stok"] -= jlbarang
            total_pembelian += jlbarang*barang["Harga"]
            print(f'Anda telah membeli {barang["Nama"]} dengan harga {barang["Harga"]*jlbarang}')
            return
    print("Barang tidak tersedia")
    developer(id)

        
# fungsi start bertugas untuk meminta input dari pengguna apakah mereka adalah developer atau pembeli.
def start():
    user_type = input("Anda developer atau pembeli? (1. Developer) (2. Pembeli)")
    if user_type == "1":
        developer()
    elif user_type == "2":
        pembeli()
    else:
        print("Maaf, pilihan tidak valid. Silakan masukkan 1 untuk Developer atau 2 untuk Pembeli.")
        start()

def pembeli():
    # Tambahkan fungsi untuk pembeli di sini
    pass

def developer():
    # Contoh data pengguna
    nama_pss = [
        {"Nama": "zidan", "pss": "123"},
        {"Nama": "andi", "pss": "sononamidawo123"}
    # Tambahkan data pengguna lainnya sesuai kebutuhan
]
    id = input("Masukkan Nama: ")
    pss = input("Masukkan Password: ")
    for nm in nama_pss:
        if nm['Nama'] == id and nm['pss'] == pss:
            print('Login berhasil')
            developer_3()
            break
    else:
        print('Maaf Nama atau Password salah')
        developer()

def developer_3():
    dv = input('Anda mau re-stok atau menambahkan barang? (1. Re-stok) (2. Tambah barang) (3. Check Data)')
    if dv == "2":
        developer_2()
    elif dv == "1":
        st = input("Masukkan ID barang yang ingin di Re-stok:   ")
        developer_4(st)
    elif dv == "3":
        tampilkan_data()
        developer_3()

def developer_2():
    print('Isi hal yang dibutuhkan')
    barang_baru = {}
    barang_baru["ID"] = input("Masukkan ID barang: ")
    barang_baru["Nama"] = input("Masukkan Nama: ")
    barang_baru["Spesifikasi"] = input("Masukkan Spesifikasi barang: ")
    barang_baru["Stok"] = int(input("Masukkan Stok barang: "))
    barang_baru["Satuan"] = input("Masukkan Satuan barang: ")
    barang_baru["Harga"] = int(input("Masukkan Harga barang: "))
    
    # Menambahkan barang baru ke data_barang
    data_barang.append(barang_baru)
    print('Produk baru sudah di tambahkan')

# fungsi re stok
def developer_4(st):
    for barang in data_barang:
        if barang["ID"] == st:
            print(f'Masukkan jumlah stok yang ingin ditambah ke {barang["Nama"]} dengan Spesifikasi {barang["Spesifikasi"]}')
            jls = int(input())
            barang["Stok"] += jls
            print(f'Stok {barang["Nama"]} telah ditambahkan sebesar', jls, f'jumlah total stok {barang["Nama"]} menjadi {barang["Stok"]}')
            return
    print('Maaf ID barang yang anda masukan tidak valid')
            
            # THISSS PROBLLEEMMM
    
def developer_5():
    dv = input('Apakah Ada Barang lain?  (1. YA)  (2. Tidak)')
    if dv == "4":
        developer_4(st)
        
# Memanggil fungsi start untuk memulai
start()

# def developer(id):
#     for nm in nama_pss:
#         if  nm['Nama'] == id and nm['pss'] == pss:
#         # Membuat dictionary untuk barang baru
#             print('Isi hal yang dibutuhkan')
#             barang_baru = {}
#             barang_baru["ID"] = input("Masukkan ID barang: ")
#             barang_baru["Nama"] = input("Masukkan Nama: ")
#             barang_baru["Spesifikasi"] = input("Masukkan Spesifikasi barang: ")
#             barang_baru["Stok"] = int(input("Masukkan Stok barang: "))
#             barang_baru["Satuan"] = input("Masukkan Satuan barang: ")
#             barang_baru["Harga"] = int(input("Masukkan Harga barang: "))
        
#         # Menambahkan barang baru ke data_barang
#             data_barang.append(barang_baru)
#             print('Produk baru sudah di tambahkan')
#             developer_2()
#         else:
#             print('Maaf Nama atau Password salah')
        
# def developer_3():
#     dv = input('Anda mau re-stok atau menambahkan barang? (1. Re-stok) (2. Tambah barang)')
#     if dv == "2":
#         developer(id)
#     elif dv == "1":
#         global st
#         st = input("Masukkan ID barang yang ingin di Re-stok:   ")
#         developer_4(st)
#         developer(id)

# fungsi re stok
# def developer_4(st):
#     for barang in data_barang:
#         if barang["ID"] == st:
#             print(f'Masukkan jumlah stok yang ingin ditambah ke {barang["Nama"]} dengan Spesifikasi {barang["Spesifikasi"]}')
#             jls = int(input())
#             barang["Stok"] += jls
#             print(f'Stok {barang["Nama"]} telah ditambahkan sebesar', jls, f'jumlah total stok {barang["Nama"]} menjadi {barang["Stok"]}')
#             return
#     print('Maaf ID barang yang anda masukan tidak valid')

# Program Utama
kondisi = True
while kondisi != False:
    print('1. Tampilkan Data')
    print('2. Beli Barang')
    print('3. Lihat Total Pembelian')
    print('4. Keluar')
    print("Masukkan nomor perintah!")
    pilihan = input()
    
    if pilihan == '1':
        tampilkan_data()
        
    elif pilihan == '2':
        id = input("Masukkan ID Barang yang ingin dibeli: ")
        jlbarang = int(input("Jumlah barang yang dibeli:  "))
        beli_barang(id)
        
    elif pilihan == '3':
        print(f'Total pembelian Anda saat ini adalah {total_pembelian}')
        
    # elif pilihan == '4':
    #     print('Anda akan memasuki mode developer, pastikan username dan passwordnya benar!')
    #     id = input('Masukkan Username  :')
    #     pss = input('Masukkan Password  :')
    #     developer_3()
    
    elif pilihan == '4':
        print("Terima Kasih Telah Menggunakan Program Kami!")
        kondisi = False
    else:
        print("Pilihan tidak valid")
        
#Kode di atas sekarang mencakup total pembelian yang akan diperbarui setiap kali membeli barang. 