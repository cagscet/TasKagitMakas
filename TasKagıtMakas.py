import random

print("-" * 30 + "\nRock, Paper, Scissors\n" + "-" * 30)

kullanici_skor, pc_skor = 0, 0

while True:
    print("\n1 - Rock\n2 - Paper\n3 - Scissors")
    kullanici_secimi = input("Senin seçimin : ")
    pc_choice = random.choice(["1", "2", "3"])

    if kullanici_secimi == "1":
        if pc_choice == "1":
            print("Bilgisayarın seçimi de Rock. Şu an durum eşit.")
        elif pc_choice == "2":
            print("Bilgisayarın seçimi Paper. Bu raundu kaybettin.")
            pc_skor += 1
        elif pc_choice == "3":
            print("Sen kazandın! Bilgisayar makas seçti.")
            kullanici_skor += 1
    elif kullanici_secimi == "2":
        if pc_choice == "1":
            print("Sen kazandın! Bilgisayar taşı seçti.")
            kullanici_skor += 1
        elif pc_choice == "2":
            print("Bilgisayarın seçimi de kağıt. Şu an durum eşit.")
        elif pc_choice == "3":
            print("Bilgisayarın seçimi makas. Bu raundu kaybettin.")
            pc_skor += 1
    elif kullanici_secimi == "3":
        if pc_choice == "1":
            print("Bu raoundu kaybettin. Bilgisayar taşı seçti.")
            pc_skor += 1
        elif pc_choice == "2":
            print("Sen kazandın! Bilgisayar kağıt seçti.")
            kullanici_skor += 1
        elif pc_choice == "3":
            print("Durum berabere. Bilgisayar da makas seçti.")
    else:
        break

    if kullanici_skor == 3:
        print("Kullanıcı kazandı,Oyun bitti.")
        break

    elif pc_skor == 3:
        print("PC kazandı,Oyun bitti. ")
        break

    print("\nSenin skorun: {}\nPC skoru: {}".format(kullanici_skor, pc_skor))


