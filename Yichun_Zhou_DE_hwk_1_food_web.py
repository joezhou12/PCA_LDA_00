#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 16:57:45 2020

@author: joezhou
"""

"""
Read the adjacency matrix.
"""

#initiate a adjacency matrix
adjacency_matrix=[
    [0,1,0,1],
    [1,0,1,1],
    [0,1,0,0],
    [1,1,0,0]
    ]
#iterate thourgh 1 to 5 
for i in [1,2,3,4,5]:
    #print i
    print(i)
"""output
1
2
3
4
5
"""

#iterate thourgh each rows in matrix
for row in adjacency_matrix:
    #print each row
    print(row)
"""output
[0, 1, 0, 1]
[1, 0, 1, 1]
[0, 1, 0, 0]
[1, 1, 0, 0]
"""
#to get each single matrix element
#iterate thourgh each rows in matrix
for row in adjacency_matrix:
    #iterate thourgh each element in row
    for a_ij in row:
        #print each element
        print(a_ij), 
    #print a blank space
    print('\r')
"""output
0
1
0
1

1
0
1
1

0
1
0
0

1
1
0
0
"""
#initiate a directed adjacency matrix 
adjacency_matrix_directed =[
    [0,1,0,1],
    [0,0,1,0],
    [0,0,0,1],
    [0,0,0,0]
    ]

"""report
Start with the matrix representaion of the graph, and the direct representation 
of nodes and edges from the NetworkX library. 
First reprent the graph through the adjacency martix using the basic list data
type, also extracted each element of each rows
"""


"""
Basic Statistics
"""
#the number of species is the number of rows or columns of the adjacency matrix
num_species = len(adjacency_matrix_directed[0])
#the number of links or predations is the non zero elements 
#of the adjacency matrix(this holds for directed graphs)
num_predations = 0
#iterate thourgh each element in num_species by index
for i in range(num_species):
    #iterate thourgh each element in num_species by index again
    for j in range(num_species):
        #if the element is not 0
        if adjacency_matrix_directed[i][j]!=0:
            #num_predations increase by 1
            num_predations = num_predations + 1
#to check if a specue us a Basal(B), an Intermediate(I) or 
#a Top(T) one we have to check the presence of 1s both in
#the row and in the column of each specie
row_count = [0,0,0,0]
column_count = [0,0,0,0]
#iterate thourgh each element in num_species by index
for i in range(num_species):
    #iterate thourgh each element in num_species by index again
    for j in range(num_species):
        #incerase the row_count[i]
        row_count[i] = row_count[i] + adjacency_matrix_directed[i][j]
        #incerase the column_count[i]
        column_count[j] = column_count[j] + \
            adjacency_matrix_directed[i][j]

#initiate a 3 number indicator
#initiate number_B
number_B = 0
#initiate number_I
number_I = 0
#initiate number_T
number_T = 0

#iterate thourgh each element in num_species by index
for n in range(num_species):
    #if row element equals 0
    if row_count[n]==0:
        #number_T increase by 1
        number_T+=1
        continue
    #if column element equals 0
    if column_count[n]==0:
        #number_T increase by 1
        number_T+=1
        continue
    #if none of row and column element equals 1
    else:
        #number_I increase by 1
        number_I+=1
        
#print the number of species
print('number of species', num_species)
#print the number of predations
print('number of predations', num_predations)
#print the number of classes Basal, Top, Intermediate
print('classes Basal, Top, Intermediate: ',number_B,number_T,number_I) 
#print the connectance which equals num_predations divided by num_species
print('connectance', float(num_predations)/float(num_species**2))

"""output
number of species 4
number of predations 4
classes Basal, Top, Intermediate:  0 2 2
connectance 0.25
"""

"""report
Scalar quantities such as size measure, connectance can be computed easily in 
the case of various food webs, get the the number of species is the number of 
rows or columns of the adjacency matrix, then check if a specie is a Basal (B), 
an Intermediate (I) or a Top (T)
"""

"""
Degree
"""
#for the undirected network
degree_node_2 = 0
#iterate thourgh each element in adjacency_matrix 
for j in adjacency_matrix[1]:
    #get the degress of node 2 increses by j
    degree_node_2 = degree_node_2 + j
#print the degree of node 2
print("degree of node 2:",degree_node_2)

"""output
degree of node 2: 3
"""
#and for the directed case we already calculated the sum over
#the rows and columns for the adjacency_matrix_directed
out_degree_node_3 = row_count[2]
in_degree_node_4 = column_count[3]
#print the out_degree node 3
print("out_degree node 3:",out_degree_node_3)
#print the out_degree node 4
print('in_degree node 4:',in_degree_node_4)

"""output
out_degree node 3: 1
in_degree node 4: 2
"""

"""report
oen characterises the vertex is the number of its connections, called degree.
The degree of a vertex shows the connection of this vertex, and computed the 
in and out degree for nodes
"""

"""
Degree in Networkx
"""
#inport the networkx package
import networkx as nx

#generate an empty graph
G = nx.Graph()

#define the nodes
#define node 1
G.add_node(1)
#define node 2
G.add_node(2)
#define node 3
G.add_node(3)
#define node 4
G.add_node(4)

#link the nodes
#link node 1 and 2
G.add_edge(1,2)
#link node 1 and 4
G.add_edge(1,4)
#link node 2 and 3
G.add_edge(2,3)
#link node 2 and 4
G.add_edge(2,4)

#degree of the node 2
print(G.degree(2))
"""output
3
"""

"""
Degree sequence
"""
#generate an empty degree sequence list
degree_sequence = []
#iterate thourgh each element in adjacency_matrix by index
for row in range (len(adjacency_matrix)):
    #set degree equlas 0 verytime it iterates
    degree = 0
    #iterate thourgh each element in adjacency_matrix rows
    for j in adjacency_matrix[row]:
        #increase the degree by j
        degree = degree + j
    #append the degree for this iteration to the degree sequence list
    degree_sequence.append(degree)

#print the degree sequence list
print(degree_sequence)   
"""output
[2, 3, 1, 2]
"""

"""report
the degree sequence is the list of the various degrees in the graph, which can
be summarised by a histogram of the degree sequence
"""

"""
Histogram
"""
#inport the matplotlib.pyplot package
import matplotlib.pyplot as plt

#plot a histgram 
plt.hist([1,1,1,1,1,1,1,2,2,2,3,3,4,5],bins=5)
plt.show

"""output
plot
"""

"""report
get a single plot that help us to descirbe the graph, a histigram is a very 
good chice for that purpose and it is very important to learn how to draw
it from analusis of the raw data. sued matplotlib to help draw the histogram
"""

"""
Clustering coefficient
"""
row = 1 #stands for the node 2
#generate an int number for count
node_index_count = 0
#generate an node index list
node_index_list = []
#iterate thourgh each element in row of adjacency_matrix by index
for a_ij in adjacency_matrix[row]:
    #condition check, if the element equals 1
    if a_ij == 1:
        #append the node_index_count to the node_index_list
        node_index_list.append(node_index_count)
    #increase the node_index_count by 1
    node_index_count = node_index_count + 1
#print a empty line
print ("\r")
#print the node index list
print(node_index_list)
"""output
[0, 2, 3]
"""
#generate an int number for count
neighb_conn = 0
#iterate thourgh each element in noed index list
for n1 in node_index_list:
    #iterate again thourgh each element in noed index list
    for n2 in node_index_list:
        # if the element is equal to 1
        if adjacency_matrix[n1][n2] == 1:
            #cneighb_conn would increase by 1
            neighb_conn = neighb_conn + 1
#divide neighb_conn by 2 
neighb_conn = neighb_conn / 2.0
#print out the neighb_conn
print(neighb_conn)
"""output
1.0
"""
#caculate for the clustering coefficient use the neighb_conn and degree node 2
clustering_coefficient = neighb_conn / \
    (degree_node_2 * (degree_node_2 - 1) / 2.0)
#print the clustering coefficient
print(clustering_coefficient)
"""output
0.3333333333333333
"""

"""report
as for node degree previously showed, code the clustering coefficient for a 
specific node, then checked all the possible neighbor coupling for whether a 
link actually exist, finally the cusltering coefficient for node 2 is given by
the expression
"""

"""
Calculating the bowtie structure for a food web network
"""
#loading the network
file_name="./FoodWebs/data/Ythan_Estuary.txt"

#generate an empty graph
DG = nx.DiGraph()

#open the file 
in_file=open(file_name,'r')

#iterate in the file
while True:
    #get lines in the file
    next_line=in_file.readline()
    #if next line is not null, continue, if null, stop the iteration
    if not next_line:
        #if null, stop the iteration
        break
    #get each field of the each lines
    next_line_fields=next_line[:-1].split(' ')
    #set a node with the first non space element of the line
    node_a=next_line_fields[1] #there is a space in the beginning 
                               #of each edge
    #set a node with the second non space element of the line
    node_b=next_line_fields[2]   
    #add each edge to the graph 
    DG.add_edge(node_a, node_b)

#deleting the environment
DG.remove_node('0')

#getting the biggest strongly connected component
scc=list((len(c),c) for c in sorted(nx.strongly_connected_components(DG), key=len, reverse=True))[0][1]

#preparing the IN and OUT component
#generate an empty list for store IN component
IN_component=[]

#iterate through the scc
for n in scc:
    #iterate through the graph predecessors
    for s in DG.predecessors(n):
        #if s is in scc, continue the rest of the loop
        if s in scc: continue
        #if s is not in the IN_component list
        if not s in IN_component:
            #add s to the IN_component list
            IN_component.append(s)

#generate an empty list for store OUT component   
OUT_component=[]
#iterate through the scc
for n in scc:
    #iterate through the graph predecessors
    for s in DG.successors(n):
        #if s is in scc, continue the rest of the loop
        if s in scc: continue
        #if s is not in the IN_component list
        if not s in OUT_component:
            #add s to the IN_component list
            OUT_component.append(s)

#generating the subgraph
#generate an list for store bowtie
bowtie = list()
#extend the scc value to bowtie list
bowtie.extend(scc)
#extend the IN_component value to bowtie list
bowtie.extend(IN_component)
#extend the OUT_component value to bowtie list
bowtie.extend(OUT_component)
#generating the subgraph called DG_bowtie, which is the bowtie subgraph
DG_bowtie = DG.subgraph(bowtie)


#defining the proper layout
#generate an empty dictionary
pos={}
#generate in_y with an float equals 100.0
in_y=100.
#set pos key 89 values equals (150, in_y)
pos['89']=(150.,in_y)
#set in_step with an float equals 700.0
in_step=700.
#iterate through the IN_component list
for in_n in IN_component:
    #set dict pos with key equals in_n, value equals (100.0, in_y)
    pos[in_n]=(100.,in_y)
    #in_y increases by in_step very time it iterates
    in_y=in_y+in_step

#generate out_y with an float equals 100.0
out_y=100.
#set out_step with an float equals 500.0
out_step=500.   
#iterate through the OUT_component list
for out_n in OUT_component:
    #set dict pos with key equals out_n, value equals (200.0, out_y)
    pos[out_n]=(200,out_y)
    #out_y increases by out_step very time it iterates
    out_y=out_y+out_step
#set pos key 90 values equals (150, out_y)
pos['90']=(150.,out_y)

#plot the bowtie structure
nx.draw(DG_bowtie, pos, node_size=50)
#plot the IN_component with color black
nx.draw_networkx_nodes(DG_bowtie, pos, IN_component,node_size=100, node_color='Black')
#plot the OUT_component with color white
nx.draw_networkx_nodes(DG_bowtie, pos, OUT_component,node_size=100, node_color='White')
#plot the scc with color grey
nx.draw_networkx_nodes(DG_bowtie, pos, scc,node_size=200, node_color='Grey')
#save the plot figure
plt.savefig("./FoodWebs/data/bowtie.png",dpi=600)

"""
Distance with Breadth First Search
"""
#creating the graph
#generate an empty new graph
G=nx.Graph()
#add edges to the graph
G.add_edges_from([('A','B'),('A','C'),('C','D'),('C','E'),('D','F'),
('D','H'),('D','G'),('E','H'),('E','I')])

#printing the neighbors of the node 'A'
print(G["A"])
"""output
{'B': {}, 'C': {}}
"""
#draw the graph G
nx.draw(G)
#set root node equlas A
root_node='A'
#generate an empty new list
queue=[]
#append A to the queue list
queue.append('A')
#set node A distance equals 0
G.nodes['A']["distance"] = 0
#iterate in len of the queue list
while len(queue):
    #set working node by pop the 0 index node
    working_node=queue.pop(0)
    #iterate through the neighbors of the working node
    for n in G.neighbors(working_node):
        #if the length of the node is 0
        if len(G.nodes[n])==0:
            #incerase distance by 1
            G.nodes[n]["distance"]=G.nodes[working_node]["distance"]+1
            #append n to the queue list
            queue.append(n)
#iterate through the nodes of the graph
for n in G.nodes():
    #print out the nodes and distance of the root node
    print(n,G.nodes[n]["distance"])
"""output
A 0
B 1
C 1
D 2
E 2
F 3
H 3
G 3
I 3
"""

"""report
 the distincetive features of food web is the possibilitu of arranging the 
 vertices along different levels defined by the distance from the enviroment
 defined categories accroding to the in and out links related to the predation
 used BFS to determined the paths and distances
