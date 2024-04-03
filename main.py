import time
import csv

tlidzeklis = []
cars = []
with open('cars.csv', encoding='utf-8') as csv_file:
    file_reader = csv.reader(csv_file, delimiter = ',', quotechar='"')

    for row in file_reader:
        cars.append(row)

cars.pop(0)
print(cars[0])

def age(car):
    try:
        return int(car[6])
    except Exception as e:
        return 9999
    
def sort_price(cars):
    return int(cars[7])

while True:
    print("-*----------------------*-")
    print("Sveicināts tranpsortlīdzekļu un 'aksesuāru' reģistrā")
    print("-*----------------------*-")
    print("Izvelies savu funkciju!")
    print("1. Atrast vissenāko reģistrēto transportlīdzekli.")
    print("2. Atrast visjaunāko reģistrēto transportlīdzekli.")
    print("3. Atrast vissmagāko reģistrēto transportlīdzekli.")
    print("4. Atrast visvieglāko transporta līdzekli.")
    print("5. Atrast transportlīdzekli pēc indeksa.")
    print("6. Izprintēt stilīgu mašīnu")
    print("7. Iziet")

    choice = input("Ieraksti savu izvēli (1-6): ")

    if choice == '1':
        cars.sort(key = age, reverse = False)
        print(cars[:1])
        pass

    if choice == '2':
        cars.sort(key = age, reverse = True)
        print(cars[:1])
        pass
    
    elif choice == '3':
      tlidzeklis.sort(key = sort_price, reverse = True)
      print(tlidzeklis)
      pass

    elif choice == '4':
      tlidzeklis.sort(key = sort_price, reverse = False)
      print(tlidzeklis)
      pass

    elif choice == '5':
       visi_tlidzekli = 0
       visi_tlidzekli = int(input("Kāds ir jūsu mašīnas kārtas nummurs? Ievadiet to: "))
       print("Mašīnas kārtas nummurs: ", visi_tlidzekli)
       print(cars[visi_tlidzekli])
       pass

    elif choice == '6':
       print("Sāk printēt..")
       time.sleep(0.5)
       print("    ---------------------------.")
       time.sleep(0.5)
       print("  `/""""/""""/|""|'|""||""|   ' \.")
       time.sleep(0.5)
       print("  /    /    / |__| |__||__|      |")
       time.sleep(0.5)
       print(" /----------=====================|")
       time.sleep(0.5)
       print(" | \  /V\  /    _.               |")
       time.sleep(0.5)
       print(" |()\ \W/ /()   _            _   |")
       time.sleep(0.5)
       print(" |   \   /     / \          / \  |-( )")
       time.sleep(0.5)
       print(" =C========C==_| ) |--------| ) _/==] _-_)")
       time.sleep(0.5)
       print("  \_\_/__..  \_\_/_ \_\_/ \_\_/__.__.")
       time.sleep(0.5)
       print(" Izprintējās.")
       pass

    elif choice == '7':
       break
