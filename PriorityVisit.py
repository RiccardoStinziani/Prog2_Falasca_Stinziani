import cProfile
import pstats
from time import time

from Collection.Graph.graph.Graph_AdjacencyList import GraphAdjacencyList
from Collection.priorityQueue.PQbinomialHeap import PQbinomialHeap
from Collection.priorityQueue.PQ_Dheap import PQ_DHeap
import random


def priorityVisit(graph, pq, d = 2):
    """
        Do the priority visit
        :param graph: object of Graph_AdicencyList.
        :param pq: Priority Queue; True for PQBiniomalHeap; False for PQ_Dheap.
        :param d: Number of sons in the case you chose the Priority Queue PQ_Dheap
        :return: The list of the nodes' index
    """
    verticeMax = graph.getNodeMaxWeight()
    if(pq == True):
        priorityQueue = PQbinomialHeap()
    elif(pq == False and d > 1):
        priorityQueue = PQ_DHeap(d)
    else:
        raise Exception("Il valore d deve essere >= 2")
    priorityQueue.insert(verticeMax.getId(), verticeMax.getWeight())
    markedNodes = [verticeMax.getId()]
    list = []

    while not priorityQueue.isEmpty():
        idNode = priorityQueue.findMax()
        list.append(idNode)
        priorityQueue.deleteMax()
        adjacentNodes = graph.getAdj(idNode)
        for nodeIndex in adjacentNodes:
            if nodeIndex not in markedNodes:
                node = graph.getNode(nodeIndex)
                priorityQueue.insert(node.getId(), node.getWeight())
                markedNodes.append(nodeIndex)
    return list

def graphGenerator(numberOfNodes, numberOfEdges):
    """
        Generate a graph
        :param numberOfNodes: number of nodes of the graph (Integer).
        :param numberOfEdges: number of edges of the graph (Integer).
        :return: Object of Graph_AdicencyList
    """
    if(numberOfEdges < numberOfNodes - 1 or numberOfEdges > (numberOfNodes * (numberOfNodes - 1)) / 2):
        raise Exception("Valore di numberOfEdges non idoneo")
    if(numberOfNodes < 2):
        raise Exception("Numero di nodi non sufficiente")

    graph = GraphAdjacencyList()

    for i in range(numberOfNodes):
        weight = random.randint(0, 100)
        graph.addNode(i, weight)

    nodes = graph.getNodes().copy()

    n = numberOfNodes
    startNode = random.randint(0, n - 1)
    startNode = nodes.pop(startNode).getId()
    n -= 1
    for i in range(n):
        node = random.randint(0, n - 1 - i)
        node = nodes.pop(node).getId()
        graph.insertEdge(startNode, node)
        graph.insertEdge(node, startNode)
        startNode = node

    k = numberOfEdges - (numberOfNodes - 1)
    for i in range(k):
        n = numberOfNodes
        nodes = graph.getNodes().copy()

        node1 = nodes.pop(random.randint(0, n - 1)).getId()
        n -= 1
        adj = graph.getAdj(node1)
        while(len(adj) == numberOfNodes - 1):
            node1 = nodes.pop(random.randint(0, n - 1)).getId()
            n -= 1
            adj = graph.getAdj(node1)

        node2 = nodes.pop(random.randint(0, n - 1)).getId()
        n -= 1
        while(node2 in adj):
            node2 = nodes.pop(random.randint(0, n - 1)).getId()
            n -= 1

        graph.insertEdge(node1, node2)
        graph.insertEdge(node2, node1)
    return graph


if __name__ == "__main__":

    #Codice per i test
    nGraphInList = 10
    testDic = {0 : True, 2 : False, 3 : False, 5 : False, 10 : False, 20 : False}
    rangeList = [10, 50, 100, 250, 500, 1000]
    for n in rangeList:
        print("\n")
        print("+++++++++++++")
        print("+\t", n , "\t+")
        print("+++++++++++++")
        #leggere relazione per spiegazione
        m1 = n - 1
        m2 = int((n**2 + 5 * n - 6) / 8) + (n**2 + 5 * n - 6) % 8
        m3 = int((3*n**2 - n -2 ) / 8)
        m4 = int(n * (n - 1) / 2)

        graphDic = {"m1" : [], "m2" : [], "m3" : [], "m4" : []}
        for i in range(nGraphInList):
            graphDic["m1"].append(graphGenerator(n, m1))
        for i in range(nGraphInList):
            graphDic["m2"].append(graphGenerator(n, m2))
        for i in range(nGraphInList):
            graphDic["m3"].append(graphGenerator(n, m3))
        for i in range(nGraphInList):
            graphDic["m4"].append(graphGenerator(n, m4))

        for t in testDic:
            print("\n\t===========================================")
            if(testDic[t]):
                print("\tBinomialHeap")
            else:
                print("\tD-Heap con d = ", t)
            print("\t===========================================\n")
            for m in graphDic:
                print("\n\t\t", m)
                start = time()
                for i in range(nGraphInList):
                    priorityVisit(graphDic[m][i], testDic[t], t)
                endTime = (time() - start) / nGraphInList
                print("\t\t--------------------------")
                print("\t\t", endTime)
                print("\t\t--------------------------")

    #Esempio di utilizzo
    graph = graphGenerator(20, 28)
    graph.print()
    print(priorityVisit(graph, True))


