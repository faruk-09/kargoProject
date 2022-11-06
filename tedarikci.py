import sqlite3 as sql



class tedarikci():

    def __init__(self, vergi_no, firma_adresi, firma_adi):
        self.vergi_no=vergi_no
        self.firma_adresi=firma_adresi
        self.firma_adi=firma_adi



    def __str__(self) -> str:
        return "vergi_no:{}\nfirma_adresi:{}\nfirma_adi:{}\n".format(self.vergi_no, self.firma_adresi, self.firma_adi)

class tedarikci_islem():
    vt = sql.connect("kargo.sqlite")
    degisiklik = vt.cursor()

    def veritabani_baglanti(self):
        self.conncect = sql.connect("kargo.sqlite")
        self.cursor = self.conncect.cursor()

    def tedarikci_listesi(self):
        sorgu = "SELECT * FROM tedarikci"
        self.degisiklik.execute(sorgu)
        tedarikci_listeleme = self.degisiklik.fetchall()

        if(len(tedarikci_listeleme) == 0):
            print("Tedarikci listemiz boş...")
        else:
            for i in tedarikci_listeleme:
                teda = tedarikci(i[0], i[1], i[2])
                print(teda)

    def tedarikci_ekle(self, tedarikci):
        sorgu = "INSERT INTO tedarikci values(?,?,?)"
        self.degisiklik.execute(sorgu, (tedarikci.vergi_no, tedarikci.firma_adresi, tedarikci.firma_adi))
        self.vt.commit()

    def tedarikci_sil(self, no):
        sorgu2 = "DELETE FROM tedarikci WHERE vergi_no = (?)"
        self.degisiklik.execute(sorgu2, (no,))
        self.vt.commit()
