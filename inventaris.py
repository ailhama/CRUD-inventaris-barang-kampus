# import os
# os.system("cls")
# print()
# print("         ============== Menu Login ==============")

# user="admin"
# pasw="admin"

# kesempatan = 50
# while kesempatan>0:
#     print()
#     username=input("Masukkan Username : ")
#     password=input("Masukkan Password : ")

#     if (username==user and password==pasw):
#         print("Selamat Datang "+ user +", Anda berhasil Login")
#         break
#     else:
#         kesempatan<=1
#         print("Maaf, Username / Password Salah. Silahkan Login kembali")
#         print()
#     if kesempatan==0:
#         print("Maaf kesempatan Anda habis")

import os
os.system("cls")
import fileinput

def menu():
    print()
    print('=====================================================================================')
    print('|                     Sistem Inventaris Barang Fakultas Teknik                      |')
    print('|===================================================================================|')
    print('|   Daftar Menu :                                                                   |')
    print('|  +---------------------------------+','    +-------------------------------------+  |')
    print('|  |           Data Barang','          |     |           Data Peminjam             |  |')
    print('|  |---------------------------------|','    |-------------------------------------|  |')
    print('|  |1. Data Inventaris Barang','       |     |6. Data Peminjam Inventaris Barang   |  |')
    print('|  |2. Tambah Data Inventaris Barang','|     |7. Tambah Peminjam Inventaris Barang |  |')
    print('|  |3. Hapus Data Inventaris Barang  |     |8. Hapus Peminjam Inventaris Barang  |  |')
    print('|  |4. Edit Data Inventaris Barang   |     |9. Cari Peminjam Inventaris Barang   |  |')
    print('|  |5. Cari Data Inventaris Barang   |     +-------------------------------------+  |')
    print('|  +---------------------------------+                                              |')
    print('|                                  +----------+                                     |')
    print('|                                  |10. Keluar|                                     |')
    print('|                                  +----------+                                     |')
    print('=====================================================================================')
    kode = int(input(" Pilih No Menu : "))
    pilihmenu(kode)

os.system("cls")

def pilihmenu(kode):
    if   kode == 1:
        databarang()
    elif kode == 2:
        tambahdata()
    elif kode == 3:
        hapusdata()
    elif kode == 4:
        editdata()
    elif kode == 5:
        caridata()
    elif kode == 6:
        datapinjam()
    elif kode == 7:
        tambahpinjam()
    elif kode == 8:
        hapuspinjam()
    elif kode == 9:
        caripinjam()
    elif kode == 10:
        exit()
    else:
        print("Maaf , kode yang Anda masukkan salah")

def databarang():
    fileinventaris = open('databarang.txt', 'r')
    nama_barang = fileinventaris.readline()
    print("\n")
    print('         Daftar Data Inventaris Barang')
    print('         =============================')
    print()
    if len(nama_barang)<=0:
        print("Maaf, Data masih kosong. Silahkan tambah data terlebih dahulu")
        print()
    while nama_barang != '':
        kode_barang = fileinventaris.readline()
        jumlah_barang = fileinventaris.readline()
        letak_barang = fileinventaris.readline()
        kondisi_barang = fileinventaris.readline()
        nama_barang = nama_barang.rstrip('\n')
        kode_barang = kode_barang.rstrip('\n')
        jumlah_barang = jumlah_barang.rstrip('\n')
        letak_barang = letak_barang.rstrip('\n')
        kondisi_barang = kondisi_barang.rstrip('\n')
        print(' ------------------------------')
        print(' Nama Barang    :', nama_barang)
        print(' Kode Barang    :', kode_barang)
        print(' Jumlah Barang  :', jumlah_barang)
        print(' Letak Barang   :', letak_barang)
        print(' Kondisi Barang :', letak_barang)
        print(' ------------------------------')
        nama_barang = fileinventaris.readline()
    fileinventaris.close()

    input("Tekan [ENTER] untuk menuju halaman utama")
    menu()

