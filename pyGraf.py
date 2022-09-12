# Ajdin Bukvic (21.1.2022)
# Algoritmi i strukture podataka - UNZE/PTF - Softversko inzenjerstvo (2. godina)
# Seminarski rad: Minimalna udaljenost s - t za grafove
# Izvorni kod je preuzet sa web stranica:
# https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/
# https://www.geeksforgeeks.org/minimum-cut-in-a-directed-graph/
# NAPOMENA: 
# kod je detaljno preveden, modifikovan i prilagodjen trazenim potrebama
# dodani potrebni komentari i uredjen ispis

from collections import defaultdict #koristenje potrebne biblioteke da bi program radio uspjesno
  
class Graf: #definisanje klase GRAF -> usmjereni graf -> rezidualni graf
  
    def __init__(self, g = None): #inicijalizacija objekta klase - atributi su po defaultu None ili 0
        self.graf = g  
        self.originalni_graf = None
        self.redovi = 0 
        self.kolone = 0
  
    def BFS(self, s, t, roditelj): #algoritam Breadth-first search
  
        posjecen = [False]*(self.redovi) #postavlja se defaulta vrijednost svih vrhova na NEPOSJECEN (FALSE)
        redNiz = [] #kreira se pomocni red
  
        redNiz.append(s) #u red se smjesta prvi element, odnosno izvor - S
        posjecen[s] = True #postavlja se posjecenost izvora S na TRUE
  
        while redNiz: #sve dok postoje elementi u redu petlja se izvrsava
            trenutniVrh = redNiz.pop(0) #vraca se element na indeksu 0 iz reda i smjesta se u pomocnu varijablu
            
            #pretrazuju se svi susjedni vrhovi trenutnug vrha

            for ind, val in enumerate(self.graf[trenutniVrh]): 
                if posjecen[ind] == False and val > 0 : 
                    #ako susjedni vrh nije posjecen onda se postavlja na TRUE i dodaje se u red
                    redNiz.append(ind) 
                    posjecen[ind] = True 
                    roditelj[ind] = trenutniVrh #roditelj posjecenog vrha postaje trenutni vrh
        
        return True if posjecen[t] else False #metoda vraca TRUE ako postoji put izmedju s - t, u suprotnom vraca FALSE
          
    def DFS(self, graf, s, posjecen): #algoritam Depth-first search

        posjecen[s] = True #postavlja se posjecenost izvora S na TRUE

        for i in range(len(graf)):
            if graf[s][i] > 0 and not posjecen[i]:
                self.DFS(graf,i,posjecen) #rekurzivno posjecivanje svih susjednih vrhova od pocetnog vrha
    
    def kreirajGraf(self): #kreiranje tezinske matrice formata n x k (redovi x kolone) => redovi == kolone [kvadratna matrica: n x n]

        testGraf = [[0, 16, 13, 0, 0, 0], 
                    [0, 0, 10, 12, 0, 0], 
                    [0, 4, 0, 0, 14, 0], 
                    [0, 0, 9, 0, 0, 20], 
                    [0, 0, 0, 7, 0, 4], 
                    [0, 0, 0, 0, 0, 0]]

        #postavljanje osnovnih parametara grafa na nove vrijednosti

        self.graf = testGraf
        self.redovi = len(testGraf) 
        self.kolone = len(testGraf[0]) 
        self.originalni_graf = [i[:] for i in testGraf] #kopiraju se vrijednosti testnog grafa u originalni graf
        print("Kreirali ste testni graf!")

    def ispis(self): #ispis tezinske matrice grafa

        if(self.graf == None):
            print("Graf jos uvijek nije kreiran!") #ako graf nije kreiran ispisuje se odgovarajuca poruka

        else:

            print("Sadrzaj grafa:")
            
            for i in range(self.redovi): 
                print("Vrh:", i, end = " : ") #detaljan prikaz vrhova i njihovih ivica
                for j in range(self.kolone):
                    print(j, end = " --- ") 
                    print("(" + str(self.graf[i][j]) + ")", end = "  ") #ispis tezina izmedju vrhova
                print()

    def FordFulkerson(self, s, t): #metoda za Ford Fulkerson algoritam

        if(self.graf == None):
            print("Graf jos uvijek nije kreiran!") #ako graf nije kreiran ispisuje se odgovarajuca poruka

        else:
            
            roditelj = [-1]*(self.redovi) #pomocni niz u koji ce BFS spremiti put
            max_flow = 0 #smatra se da na pocetku nema protoka i postavlja se na 0
    
            while self.BFS(s, t, roditelj): #sve dok postoji put od s - t petlja se izvrsava
    
                path_flow = float("Inf")
                temp = t #vrijednost ponora/destinacije se smjesta u pomocnu varijablu
                while(temp != s): #sve dok je pomocna varijabla razlicita od izvora petlja se izvrsava
                    path_flow = min(path_flow, self.graf[roditelj[temp]][temp]) #uzima se minimalna vrijednost puta
                    temp = roditelj[temp] 
    
                max_flow += path_flow #dodaje se vrijednost puta u maksimalni protok
    
                v = t #vrijednost ponora/destinacije se smjesta u pomocnu varijablu
                while(v != s): #sve dok je pomocna varijabla razlicita od izvora petlja se izvrsava
                    u = roditelj[v] 
                    self.graf[u][v] -= path_flow 
                    self.graf[v][u] += path_flow 
                    v = roditelj[v] 
                    #mijenjaju se kapaciteti ivica
            
            return max_flow #vraca se maksimalni protok

    def minCut(self, s, t): #metoda za Minimalni s - t odsjecak

        if(self.graf == None):
            print("Graf jos uvijek nije kreiran!") #ako graf nije kreiran ispisuje se odgovarajuca poruka

        else:

            protok = self.FordFulkerson(s, t) #poziv metode za Ford Fulkersonov algoritam 
    
            posjecen = len(self.graf)*[False] #postavlja se defaulta vrijednost svih vrhova na NEPOSJECEN (FALSE)
            self.DFS(self.graf,s,posjecen) #poziv metode DFS algoritma koja posjecuje vrhova od izvora S

            print("Prikaz izracunate putanje: ")

            for i in range(self.redovi): 
                for j in range(self.kolone): 
                    if self.graf[i][j] == 0 and\
                    self.originalni_graf[i][j] > 0 and posjecen[i]: 
                        print("S(" + str(i) + ")" + " - " + "T(" + str(j) + ") --- tezina: [",self.originalni_graf[i][j],"]")
                    #ispisuju se sve ivice koje su na pocetku imale tezinu vecu od 0, a sada imaju tezinu jednaku 0
            
            print("Maksimalni protok u grafu je: " + str(protok)) #ispis maksimalnog protoka grafa
