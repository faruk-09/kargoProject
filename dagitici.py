import sqlite3 as sql



class dagitici():

    def __init__(self, calisan_id, isim, soy_isim):
        self.calisan_id=calisan_id
        self.isim=isim
        self.soy_isim = soy_isim



    def __str__(self) -> str:
        return "calisan_id:{}\nisim:{}\nsoy_isim:{}\n".format(self.calisan_id, self.isim, self.soy_isim)

class dagitici_islem():
    vt = sql.connect("kargo.sqlite")
    degisiklik = vt.cursor()

    def veritabani_baglanti(self):
        self.conncect = sql.connect("kargo.sqlite")
        self.cursor = self.conncect.cursor()

    def dagitici_listesi(self):
        sorgu = "SELECT * FROM dagitici"
        self.degisiklik.execute(sorgu)
        dagitici_listeleme = self.degisiklik.fetchall()

        if(len(dagitici_listeleme) == 0):
            print("Dağıtıcı listemiz boş...")
        else:
            for i in dagitici_listeleme:
                dagiti = dagitici(i[0], i[1], i[2])
                print(dagiti)

    def dagitici_ekle(self, dagitici):
        sorgu = "INSERT INTO dagitici values(?,?,?)"
        self.degisiklik.execute(sorgu, (dagitici.calisan_id, dagitici.isim, dagitici.soy_isim))
        self.vt.commit()

    def dagitici_sil(self, calisan_id):
        sorgu2 = "DELETE FROM dagitici WHERE calisan_id = (?)"
        self.degisiklik.execute(sorgu2, (calisan_id,))
        self.vt.commit()