def tambahdata():
    fileinventaris = open('databarang.txt', 'a')
    print("\n")
    print("         Tambah Data Inventaris Barang")
    print("         =============================")
    print()
    print("Note*")
    print("    Untuk kondisi barang disesuaikan dengan keadaan saat ini seperti :")
    print("""        1. Baik atau rusak ringan
        2. Rusak berat
        3. Tidak ditemukan atau hilang
        4. berlebih """)
    nama_barang = input("\nMasukkan nama barang     : ")
    kode_barang = input("Masukkan kode barang     : ")
    jumlah_barang = input("Masukkan jumlah barang   : ")
    letak_barang = input("Masukkan letak barang    : ")
    kondisi_barang = input("Masukkan kondisi barang    : ")
    fileinventaris.write(nama_barang + '\n')
    fileinventaris.write(kode_barang + '\n')
    fileinventaris.write(jumlah_barang + '\n')
    fileinventaris.write(letak_barang + '\n')
    fileinventaris.write(kondisi_barang + '\n')
    fileinventaris.close()
    print()
    kode = input('Apakah Anda ingin menambah barang lagi ? (y/t) : ')
    if kode == 'y':
            tambahdata()
    else:
        menu()

def hapusdata():
    print("\n")
    print("         Hapus Data Inventaris Barang")
    print("         ============================")
    print()
    fileinventaris = open('databarang.txt', 'r')
    nama_barang = fileinventaris.readline()
    if len(nama_barang)<=0:
        print("Maaf, Data masih kosong. Silahkan kembali ke halaman utama")
        input("Tekan [ENTER] untuk menuju halaman utama")
        menu()
        print()
    while nama_barang != '':
        kode_barang = fileinventaris.readline()
        jumlah_barang = fileinventaris.readline()
        letak_barang = fileinventaris.readline()
        kondisi_barang = fileinventaris.readline()
        nama_barang = nama_barang.rstrip('\n')
        kode_barang = kode_barang.rstrip('\n')
        jumlah_barang = jumlah_barang.rstrip('\n')
        letak_barang = letak_barang.rstrip('\n')
        kondisi_barang = kondisi_barang.rstrip('\n')
        print(' ------------------------------')
        print(' Nama Barang    :', nama_barang)
        print(' Kode Barang    :', kode_barang)
        print(' Jumlah Barang  :', jumlah_barang)
        print(' Letak Barang   :', letak_barang)
        print(' Kondisi Barang :', letak_barang)
        print(' ------------------------------')
        nama_barang = fileinventaris.readline()
    fileinventaris.close()
    nama_barang = input("Masukkan nama barang yang akan dihapus : ")
    file = fileinput.input('databarang.txt', inplace=True)

    for line in file:
        if nama_barang in line:
            for i in range(4):
                next(file, None)
        else:
            print(line.strip('\n'), end='\n')
    nama_barang
    print()
    kode = input('Apakah Anda ingin menghapus barang lagi ? (y/t) : ')
    if kode == 'y':
            hapusdata()
    else:
        menu()

