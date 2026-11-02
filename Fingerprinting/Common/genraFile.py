import struct
import sys
import math

# 30 bit di dati, ad esempio il valore 0b101010101010101010101010101010
valore = 0b111011101110111010101010101010  # 30 bit
# Lo impacchetta in 4 byte (32 bit), i primi 30 sono i tuoi dati
dati = struct.pack(">I", valore)  # big-endian, unsigned int 32 bit

with open("fileAlice.bin", "wb") as f:
    f.write(dati)


