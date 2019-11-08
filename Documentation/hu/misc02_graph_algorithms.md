![Pythonarium](../../PythonariumLogo.png)

<p align="right"><sup><a href="README.md">Tartalom</a></sup></p>

# Gráfalgoritmusok Pythonban

Ebben a cikkben gráfokkal kapcsolatos közismert algoritmusok példaimplementációiról lesz szó. A cikkhez a következő Python package-eket fogom használni:
- `networkx`
- `numpy`

# Mik a gráfok?

A gráf formális definíciója egy *G(V,E)* pár, ahol *V* a csúcsok véges halmaza, *E* pedig az élek halmaza. Egy él két csúcsból alkotott rendezetlen vagy rendezett pár. Egy gráf élei lehetnek irányítottak vagy irányítatlanok, lehetnek súlyozottak vagy súlyozatlanok. Tehát megkülönböztetjük az alábbiakat:
- irányítatlan, súlyozatlan gráfok
- irányított, súlyozatlan gráfok
- irányítatlan, súlyozott gráfok
- irányított, súlyozott gráfok

A súlyozatlan gráfokat elképzelhetjük úgy, mint a súlyozott gráfok speciális esetét, amikor minden súly 1. Az irányítatlan gráfokat pedig elképzelhetjük úgy, mint az irányított gráfok speciális esetét, amikor minden él mindkét irányban járható.

Amennyiben egy él mindkét végpontja ugyanaz a csúcs, akkor hurokélről beszélünk.

# Gráfok tárolása

Rögtön adódik a kérdés, hogy hogyan érdemes tárolni, ábrázolni egy gráfot. Két általánosan elterjedt ábrázolási módot ismertetek, a szomszédsági mátrixot és az éllistás ábrázolást.

## Szomszédsági mátrix

Vegyük példaként az alábbi, irányítatlan, súlyozatlan gráfot.

![Gráf 1](./assets/graph1.png "Gráf 1")

A szomszédsági mátrix (adjacencia mátrix, csúcsmátrix) egy olyan, számokból álló táblázat, amelynek annyi sora és oszlopa van, ahány csúcsa van a gráfnak. A példánkban használt gráfnak 5 csúcsa van, ezért a mátrix 5x5-ös. A mátrix i. sorának j. oszlopában szerepel annak az élnek a súlya, amelyik az i. csúcsból a j. csúcsba megy. Ha nincs él az i.-ből a j. csúcsba, akkor a *végtelen* értéket kell használnunk a mátrix elemeként. Súlyozatlan gráfoknál minden elem 0 vagy 1 értékű. Irányítatlan gráfoknál a mátrix szimmetrikus.

A továbbiakban egyszerű gráfokkal dolgozunk, amelyek nem tartalmaznak sem hurokéleket, sem többszörös éleket. Így a mátrix főátlójában mindig 0-k szerepelnek. 

A fenti gráfnak a szomszédsági mátrixa a következőképpen néz ki:

![Gráf 1 Adjacencia mátrix](./assets/graph1_adjacency_matrix.png "Gráf 1 Adjacencia mátrix")

## Éllistás ábrázolás

Ebben az esetben a gráf csúcsai egy listában tároljuk. A lista minden eleméhez hozzárendelünk egy-egy listát: a csúcsból induló élek listáját.

A csúcshoz rendelt lista elemeiben a csúcsból kiinduló élek célcsúcsainak azonosítóját tároljuk. Irányítatlan esetben a célcsúcshoz tartozó listában is eltároljuk az él másik végpontját. Súlyozott esetben a célcsúcsot tartalmazó listaelem tartalmazni fogja az él súlyát is.

A fenti gráf éllistás ánrázolása a következő:

![Gráf 1 Éllistás ábrázolása](./assets/graph1_edge_list.png "Gráf 1 Éllistás ábrázolása")

# Gráfok kezelése Pythonban

A Pythonban a gráfok kezelése ebben a cikkben a `networkx` csomagot fogom használni. Ez a csomag összetett hálózatok létrehozását, manipulálását, tanulmányozását teszi lehetővé.

A `networkx` használatához telepíteni kell azt a `pip` segítségével:

```
pip install networkx --upgrade
```

## Gráfok megjelenítése

Az alábbi program a fent vázolt gráfot definiálja majd megjeleníti a `networkx` csomag használatával:

```python
import networkx as nx

G=nx.Graph()
G.add_nodes_from(["a", "b", "c", "d", "e"])
G.add_edges_from([("a", "b"), ("b", "c"), ("c", "a"), ("a", "d"), ("c", "e"), ("d", "e")])

nx.draw_networkx(G)
```

## Gráfok él- és csűcsszámának lekérdezése

```python
print("Nodes of graph: {}".format(G.nodes()))
print("Edges of graph: {}".format(G.edges()))
```

