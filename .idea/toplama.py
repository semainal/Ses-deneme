import random
import math

sayi1 = int(random.randint(0,10))
sayi2 = int(random.randint(0,10))

print(sayi1,'+' ,sayi2)
sonuc = int(input("Sonuç:"))

toplam = int(sayi1 + sayi2)

if sonuc == toplam:
    print("doğru")
else:
    print("yanlış")