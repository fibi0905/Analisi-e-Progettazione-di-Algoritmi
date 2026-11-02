import sys
import math

N=65

# Reindirizza l'output standard sul file output.txt nella stessa cartella
sys.stdout = open("output.txt", "w", encoding="utf-8")

ris = {}
bugiardi = []
test_B = []
test_NotB = [] 
Zna = []

# True  --> Supera il test per la base 'a' (Non dimostrato composto / Probabilmente primo)
# FasGe --> Fallisce il test (Dimostrato composto / Testimone)
def MCprimalityTest_aux(a: int, s: int, q: int | float, n: int):
    # Passo 5: Calcolo iniziale x = a^q (mod n)
    x = pow(a, int(q), n) 

    # Passo 6: Se il risultato è 1 o -1 (rappresentato da n-1)
    if x == 1 or x == n - 1: 
        print(f"{a}: Non composto")
        return True
    
    # Passo 7: Ciclo delle quadrature successive (eseguito esattamente s volte)
    while s - 1 >= 0:
        x = pow(x, 2, n)
        if x == n - 1: 
            print(f"{a}: Non composto")
            return True
        s = s - 1
        
    # Passo 8: Se non intercettato prima, il numero è composto per la base 'a'
    print(f"{a}: composto")
    return False


def MCprimalityTest(n: int):
    if n < 3 or n % 2 == 0:
        print(f"{n}: non è dispari né maggiore di 3")
        return

    s = 0
    q = n - 1
    while q % 2 == 0:
        s = s + 1
        q = q // 2  # Divisione intera per evitare float nell'esponente
    
    print(f"Dato {n}:\n\ts:{s}\n\tq={int(q)}\n")
    print(f"--------- OUTPUT n:{n} ---------")
    
    # range(2, n-1) analizza le basi da 2 a n-2 (da 2 a 63 per n=N)
    for a in range(2, n - 1):
        ris[a] = MCprimalityTest_aux(a, s, q, n)
        
    print(f"--------- FINE ---------\n")


# 1. Esecuzione del test principale per n = N
MCprimalityTest(N) 

# 2. Suddivisione delle basi in base ai risultati del test
for a, res in ris.items():
    if res: 
        bugiardi.append(a)
    
for a in range(2, (N-1)):
    if math.gcd(a, N) > 1:
        test_B.append(a)

for a, res in ris.items():
    if math.gcd(a, N) == 1 and not res:
        test_NotB.append(a)

# 3. Calcolo del gruppo moltiplicativo Z*_65
for i in range(1, N):
    if math.gcd(i, N) == 1:
        Zna.append(i)


H_65 = []
for a in Zna:
    if ((pow(a,(N-1),N)) == 1):
        H_65.append(a)

def check (sG: list[int], G:list[int]):

    for x in sG:
        for y in sG:
            mod = ((x*y) % N)
            if( mod not in sG):
                
                return f"Non è un gruppo: {x} * {y} mod {N} = {mod} " 
    
    if len(G) % len(sG) != 0:
        return "E un Gruppo, ma non è sottogruppo di Zn"
    else:
        return "E sottogruppo"





# Stampa dei riepiloghi finali nel file di testo
print("Bugiardi (nell'intervallo 2-63): ", bugiardi)
print("Testimoni Banali: ", test_B)
print("Testimoni NON Banali: ", test_NotB)
print("\nZ*_n: ", Zna)
print("Insieme H_n con definzione: ", H_65)
print(check(H_65, Zna), " Verificato su:\n\tGruppo in eseme:",H_65,"\n\tGruppo:", Zna)

# Chiude il file e ripristina l'output sulla console
sys.stdout.close()
sys.stdout = sys.__stdout__