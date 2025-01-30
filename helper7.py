from client import call_server

def warm_up(user='000000',password='test',amount=1):
    for _ in range(amount):
        result=call_server(username=user,password=password)