```
Nodes of graph: ['a', 'b', 'c', 'd', 'e']
Edges of graph: [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('c', 'e'), ('d', 'e')]
```

## Gráfok adjacenciamátrixának elérése

Az adjacenciamátrixot a `to_numpy_matrix()` függvénnyel lehet elérni. (További lehetőségekről a referencia dokumentáció ad tájékoztatást.)

```python
m = nx.to_numpy_matrix(G)
print(m)
```

```
[[0. 1. 1. 1. 0.]
 [1. 0. 1. 0. 0.]
 [1. 1. 0. 0. 1.]
 [1. 0. 0. 0. 1.]
 [0. 0. 1. 1. 0.]]
```

Az alább ismertetett algoritmusoknál az adjacenciamátrixot fogom használni a gráf elérésére. Az algoritmusokat a Google Colab rendszerben implementáltam.

A szélességi és mélységi bejáráshoz a következő gráfot fogom használni:

![Gráf 2](./assets/graph2.png "Gráf 2")

# Gráfbejárás mélységi kereséssel

A mélységi bejárás algoritmusát itt is a `visit_vertex()` függvény tartalmazza. A mélységi bejárás lényege, hogy egy adott csúcsból kiindulva először a csúcs első szomszédját látogatom meg, és már az első szomszéd meglátogatásakor meglátogatom ennek is az első szomszédját. Csak akkor lépek tovább a következő szomszéd meglátogatására, amikor az előző szomszéd minden szomszédja (és azoknak is minden szomszédja) meg lett látogatva. Így a bejárás során hamar a gráf mélyére jutok, a legtávolabbi csúcshoz.

Az alábbi programban figyelemmel kísérjük a meglátogatott csúcsokat (`visited_vertices`).

```python
import networkx as nx
import numpy as np

def visit_vertex(v, m, visited_vertices, depth):
    padding = "  "
    if v not in visited_vertices:
        print("{}visiting {}".format(padding*depth, v))
        visited_vertices.append(v)
        num_of_vertices = np.shape(m)[0]
        print("{}visiting neighbours of {}".format(padding*depth, v))
        for j in range(0, num_of_vertices):
            if m[v,j] != 0:
                print("{}stepping to edge ({}, {})".format(padding*depth, v, j))
                visit_vertex(j, m, visited_vertices, depth + 1)
    else:
        print("{}{} was already visited".format(padding*depth, v))


G=nx.Graph()
G.add_nodes_from(["0", "1", "2", "3", "4", "5", "6", "7"])
G.add_edges_from([("0", "1"), 
                  ("1", "2"), 
                  ("2", "0"), 
                  ("0", "3"), 
                  ("2", "4"), 
                  ("3", "4"), 
                  ("0", "6"), 
                  ("4", "6"), 
                  ("2", "5"), 
                  ("3", "5"), 
                  ("0", "5"), 
                  ("2", "7")])

print("Nodes of graph: {}".format(G.nodes()))
print("Edges of graph: {}".format(G.edges()))

nx.draw_networkx(G)

visited_vertices = []

visit_vertex(0, nx.to_numpy_matrix(G), visited_vertices, 0)

print("Vertices were visited in the following sequence: {}".format(visited_vertices))
```

A program a kimenetre kiírja a csúcsok meglátogatásának sorrendjét.

```
Nodes of graph: ['0', '1', '2', '3', '4', '5', '6', '7']
Edges of graph: [('0', '1'), ('0', '2'), ('0', '3'), ('0', '6'), ('0', '5'), ('1', '2'), ('2', '4'), ('2', '5'), ('2', '7'), ('3', '4'), ('3', '5'), ('4', '6')]
visiting 0
visiting neighbours of 0
stepping to edge (0, 1)
  visiting 1
  visiting neighbours of 1
  stepping to edge (1, 0)
    0 was already visited
  stepping to edge (1, 2)
    visiting 2
    visiting neighbours of 2
    stepping to edge (2, 0)
      0 was already visited
    stepping to edge (2, 1)
      1 was already visited
    stepping to edge (2, 4)
      visiting 4
      visiting neighbours of 4
      stepping to edge (4, 2)
        2 was already visited
      stepping to edge (4, 3)
        visiting 3
        visiting neighbours of 3
        stepping to edge (3, 0)
          0 was already visited
        stepping to edge (3, 4)
          4 was already visited
        stepping to edge (3, 5)
          visiting 5
          visiting neighbours of 5
          stepping to edge (5, 0)
            0 was already visited
          stepping to edge (5, 2)
            2 was already visited
          stepping to edge (5, 3)
            3 was already visited
      stepping to edge (4, 6)
        visiting 6
        visiting neighbours of 6
        stepping to edge (6, 0)
          0 was already visited
        stepping to edge (6, 4)
          4 was already visited
    stepping to edge (2, 5)
      5 was already visited
    stepping to edge (2, 7)
      visiting 7
      visiting neighbours of 7
      stepping to edge (7, 2)
        2 was already visited
stepping to edge (0, 2)
  2 was already visited
stepping to edge (0, 3)
  3 was already visited
stepping to edge (0, 5)
  5 was already visited
stepping to edge (0, 6)
  6 was already visited
Vertices were visited in the following sequence: [0, 1, 2, 4, 3, 5, 6, 7]
```