"""

    
"""
Reading the file with Food Web data
"""
#loading and set the file
file_name="./FoodWebs/data/Little_Rock_Lake.txt"
#generate an empty graph
DG = nx.DiGraph()
#open and readd the file 
in_file=open(file_name,'r')
#iterate in the file
while True:
    #get lines in the file
    next_line=in_file.readline()
    #if next line is not null, continue, if null, stop the iteration
    if not next_line:
        #if null, stop the iteration
        break
    #get each field of the each lines
    next_line_fields=next_line[:-1].split(' ')
    #set a node with the first non space element of the line
    node_a=next_line_fields[1] #there is a space in the beginning 
                               #of each edge
    #set a node with the second non space element of the line
    node_b=next_line_fields[2]
    #print both nodes
    print(node_a,node_b)
    #add each edge to the graph 
    DG.add_edge(node_a, node_b)
"""output
0 11
0 61
0 80
0 123
0 124
0 125
0 126
0 127
0 128
0 129
0 130
0 131
0 132
0 133
0 134
0 135
0 136
0 137
0 138
0 139
0 140
0 141
0 142
0 143
0 144
0 145
0 146
0 147
0 148
0 149
0 150
0 151
0 152
0 153
0 154
0 155
0 156
0 157
0 158
0 159
0 160
0 161
0 162
0 163
0 164
0 165
0 166
0 167
0 168
0 169
0 170
0 171
0 172
0 173
0 174
0 175
0 176
0 177
0 178
0 179
0 180
0 181
0 182
1 2
1 4
1 6
1 8
1 9
1 13
1 14
2 4
2 116
3 2
3 4
...
"""

"""report
once the food web is loaded in the NexworkX, operated on it, the first thing 
is to generate tropic version of this network, used the property of dictionary 
key 
"""

"""
Defining the trophic pattern key
"""
#define a new function called get_node_key, which requires a node
def get_node_key(node):
    #generate an empty list called out_list
    out_list=[]
    #iterate through the node of out_edges
    for out_edge in DG.out_edges(node):
        #append the edge to out_list
        out_list.append(out_edge[1])
    #generate an empty list called in_list
    in_list=[]
    #iterate through the node of in_edges
    for in_edge in DG.in_edges(node):
        #append the edge to in_list
        in_list.append(in_edge[0])
    #sort the out_list
    out_list.sort()
    #append - to out_list
    out_list.append('-')
    #sort the in_list
    in_list.sort()
    #extend the in_list to out_list
    out_list.extend(in_list)
    #function retunr the out_list
    return out_list

#define a new function called TrophicNetwork, which requires a graph DG
def TrophicNetwork(DG):
    #generate an empty dictionary called trophic
    trophic={}
    #iterate through the node of graph  
    for n in DG.nodes():
        #generate k equals the tuple of key n
        k=tuple(get_node_key(n))
        #if k is not in the dict
        if not k in trophic:
            #add k to the dict
            trophic[k]=[]
        #append n to the dict where key is k
        trophic[k].append(n)
    #iterate through the dict keys  
    for specie in trophic.keys():
        #if the length of the key is larger than 1
        if len(trophic[specie])>1:
            #set the key in the dict with values
            for n in trophic[specie][1:]:
                DG.remove_node(n)
    #return the graph
    return DG

#deleting the environment
DG.remove_node('0')

#call the TrophicNetwork function, pass DG into that function
#store result called TrophicDG
TrophicDG=TrophicNetwork(DG)
#print the number of nodes in the graph
print ("S:",TrophicDG.number_of_nodes())
#print the number of edges in the graph
print ("L:",TrophicDG.number_of_edges())
#print the L/S, caculated by number of edges divided number of nodes
print ("L/S:",float(TrophicDG.number_of_edges())/ \
TrophicDG.number_of_nodes())

"""output
S: 93
L: 1034
L/S: 11.118279569892474
"""

"""report
leveraging from function, that can extract the trophic species, very useful 
functions defined previously, ge the number of S and L 
"""


"""
Classes in food webs 
"""
#define a new function called compute_classes, which requires a graph DG
def compute_classes(DG):
    #generate an empty list called basal_species
    basal_species=[]
    #generate an empty list called top_species
    top_species=[]
    #generate an empty list called intermediate_species
    intermediate_species=[]
    #iterate through the nodes of the graph 
    for n in DG.nodes():
        #if the in degree of the node is 0
        if DG.in_degree(n)==0:
            #append the node into basal_species
            basal_species.append(n)
        #else if the out degree of the node is 0
        elif DG.out_degree(n)==0:
            ##append the node into top_species
            top_species.append(n)
        #else append the node into intermediate_species
        else: #both the in or out degree of the node is not 0
            intermediate_species.append(n)
    #return the basal, intermediate, and top species
    return (basal_species,intermediate_species,top_species)

#Call the compute_classes functin for TrophicDG
(B,I,T)=compute_classes(TrophicDG)
#print percentage of basal_species
print ("B:",float(len(B))/(len(B)+len(T)+len(I)))
#print percentage of intermediate_species
print ("I:",float(len(I))/(len(B)+len(T)+len(I)))
#print percentage of top_species
print ("T:",float(len(T))/(len(B)+len(T)+len(I)))
"""output
B: 0.12903225806451613
I: 0.8602150537634409
T: 0.010752688172043012
"""

"""report
catagories shows the relation to in and out of each species, have B I and T, 
code above that categorised the little rock food web network introduced earlier
"""

"""
Proportion of links among classes and ratio prey/predators
"""
#define a new function called InterclassLinkProportion, which requires a graph
#DG and two classes
def InterclassLinkProportion(DG,C1,C2):
    #generatea count equals 0
    count=0
    #iterate through the first class
    for n1 in C1:
        ##iterate through the second class
        for n2 in C2:
            #if the there is an edge between the n1 and n2
            if DG.has_edge(n1,n2):
                #count increases by 1
                count+=1
    #return the propotion of the inter class link
    return float(count)/DG.number_of_edges()

#print the inter class link betwwen basal and Top
print ("links in BT:",InterclassLinkProportion(TrophicDG,B,T))
#print the inter class link betwwen basal and intermediate
print ("links in BI:",InterclassLinkProportion(TrophicDG,B,I))
#print the inter class link betwwen intermediate and intermediate
print ("links in II:",InterclassLinkProportion(TrophicDG,I,I))
#print the inter class link betwwen intermediate and Top
print ("links in IT:",InterclassLinkProportion(TrophicDG,I,T))

#Ratio prey/predators
print ("P/R:",float((len(B)+len(I)))/(len(I)+len(T)))

"""output
links in BT: 0.0009671179883945841
links in BI: 0.09090909090909091
links in II: 0.9081237911025145
links in IT: 0.0
P/R: 1.1358024691358024
"""

"""report
finally compute the propotion of the linkes among the various classes previouly
defined and the ratio prey/ predator 
"""

    
