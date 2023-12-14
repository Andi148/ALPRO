# TUGAS PRAKTIKUM PERTEMUAN KE-13
# ALGORITMA PEMROGRAMAN I, GANJIL 2023/2024
# NPM : 2313020180
# Nama : Andi Kusuma Wardana
# Kelas : 1-D

# Data barang
data_barang = [
    {"ID": "B07", "Nama": "Ballpoint", "Spesifikasi": "faster C600", "Stok": 19,"Satuan": "Lusin", "Harga": 28600},
    {"ID": "B21", "Nama": "Ballpoint", "Spesifikasi": "pilot BPTP", "Stok": 15,"Satuan": "Lusin", "Harga": 24700},
    {"ID": "B44", "Nama": "Ballpoint", "Spesifikasi": "snowman V2", "Stok": 17,"Satuan": "Lusin", "Harga": 24100},
    {"ID": "L04", "Nama": "Lakban", "Spesifikasi": "panfix 1/2x72", "Stok": 30, "Satuan": "Roll", "Harga": 13200},
    {"ID": "L17", "Nama": "Lakban", "Spesifikasi": "nachi 1/2x72", "Stok": 36, "Satuan": "Roll", "Harga": 5400},
    {"ID": "C09", "Nama": "Cutter", "Spesifikasi": "joyko A-300A", "Stok": 24, "Satuan": "Buah","Harga": 7900},
    {"ID": "C31", "Nama": "Cutter", "Spesifikasi": "SDI 0405", "Stok": 20, "Satuan": "Buah","Harga": 11500},
    {"ID": "C35", "Nama": "Cutter", "Spesifikasi": "SDI 0416", "Stok": 30, "Satuan": "Buah","Harga": 18900},
    {"ID": "P15", "Nama": "Penggaris Plastik", "Spesifikasi": "Joy-art RLS-A3", "Stok": 12, "Satuan": "Set","Harga": 15200},
    {"ID": "P37", "Nama": "Penggaris Plastik", "Spesifikasi": "Joy-art RLS-S-T4", "Stok": 18, "Satuan": "Set","Harga": 13200},
    {"ID": "Q24", "Nama": "Penghapus", "Spesifikasi": "joyko-345", "Stok": 20, "Satuan": "Buah",     "Harga": 4500},
    {"ID": "Q12", "Nama": "Penghapus", "Spesifikasi": "ATM-60", "Stok": 10, "Satuan": "Buah", "Harga": 1500},
    {"ID": "K12", "Nama": "Folio", "Spesifikasi": "Sidu F4", "Stok": 30,"Satuan": "Rim", "Harga": 45000},
    {"ID": "K15", "Nama": "A4", "Spesifikasi": "Sidu A4", "Stok": 15, "Satuan": "Rim","Harga": 65000}
    # Tambahkan data lainnya sesuai kebutuhan
]
nama_pss = [
    {"Nama": "Andi", "pss":"sononamidawo123"}
]


total_pembelian = 0
# Menampilakan Tabel barang
def tampilkan_data():
    print("{:<8} {:<20} {:<20} {:<10} {:<10} {:<8}".format("ID","Nama Barang", "Spesifikasi", "Stok", "Satuan", "Harga"))
    for barang in data_barang:
        print("{:<8} {:<20} {:<20} {:<10} {:<10} {:<8}".format(barang["ID"], barang["Nama"], barang["Spesifikasi"], barang["Stok"], barang["Satuan"], barang["Harga"]))
        
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

def developer(id):
    for nm in nama_pss:
        if  nm['Nama'] == id and nm['pss'] == pss:
        # Membuat dictionary untuk barang baru
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
            developer_2()
        else:
            print('Maaf Nama atau Password salah')

def developer_2():
    kn = input('Apakah Ada Barang lain?  (1. YA)  (2. Tidak)')
    if kn == "1":
        developer(id)
        
def developer_3():
    dv = input('Anda mau re-stok atau menambahkan barang? (1. Re-stok) (2. Tambah barang)')
    if dv == "2":
        developer(id)
    elif dv == "1":
        global st
        st = input("Masukkan ID barang yang ingin di Re-stok:   ")
        developer_4(st)

# fungsi re stok
def developer_4(st):
    for barang in data_barang:
        if barang["ID"] == st:
            print(f'Masukkan jumlah stok yang ingin ditambah ke {barang["Nama"]}')
            jls = int(input())
            barang["Stok"] += jls
        else:
            print('Maaf ID barang yang anda masukan tidak valid')

        
# Program Utama
kondisi = True
while kondisi != False:
    print('1. Tampilkan Data')
    print('2. Beli Barang')
    print('3. Lihat Total Pembelian')
    print('4. Tambahkan produk')
    print('5. Keluar')
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
        
    elif pilihan == '4':
        print('Anda akan memasuki mode developer, pastikan username dan passwordnya benar!')
        id = input('Masukkan Username  :')
        pss = input('Masukkan Password  :')
        developer_3()
    elif pilihan == '5':
        print("Terima Kasih Telah Menggunakan Program Kami!")
        kondisi = False
    else:
        print("Pilihan tidak valid")
        
#Kode di atas sekarang mencakup total pembelian yang akan diperbarui setiap kali membeli barang. 