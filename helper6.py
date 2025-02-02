from random import shuffle, choice
from string import ascii_lowercase, digits

#### Info
## het bestand 'helper6.py' bevat enkele losse definities die aangeroepen moeten worden


def maak_set_van_lengte_aanvallen(min_length=1,max_length=8,samplesize=100):
    """ Deze functie geeft een lijst van getallen. Deze getallen representeren de lengte van het wachtwoord
    """
    sub_result=[sample for sample in range(min_length,max_length+1) for _ in range(0,samplesize)]
    shuffle(sub_result)
    return sub_result

def maak_set_van_characters(characters=ascii_lowercase+digits,samplesize=30):
    """Deze functie maakt een gerandimiseerde lijst van tekens. input character * samplesize
    """
    sub_list=list((characters)*samplesize)
    shuffle(sub_list)
    return sub_list

def maak_sub_wachtwoord(sampleset=ascii_lowercase+digits,min_length=0, max_length=8):
     """ Deze functie maakt een random wachtwoord aan in de een lijst vorm
     """
     return  [choice(sampleset) for _ in range(min_length,max_length)]

def pas_sub_wachtwoord_aan(index=0,wachtwoord=[],character="b"):
    """ Deze functie past een lijst aan als wachtwoord. De betreffende index wordt vervangen 
        door het character
    """
    wachtwoord[index]=character
    return wachtwoord 

