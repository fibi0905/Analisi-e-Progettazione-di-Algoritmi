import struct
import sys
import math
import random

N_BIT = 30
K = 10000

arrPrim = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887]


sys.stdout = open("output.txt", "w", encoding="utf-8")


def bits_to_decimal(filename):
    with open(filename, "rb") as f:
        dati = f.read()
    
    # Converti i byte in una stringa di bit
    bits = ''.join(format(byte, '08b') for byte in dati)
    
    # Converti la stringa di bit in decimale
    return int(bits, 2)



def GetP () -> int:
    return random.choice(arrPrim) 

def MCStringEqualityVerifer(a:int, b:int, p:int):
    fa = a % p
    fb = b % p

    return ((abs (fa-fb) % p) == 0) 



p = GetP()
a = bits_to_decimal("fileAlice.bin")
b = bits_to_decimal("fileBob.bin")

# Esempio d'uso
print(f"Decimale letto in fileAlice.bin: {a}")
print(f"Decimale letto in fileBob.bin: {b}")
print("\n-------- Inizio MCStringEqualityVerifer --------\n")
print("array di numeri primi: ", arrPrim)
print(f"Dimensione array: {len(arrPrim)}")

print(f"Numero p random: {p}\n")

print(f"Esiti per {K} volte :")

arrNumFalsi = []

for i in range(0,K):

    if(MCStringEqualityVerifer(a,b,p)):
        if(p not in  arrNumFalsi): arrNumFalsi.append(p)
        print(f"\t{i+1}: I file sono uguali")
    else:
        print(f"\t{i+1}: I file NON sono uguali")
    
    p = GetP()
    print(f"Tentativo con {p}: ")


print("\n-------- Fine MCStringEqualityVerifer --------\n")

if(len(arrNumFalsi) != 0):

    print("I numeri che hanno generato un falso positivo sono: \n", arrNumFalsi)

sys.stdout.close()
sys.stdout = sys.__stdout__