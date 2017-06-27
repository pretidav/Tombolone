"""
Author: Francesco Capponi <capponi.francesco87@gmail.com>
        David Preti       <preti.david@gmail.com>

License: BSD 3 clause

"""

import numpy as np





class cartella(object):

    """
    Extraction and study of features with missing data from a given dataset.

    Private parameters
    ----------
    __missings : pandas data frame built after the extraction of features with Nan values. To be used internally by the class methods
    __ifcount : boolean variable, used to check whether or not the "count" method has been called
    __trs : double variable, used to store the threshold value

    Attributes
    ----------
    n_features_ : int
    The number of features containing missing values.

    support_ : array of shape [n_features].
    The mask of selected features.

    n_features_filter_ : int.
    The number of features whose missing values percentage is higher than a given threshold.

    support_filter_ : array of shape [n_features_filter_].
    The mask of selected features whose missing value percentage is higher than a given threshold.

    """



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





class tabellone(object):

	"""
	
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

    def __init__(self):
    	self.__columns=10
    	self.__rows=9
        #self.__missings = None
        #self.__ifcount = True
        #self.__trs = 0.



    def fill_tabellone(self):

        """

            Fill our tabellone according to the italian convention
            Parameters
            ----------
 
            Return:

            self.tabellone: numpy array type, shape=[self.__rows,self.__columns]  

        """

        return self._fill_tabellone()


 ##############################################################################################

    def _fill_tabellone(self):
     
    	self.tab = np.zeros((self.__rows, self.__columns))
        for i in range(0,self.__rows):
        	self.tab[i]= list(np.asarray(self.__columns*i) + range(1, 11))   







class player(object):

	"""
		player is an object which can have Ncartella number of cartelle. 
		if Ncartella==0 means the player has a tabellone
	"""

	def __init__(self,Ncart):
		self.Ncart=Ncart
		if not isinstance(self.Ncart, int):
        	raise ValueError('Number of Cartelle has to be an integer!')
        #self.__missings = None
        #self.__ifcount = True
        #self.__trs = 0.


    def check_cartella(self):

        """

            Fill our cartella according to the italian convention
            Parameters
            ----------
            seed : int type

            Return:

            self.cartella: numpy array type, shape=[self.rows,self.__columns]

        """

        return self._check_cartella()




 ##############################################################################################

    def _check_cartella(self):

	#TODO