def editdata():
    print("\n")
    print("         Edit Data Inventaris Barang")
    print("         ===========================")
    print()
    fileinventaris = open('databarang.txt', 'r')
    nama_barang = fileinventaris.readline()
    if len(nama_barang)<=0:
        print("Maaf, Data masih kosong. Silahkan kembali ke halaman utama")
        input("Tekan [ENTER] untuk menuju halaman utama")
        menu()
        print()
    while nama_barang != '':
        kode_barang = fileinventaris.readline()
        jumlah_barang = fileinventaris.readline()
        letak_barang = fileinventaris.readline()
        kondisi_barang = fileinventaris.readline()
        nama_barang = nama_barang.rstrip('\n')
        kode_barang = kode_barang.rstrip('\n')
        jumlah_barang = jumlah_barang.rstrip('\n')
        letak_barang = letak_barang.rstrip('\n')
        kondisi_barang = kondisi_barang.rstrip('\n')
        print(' ------------------------------')
        print(' Nama Barang    :', nama_barang)
        print(' Kode Barang    :', kode_barang)
        print(' Jumlah Barang  :', jumlah_barang)
        print(' Letak Barang   :', letak_barang)
        print(' Kondisi Barang :', letak_barang)
        print(' ------------------------------')
        nama_barang = fileinventaris.readline()
    fileinventaris.close()
    print()
    nama_barang = input('Masukkan nama barang yang akan di edit : ')
    jumlah_barang = int(input("Masukkan Jumlah barang terkini : "))
    print("Anda berhasil mengedit data")

    with open('databarang.txt', 'r') as f:
        filedata = f.readlines()

    replace = ""
    line_number = 0
    count = 0
    f = open('databarang.txt','r')
    cari = f.read().split('\n')
    for i, line in enumerate(cari):
        if nama_barang in line:
            for d in cari[i+2:i+3]:
                value = int(d)
                change = (jumlah_barang)
                replace = d.replace(d, str(change))
                line_number = count
            count = i + 2      
    f.close()
    
    filedata[count] = replace + '\n'

    with open('databarang.txt', 'w') as f:
        for line in filedata:
            f.write(line)
    print()
    kode = input('Apakah Anda ingin mengedit barang lagi ? (y/t) : ')            
    if kode == 'y':
            editdata()
    else:
        menu()

def caridata():
    print("\n")
    print('         Cari Data Inventaris Barang')
    print('         ===========================')
    print()
    nama_barang = input('Masukkan nama barang yang akan di cari : ')

    f = open('databarang.txt', 'r')
    cari = f.readlines()
    f.close
    for i, line in enumerate(cari):
        if nama_barang in line:
            for b in cari[i:i+1]:
                print()
                print('------------------------')
                print('Nama Barang   :', b, end='')
            for c in cari[i+1:i+2]:
                print('Kode Barang   :', c, end='')
            for d in cari[i+2:i+3]:
                print('Jumlah Barang :', d, end='')
            for e in cari[i+3:i+4]:
                print('Letak Barang  :', e, end='')
            for e in cari[i+4:i+5]:
                print('Kondisi Barang  :', e, end='')
                print('------------------------')
        
    kode = input('Apakah Anda ingin mencari barang lagi ? (y/t) : ')
    if kode == 'y':
            caridata()
    else:
        menu()

def datapinjam():
    fileinventaris = open('datapeminjam.txt', 'r')
    peminjam = fileinventaris.readline()
    print("\n")
    print('         Daftar Data Peminjam Inventaris Barang')
    print('         ======================================')
    print()
    if len(peminjam)<=0:
        print("Maaf, Data masih Kosong. Silahkan tambah data terlebih dahulu")
        print()
    while peminjam != '':
        brgpnj = fileinventaris.readline()
        jlbrgpnj = fileinventaris.readline()
        tglpnj = fileinventaris.readline()
        tglkbl = fileinventaris.readline()
        peminjam = peminjam.rstrip('\n')
        brgpnj = brgpnj.rstrip('\n')
        jlbrgpnj = jlbrgpnj.rstrip('\n')
        tglpnj = tglpnj.rstrip('\n')
        tglkbl = tglkbl.rstrip('\n')
        print(' ----------------------------------------------')
        print(' Nama Peminjam               :', peminjam)
        print(' Nama barang yang dipinjam   :', brgpnj)
        print(' Jumlah barang yang dipinjam :', jlbrgpnj)
        print(' Tanggal peminjaman barang   :', tglpnj)
        print(' Tanggal kembalian barang    :', tglkbl)
        print(' ----------------------------------------------')
        peminjam = fileinventaris.readline()
    fileinventaris.close()

    input("Tekan [ENTER] untuk menuju halaman utama")
    menu()

