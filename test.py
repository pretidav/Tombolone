from TOMBOLONE import cartella,tabellone
import numpy as np
A=cartella(3)
A.fill_cartella(1500)
B=cartella(3)
C=tabellone()
C.fill_tabellone()

for i in range(1,7):
    B.lex_fill_cartella(i)
    print B.scheda 
print "\n\n"
print A.scheda
print "\n\n"
print C.tab[1]
