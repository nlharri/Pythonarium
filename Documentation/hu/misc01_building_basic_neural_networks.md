![Pythonarium](../../PythonariumLogo.png)

<p align="right"><sup><a href="README.md">Tartalom</a></sup></p>

# Egyszerű neurális hálózatok építése Pythonban

Ebben a cikkben egyszerű neurális hálózatokat építek Python nyelven. A feladathoz kizárólag a következő Python könyvtárakat használom: `numpy`, `tqdm`.

Az itt bemutatott neurális hálózatok egyszerű boolean függvényeket modelleznek. Kitérek arra, hogy 1 db neuronnal milyen boolean függvényeket lehet megvalósítani.

# Bevezető

Jelen cikknek nem célja, hogy általános alapfogalmakkal ismertesse meg az olvasót a mesterséges intelligenciával, gépi tanulással, neurális hálózatokkal, mély tanulással kapcsolatban. A referenciákban felsorolt szakirodalomban alaposan lehet tájékozódni ezekben a témákban. 

A cikkben implementált neurális hálózatok logikai függvényeket valósítanak meg. Az egyszerű logikai `ÉS` illetve `VAGY` függvénytől kiindulva az összetettebb függvényekig. Látni fogjuk, hogy egyetlen neuronnal mit lehet megvalósítani, és mi az, amihez már több neuronból álló hálózat szükséges.

A cikk tartalmának értelmezéséhez a következő alapfogalmak ismerete szükséges, ezekkel csak érintőlegesen foglalkozom ebben a cikkben:

- neurális hálózat

- tanítási fázis

- előreterjesztés (feed forward)

- hiba-visszaterjesztés (backpropagation)

- gradiensereszkedés (gradient descent)

- aktivációs függvény (activation function)

- szigmoid függvény / logisztikai függvény (sigmoid function / logistic function)

- súlyok (weights)

- predikció (prediction)

- hipotézis függvény (hypothesis function)

- tanulási ráta (learning rate)

- vektor (vector)

- mátrix (matrix)

- alapvető lineáris algebrai ismeretek

# Egyetlen neuron 

Az általam használt egyszerű mesterséges neuron modellje az alábbi ábrán látható. Három bemeneti változója van, de igazából csak kettő az, ami a valós bemenő adatokat tartalmazza, az x0 változó mindig 1-es értéket tartalmaz. A neuron által adott predikció a bemenő értékek, és a súlyok szorzata, ami egy lineáris függvényt ad, majd ennek eredményére a szigmoid függvény van alkalmazva, mint aktivációs függvény.

Az alábbi ábrán egyszeres aláhúzás jelöli a vektor típusú változókat (sorvektorokat és oszlopvektorokat).

![Egyszerű neuron](./assets/Basic_Neuron.png "Egyszerű neuron")

A bemeneti adatokat `x`-szel jelölöm:

![x = (x0, x1, x2)](./assets/x_x0_x1_x2.png "x = (x0, x1, x2)")

A súlyokat, jelen esetben egy vektort, `w` jelöli.

![w = (w0, w1, w2)](./assets/w_w0_w1_w2.png "w = (w0, w1, w2)")

A hipotézis függvény `h`, vagyis ami a neurális hálózat kimenet egy adott `x` bemenetre, `w` súlyok mellett:

![h(x) = g(wx) = g(x0w0+x1w1+x2w2)](./assets/h_x_g_wx_g_x0w0_x1w1_x2w2.png "h(x) = g(wx) = g(x0w0+x1w1+x2w2)")

A szigmoid függvény, `g`:

![Egyszerű neuron](./assets/Basic_Neuron.png "Egyszerű neuron")

(IDE 2 DB ÁBRA KELL!!!)

Ha például a logikai `ÉS` műveletet szeretnénk megvalósítani, akkor intuitív módon felírhatunk egy olyan súlyvektort, amivel a neurális hálózat, ami jelen esetben csak egyetlen neuronból áll, kb. az `ÉS` műveletnek megfelelő eredményt ad a kimenetén. Hasonlóan járhatunk el más logikai műveletekkel is. Az alábbi ábrán a logikai `ÉS` és `VAGY` művelet egy neuronnal történő megvalósításához tartozó súlyokat láthatjuk. Érdemes észrevenni, hogy ha megfordítom a súlyok előjelét, akkor a végeredmény negáltját kapom, tehát így megvan további két függvény implementációja.

![Egyszerű neuron](./assets/Basic_Neuron.png "Egyszerű neuron")

(IDE 4 db ábra kell!!!)

Az `ÉS` és a `VAGY` függvény igazságtáblája, és a neurális hálózat kimenete, ha az előbbi súlyokat használjuk:

![Egyszerű neuron](./assets/Basic_Neuron.png "Egyszerű neuron")

# Egyszerű neuron implementációja

Az alábbi példaprogram egyetlen neuron tanítását valósítja meg. A gradiensereszkedést (gradient descent) használom, de a hibafüggvény parciális deriválása helyett egy közelítést alkalmazok a jól ismert módszerrel.

1. *inicializálás*: véletlenszerű kezdő súly értékek beállítása

2. *előreterjesztés (feed forward)*: kiszámolom a neuron kimeneteit minden egyes bemenetre.

<p align="right"><sup><a href="README.md">Tartalom</a></sup></p>
