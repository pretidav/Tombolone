

from TOMBOLONE import cartella,tabellone,player,partita
import numpy as np

#"""
#A=cartella(5)
#A.fill_cartella(1500)
#C=tabellone(5)
#C.fill_tabellone()

#for i in range(1,7):
#    B.lex_fill_cartella(i)
#    print B.scheda
#print "\n\n"
#print A.scheda
#print "\n\n"
#print C.tab[0]
#print C.tab[1]
#print C.tab[2]
#print C.tab[3]
#print C.tab[4]
#print C.tab[5]

#david=player(100,2)
#david.take_cartella(2)
#for j in range(0,len(david.collection)):
#    print(david.collection[j])
#for i in range(0,2):
#    for j in range(0,5):
#        num=david.collection[0][i,j]
#        print("test number = ", num)
#        david.check_cartella(num)
#"""

A=partita(1,[1],3)
A.play()
