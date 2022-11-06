# Routes

This is an implementation of an algorithm used for CSC263. 

<img width="133" alt="boardgame" src="https://user-images.githubusercontent.com/89807997/200196647-3a66e7a1-e67e-4383-870c-f726f655945a.PNG">

The game will have a map of cities and villages and two
ports. Playing the game will involve travelling from the starting port to an ending port
through some cities and villages. Some cities and villages are connected while others are
not. This diagram shows one possible board layout. The red circle indicates that B is a city.
A, C, and D are villages. Travel is permitted in both directions on all roads. You can not
travel through a port – only start or end at one. 
Consider three different scenarios:
- Scenario 1: Routes can travel through any city or village at most once.
- Scenario 2: Routes can travel through any village at most once, but they can pass
through a city multiple times.
- Scenario 3: There is a special village passport card. A player may play it on one village
and then is permitted to travel a route that passes through that village one extra time.
Routes can still travel through cities multiple times and all the other villages at most
once. The village passport can not be played on a port. The village passport does not
have to be played, so all the routes from scenario 2 are still permitted under scenario 3.

The task was to design efficient algorithms and associated data structures to count
the number of possible routes under each of the three scenarios for an arbitrary board
configuration.
