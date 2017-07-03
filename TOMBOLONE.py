"""
Author: Francesco Capponi <capponi.francesco87@gmail.com>
        David Preti       <preti.david@gmail.com>

License: BSD 3 clause

"""



import numpy as np



class cartella(object):


    def __init__(self,rows):
        self.rows=rows
        if not isinstance(self.rows, int):
            raise ValueError('Number of rows has to be an integer!')
        self.__columns=5



    def fill_cartella(self, seed=1234):

        """

            Fill our cartella according to the italian convention
            Parameters
            ----------
            seed : int type

            Return:

            self.cartella: numpy array type, shape=[self.rows,self.__columns]

                        Cartella
            ----------------------------------
            | x11  		x12  	...  	x15  |
            | x22 		x22 	... 	x25  |
            | x33 		x32	...     x35  |
            ----------------------------------

        """

        return self._fill_cartella(seed)



    def lex_fill_cartella(self,ntab=1):

        """

            Fill our cartella according to be a part of Cartellone
            Parameters
            ----------
            ntab : is the position in Cartellone

            Return:

            self.cartella: numpy array type, shape=[self.rows,self.__columns]

        """

        return self._lex_fill_cartella(ntab)



 ##############################################################################################

    def _fill_cartella(self,seed=1234):

        if not isinstance(seed, int):
            raise ValueError('Random seed has to be an integer!')
        self.scheda = np.zeros((self.rows, self.__columns))

        for i in range(0,self.rows):
            unit_deca=np.sort(np.random.choice((self.rows*3), self.__columns,replace=False)*10)+np.random.randint(1, 9,size=self.__columns)
            if(unit_deca[-1]>(self.rows*30)):
                unit_deca[-1]=(self.rows*30)
            self.scheda[i]=unit_deca

        control=True
        while control:
            control=False
            occur,count=np.unique(self.scheda,return_counts=True)
            for j in [t for t in zip(occur,count) if t[1]>1]:
                control=True
                lenght=len(self.scheda[self.scheda==j[0]])
                numbo=int((j[0]/10))*10+np.random.randint(1, (self.rows*3),size=lenght)
                if( (numbo>(self.rows*30)).any() ):
                    numbo=(self.rows*30-10)+np.random.randint(1, 10,size=length)
                self.scheda[self.scheda==j[0]]=numbo


    def _lex_fill_cartella(self,ntab=1):
        self.scheda = np.zeros((self.rows, self.__columns))
        inc=np.zeros(6)
        for j in range(0,3):
            inc[2*j]=(self.rows-1)*2*j   -1 
            inc[2*j+1]=(self.rows-1)*2*j -1
        for i in range(0,self.rows):
            self.scheda[i]= np.asarray(self.__columns*( 2*i + ntab + inc[ntab-1]  )) + np.arange(1, self.__columns+1)




##############################################################################################
##############################################################################################



class tabellone(cartella):

    def __init__(self,rows):
        self.rows=rows

    def fill_tabellone(self):
        """

        Tabellone contains all the numbers from 1 to (rows*5*6) in lexicographic order, i.e. if rows==3 : 

        --------------------------------------------------------------------------------------------
        | 1  		2  		... 	5   | 6		7		...		10 |
        | 11 		12 		... 	15  | 16	17		...		20 |
        | 21 		22		...	25  | 26	27		...		30 |
        --------------------------------------------------------------------------------------------
        | ...		...		...	... | ...	...		...		...|
        --------------------------------------------------------------------------------------------
        | 31		32		...	35  | 36	37		...		40 |
        | ...		...		...	... | ...	...		...		...|
        | 81		82		...	85  | 86 	87		...		90 |
        --------------------------------------------------------------------------------------------

        """
        return self._fill_tabellone()

 ##############################################################################################



    def _fill_tabellone(self):

        self.tab=[]
        for i in range(0,6):
            A=cartella(self.rows)   #to be generalized 
            A.lex_fill_cartella(i+1)
            self.tab.append(A.scheda)







class player(tabellone):

    """

    player is an object which can have Ncartella number of cartelle.
	if Ncartella==0 means the player has a tabellone

    """

    def __init__(self,seedplayer,rows):
        self.__seedplayer=seedplayer
        self.prize=dict.fromkeys(['ambo','terna','quaterna','cinquina','tombola'])
        self.__checklist=[2,3,4,5]
        self.__checkbool=[['ambo',False],['terna',False],['quaterna',False],['cinquina',False],['tombola',False]]
        self.rows=rows
	if not isinstance(self.__seedplayer, int):
            raise ValueError('Player ID has to be an integer!')


    def take_cartella(self,Ncart):
        return self._take_cartella(Ncart)

    def check_cartella(self,extraction):
        return self._check_cartella(extraction)


 ##############################################################################################

    def _take_cartella(self,Ncart):
        if(Ncart>0):
            self.collection=[]
            for i in range(0,Ncart):
                C=cartella(self.rows)#to be generalized
                C.fill_cartella(i+self.__seedplayer)
                self.collection.append(C.scheda)
        elif(Ncart==0):
            temp=tabellone()
            temp.fill_tabellone()
            self.collection=temp.tab
        self.__rep=np.zeros([len(self.collection),self.rows])



    def _check_cartella(self,extraction):
        length=(len(self.collection))
        if(length==0):
            raise ValueError('You have to call the \"take_cartella\" method before!')
        for j in range(0,length):
            if extraction in self.collection[j]:
                self.__rep[j,np.where(self.collection[j]==extraction)[0]]+=1
            if(self.__rep[j].sum()==(self.rows*5)):#to be generalized 
                self.prize['tombola']=True
                
        for j in range(0,len(self.__checklist)):
            if (self.__rep==self.__checklist[j]).any(): self.__checkbool[j][1]=True
        index=[i[0] for i in enumerate(self.__checkbool) if i[1][1]]
        if(len(index)>0):
            self.prize[self.__checkbool[index[0]][0]]=True

        self.__checklist=[d for (d, [blobo,remove]) in zip(self.__checklist, self.__checkbool) if not remove]
        self.__checkbool=[[d,j] for d,j in self.__checkbool if not j]

        print(self.__rep)
        print(self.prize)





#TODO
class partita(player):

    """
    partita is an object which takes as input a list of a list with pairs {(playerID,Ncart)}. 
    It ends when a player scores tombola, and report a log of prizes for every player.
    """

    def __init__(self,Nplayer,cartlist,rows):
        self.__Nplayer=Nplayer
        if not isinstance(self.__Nplayer, int):
            raise ValueError('Number of players has to be an integer!')
        self.__cartlist=cartlist
        if not isinstance(self.__cartlist,):
             raise ValueError('list of cartelle is not a list!')
        if(len(self.__cartlist)!=Nplayer):
             raise ValueError('list of cartelle has to be have Nplayer length!')

    def start(self,seedplay):
        return self._start(seedplay)

    def log(self):
        return self._log()
        
###########################################################################################
###########################################################################################

    def _start(self,seedplay):
        extractions=np.arange(1,91)
        np.random.shuffle(extractions) #seed? 
        for i in range(0,len(extractions)):
            print i

