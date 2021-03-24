def giris_ekrani():
    print("Select operation.\n")
    i = 1
    for secenek in secenekler:
        print(i,"--->",secenek)
        i += 1
    print("\nTo Exit Press E/e\n")

def veri_girisi():
    sayilar = []
    while True:
        sayi = input("Enter a Number (To Exit Press E/e) : ")

        if sayi == "E" or sayi == "e":
            break
        sayi = int(sayi)
        sayilar.append(sayi)
    return sayilar

def toplama(sayilar):
    toplam = sayilar[0]
    for index in range(1,len(sayilar)):
        toplam = toplam + sayilar[index]
    print(f"Result : {toplam}\n")

def cikarma(sayilar):
    cikarma = sayilar[0]
    for index in range(1,len(sayilar)):
        cikarma = cikarma - sayilar[index]
    print(f"Result  : {cikarma}\n")

def carpma(sayilar):
    carpma = sayilar[0]
    for index in range(1,len(sayilar)):
        carpma = carpma * sayilar[index]
    print(f"Result : {carpma}\n")

def bolme(sayilar):
    bolme = sayilar[0]
    for index in range(1,len(sayilar)):
        bolme = bolme / sayilar[index]
    print(f"Result : {bolme}\n")

def k_secim():
    k_secim = input("Enter Choice : ")
    return k_secim

def ana_program():
    while True:
        giris_ekrani()
        
        secim = k_secim()
        if secim in bitis:
            print("Calculated.")
            break
        if secim not in islemler.keys():
            
            print("Invalid Input.")
            continue
        
        sayilar=veri_girisi()
        print(sayilar)
        if secim in islemler.keys():
            islemler[secim](sayilar)

islemler = {"1":toplama,"2":cikarma,"3":carpma,"4":bolme}
secenekler = ["Add","Subtract","Multiply","Divide"]
bitis = {"E","e"}
ana_program()  
    