def tambahpinjam():
    fileinventaris = open('datapeminjam.txt', 'a')
    print("\n")
    print("         Input Peminjam Inventaris Barang")
    print("         ================================")
    print()
    peminjam = input("Masukkan nama Peminjam                : ")
    brgpnj = input("Masukkan barang yang dipinjam         : ")
    jlbrgpnj = input("Masukkan jumlah barang yang dipinjam  : ")
    tglpnj = input("Masukkan tanggal pinjam               : ")
    tglkbl = input("Masukkan tanggal kembali              : ")
    fileinventaris.write(peminjam + '\n')
    fileinventaris.write(brgpnj + '\n')
    fileinventaris.write(jlbrgpnj + '\n')
    fileinventaris.write(tglpnj + '\n')
    fileinventaris.write(tglkbl + '\n')
    fileinventaris.close()
    print()
    kode = input('Apakah Anda ingin menambah data peminjam lagi ? (y/t) : ')
    if kode == 'y':
            tambahpinjam()
    else:
        menu()

def hapuspinjam():
    print("\n")
    print("         Hapus Peminjam Inventaris Barang")
    print("         ================================")
    print()
    fileinventaris = open('datapeminjam.txt', 'r')
    peminjam = fileinventaris.readline()
    if len(peminjam)<=0:
        print("Maaf, data masih kosong. Silahkan kembali ke halaman utama")
        input("Tekan [ENTER] untuk menuju halaman utama")
        menu()
        print()
    while peminjam != '':
        brgpnj = fileinventaris.readline()
        jlbrgpnj = fileinventaris.readline()
        tglpnj = fileinventaris.readline()
        tglkbl = fileinventaris.readline()
        peminjam = peminjam.rstrip('\n')
        brgpnj = brgpnj.rstrip('\n')
        jlbrgpnj = jlbrgpnj.rstrip('\n')
        tglpnj = tglpnj.rstrip('\n')
        tglkbl = tglkbl.rstrip('\n')
        print(' ----------------------------------------------')
        print(' Nama Peminjam               :', peminjam)
        print(' Nama brgpnj yang dipinjam   :', brgpnj)
        print(' Jumlah brgpnj yang dipinjam :', jlbrgpnj)
        print(' Tanggal peminjaman barang   :', tglpnj)
        print(' Tanggal kembalian barang    :', tglkbl)
        print(' ----------------------------------------------')
        peminjam = fileinventaris.readline()
    fileinventaris.close()
    print()
    peminjam = input("Masukkan nama peminjam yang akan dihapus : ")

    file = fileinput.input('datapeminjam.txt', inplace=True)

    for line in file:
         if peminjam in line:
             for i in range(4):
                 next(file, None)
         else:
             print(line.strip('\n'), end='\n')
    peminjam
    print()
    kode = input('Apakah Anda ingin menghapus data peminjam lagi ? (y/t) : ')
    if kode == 'y':
            hapuspinjam()
    else:
        menu()

def caripinjam():
    print("\n")
    print('         Cari Peminjam Inventaris Barang')
    print('         ===============================')
    print()
    peminjam = input('Masukkan nama peminjam yang akan di cari : ')
    
    f = open('datapeminjam.txt', 'r')
    cari = f.readlines()
    f.close
    for i, line in enumerate(cari):
        if peminjam in line:
            for b in cari[i:i+1]:
                print()
                print('--------------------------------------')
                print('Nama Peminjam                :', b, end='')
            for c in cari[i+1:i+2]:
                print('Barang yang dipinjam         :', c, end='')
            for d in cari[i+2:i+3]:
                print('Jumlah Barang yang dipinjam  :', d, end='')
            for e in cari[i+3:i+4]:
                print('Tanggal peminjaman barang    :', e, end='')
            for f in cari[i+4:i+5]:
                print('Tanggal kembali barang       :', f, end='')
                print('--------------------------------------')
        
    kode = input('Apakah Anda ingin mencari lagi ? (y/t) : ')
    if kode == 'y':
            caripinjam()
    else:
        menu()
menu()
