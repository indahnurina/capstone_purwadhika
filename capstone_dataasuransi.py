# Author: Indah Nurina Fitri Hapsari
# Pembuatan Tools Sederhana untuk Membangun Database Penutupan Asuransi Menggunakan Python
#    Bagian 1: Penjelasan Fitur Program
#    Bagian 2: Penjelasan Mengenai Cara Untuk Membuat Data Initial dan Fungsi-Fungsi yang Nantinya Digunakan pada Program Utama
#    Bagian 3: Penjelasan Mengenai Main Program / Program Utama dari Tools Sederhana Ini
# Program ini dapat digunakan oleh underwriter asuransi untuk mencatat daftar penutupan/polis asuransi
# Pada program ini, saya memanfaatkan beberapa fungsi dari python, yaitu:
    # for loop
    # while loop
    # conditional if else
    # dictionary dan list
# Menu yang terdapat pada program:
#   1. Menampilkan seluruh database risiko terkini
#   2. Menampilkan data risiko dengan nama tertanggung yang memuat nama tertentu
#   3. Menambahkan data risiko / polis baru ke dalam database
#   4. Mengubah nilai Sum Insured untuk suatu polis (endorsement)
#   5. Melakukan cancellation terhadap suatu polis -> risiko/polis tertentu akan terhapus dari database
#   6. Quit

#Import Library
import datetime as dt

#Membuat data initial berupa variable dengan tipe dictionary: 3 keys, 4 values untuk masing-masing key
data={
    "POLICY-00001":["INDAH NURINA",15000,dt.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),"New"],
    "POLICY-00002":["INDAH KARTIKA",25000,dt.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),"New"],
    "POLICY-00003":["SHERINA",13000,dt.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),"New"],
}

run_num=len(data) #policy number pada data -> agar tidak terjadi duplicate saat menambahkan data polis baru ke dalam database

#Menu 1 - Fungsi Read / Menampilkan Data di Terminal
def read_data(data,out=[]):# 2 argumen: data=keseluruhan database dan out= key dari data yang tidak akan ditampilkan
    print("{:<15} {:<20} {:<12} {:<25} {:<8}".format("Policy ID","Nama","Sum Insured","Date Updated","Status")) #Menampilkan judul kolom
    for key, val in data.items(): #menampilkan pasangan key-values pada data
        if key not in out: #apabila key tidak terdapat dalam variable out, maka data akan ditampilkan ke terminal
            name,sum_insured,input_date,status=val
            print("{:<15} {:<20} {:<12} {:<25} {:<8}".format(key,name,sum_insured,input_date,status))

#Menu 2 - Fungsi Print Data secara Parsial berdasarkan Nama Tertanggung
def read_part_data(data): # 1 argumen: data=keseluruhan database
    lookupnama=input("\nMasukkan nama tertanggung yang ingin dicari: ").upper() #Input user. Local variable -> terhapus setelah fungsi selesai dijalankan
    listnama=[data[key][0] for key in data.keys()] #list comprehension untuk extract seluruh nama yang termuat pada data
    out=[] #initial list yang nantinya akan diisi dengan dictionary key dari data yang tidak memiliki nama yang dicari
    for loc,names in enumerate(listnama): #mencari secara iteratif nama yang terdapat pada var. lookupnama ke setiap element listnama
        try:
            names.index(lookupnama)
        except:
            out.append(list(data.keys())[loc]) #apabila ada nama yang tidak sesuai -> sistem menambahkan key terkait pada variable out
    if len(out)!= len(data): #jika panjang variable out tidak sama dengan jumlah keys, maka terdapat data yangf berisi nama yang dicari
       read_data(data,out) #print data yang memiliki nama sesuai
    else:
       print("\nMaaf, data tidak ditemukan") #jika panjang list out = jumlah keys, maka data tidak ditemukan

