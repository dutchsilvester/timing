from collections import Counter

### De file helper5.py bevat classes. Deze classes bevatten functies specifiek voor het in lijsten bijhouden van resultaten
## classes omdat er sprake is van het modelleren van data in lijsten

class Timing:
    """ De class timing is het kleinste datatype. Het bevat een lijst van twee elementen : [teken, tijd]
        de funcite value geeft de meest gebruikte vorm terug van de lijst
    """

    def __init__(self,character:str,time:float):
        self.character=character
        self.time=time

    def value(self):
        if self.character:
            return [self.character, self.time]
        return False
        

class TimeList:
    """ De classe TimeList bestaat uit een lijst van de class Timings
        Er zijn verschillende funcites die waarde onttrekken aan de ruwe lijst van Timings
    """

    def __init__(self,sample:Timing):
        self.content=[sample]

    def add(self,sample:Timing):
        if self.content:
            self.content+=[sample]
            return True
        return False

    def value(self):
        if self.content:
            return [item.value() for item in self.content]
        return False

    def keys(self):
        """ Deze functie geeft de sleutelwaarden van de lijst terug. element 0  uit ieder element.
        """
        if self.content:
            return [item.value()[0] for item in self.content]
        return False

    def filter(self,filter_char:str):
        """ Deze functie geeft een lijst van tijden voor een gegeven teken ( filter_char )
        """
        if self.content:
            return [item.value()[1] for item in self.content if filter_char==item.value()[0]]
        return False

    def filter_minimum(self,filter_char:str):
        """ Deze functie geeft de kleinste waarde uit een lijst van tijden voor het gegeven filter charachter
        """
        if self.content:
            return min([item.value()[1] for item in self.content if filter_char==item.value()[0]])
        return False

    def pivot(self):
        """ Deze functie pitot de ruwe waarde naar sleutels voor rijen en timings voor colums
        """
        if self.content:
            return [ [item,self.filter(item)]for item in set(self.keys())]

        return False

    def endlist(self):
        """ Deze functie maakt een lijst van Timings met de winnende waarde
        """
        if self.content:
            return [ [item,self.filter_minimum(item)]for item in set(self.keys())]
        return False

    def _winner_helper(self,l=[]):
        """ Recursive helper functie voor het bepalen van het winnende teken in de lijst. Geeft de langste timing terug voor de lijst
        """
        if len(l)<1:
            return [0,0]
        sub_result=self._winner_helper(l[1:])
        if l[0][1] > sub_result[1]:
            return l[0]
        else:
            return sub_result
        return False

    def winner(self):
        """ Deze functie bepaalt het winnende teken in de lijst. Statisch op basis van de minste vertraging en de langste verwerking
        """
        if self.content:
            return self._winner_helper(self.endlist())[0]
        return False
    


class MyCounter(Counter):
    """
    Extra klasse om het scoreboard beter bij te houden. Door het aanpassen van de __str__ is de weergave bij het printen eenvoudiger.
    Hierdoor blijven de tekens langer op 1 regel. Verder blijft dit een standaard Counter uit de python collections
    """
    def __str__(self):
        return "".join('|{}:{}|'.format(k, v) for k, v in self.items())


                
class ScoreBoard:
    """ Class om het bijhouden van een scoreboard en verwantw functies
        Winconditie is de statische verhouding van significantie voor het winnen van de game, snitch is de statische verhouding voor het winnen van een game. 
        Het scoreboard word bijgehouden in een string. Input van scores is dus een char/string
    """

    def __init__(self,setwinner="",win_condition=7/10,min_rounds=10,snitch=10):
        self.board=setwinner
        self.win_condition=win_condition
        self.min_rounds=min_rounds
        self.snitch=snitch

    def reset(self):
        self.board=""
        return #niets
    
    def add(self,character=""):
        self.board+=character
        return #niets
        

    def most_common(self,set=2):
        """ Most common geeft de meest voorkomende waarde op het scoreboard
            In het geval er slechts 1 teken het scorenboard meerder keren heeft bereikt is er een statische kopie naar runner. 
        """
        if len(MyCounter(self.board).most_common(set))>1:
            self.winner, self.runner = MyCounter(self.board).most_common(set)
            return self.winner, self.runner
        else:
            self.winner = MyCounter(self.board).most_common(set)[0]
            self.runner = self.winner
            return self.winner, self.runner
        
    def do_we_have_a_winner(self):
        """ Functie om te bepalen of er inmiddels een winconditie is. 
        """
        if self.board:
            if self.min_rounds:
                if len(self.board)>self.min_rounds:
                    self.most_common()
                    if self.winner[1]/len(self.board)>self.win_condition:
                        return True
                    elif self.winner[1]-self.snitch>self.runner[1]:
                        return True
        return False
    
    def __repr__(self):
        return str(MyCounter(self.board))
        

    def __str__(self):
        return self.__repr__()


    def status(self):
        self.most_common()
        return f"Koploper is {self.winner} met als tweede {self.runner}"

            
            
    