# Gráfbejárás szélességi kereséssel

A szélességi bejárás algoritmusát a `visit_vertex()` függvény tartalmazza. A szélességi bejárás lényege, hogy egy adott csúcsból kiindulva először a csúcs szomszédait látogatom meg. Majd veszem az első, második, stb. szomszédját, és újra ugyanígy járok el. Így a látogatások egyre távolabb kerülnek a kiinduló csúcstól, de közben az adott távolságig az összes csúcsot meglátogatom.

Az alábbi programban figyelemmel kísérjük a meglátogatott csúcsokat (`visited_vertices`) és a meglátogatott éleket is (`visited_edges`).

```python
import networkx as nx
import numpy as np

padding = "  "

def mark_as_visited(v, visited_vertices, depth):
    print("{}visiting {}".format(padding*depth, v))

def visit_vertex(v, m, visited_vertices, visited_edges, depth):
    num_of_vertices = np.shape(m)[0]
    print("{}visiting neighbours of {}".format(padding*depth, v))
    for j in range(0, num_of_vertices):
        if m[v,j] != 0:
            if j not in visited_vertices:
                mark_as_visited(j, visited_vertices, depth + 1)
                visited_vertices.append(j)
            else:
                print("{}{} was already visited".format(padding*(depth + 1), j))
    for j in range(0, num_of_vertices):
        if m[v,j] != 0:
            if (v,j) not in visited_edges:
                print("{}stepping to edge ({}, {})".format(padding*(depth + 1), v, j))
                visited_edges.append((v,j))
                visit_vertex(j, m, visited_vertices, visited_edges, depth + 1)

def breadth_first_search(v, m, visited_vertices, visited_edges, depth):
    mark_as_visited(v, visited_vertices, depth)
    visited_vertices.append(v)
    num_of_vertices = np.shape(m)[0]
    print("{}visiting neighbours of {}".format(padding*depth, v))
    for j in range(0, num_of_vertices):
        if m[v,j] != 0:
            if j not in visited_vertices:
                mark_as_visited(j, visited_vertices, depth + 1)
                visited_vertices.append(j)
            else:
                print("{}{} was already visited".format(padding*(depth + 1), j))
    for j in range(0, num_of_vertices):
        if m[v,j] != 0:
            if (v,j) not in visited_edges:
                print("{}stepping to edge ({}, {})".format(padding*depth, v, j))
                visited_edges.append((v,j))
                visit_vertex(j, m, visited_vertices, visited_edges, depth + 1)



G=nx.Graph()
G.add_nodes_from(["0", "1", "2", "3", "4", "5", "6", "7"])
G.add_edges_from([("0", "1"), 
                  ("1", "2"), 
                  ("2", "0"), 
                  ("0", "3"), 
                  ("2", "4"), 
                  ("3", "4"), 
                  ("0", "6"), 
                  ("4", "6"), 
                  ("2", "5"), 
                  ("3", "5"), 
                  ("0", "5"), 
                  ("2", "7")])

print("Nodes of graph: {}".format(G.nodes()))
print("Edges of graph: {}".format(G.edges()))

nx.draw_networkx(G)

visited_vertices = []
visited_edges = []

breadth_first_search(0, nx.to_numpy_matrix(G), visited_vertices, visited_edges, 0)

print("Vertices were visited in the following sequence: {}".format(visited_vertices))
```

# Legrövidebb út kereséses két csúcs között

# Leghosszabb út kereséses két csúcs között

# Referenciák

- [Gráf](https://hu.wikipedia.org/wiki/Gráf)
- [Benjamin Baka: Python Data Structures and Algorithms](https://www.amazon.com/Python-Data-Structures-Algorithms-application-ebook/dp/B01IF7NLM8)
- [Algoritmusok és adatszerkezetek / Gráfok ábrázolása](http://tamop412.elte.hu/tananyagok/algoritmusok/lecke23_lap1.html)
- [networkx 2.3 at pypi](https://pypi.org/project/networkx/2.3/)
- [NetworkX Reference Release 2.3](https://networkx.github.io/documentation/stable/_downloads/networkx_reference.pdf)

<p align="right"><sup><a href="README.md">Tartalom</a></sup></p>
