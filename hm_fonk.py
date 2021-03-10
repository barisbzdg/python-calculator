def giris_ekrani():
    print("Hangi islemi yapacaksiniz?\n")
    i = 1
    for fonksiyon in fonksiyonlar:
        print(i,"--->",fonksiyon)
        i += 1
    print("\nÇıkmak için Ç/ç\n")
def veri_girisi():
    sayilar = []
    while True:
        sayi = input("Sayiyi girin (Çıkmak için Ç/ç) : ")

        if sayi == "Ç" or sayi == "ç":
            break
        sayi = int(sayi)
        sayilar.append(sayi)
    return sayilar
def toplama(sayilar):
    toplam = sayilar[0]
    for index in range(1,len(sayilar)):
        toplam = toplam + sayilar[index]
    print(f"Toplama sonucu : {toplam}\n")
def cikarma(sayilar):
    cikarma = sayilar[0]
    for index in range(1,len(sayilar)):
        cikarma = cikarma - sayilar[index]
    print(f"Cikarma sonucu : {cikarma}\n")
def carpma(sayilar):
    carpma = sayilar[0]
    for index in range(1,len(sayilar)):
        carpma = carpma * sayilar[index]
    print(f"Carpma sonucu : {carpma}\n")
def bolme(sayilar):
    bolme = sayilar[0]
    for index in range(1,len(sayilar)):
        bolme = bolme / sayilar[index]
    print(f"Bolme sonucu : {bolme}")
def k_secim():
    k_secim = input("Seçiminizi giriniz : ")
    return k_secim
def ana_program():
    while True:
        giris_ekrani()
        
        secim = k_secim()
        if secim in bitis:
            print("işleminiz bitti.")
            break
        if secim not in islemler.keys():
            
            print("yanlis giris")
            continue
        
        sayilar=veri_girisi()
        print(sayilar)
        if secim in islemler.keys():
            islemler[secim](sayilar)

islemler = {"1":toplama,"2":cikarma,"3":carpma,"4":bolme}
fonksiyonlar = ["Toplama","Cikarma","Carpma","Bolme"]
bitis = {"Ç","ç"}
ana_program()  
    