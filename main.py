import pyGraf #importujemo fajl u kojem se nalazi klasa graf i implementacija njenih metoda

#meni sa opcijima koji se ispisuje prilikom pokretanja programa
print("-"*50)
print("***** GRAFOVI - minimalna s-t udaljenost *****")
print("-"*50)
print("1. BFS")
print("2. DFS")
print("3. Kreiraj testni graf")
print("4. Ispis grafa")
print("5. Ford Fulkerson algoritam")
print("6. Minimalni s-t cut")
print("0 - Zavrsetak programa...")
print("-"*50)

izbor = int(input("Odabir opcije: ")) #unos opcije se automatski pretvara u tip podatka "int"

g = pyGraf.Graf() #kreiramo instancu klase graf

def menu(izbor): #funkcija za odabir opcije menu-a
    match izbor:
        case 0:
            print("Kraj programa!\n") #u slucaju izbora 0 program se automatski zatvara
            exit()
        case 1:
            g.BFS() #odabir 1 - Breadth-first search - trazenje po sirini
        case 2:
            g.DFS() #odabir 1 - Depth-first search - trazenje po dubini
        case 3:
            g.kreirajGraf() #odabir 3 - kreira se testni graf s unaprijed odredjenim vrijednostima
        case 4:
            g.ispis() #ispisuje se tezinska susjedstva kreiranog grafa
        case 5:
            s = int(input("Pocetak: ")) #unos source se pretvara u int
            t = int(input("Kraj: ")) #unos destinacije se pretvara u int
            max_flow = g.FordFulkerson(s, t) #poziv metode za Fold Fulkerson algoritam - proracun maximum flowa grafa
            print("Maksimalni protok u grafu je: " + str(max_flow))
        case 6:
            s = int(input("Pocetak: ")) #unos source se pretvara u int
            t = int(input("Kraj: ")) #unos destinacije se pretvara u int
            g.minCut(s, t) #poziv metode za izracunavanje i ispis minimalnog odsjecka grafa
        case _:
            print("Pogresan unos!") #u slucaju da se izabere pogresna opcija

while (izbor): #petlja se ponavlja sve dok se ne odabere kraj programa - opcija 0
    menu(izbor)
    izbor = int(input("Odabir opcije: ")) #nakon svakog unosa nudi se mogucnog narednog unosa



  

  
