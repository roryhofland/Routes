# make a dictionary hash table from vertex number to information

class Board:
    def __init__(self, size):
        # initialize board size and adjacency list
        self.size = size
        self.adjList = [[] for i in range(self.size)]

    def addRoad(self, u, v):
        # add a road from vertex u to vertex v
        self.adjList[u].append(v)

    def countRoutes(self, start, end):
        # set all vertices to undiscovered
        discovered = [False] * self.size

        # use helper function to print all paths between the start and end port
        routeCount = [0]
        self.countRoutesRecur(start, end, discovered, routeCount)
        return routeCount[0]

    def countRoutesRecur(self, curr, end, discovered, routeCount):
        if curr != 2:
            discovered[curr] = True

        # if curr is end port, record the path
        if (curr == end):
            routeCount[0] += 1

        # if curr is not end port, recurse for each undiscovered neighbour
        else:
            i = 0
            while i < len(self.adjList[curr]):
                if (not discovered[self.adjList[curr][i]]):
                    self.countRoutesRecur(self.adjList[curr][i], end, discovered, routeCount)
                i += 1

        discovered[curr] = False


if __name__ == "__main__":
    g = Board(6)
    g.addRoad(0, 1)
    g.addRoad(1, 2)
    g.addRoad(1, 5)
    g.addRoad(2, 1)
    g.addRoad(2, 3)
    g.addRoad(2, 4)
    g.addRoad(2, 5)
    g.addRoad(3, 2)
    g.addRoad(4, 2)
    g.addRoad(4, 5)
    g.addRoad(5, 1)
    g.addRoad(5, 2)
    g.addRoad(5, 4)

    print(g.countRoutes(0, 5))
