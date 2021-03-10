def giris_ekrani():
    print("Hangi islemi yapacaksiniz?")
    print("1-Toplama\n2-Cikarma\n3-Carpma\n4-Bolme\nCıkış için Ç/ç\n")
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
while True:
    giris_ekrani()
    
    secim = k_secim()
    if secim == "Ç" or secim == "ç":
        print("işleminiz bitti.")
        break
    if secim != "1" and secim != "2" and secim != "3" and secim != "4":
        #if not (secim=="1" or secim == "2" or secim == "3" or secim == "4"):
        print("yanlis giris")
        continue
    
    sayilar=veri_girisi()
    print(sayilar)
    
    if secim == '1':
        toplama(sayilar)
    elif secim == '2':
        cikarma(sayilar)
    elif secim == '3':
        carpma(sayilar)
    elif secim == '4':
        bolme(sayilar)
    
  
    