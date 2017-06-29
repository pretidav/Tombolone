#!/usr/bin/python

from TOMBOLONE import cartella,tabellone,player
import numpy as np
#A=cartella(3)
#A.fill_cartella(1500)
C=tabellone()
C.fill_tabellone()

#for i in range(1,7):
#    B.lex_fill_cartella(i)
#    print B.scheda
#print "\n\n"
#print A.scheda
#print "\n\n"
#print C.tab[1]

david=player(100)
david.take_cartella(0)

#print david.collection
