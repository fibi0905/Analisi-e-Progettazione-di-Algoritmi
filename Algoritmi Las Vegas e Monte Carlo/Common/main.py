import random
import numpy as np
import matplotlib.pyplot as plt

# ---------DEF---------
N_ELEM = 10000
N_RUN = 10000   

MAX = 100
MIN = 0

totConfronti = []
    # ogni elemento X --> il numero di confornti (mai negativo) 
    # la probabilità che X superi la media è P(X >= a) <= (E[x]/a)
    # se scegliamo come a -> 2E[x] abbiamo che la probabilità è di 1/2 (50%) {nel grafico vediamo che è pessimista}
 

U  = N_ELEM * np.log(N_ELEM) # E[x]
UU = 2 * U # 2E[x]

K=3

notOk = [0]
Ok = [0]

e= 0
# ----------------------


def quicksortLV(lst: list, s: int, f: int, count: list):
    if s >= f:
        return

    # Pivot casuale
    pivot_idx = random.randint(s, f)
    pivot_val = lst[pivot_idx]

    # Sposta il pivot alla fine
    lst[pivot_idx], lst[f] = lst[f], lst[pivot_idx]

    # Partizione in-place (Lomuto)
    store = s
    for i in range(s, f):
        count[0] += 1
        if lst[i] <= pivot_val:
            lst[i], lst[store] = lst[store], lst[i]
            store += 1

    # Rimetti il pivot al posto giusto
    lst[store], lst[f] = lst[f], lst[store]

    quicksortLV(lst, s, store - 1, count)
    quicksortLV(lst, store + 1, f, count)


# --- Calcolo dei confronti nelle N_RUN run ---
for _ in range(N_RUN):
    count = [0]
    listNum = [random.uniform(MIN, MAX) for _ in range(N_ELEM)]
    quicksortLV(listNum, 0, N_ELEM - 1, count)
    totConfronti.append(count[0])

mediaEmp = np.mean(totConfronti)
for x in totConfronti:
    if x >= UU: 
        e += 1




# --- Plot ---
plt.figure()  # nuova finestra
plt.hist(totConfronti, bins=50, color='steelblue', edgecolor='black')
plt.title(f"Distribuzione dei confronti in LVQuickSort |  N={N_ELEM}, Run={N_RUN}")
plt.xlabel("Numero di confronti")
plt.ylabel("Frequenza")

plt.axvline(x=mediaEmp, color='orange', linestyle='-',  linewidth=2, label=f'Media emp: {mediaEmp:.0f}')
plt.axvline(x=U,        color='red',    linestyle=':', linewidth=2, label=f'E[x] = N·ln(N): {U:.0f}')
plt.axvline(x=UU,       color='green',  linestyle=':', linewidth=2, label=f'2E[x]: {UU:.0f}')

plt.legend()
plt.tight_layout()
plt.show()


def quicksortLV_stop(lst: list, s: int, f: int, count: list, limit:int):
    if s >= f:
        return True
    
    if count[0] >= limit:
        return False

    # Pivot casuale
    pivot_idx = random.randint(s, f)
    pivot_val = lst[pivot_idx]

    # Sposta il pivot alla fine
    lst[pivot_idx], lst[f] = lst[f], lst[pivot_idx]

    # Partizione in-place (Lomuto)
    store = s
    for i in range(s, f):
        count[0] += 1
        if lst[i] <= pivot_val:
            lst[i], lst[store] = lst[store], lst[i]
            store += 1

    # Rimetti il pivot al posto giusto
    lst[store], lst[f] = lst[f], lst[store]

    return (quicksortLV_stop(lst, s, store - 1, count, limit) and quicksortLV_stop(lst, store + 1, f, count, limit)); 
     
    

def quicksortMC(listN:list[int], k:int):

    for _ in range(k):
        count = [0]
        listNum = [random.uniform(MIN, MAX) for _ in range(N_ELEM)]

        if quicksortLV_stop(listN, 0, N_ELEM-1, count, (2*mediaEmp)):
            return True
    
    return False
            

for _ in range(N_RUN):
    if quicksortMC (listNum, 3) :
        Ok[0] +=1
    else:
        notOk[0] +=1



print(f"Media empirica:  {mediaEmp:.2f}")
print(f"E[X]  = N*ln(N):    {U:.2f}")
print(f"2E[X] formula(3) = 2*N*ln(N):  {UU:.2f}")
print(f"Elementi sopra limite Markov: {e} ")
print(f"PMF empirica (Formula 4): {(e/N_RUN):.5f}")
print(f"-------------MonteCarlo-------------")
print(f"K= {K}")

print(f"-Probabilità successo: {Ok[0]/N_RUN:.4f}")
print(f"-Probabilità teorica (1 - 1/2^k): {1 - 1/2**K:.4f}")

