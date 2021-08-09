print("Hikaye ve oyun adı ve benzeri bilgileri buraya yaza bilirsiniz.")




#------------------Örnek ayrım-------------------
def soru1_secim1():
    print("1.Secime Göre Hikaye Devamı")


def soru1_secim2():
    print("2.Secime Göre Hikaye Devamı")


def soru1():
    print("""Seçim yapılacak yerin soru kısmıdır.
  [1]Seçim 1
  [2]Secim 2""")

    soru1_secim = int(input(":"))
    if soru1_secim == 1:
        soru1_secim1()
    elif soru1_secim == 2:
        soru1_secim2()
    elif soru1_secim >= 3:
      input("Hata 1:")
      quit()    


soru1()
#------------------Örnek ayrım-------------------
