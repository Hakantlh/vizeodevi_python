class tarifler :
    def tarif_ekle(self) :
        tarifIsmi = input("Tarıf İsmi : ")
        tarif.append(tarifIsmi)
        while True :
            tarifAsama = input('Tarif Aşaması Ekle(Aşamalarınız Sonlandıysa "-1" giriniz.) : ')
            if tarifAsama == "-1" :
                tarifler_listesi.append(tarif)
                tarif.append("\n")
                break
            else :
                tarif.append(tarifAsama)


    def goster(self) :
        number = len(tarifler_listesi)
        print("Bütün Tarifler")
        for adim in tarif :
                print(adim)




def menux() :
    while True :
        print("\Tarif Ekle : 1\nTarifleri Goster : 2\n Çıkış Yap : 3 ")
        secim = input("Yapmak İstediğiniz İşlem Numarasını Giriniz: ")
        islem = tarifler()
        if secim == "1" :
            islem.tarif_ekle()
        elif secim == "2" :
            islem.goster()
        elif secim == "3" :
            exit(0)
        else :
            print("Hatalı Giriş Yaptınız.")



tarifler_listesi = []
tarif = []

menux()