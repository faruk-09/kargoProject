from musteri import *
from dagitici import *
from siparis import *
from tedarikci import *


musteri1 = musteri_islem()
dagitici1 = dagitici_islem()
siparis1 = siparis_islem()
tedarikci1 = tedarikci_islem()


while True:
    print(""" 
    Kargo Takip sistemine Hoşgeldiniz

    işlemler;

    m->Müşteri işlemleri

    d->Dağıtıcı işlemleri
    
    s->Sipariş işlemleri
    
    t->Tedarikci işlemleri

    Çıkmak İçin 'q' ya basınız
    **********
    """)
    islem = input("Yapacağınız işlem:")
    print(islem)
    if (islem == "q"):
        print("Program sonlandırılıyor...")
        print("Yine bekleriz...")
        break
    elif (islem == "m"): #müşteri işlemleri
        print(""" 
        Müşteri Takip sistemine Hoşgeldiniz

        işlemler;

        1.Müşteri Ekle

        2.Müşteri Silme

        3.Müşteri Listesini Göster
        
        4.Ana menüye dönmek

        
        **********
        """)
        m_islem = input("Müşterilerde Yapacağınız işlem:")
        if(m_islem == "1"):
            print("Eklemek istediğiniz müşterinin bilgilerini giriniz...")
            id = input("id:")
            isim = input("İsim:")
            soy_isim = input("Soyisim:")
            adres = input("adres:")
            iletisim = int(input("iletişim bilgileri:"))

            yeni_musteri = musteri(id, isim, soy_isim, adres, iletisim)

            print("Müşteri ekleniyor...")

            musteri1.musteri_ekle(yeni_musteri)
            print("Müşteri Eklendi...")

        elif (m_islem == "2"):
            print("Hangi müsteriyi silmek istiyorsunuz ?")
            id = input("müsteri id:")

            musteri_silmek = musteri1.musteri_sil(id)

            cevap = input("Eminmisiniz ? (E/H)")
            if (cevap == "E" or "e"):
                print("Müşteri siliniyor...")

                musteri1.musteri_sil(musteri_silmek)
                print("Müşteri Silindi...")
        elif (m_islem == "3"):
            musteri1.musteri_listesi()
        else:
            print("Ana menü")
    elif (islem == "d"): #dağıtıcı işlemleri
        print(""" 
                Dağıtıcı Takip sistemine Hoşgeldiniz

                işlemler;

                1.Dağıtıcı Ekle

                2.Dağıtıcı Silme

                3.Dağıtıcı Listesini Göster

                4.Ana menüye dönmek

                
                **********
                """)
        d_islem = input("Dağıtıcılarda Yapacağınız işlem:")
        if (d_islem == "1"):
            print("Eklemek istediğiniz dağıtıcının bilgilerini giriniz...")
            calisan_id = input("çalışan id:")
            isim = input("İsim:")
            soy_isim = input("Soyisim:")


            yeni_dagitici = dagitici(calisan_id, isim, soy_isim)

            print("Dağıtıcı ekleniyor...")

            dagitici1.dagitici_ekle(yeni_dagitici)
            print("Dağıtıcı Eklendi...")

        elif (d_islem == "2"):
            print("Hangi dağıtıcıyı silmek istiyorsunuz ?")
            id = input("çalışan id:")

            dagitici_silmek = dagitici1.dagitici_sil(id)

            cevap = input("Eminmisiniz ? (E/H)")
            if (cevap == "E" or "e"):
                print("Dağıtıcı siliniyor...")

                dagitici1.dagitici_sil(dagitici_silmek)
                print("Dağıtıcı Silindi...")
        elif (d_islem == "3"):
            dagitici1.dagitici_listesi()
        else:
            print("Ana menü")

    elif (islem == "s"): #siparis işlemleri
        print(""" 
                siparis Takip sistemine Hoşgeldiniz

                işlemler;

                1.Siparis Ekle

                2.Siparis Silme

                3.Siparis Listesini Göster

                4.Ana menüye dönmek

                
                **********
                """)
        s_islem = input("Siparişlerde Yapacağınız işlem:")
        if (s_islem == "1"):
            print("Eklemek istediğiniz siparişin bilgilerini giriniz...")
            id = input("sipariş id:")
            siparis_sinifi = input("Sipariş Sınıfı:")
            debi = input("Debi:")
            oncelik_derecesi = input("Öncelik derecesini giriniz:")

            yeni_siparis = siparis(id, siparis_sinifi, debi, oncelik_derecesi )
            print("Sipariş ekleniyor...")

            siparis1.siparis_ekle(yeni_siparis)
            print("Sipariş Eklendi...")

        elif (s_islem == "2"):
            print("Hangi siparişi silmek istiyorsunuz ?")
            id = input("sipariş id:")

            siparis_silmek = siparis1.siparis_sil(id)

            cevap = input("Eminmisiniz ? (E/H)")
            if (cevap == "E" or "e"):
                print("Sipariş siliniyor...")

                siparis1.siparis_sil(siparis_silmek)
                print("Sipariş Silindi...")
        elif (s_islem == "3"):
            siparis1.siparis_listesi()
        else:
            print("Ana menü")
    elif (islem == "t"):  # tedarikci işlemleri
        print(""" 
        Tedarikçi Takip sistemine Hoşgeldiniz

        işlemler;

        1.Tedarikci Ekle

        2.Tedarikci Silme

        3.Tedarikci Listesini Göster

        4.Ana menüye dönmek

        
        **********
        """)
        t_islem = input("Tedarikci Yapacağınız işlem:")
        if (t_islem == "1"):
            print("Eklemek istediğiniz müşterinin bilgilerini giriniz...")
            vergi_no = input("Vergi no :")
            firma_adresi = input("Firma adresi:")
            firma_adi = input("Firma Adı:")

            yeni_tedarikci = tedarikci(vergi_no, firma_adresi, firma_adi)

            print("Tedarikci ekleniyor...")

            tedarikci1.tedarikci_ekle(yeni_tedarikci)
            print("Tedarikci Eklendi...")

        elif (t_islem == "2"):
            print("Hangi tedarikciyi silmek istiyorsunuz ?")
            vergi_no = input("Tedarikci Vergi no:")

            tedarikci_silmek = tedarikci1.tedarikci_sil(vergi_no)

            cevap = input("Eminmisiniz ? (E/H)")
            if (cevap == "E" or "e"):
                print("Tedarikci siliniyor...")

                tedarikci1.tedarikci_sil(tedarikci_silmek)
                print("Tedarikci Silindi...")
        elif (t_islem == "3"):
            tedarikci1.tedarikci_listesi()
        else:
            print("Ana menü")
    else:
        print("Geçersiz işlem")