from musteri import *


print(""" 
Kargo Takip sistemine Hoşgeldiniz

işlemler;

1.Müşteri Ekle

2.Müşteri Silme

3.Müşteri Listesini Göster

Çıkmak İçin 'q' ya basınız
**********
""")

musteri1 = musteri_islem()

while True:
    islem = input("Yapacağınız işlem:")
    print(islem)
    if (islem == "q"):
        print("Program sonlandırılıyor...")
        print("Yine bekleriz...")
        break
    elif(islem == "1"):
        print("Eklemek istediğiniz müşterinin bilgilerini giriniz...")
        id = input("id:")
        isim = input("İsim:")
        soy_isim = input("Soyisim:")
        adres = input("adres:")
        iletisim = int(input("iletişim bilgileri:"))

        yeni_musteri = musteri(id, isim, soy_isim, adres, iletisim)

        print("Kisi ekleniyor...")

        musteri1.musteri_ekle(yeni_musteri)
        print("Kisi Eklendi...")

    elif (islem == "2"):
        print("Hangi müsteriyi silmek istiyorsunuz ?")
        id = input("müsteri id:")

        musteri_silmek = musteri1.musteri_sil(id)

        cevap = input("Eminmisiniz ? (E/H)")
        if (cevap == "E" or "e"):
            print("Kisi siliniyor...")

            musteri1.musteri_sil(musteri_silmek)
            print("Kisi Silindi...")
    elif (islem == "3"):
        musteri1.musteri_listesi()
    else:
        print("Geçersiz işlem")