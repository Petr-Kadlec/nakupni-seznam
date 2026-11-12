
def ulozit_nakup(nakup):
    with open("nakup.txt", "w", encoding="utf-8") as soubor:
     for polozka , cena in nakup.items():
      soubor.write(f"{polozka};{cena}\n")
      
def nacti_nakup():
    nakup = {}
    try:
       with open("nakup.txt", "r", encoding="utf-8") as soubor:
        for radek in soubor:
         radek =radek.strip()
         nazev , cena = radek.split(";")
         nakup[nazev] = int(cena)
    except FileNotFoundError:
        pass      # „nic nedělej“, prostě se vrátí prázdný slovník
   
    return nakup
nakup = nacti_nakup()    

def add():
 
 while True:
    polozka = input("napis jméno produktu co chceš přidat do seznamu a nebo stop pro konec přidávání ")
    
    
    
    if polozka == "stop":
     break
    while True:


     try:
      cena = input("napis cenu produktu co chceš přidat do seznamu  ")
      cena = int(cena)
      break
     except ValueError:
       print("neplatný formát čísla")
       
    nakup[polozka] = cena  
      
    
    
   
    
  
 


def vypisseznam():
   if len(nakup) == 0:
      print("seznam je prázdný")
   else:
    for polozka , cena in nakup.items():
      print(f"seznam obsahuje {polozka} s cenou  {cena} ")
   
def celkovacena(nakup):
   Celkem = 0
   for  nazev, cena in nakup.items():
      Celkem = Celkem + cena
   return Celkem
   
   




   
while True:
    volba = input("co chceš dělat \n 1 přidat do nákupu \n 2 vypsat položky nákupu  \n 3 odejít z programu \n 4 vypsat celkovou cenu nákupu")
    if volba == "1":
        add()
    elif volba == "2":
        vypisseznam()
    elif volba == "3":
        ulozit_nakup(nakup)
        break
    elif volba == "4":
        print(f" celkova cena nákupu je {celkovacena(nakup)}")
    else:
        print("Neznámá volba, zkus to znovu.")





