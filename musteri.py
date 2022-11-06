import sqlite3 as sql



class musteri():

    def __init__(self, id, isim, soy_isim, adres, iletisim):
        self.id=id
        self.isim=isim
        self.soy_isim = soy_isim
        self.adres=adres
        self.iletisim=iletisim


    def __str__(self) -> str:
        return "id:{}\nisim:{}\nsoy_isim:{}\nadres:{}\niletisim:{}\n"\
            .format(self.id, self.isim, self.soy_isim, self.adres, self.iletisim)

class musteri_islem():
    vt = sql.connect("kargo.sqlite")
    degisiklik = vt.cursor()

    def veritabani_baglanti(self): # veri tabanı bağlantı işlemi
        self.conncect = sql.connect("kargo.sqlite")
        self.cursor = self.conncect.cursor()

    def musteri_listesi(self): # Müşteri listeleme işlemi sorgusu ve kodları
        sorgu = "SELECT * FROM musteri"
        self.degisiklik.execute(sorgu)
        musteri_listeleme = self.degisiklik.fetchall()

        if(len(musteri_listeleme) == 0):
            print("Müşteri listemiz boş...")
        else:
            for i in musteri_listeleme:
                muste = musteri(i[0], i[1], i[2], i[3], i[4])
                print(muste)

    def musteri_ekle(self, kisi): # Müşteri ekleme işlemi sorgusu ve kodları
        sorgu = "INSERT INTO musteri values(?,?,?,?,?)"
        self.degisiklik.execute(sorgu, (kisi.id, kisi.isim, kisi.soy_isim, kisi.adres, kisi.iletisim))
        self.vt.commit()

    def musteri_sil(self, id): #Müşteri silme işlemi sorgusu ve kodları
        sorgu2 = "DELETE FROM musteri WHERE id = (?)"
        self.degisiklik.execute(sorgu2, (id,))
        self.vt.commit()
