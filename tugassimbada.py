nama=[]
alamat= []
ttl= []
jkelamin= []
agama= []
jurusan= []
univ = []
nim = []
print("=======================")
print(" FORM DATA DIRI ")
print("=======================")
pilih=1
while (pilih!=0) :
    print("""
    1. Tambah Biodata
    2. Tampilkan Biodata
    3. Hapus Biodata
    0. Keluar
    """)
    pilih=int(input("Masukan pilihan anda : "))
    if (pilih==1) :
        masnama=input("Masukan nama anda : ")
        nama.append({"nama" : masnama})
        masnim=input("Masukan NIM anda : ")
        nim.append({"nim" : masnim})
        masalamat=input("Masukan alamat anda : ")
        alamat.append({"alamat" : masalamat})
        masttl=input("Masukan Tempat Tanggal lahir anda : ")
        ttl.append({"ttl" : masttl})
        masjkelamin=input("Masukan Jenis Kelamin anda : ")
        jkelamin.append({"jkelamin" : masjkelamin})
        masagama=input("Masukan nama Agama anda : ")
        agama.append({"agama" : masagama})
        masjurusan=input("Masukan nama Jurusan anda : ")
        jurusan.append({"jurusan" : masjurusan})
        masuniv=input("Masukan nama Universitas : ")
        univ.append({"univ" : masuniv})
    elif (pilih==2) :
        print("==========================================================================================================================")
        print("NAMA      |  NIM        |  ALAMAT        |  TTL               |  JENIS KELAMIN  |   AGAMA  |   JURUSAN   |    UNIVERSITAS|")
        for i in range (len(nim)) :
            print(nama[i]["nama"],"  |  ",nim[i]["nim"],"|",alamat[i]["alamat"],"|",ttl[i]["ttl"],"|",jkelamin[i]["jkelamin"],"|",agama[i]["agama"],"|",jurusan[i]["jurusan"],"|",univ[i]["univ"],"|")
    elif (pilih==3) :
        masnim = input("masukan nim : ")
        for i in range (len(nim)) :
            if masnim == nim[i]['nim'] :
                print (i)
                del nama[i]
                del nim[i]
                del alamat[i]
                del ttl[i]
                del jkelamin[i]
                del agama[i]
                del jurusan[i]
                del univ[i]
                break
    else :
        print("Terima Kasih")
        
