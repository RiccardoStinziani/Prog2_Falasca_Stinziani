from Collection.Graph.graph.Graph_AdjacencyList import GraphAdjacencyList
from Collection.priorityQueue.PQbinomialHeap import PQbinomialHeap
from Collection.priorityQueue.PQ_Dheap import PQ_DHeap
from Collection.priorityQueue.PQbinaryHeap import PQbinaryHeap
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
        raise("sei scemo")
    priorityQueue.insert(verticeMax.getId(), verticeMax.getWeight())
    markedNodes = [verticeMax.getId()]
    list = []

    while not priorityQueue.isEmpty():
        idNode = priorityQueue.findMax()
        list.append(idNode)
    #   print("id: ", idNode)
    #   print("peso: ", graph.getNode(idNode).getWeight(), "\n\n")
        priorityQueue.deleteMax()
        adjacentNodes = graph.getAdj(idNode)
        for nodeIndex in adjacentNodes:
            if nodeIndex not in markedNodes:
                node = graph.getNode(nodeIndex)
                priorityQueue.insert(node.getId(), node.getWeight())
                markedNodes.append(nodeIndex)
    print(len(list))
    return list

def graphGenerator(numberOfNodes):
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

    k = random.randint(1, int(numberOfNodes / 2) + 1)

    for i in range(k):
        n = numberOfNodes
        nodes = graph.getNodes().copy()

        node1 = nodes.pop(random.randint(0, n - 1)).getId()
        while(len(graph.getAdj(node1)) == numberOfNodes - 1):
            nodes.append(node1)
            node1 = nodes.pop(random.randint(0, n - 1)).getId()
        n -= 1

        node2 = nodes.pop(random.randint(0, n - 1)).getId()
        n -= 1
        while(graph.isAdj(node1, node2)):
            node2 = nodes.pop(random.randint(0, n - 1)).getId()
            n -= 1

        graph.insertEdge(node1, node2)
        graph.insertEdge(node2, node1)
    #print("Numero Archi:", len(graph.getEdges()))
    graph.print()
    return graph


if __name__ == "__main__":
    print(priorityVisit(graphGenerator(10)))
