def satu():
    print("NO.1 Rata-Rata ")
    a,b,c,d,e = 1,2,3,4,5

    mean = (a+b+c+d+e)/5
    print("rata-rata =",mean)


def dua():
    print("NO.2 Luas dan Keliling")
    print("========================================================================")
    print(" ")
    print("1. Luas persegi")
    print("2. Luas persegi panjang")
    print("3. Keliling persegi")
    print("4. Keliling persegi panjang")
    a = int(input("Masukkan nomor yang kamu pilih : "))
    if a == 1:
        print("========================================================================")
        print("Luas Persegi")
        b = float(input("masukkan panjang sisinya : "))
        c = b**2
        print("luas persegi : " + str(c))
    elif a == 2:
        print("========================================================================")
        print("Luas persegi panjang")
        d = float(input("masukkan panjang persegi panjang : "))
        e = float(input("masukkan lebar persegi panjang : " ))
        f = d*e
        print("luas persegi panjang: " + str(f))
    elif a == 3:
        print("========================================================================")
        print("Keliling Persegi")
        a = float(input("masukkan panjang sisinya : "))
        b = 4*a
        print("Keliling persegi : ",str(b))
    elif a == 4:
        print("========================================================================")
        print("Keliling Persegi Panjang")
        a = float(input("masukkan panjangnya : "))
        b = float(input("masukkan lebarnya : "))
        k = (2*a)+(2*b) 
        print("Keliling persegi : ",str(k))

    else:
        print("anda salah memasukkan input")

def tiga():
    print("NO.3 BMI")
    tinggi = float(input("masukkan tinggi badan anda (dalam satuan meter) = "))
    berat = float(input("masukkan berat badan anda (dalam satuan kilogram) = "))
    BMI = berat/(tinggi**2)
    print("indeks masa tubuh anda adalah : ", BMI)
    if BMI<18.5:
        print("berat badan kurang")
    elif 18.5<=BMI<23:
        print("berat badan normal")
    elif 23<=BMI<30:
        print("Berat badan berlebih (kecenderungan obesitas)")
    else:
        print("obesitas")


def empat():
    print("NO.4 Nilai Maks & Min")
    angka = []
    while True:
        inputan = float(input("masukkan angka = "))
        angka.append(inputan)
        tanya = input("apakah anda ingin memasukkan angka lagi ? y/n ")
        if tanya == "y":
            continue
        elif tanya == "n":
            break
        else:
            print("jangan sampai salah huruf")
            break
    besar = angka[0]
    kecil = angka[0]
    for i in angka:
        if i > besar:
            besar = i
        elif i < kecil:
            kecil = i
    print("ini list", angka)
    print("ini maksimal",besar)
    print("ini minimal", kecil)

def lima():
    uname = "Musta"
    pasw = "aku123"
    temp = 3
    while temp >= 0:
        if temp == 0:
            print("")
            print('''silahkan konfigurasi ulang username dan password anda,
dikarenakan anda sudah 3x melakukan kesalahan.''')
            break
        username = input("masukkan username anda :")
        password = input("masukkan password anda :")
        if username == uname and password == pasw :
            print("")
            print("anda berhasil masuk")
            break
        elif username != uname or password != pasw :
            print("maaf user name dan password anda salah")
            temp -=1
            continue


satu()
#dua()
#tiga()
#empat()
#lima()
































    