#Menu 3 - Fungsi Menambahkan Data Risiko Asuransi
def add_data(data):
    global run_num #agar tidak terjadi duplicate saat menambahkan data polis baru ke dalam database
    temp_name=input("\nMasukkan Nama Tertanggung: ").upper()
    temp_tsi=input("Masukkan Nilai Sum Insured: ")
    try:
        if any(char.isdigit() for char in temp_name)==True or run_num==99999: 
            raise SystemExit('Nama memuat angka')#Jika terdapat angka dalam nama atau run_num sudah mencapai 99999-> masuk error
       
        # Jika tidak error -> menambahkan key-valued baru berdasarkan input user
        data["POLICY-{:05d}".format(run_num+1)]=[temp_name,float(temp_tsi),\
        dt.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),"New"] 

        # Menampilkan data yang sudah ditambahkan dengan data baru
        print("\nTerima kasih. Data telah berhasil ditambahkan, sbb:")
        read_data(data)
        run_num+=1 #menambahkan nilai running number setelah data baru berhasil ditambahkan
    except:
        print("\nTerdapat kesalahan pada data. Data tidak berhasil ditambahkan.")

#Menu 4 - Fungsi Mengubah Nilai Sum Insured dari Suatu Data Risiko Asuransi
def change_data(data):
    po_id=input("\nMasukkan nomor dari policy_id yang ingin diubah [contoh input:1]: ")
    new_si=input("Masukkan nilai sum insured yang baru: ")
    try:
        po_id="POLICY-{:05d}".format(int(po_id)) #reformat untuk menyesuaikan dengan penulisan policy id
        data[po_id][1:]=float(new_si),\
            dt.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),"Endorsed" #Mengubah SI, Update Time, dan Status
        print("Data berhasil diubah, sbb: ")
        read_data(data)  # Menampilkan data terkini
    except:
        print("\nTerdapat kesalahan, sehingga data tidak berhasil diubah")

#Menu 5 - Fungsi Menghapus Suatu Data Risiko Asuransi Berdasarkan Nomor dari Policy ID (Cancellation Polis)
def del_data(data):
    po_id=input("Masukkan nomor dari policy_id yang ingin dihapus: ")
    try:
        po_id="POLICY-{:05d}".format(int(po_id)) #reformat untuk menyesuaikan dengan format policy id
        del data[po_id] #menghapus berdasarkan key policy id
        print("Data berhasil dihapus, sbb: ")
        read_data(data)
    except:
        print("\nTerdapat kesalahan, sehingga data tidak berhasil dihapus")
                
#Main Program
menu=0 #set awal agar masuk ke dalam while loop
count=0 #set untuk nantinya menghitung berapa kali user salah meng-input menu (memasukkan selain angka)

while menu not in [1,2,3,4,5,6]:
    print('''Berikut adalah fitur yang dapat dipilih
      1. Menampilkan seluruh database terkini
      2. Menampilkan data risiko dengan nama tertanggung yang memuat nama tertentu
      3. Menambahkan data risiko / polis baru ke dalam database
      4. Mengubah nilai Sum Insured untuk suatu polis (endorsement)
      5. Melakukan cancellation terhadap suatu polis
      6. Quit : Keluar
      ''')
    try: 
        menu=int(float((input("Masukkan menu yang dipilih: ")))) #convert ke float, lalu integer untuk menghindari error jika input 5.0 (contoh)
    except:
        count+=1
        if count<3:
           print("Menu yang diinput tidak dalam angka. Silahkan input kembali\n")
           continue
        else:
           print("Maaf, anda sudah mencoba 3 kali. Silahkan coba kembali nanti")
           break
    if menu not in [1,2,3,4,5,6]:
        print("Maaf, menu tidak terdapat dalam daftar.\n")
        break
    else:
        if menu==1:
            read_data(data)
        if menu==2:
            read_part_data(data)
        if menu==3:
            add_data(data)
        if menu == 4:
            read_data(data)
            change_data(data)
        if menu==5:
            read_data(data)
            del_data(data)
        if menu==6:
            break

    opsi=input("\nApakah ingin memilih menu lainnya (Y/N):")
    if opsi in ["Y","y","Yes","yes","ya"]:
       menu=0
    
print("\nClosing Program...Thanks!!")