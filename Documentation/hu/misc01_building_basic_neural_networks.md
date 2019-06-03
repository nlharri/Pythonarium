![Pythonarium](../../PythonariumLogo.png)

<p align="right"><sup><a href="01_introduction.md">Előző fejezet</a> | <a href="README.md">Tartalom</a></sup></p>

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

<p align="right"><sup><a href="01_introduction.md">Előző fejezet</a> | <a href="README.md">Tartalom</a></sup></p>
