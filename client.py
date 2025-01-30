import asyncio, websockets
from json import dumps, loads
from time import sleep
import time

async def client_connect(username, password, variance=0.0001):
    """Handle sending and receiving logins to & from the server.
    'while True' structure prevents singular network/socket
    errors from causing full crash.

    Parameters
    ----------
        username -- string of student ID for login attempt
        password -- string of password for login attempt
        variance -- float of maximum network delay

    Returns
    -------
        reply -- string of server's response to login attempt
    """

    #server_address = "ws://20.224.29.49:8080"
    #server_address = "ws://127.0.0.1:3840"
    server_address = "ws://192.168.20.17:3840"
    
    while True:
        try:
            async with websockets.connect(server_address) as websocket:

                # The (local) Docker server does not accept variance.
                # When switching to the Hanze server, you can add the variance parameter to the request.
                await websocket.send(dumps([username, password]))
                #await websocket.send(dumps([username, password, variance]))

                reply = await websocket.recv()

            return loads(reply)
        except:
            continue

def call_server(username, password, variance=0.0001):
    """Send a login attempt of username + password to the server
    and return the response. Optionally takes the variable variance to
    allow simulation of random network delays; the server will then
    delay its response by n microseconds, where 0 < n < variance.
    A higher variance will make guessing the password harder.


    Parameters
    ----------
        username -- string of student ID for login attempt
        password -- string of password for login attempt
        variance -- float of maximum delay, must be greater than 0.000001

    Returns
    -------
        reply -- string of server's response to login attempt
    """

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    start = time.perf_counter()
    try:
        reply = asyncio.run(client_connect(username, password, variance))
    except KeyboardInterrupt:
        pass
    end= time.perf_counter()
    sleep(0.001) # Wait so as to not overload the server with 90 students at once!
    return (reply), end - start




# Test basic server connectivity & functionality
#print(call_server('000000', 'hunter2'))
print(call_server('000000', 'ssss'))
print(call_server('test', 'test'))
#print(call_server('479358', 'e6vj1qa'))