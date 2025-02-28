ogrenciler = []

def ogrenci_ekle():
    isim = input("Öğrencinin adını girin: ")
    soyisim = input("Öğrencinin soyadını girin: ")
    numara = input("Öğrencinin numarasını girin: ")
    bolum = input("Öğrencinin bölümünü girin: ")
    not_ortalama = float(input("Öğrencinin not ortalamasını girin: "))
    ogrenci = {
        "isim": isim,
        "soyisim": soyisim,
        "numara": numara,
        "bolum": bolum,
        "not_ortalama": not_ortalama
    }
    ogrenciler.append(ogrenci)
    print(f"{isim} {soyisim} başarıyla eklendi.")

def ogrencileri_goruntule():
    if not ogrenciler:
        print("Sistemde hiç öğrenci bulunmamaktadır.")
        return
    print("Tüm Öğrenciler:")
    for ogrenci in ogrenciler:
        print(f"Öğrenci Numarası: {ogrenci['numara']}")
        print(f"Adı: {ogrenci['isim']} {ogrenci['soyisim']}")
        print(f"Bölüm: {ogrenci['bolum']}")
        print(f"Not Ortalaması: {ogrenci['not_ortalama']}")
        print("-" * 30)

def ogrenci_bilgisi_goster():
    numara = input("Öğrencinin numarasını girin: ")
    for ogrenci in ogrenciler:
        if ogrenci["numara"] == numara:
            print(f"Öğrenci Numarası: {ogrenci['numara']}")
            print(f"Adı: {ogrenci['isim']} {ogrenci['soyisim']}")
            print(f"Bölüm: {ogrenci['bolum']}")
            print(f"Not Ortalaması: {ogrenci['not_ortalama']}")
            return
    print("Bu numaraya sahip öğrenci bulunmamaktadır.")

def ogrenci_guncelle():
    numara = input("Güncellemek istediğiniz öğrencinin numarasını girin: ")
    for ogrenci in ogrenciler:
        if ogrenci["numara"] == numara:
            ogrenci["isim"] = input("Yeni adı girin: ")
            ogrenci["soyisim"] = input("Yeni soyadı girin: ")
            ogrenci["bolum"] = input("Yeni bölüm girin: ")
            ogrenci["not_ortalama"] = float(input("Yeni not ortalamasını girin: "))
            print(f"{numara} numaralı öğrenci başarıyla güncellenmiştir.")
            return
    print("Bu numaraya sahip öğrenci bulunmamaktadır.")

def ogrenci_sil():
    numara = input("Silmek istediğiniz öğrencinin numarasını girin: ")
    for ogrenci in ogrenciler:
        if ogrenci["numara"] == numara:
            ogrenciler.remove(ogrenci)
            print(f"{numara} numaralı öğrenci başarıyla silindi.")
            return
    print("Bu numaraya sahip öğrenci bulunmamaktadır.")

def menu():
    while True:
        print("\nÖğrenci Yönetim Sistemi")
        print("1. Öğrenci Ekle")
        print("2. Öğrencileri Görüntüle")
        print("3. Öğrenci Bilgisi Görüntüle")
        print("4. Öğrenci Güncelle")
        print("5. Öğrenci Sil")
        print("6. Çıkış")

        secim = input("Bir seçenek girin: ")

        if secim == "1":
            ogrenci_ekle()
        elif secim == "2":
            ogrencileri_goruntule()
        elif secim == "3":
            ogrenci_bilgisi_goster()
        elif secim == "4":
            ogrenci_guncelle()
        elif secim == "5":
            ogrenci_sil()
        elif secim == "6":
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")

menu()