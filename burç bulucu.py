import time
# ilk kısım = gün.ay.yıl mevzusu


print("Burç Hesaplama Makinesi")

onay = ""

while True:

 while True:
    try:
        doğum_günü = int(input("Doğumgünü: "))
        if not (32 > doğum_günü > 0):
            print("Lütfen gün aralığına dikkat ediniz!")
            continue
        else:
            break
    except ValueError:
        print("Lütfen sayıyla giriniz!")
        continue

 while True:
    try:
        doğum_ayı = int(input("Doğumayı: "))
        if not 13 > doğum_ayı > 0:
            print("Lütfen gün aralığına dikkat ediniz!")
            continue
        else:
            break
    except ValueError:
        print("Lütfen sayıyla giriniz!")
        continue

 while True:
    try:
        doğum_yılı = int(input("Doğumyılı: "))
        if len(str(doğum_yılı)) != 4:
            print("Lütfen yılı doğru girdiğinize dikkat ediniz!")
            continue
        else:
            break
    except ValueError:
        print("Lütfen sayıyla giriniz!")
        continue
 
 print("Verileriniz: ")
 print(f"{doğum_günü}.{doğum_ayı}.{doğum_yılı}")
 
 onay = input("Onaylıyor musunuz(evet/hayır): ").lower()

 if onay == "evet".lower() or "hayır".lower():
  if onay == "evet".lower() :
    print("Verileriniz: ")
    print(f"{doğum_günü}.{doğum_ayı}.{doğum_yılı}")
    break
  elif onay == "hayır":
    continue

time.sleep(2)

if (31 >= doğum_günü >= 21 and doğum_ayı == 3) or (19 >= doğum_günü >= 1 and doğum_ayı==4):
   print(f"{doğum_günü}.{doğum_ayı}.{doğum_yılı}")
   print("Burcunuz: KOÇ")
elif (30 >= doğum_günü >= 20 and doğum_ayı == 4) or (20 >= doğum_günü >= 1 and doğum_ayı==5):
   print(f"{doğum_günü}.{doğum_ayı}.{doğum_yılı}")
   print("Burcunuz: BOĞA")   
elif (31 >= doğum_günü >= 21 and doğum_ayı == 5) or (20 >= doğum_günü >= 1 and doğum_ayı==6):
   print(f"{doğum_günü}.{doğum_ayı}.{doğum_yılı}")
   print("Burcunuz: İKİZLER")
elif (30 >= doğum_günü >= 21 and doğum_ayı == 6) or (22 >= doğum_günü >= 1 and doğum_ayı==7):
   print(f"{doğum_günü}.{doğum_ayı}.{doğum_yılı}")
   print("Burcunuz: YENGEÇ")
elif (31 >= doğum_günü >= 23 and doğum_ayı == 7) or (22 >= doğum_günü >= 1 and doğum_ayı==8):
   print(f"{doğum_günü}.{doğum_ayı}.{doğum_yılı}")
   print("Burcunuz: ASLAN")
elif (31 >= doğum_günü >= 23 and doğum_ayı == 8) or (22 >= doğum_günü >= 1 and doğum_ayı==9):
   print(f"{doğum_günü}.{doğum_ayı}.{doğum_yılı}")
   print("Burcunuz: BAŞAK")
elif (30 >= doğum_günü >= 23 and doğum_ayı == 9) or (22 >= doğum_günü >= 1 and doğum_ayı==10):
   print(f"{doğum_günü}.{doğum_ayı}.{doğum_yılı}")
   print("Burcunuz: TERAZİ")
elif (31 >= doğum_günü >= 23 and doğum_ayı == 10) or (21 >= doğum_günü >= 1 and doğum_ayı==11):
   print(f"{doğum_günü}.{doğum_ayı}.{doğum_yılı}")
   print("Burcunuz: AKREP")
elif (30 >= doğum_günü >= 22 and doğum_ayı == 11) or (21>= doğum_günü >= 1 and doğum_ayı==12):
   print(f"{doğum_günü}.{doğum_ayı}.{doğum_yılı}")
   print("Burcunuz: YAY")
elif (31 >= doğum_günü >= 22 and doğum_ayı == 12) or (19 >= doğum_günü >= 1 and doğum_ayı==1):
   print(f"{doğum_günü}.{doğum_ayı}.{doğum_yılı}")
   print("Burcunuz: OĞLAK")
elif (31 >= doğum_günü >= 20 and doğum_ayı == 1) or (18 >= doğum_günü >= 1 and doğum_ayı==2):
   print(f"{doğum_günü}.{doğum_ayı}.{doğum_yılı}")
   print("Burcunuz: KOVA") # şubatlı 
elif (28 or 29 >= doğum_günü >= 19 and doğum_ayı == 2) or (20 >= doğum_günü >= 1 and doğum_ayı==3):
   print(f"{doğum_günü}.{doğum_ayı}.{doğum_yılı}")
   print("Burcunuz: BALIK") # şubatlı



      













     


