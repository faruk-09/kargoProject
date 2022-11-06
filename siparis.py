import sqlite3 as sql



class siparis():

    def __init__(self, id, siparis_sinifi, debi, oncelik_derecesi):
        self.id=id
        self.siparis_sinifi=siparis_sinifi
        self.debi = debi
        self.oncelik_derecesi=oncelik_derecesi



    def __str__(self) -> str:
        return "id:{}\nsiparis_sinifi:{}\ndebi:{}\noncelik_derecesi:{}\n".format(self.id, self.siparis_sinifi, self.debi, self.oncelik_derecesi)

class siparis_islem():
    vt = sql.connect("kargo.sqlite")
    degisiklik = vt.cursor()

    def veritabani_baglanti(self):
        self.conncect = sql.connect("kargo.sqlite")
        self.cursor = self.conncect.cursor()

    def siparis_listesi(self):
        sorgu = "SELECT * FROM siparis"
        self.degisiklik.execute(sorgu)
        siparis_listeleme = self.degisiklik.fetchall()

        if(len(siparis_listeleme) == 0):
            print("sipariş listemiz boş...")
        else:
            for i in siparis_listeleme:
                sipar = siparis(i[0], i[1], i[2], i[3])
                print(sipar)

    def siparis_ekle(self, siparis):
        sorgu = "INSERT INTO siparis values(?,?,?,?)"
        self.degisiklik.execute(sorgu, (siparis.id, siparis.siparis_sinifi, siparis.debi, siparis.oncelik_derecesi))
        self.vt.commit()

    def siparis_sil(self, id):
        sorgu2 = "DELETE FROM siparis WHERE id = (?)"
        self.degisiklik.execute(sorgu2, (id,))
        self.vt.commit()