"""
Author: Francesco Capponi <capponi.francesco87@gmail.com>
        David Preti       <preti.david@gmail.com>

License: BSD 3 clause

"""



"""
Cartella   
----------------------------------
| x11  		x12  	...  	x15  | 
| x22 		x22 	... 	x25  |	
| x33 		x32		...		x35  |
----------------------------------

Tabellone contains all the numbers from 1 to 90 in lexicographic order, i.e. 
------------------------------------------------------------
| 1  		2  		... 	5   | 6		7		...		10 | 
| 11 		12 		... 	15  | 16	17		...		20 |	
| 21 		22		...		25  | 26	27		...		30 |
------------------------------------------------------------
| ...		...		...		... | ...	...		...		...|
------------------------------------------------------------
| 31		32		...		35	| 36	37		...		40 |
| ...		...		...		...	| ...	...		...		...|
| 81		82		...		85  | 86 	87		...		90 |
------------------------------------------------------------
"""



import numpy as np





class cartella(object):


    def __init__(self,rows):
        self.rows=rows
        if not isinstance(self.rows, int):
            raise ValueError('Number of rows has to be an integer!')
        self.__columns=5
        #self.__missings = None
        #self.__ifcount = True
        #self.__trs = 0.



    def fill_cartella(self, seed=1234):

        """

            Fill our cartella according to the italian convention
            Parameters
            ----------
            seed : int type

            Return:

            self.cartella: numpy array type, shape=[self.rows,self.__columns]

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
                numbo=int((j[0]/10))*10+np.random.randint(1, 9,size=j[1])
                if((numbo>90).any()):
                    numbo=80+np.random.randint(1, 10,size=j[1])
                self.scheda[self.scheda==j[0]]=numbo


    def _lex_fill_cartella(self,ntab=1):
        if not isinstance(ntab, int):
            raise ValueError('ntab has to be a strictly positive integer <=6 !')
        if(ntab<=0 or ntab>7):
        	raise ValueError('ntab has to be a strictly positive integer <=6 !')  
        self.scheda = np.zeros((self.rows, self.__columns))

        for i in range(0,self.rows):
        	if(ntab<3):
        		self.scheda[i]= list(np.asarray(self.__columns*( 2*i + ntab -1  )) + range(1, self.__columns+1))  
        	if(ntab>2 and ntab <5):
        		self.scheda[i]= list(np.asarray(self.__columns*( 2*i + ntab -1 +4 )) + range(1, self.__columns+1))
        	if(ntab>4 and ntab <7):	
        		self.scheda[i]= list(np.asarray(self.__columns*( 2*i + ntab -1 +8 )) + range(1, self.__columns+1))


class tabellone(cartella):

    def fill_tabellone(self):

	   return self._fill_tabellone()


 ##############################################################################################

    def _fill_tabellone(self):
     
#         for i in range(0,6):
#        	self.tab.append(cartella)   








#class player(cartella):

	"""
		player is an object which can have Ncartella number of cartelle. 
		if Ncartella==0 means the player has a tabellone
	"""

#	def __init__(self,Ncart):
#		self.Ncart=Ncart
#		if not isinstance(self.Ncart, int):
 #      		raise ValueError('Number of Cartelle has to be an integer!')
        #self.__missings = None
        #self.__ifcount = True
        #self.__trs = 0.


  #  def check_cartella(self):

        """

            Fill our cartella according to the italian convention
            Parameters
            ----------
            seed : int type

            Return:

            self.cartella: numpy array type, shape=[self.rows,self.__columns]

        """

   #     return self._check_cartella()

    #def check_tabellone(self):

        """

            Fill our cartella according to the italian convention
            Parameters
            ----------
            seed : int type

            Return:

            self.cartella: numpy array type, shape=[self.rows,self.__columns]

        """

 #       return self._check_tabellone()




 ##############################################################################################

  #  def _check_cartella(self):

	#TODO

  #  def _check_tabellone(self):

	#TODO
