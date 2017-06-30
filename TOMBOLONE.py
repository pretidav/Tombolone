"""
Author: Francesco Capponi <capponi.francesco87@gmail.com>
        David Preti       <preti.david@gmail.com>

License: BSD 3 clause

"""



import numpy as np



class cartella(object):


    def __init__(self,rows=3):
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
            unit_deca=np.sort(np.random.choice(9, self.__columns,replace=False)*10)+np.random.randint(1, 9,size=self.__columns)
            if(unit_deca[-1]>90):
                unit_deca[-1]=90
            self.scheda[i]=unit_deca

        control=True
        while control:
            control=False
            occur,count=np.unique(self.scheda,return_counts=True)
            for j in [t for t in zip(occur,count) if t[1]>1]:
                control=True
                lenght=len(self.scheda[self.scheda==j[0]])
                numbo=int((j[0]/10))*10+np.random.randint(1, 9,size=lenght)
                if((numbo>90).any()):
                    numbo=80+np.random.randint(1, 10,size=length)
                self.scheda[self.scheda==j[0]]=numbo


    def _lex_fill_cartella(self,ntab=1):
        self.scheda = np.zeros((self.rows, self.__columns))
        inc=np.array([-1,-1,3,3,7,7])
        for i in range(0,self.rows):
            self.scheda[i]= np.asarray(self.__columns*( 2*i + ntab + inc[ntab-1]  )) + np.arange(1, self.__columns+1)



##############################################################################################
##############################################################################################



class tabellone(cartella):

    def __init__(self):
        self.__missings = None


    def fill_tabellone(self):
        """

        Tabellone contains all the numbers from 1 to 90 in lexicographic order, i.e.
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
            A=cartella(3)
            A.lex_fill_cartella(i+1)
            self.tab.append(A.scheda)







class player(tabellone):

    """

    player is an object which can have Ncartella number of cartelle.
	if Ncartella==0 means the player has a tabellone

    """

    def __init__(self,seedplayer):
        self.__seedplayer=seedplayer
        self.prize=dict.fromkeys(['ambo','terna','quaterna','cinquina','tombola'])
        self.__checklist=[2,3,4,5]
        self.__checkbool=[['ambo',False],['terna',False],['quaterna',False],['cinquina',False],['tombola',False]]

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
                C=cartella(3)#to be generalized
                C.fill_cartella(i+self.__seedplayer)
                self.collection.append(C.scheda)
        elif(Ncart==0):
            temp=tabellone()
            temp.fill_tabellone()
            self.collection=temp.tab
        self.__rep=np.zeros([len(self.collection),3])



    def _check_cartella(self,extraction):
        length=(len(self.collection))
        if(length==0):
            raise ValueError('You have to call the \"take_cartella\" method before!')
        for j in range(0,length):
            if extraction in self.collection[j]:
                self.__rep[j,np.where(self.collection[j]==extraction)[0]]+=1
            if(self.__rep[j].sum()==15):
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
