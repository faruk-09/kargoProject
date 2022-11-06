import sqlite3 as sql

#alici bilgileri tutacağımız tablo

#bağlacak olduğumuz veri tabanın adını yazıyoruz
vt = sql.connect("kargo.sqlite")

# veri tabanı üzerinde işlem yapabilmek için islem tanımlıyoruz
islem = vt.cursor()

#alici, siparis, tedarikci, dagitici varlıkları için tabloları oluşturuyoruz
musteri_create_table = """CREATE TABLE musteri (
                        id NUMBER NOT NULL,
                        isim VARCHAR (20),
                        soy_isim VARCHAR (20),
                        adres VARCHAR (30),
                        iletisim VARCHAR (11),
                        CONSTRAINT PK_alici PRIMARY KEY (id) ) ;
                        """

siparis_create_table = """CREATE TABLE siparis (
                        id NUMBER NOT NULL,
                        siparis_sınıfı VARCHAR (20),
                        debi NUMBER NOT NULL,
                        oncelik_derecesi VARCHAR (11),
                        CONSTRAINT PK_siparis PRIMARY KEY (id));
                        """

tedarikci_create_table = """CREATE TABLE tedarikci(
                        vergi_no VARCHAR (11),
                        firma_adresi VARCHAR (50),
                        firma_adı VARCHAR (50),
                        CONSTRAINT PK_tedarikci PRIMARY KEY (vergi_no));
                        """

dagitici_create_table = """CREATE TABLE dagitici (
                        calisan_id NUMBER NOT NULL,
                        isim VARCHAR (30),
                        soy_isim VARCHAR (30),
                        CONSTRAINT PK_dagitici PRIMARY KEY (calisan_id));
                        """

verir_create_table = """CREATE TABLE give(
                    siparis_id NUMBER,
                    calisan_id NUMBER,
                    musteri_id NUMBER,
                    CONSTRAINT PK_give PRIMARY KEY (siparis_id,calisan_id, 
                    müsteri_id),
                    CONSTRAINT FK_orderNo FOREIGN KEY (siparis_id) 
                    REFERENCES siparis(id),
                    CONSTRAINT FK_employeeNo FOREIGN KEY (calisan_id) 
                    REFERENCES dagitici(employeeId),
                    CONSTRAINT FK_customerNo FOREIGN KEY (musteri_id) 
                    REFERENCES musteri(id));
                    """

saglar_create_table = """CREATE TABLE supply(
                    vergi_no NUMBER,
                    siparis_no NUMBER,
                    CONSTRAINT PK_supply PRIMARY KEY (vergi_no, 
                    siparis_no),
                    CONSTRAINT FK_supplierNo FOREIGN KEY (vergi_no) 
                    REFERENCES tedarikci(vergi_no),
                    CONSTRAINT FK_orderId FOREIGN KEY (orderId) 
                    REFERENCES siparis(id));
                    """



islem.execute(musteri_create_table)
islem.execute(siparis_create_table)
islem.execute(tedarikci_create_table)
islem.execute(dagitici_create_table)
islem.execute(verir_create_table)
islem.execute(saglar_create_table)


