from node import *
import json

leaf1 = node("leaf1")
leaf2 = node("leaf2")
root = node("root", [leaf1, leaf1, leaf2])

def out(graph, gList = {}):
    child = {}
    for i in range(len(graph.children)):
        child[i] = graph.children[i].name
        gList = out(graph.children[i], gList)
    temp = {"val":graph.val, "children":child}
    gList.update({graph.name:temp})
    return gList

def Jstring(graph):
    gList = out(graph)
    file = open("json.request","w")
    result = json.dumps(gList)
    file.write(result)
    return result

def buildJson(Str):
    glist = json.loads(Str)
    gkeys = list(glist.keys())
    nodes = {}
    for i in range(len(glist)):
        nodes[gkeys[i]] = node(gkeys[i])
    for i in gkeys:
        nodes[i].val = glist[i]["val"]
        temp = glist[i]["children"].values()
        nodes[i].children = []
        for j in temp:
            nodes[i].children.append(nodes[j])
    return nodes["root"]
