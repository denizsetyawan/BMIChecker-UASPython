#Nama  : Denis Setiawan
#NIM   : 18.01.4142
#Kelas : 18-D3-TI-01

from os import system, name

#fungsi cls
def clearscreen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('cls')

#data
name = []
tinggi = []
berat = []
besaran = []
status = []
    
while True:
    #Menu
    print('')
    print(25*"=")
    print('UAS - Denis Setiawan')
    print(25*"=")
    print('')
    print("1. Hitung BMI",
          "\n2. Riwayat Hitung BMI",
          "\n3. Keluar");
    print(25*"-")
    pilihan = int(input('pilihan : '));

    #pilihan 1
    if pilihan == 1 :
        print(25*"=");
        
        #perhitungan bmi
        nama = input("Nama : ")
        tb = int(input("Masukkan tinggi (cm) = "))
        bb = int(input("Masukkan berat (kg)  = "))
        print(" ")

        x = float(tb)
        a = x/100
        b = float(bb)

        hasil = b/a**2

        name.append(nama)
        tinggi.append(tb)
        berat.append(bb)
        besaran.append(hasil)

        if(hasil < 18.5):
            stat = 'Kekurangan berat badan';
            status.append(stat)
            
            print("Hasilnya :")
            print("Status berat : Kekurangan berat badan")
            print("Besaran BMI  :", hasil)

            input("Tekan enter untuk melanjutkan")
            clearscreen()
        elif(18.5 <= hasil <= 24.9):
            stat = 'Normal(ideal)';
            status.append(stat)
            
            print("Hasilnya :")
            print("Status berat : Normal(ideal)")
            print("Besaran BMI  :", hasil)

            input("Tekan enter untuk melanjutkan")
            clearscreen()
        elif(25.0 <= hasil <= 29.9):
            stat = 'Kelebihan berat badan';
            status.append(stat)
            
            print("Hasilnya :")
            print("Status berat : Kelebihan berat badan")
            print("Besaran BMI  :", hasil)

            input("Tekan enter untuk melanjutkan")
            clearscreen()
        elif(hasil >= 30.0):
            stat = 'Kegemukan (Obesitas)';
            status.append(stat)
            
            print("Hasilnya :")
            print("Status berat : Kegemukan (Obesitas)")
            print("Besaran BMI  :", hasil)

            input("Tekan enter untuk melanjutkan")
            clearscreen()
        else:
            print("Nilai yang anda masukkan tidak valid")

    #pilihan 2
    elif pilihan == 2 :
        if not name:
            print("\nRiwayat Hitung BMI");
            print(111*"=");
            print("|{:<20}|{:<20}|{:<20}|{:<20}|{:<25}|".format('nama', 'tinggi (cm)', 'berat (kg)', 'besaran BMI', 'Status'));
            print(111*"=");
            print("Data masih kosong");
            print(111*"=");
            
            input("Tekan enter untuk melanjutkan")
            clearscreen()
            
        else:
            print("\nRiwayat Hitung BMI");
            print(111*"=");
            print("|{:<20}|{:<20}|{:<20}|{:<20}|{:<25}|".format('nama', 'tinggi (cm)', 'berat (kg)', 'besaran BMI', 'Status'));
            print(111*"=");

            for i in range(len(name)) :
                print("|{:<20}|{:<20}|{:<20}|{:<20}|{:<25}|".format(name[i], tinggi[i], berat[i], besaran[i], status[i]))

            print(111*"=", "\n");
            
            input("Tekan enter untuk melanjutkan")
            clearscreen()

    #pilihan 3
    elif pilihan == 3 :
        print ('');
        print ('Berhasil Keluar');
        break;
    else :
        print ('Pilihan yang anda masukkan salah.')