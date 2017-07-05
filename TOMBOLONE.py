"""

Author: Francesco Capponi <capponi.francesco87@gmail.com>
        David Preti       <preti.david@gmail.com>

License: BSD 3 clause

"""



import numpy as np
import time



class cartella(object):

    """
        Creation of "cartella" class, the basic building block for tombola game.
    
        Private parameters
        ----------
        __columns : int 
        cartella is a numpy array with rows*__columns numbers. In the traditional game __columns=5.
        
        Attributes
        ----------
        rows : int
        number of rows of our cartella. The default is set ==3 but can be changed by users to generalize the game.
    """


    

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
        np.random.seed(seed)
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
            A=cartella(self.rows)
            A.lex_fill_cartella(i+1)
            self.tab.append(A.scheda)







class player(tabellone):

    """

    player is an object which can have Ncartella number of cartelle.
	if Ncartella==0 means the player has a tabellone

    """

    def __init__(self,rows):
        self.prize=dict.fromkeys(['ambo','terna','quaterna','cinquina','tombola'])
        self.__checklist=[2,3,4,5]
        self.__checkbool=[['ambo',False],['terna',False],['quaterna',False],['cinquina',False],['tombola',False]]
        self.rows=rows


    def take_cartella(self,Ncart):
        """                                                                                                                                      
                                                                                                                                                     
            Draw Ncart cartella if Ncart==0 is the cartellone (e.g. 6 cartelle ordered lexicographically)                                                                                     
            Parameters                                                                                                                                 
            ----------                                                                                                                                 
            Ncart : int type                                                                                                                           
                                                                                                                                                       
            Return:                                                                                                                                    
            self.collection = list of Ncart cartella objects


        """
            
        return self._take_cartella(Ncart)

    def check_cartella(self,extraction):

        """
           
           Check in every cartella if the following configuration are satisfyed: 
           ambo     = two numbers on the same row
           terna    = three numbers on the same row
           quaterna = four numbers on the same row
           cinquina = five numbers on the same row
           tombola  = all the number inside cartella (default 15 numbers)

           Parameters:
           -----------
           extraction = int type 
           the number to be checked 

           Return:
           -------
           self.prize = a dictionary with keys "ambo,terna,quaterna,cinquina,tombola" corresponding to boolean variables True, False
           by default all the prizes are set to False, and turned to True once some of the above conditions are satisfyed.
        
        """

        return self._check_cartella(extraction)


 ##############################################################################################

    def _take_cartella(self,Ncart):
        if(Ncart>0):
            self.collection=[]
            #np.random.seed(self.__seedplayer)
            for i in range(0,Ncart):
                C=cartella(self.rows)
                timeseed = int((time.time() - np.fix(time.time()))*10**5)
                C.fill_cartella(timeseed)
                self.collection.append(C.scheda)
        elif(Ncart==0):
            temp=tabellone(self.rows)
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
            if(self.__rep[j].sum()==(self.rows*5)):
                self.prize['tombola']=True

        for j in range(0,len(self.__checklist)):
            if (self.__rep==self.__checklist[j]).any(): self.__checkbool[j][1]=True
        index=[i[0] for i in enumerate(self.__checkbool) if i[1][1]]
        if(len(index)>0):
            self.prize[self.__checkbool[index[0]][0]]=True

        self.__checklist=[d for (d, [blobo,remove]) in zip(self.__checklist, self.__checkbool) if not remove]
        self.__checkbool=[[d,j] for d,j in self.__checkbool if not j]


 ##############################################################################################

class partita(player):

    def __init__(self,Nplayer,cartlist,rows):
        self.__Nplayer=Nplayer
        if not isinstance(self.__Nplayer, int):
            raise ValueError('Number of players has to be an integer!')
        self.__cartlist=cartlist
        if not isinstance(self.__cartlist,list):
            raise ValueError('list of cartelle is not a list!')
        elif not all(isinstance(s, int) for s in cartlist):
            raise ValueError('cartlist has to be a list of integers!')
        elif(len(self.__cartlist)!=Nplayer):
            raise ValueError('list of cartelle has to have Nplayer length!')
        self.rows=rows
        if not isinstance(self.rows,int):
            raise ValueError('Number of rows has to be int!')
        self.prizes=['ambo','terna','quaterna','cinquina','tombola']

    def play(self):
        """

           Is the main class, simulating a Tombola round with a given extracted random value among Nplayer platers. 

           Parameters:
           ----------
           Nplayer = int type 
           total number of players
           cartlist = numpy array with the number of cartella for each player. len(cartlist) == Nplayer
           rows = is the number of rows which is used in all the subclasses.
        

        """
        return self._play()

    def log(self):

        """

           Print to file the log of Partita, in a csv format the player identified by the number of cartellas taken with take_cartella, the prize won, and the turn (meaning the number of random extractions) after which the prize is won. 

           Ncart, "prize", turn  


        """
        
        return self._log()

###########################################################################################
###########################################################################################

    def _play(self):
        extractions=np.arange(1,self.rows*30+1)
        np.random.shuffle(extractions)
        players=[]
        self.player_prizes=[]
        for i in range(0,self.__Nplayer):
            A=player(self.rows)
            A.take_cartella(self.__cartlist[i])
            players.append(A)
            self.player_prizes.append(dict())

     #   for i in players:
     #       print i.collection

        for i in range(0,self.rows*30):
            for j in players:
                j.check_cartella(extractions[i])
            if(i>=1):
                check=False
                for k in range(0,len(players)):
                    if (len(self.prizes)):
                        if(players[k].prize[self.prizes[0]]==True):
                            self.player_prizes[k][self.prizes[0]]=i+1
                            check=True
                if(check):
                    self.prizes.remove(self.prizes[0])




    def _log(self):
        for i in range(0,len(self.player_prizes)):
            for j,l in self.player_prizes[i].items():
                print self.__cartlist[i],",",j,",",l
