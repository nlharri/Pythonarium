![Pythonarium](../../PythonariumLogo.png)

# Python Tananyag

Ebből a dokumentációból megismerheted a Python programozási nyelv alapjait. Ez a leírás alapvetően programozóknak készült. Amennyiben még sosem programoztál semmilyen programozási nyelven, akkor is hasznos lehet ez a leírás. Viszont általánosságban a programozás alapvető elemeinek megismeréséhez javaslom egyéb források keresését. A Python egy nagyon jó kezdő nyelv azok számára, akik még nem tanultak programozni. Ennek az irománynak a célja mégsem az, hogy az abszolút nulla szintről megtanulj programozni. Alapvetően jó, ha úgy olvasod ezt a dokumentációt, hogy van már némi tapasztalatod a programozás terén.

Az Interneten rengeteg forrásanyag található Python programozással kapcsolatban. Ebben a dokumentációban lépésről lépésre ismerkedhetsz meg a Python nyelv elemeivel, az egyszerűbb témaköröktől a bonyolultabbak felé haladva. Sok szemléletes példa és alkalmazás segítségével megismerheted, hogy mennyire sokrétűen lehet használni ezt a programozási nyelvet.

# Jogi nyilatkozat

A nlharri Github usernévhez tartozó Pythonarium Github repositoryban közzétett cikkekben kifejezett nézetek és vélemények a szerzőé, és nem tükrözik a szerző munkáltatójának hivatalos álláspontját. A cikkek megjelenését nem támogatja semmilyen szervezet vagy vállalat. A cikkekben közölt információk kizárólag általános útmutatásul szolgálnak a cikk témájával kapcsolatban az Ön számára személyes használatra. Ön teljes mértékben elfogadja a cikkekben közölt információk használatával járó felelősséget. A cikkek szerzője mindent megtett, hogy a cikkekben közölt információk a valóságnak megfeleljenek a cikkek megírása idején. A cikkek szerzője kizár minden felelősséget a cikkekben közölt információk Ön által történő használata, és/vagy ennek eredménye által bármilyen módon, közvetlenül és/vagy közvetve okozott mindennemű kárért, beleértve, de nem kizárólagossággal a következők által bármilyen módon okozott és/vagy azokból bármilyen módon fakadó károkat:
- az Ön bármiféle tevékenysége, melyre esetleg a cikkekben közzétett információk ösztönözték Önt
- a cikkek elérésének lehetetlensége
- a cikkekben szereplő bizonyos információk helytelensége, hiányossága vagy elavultsága

# Tartalomjegyzék

## [Bevezetés a Python programozásba](01_introduction.md)

Bevezetés a Python programozási nyelv alapjaiba.

Tartalom:
- A Python programozási nyelv története
- Motiváció
- Telepítés
- Python shell
- Csomagkezelés: pip
- Virtuális környezet: virtualenv
- Python program futtatása online
- Kódszerkesztők, Integrált Fejlesztői Környezetek (IDE-k)

## [Bevezetés a Python nyelv szintakszisába](02_base_syntax.md)

Ebben a fejezetben a Python nyelv alap szintakszisáról olvashatsz.

- Hello World! program
- A Python interpreter
- Azonosítók
- Foglalt szavak
- Python objektumok, belső azonosító: `id()`, `is`
- Sorok és bekezdés
- Többsoros utasítások
- Megjegyzések elhelyezése a kódban
- Felhasználói bemenet feldolgozása
- Parancssori argumentumok

## [Haladó Python - Első rész](03_advanced_python_part_01.md)

Ebben a részben az összetett adatokkal való műveletekről lesz szó.

- Adattípusok
- Függvények
- Dekorátorok
- Összetett adattípusok
- Referenciák

<!--

## [Haladó Python - Második rész](03_advanced_python_part_02.md)

Ebben a részben az összetett adatokkal való műveletekről lesz szó, továbbá megismerjük a Python vezérlő utasításait.

- Összetett adattípusok - folytatás
- Iterátorok
- Beépített könyvtárak
- Vezérlő utasítások (control flow)
- Referenciák


## Modulok, csomagok (package), névtér (namespace), hatáskör (scope)

## Objektumorientált programozás Pythonban

## Adatstruktúrák és algoritmusok

## Unit teszt és integration teszt Pythonban

A fejezet alapjául szolgáló mű: [Getting Started With Testing in Python (by RealPython)](https://realpython.com/python-testing/)

## Külső könyvtárak használata

## Python használata automatizálásra

Ebben a fejezetben megismerheted, hogy hogyan lehet a Python nyelvet praktikusan használni olyan feladatokra, amelyek kézzel elvégezve órákig tartanának. A fejezet alapjául szolgáló mű: [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/).

## Python használata weboldalak szisztematikus feldolgozására (webscraping). A BeautifulSoup csomag

A fejezet alapjául a következő tutorial szolgált: [Tutorial: Python Web Scraping Using BeautifulSoup (by DataQuest)](https://www.dataquest.io/blog/web-scraping-tutorial-python/)

## Python használata hálózati programozáshoz

## Python használata felhasználói felületek létrehozására: Tkinter, Kivy, PySide2

Ebben a fejezetben desktop alkalmazások fejlesztését mutatom be három különböző Python könyvtár használatán keresztül.

### Tkinter alapok

### Kivy alapok

### PySide2 alapok

## Python használata webfejlesztésre. Django és Flask

### Django alapok

### Flask alapok

## Python használata képfeldolgozásra. Ismerkedés az OpenCV-vel (Open Source Computer Vision Library)

Ebben a fejezetben a képfeldolgozás alapjaival ismerkedhetsz meg a népszerű OpenCV könyvtár használatán kersztül. 

A fejezet alapjául szolgáló weboldal: [OpenCV Tutorial: A Guide to Learn OpenCV](https://www.pyimagesearch.com/2018/07/19/opencv-tutorial-a-guide-to-learn-opencv/)

## Python használata a tudományos számításokhoz

Ebben a fejezetben a Python felhasználási lehetőségeit ismertetem a tudományos számítások világában.

Referencia: [Python Data Science Handbook (Jake VanderPlas)](https://jakevdp.github.io/PythonDataScienceHandbook/)

### A SciPy ökoszisztéma

A SciPy ökoszisztéma elemei.

- NumPy
- SciPy könyvtár
- Matplotlib
- IPython
- SymPy
- Pandas

### Ismerkedés a NumPy könyvtárral

### Ismerkedés a SciPy könyvtárral

### Ismerkedés a Matplotlib könyvtárral

### Ismerkedés a IPython könyvtárral

### Ismerkedés a SymPy könyvtárral

### Ismerkedés a Pandas könyvtárral

## Python használata a mesterséges intelligenciában és gépi tanulásban. Bevezetés a Tensorflow és a Keras használatába

Referencia: [Python Data Science Handbook (Jake VanderPlas)](https://jakevdp.github.io/PythonDataScienceHandbook/)

### Mesterséges intelligencia, neurális hálózatok

### Neurális hálózatok architektúrája

### Népszerű Python könyvtárak gépi tanuláshoz és neurális hálózatok létrehozásához

A jeleneg legnépszerűbb Python könyvtárak rövid ismertetése.

- Tensorflow és Keras
- PyTorch
- Theano
- Scikit-learn
- Microsoft Cognitive Toolkit (CNTK)


### TensorFlow és Keras alapok

Ismerkedés a Tensorflow alapjaival.

- Session-ök
- Gráfok
- Változók, tenzorok
- Placeholder-ek

### Az első Tensorflow neurális hálózataink felépítése: egy egyszerű neuron

### Az első Tensorflow neurális hálózataink felépítése: képek klasszifikálása, az MNIST adathalmaz

### Az első Tensorflow neurális hálózataink felépítése: képek klasszifikálása, kutya vagy macska?

### CNNs - Convolutional Neural Networks

### RNNs - Recurrent Neural Networks

### GANs - Generative Adversarial Networks

-->

## [Egyszerű neurális hálózatok építése Pythonban](misc01_building_basic_neural_networks.md)

- Bevezető
- Egyetlen neuron 
- Egyszerű neuron implementációja
- Mire alkalmas egyetlen neuron?
- Több neuronból álló hálózat
- Több neuronból álló hálózat tanítása
- Referenciák


## [Gráfalgoritmusok Pythonban - Szélességi és mélységi bejárás](misc02_graph_algorithms.md)

- Mik a gráfok?
- Gráfok tárolása
- Gráfbejárás szélességi kereséssel
- Gráfbejárás mélységi kereséssel
- Referenciák

<!--

## [Gráfalgoritmusok Pythonban - Legrövidebb és leghosszabb utak keresése](misc03_graph_algorithms.md)

- Bevezető
- Legrövidebb út kereséses két csúcs között
- Leghosszabb út kereséses két csúcs között
- Referenciák


## Python példafeladatok megoldással

-->

## Források, Hivatkozások
- [Bevezetés a Python Programozásba](http://szerver2.lacszki.sulinet.hu/tananyag/informatika/python.pdf)
- [Python - Basic Syntax](https://www.tutorialspoint.com/python/python_basic_syntax.htm)
- [Python Oktató](http://pythontutorial.pergamen.hu/downloads/tut.pdf)
- [Python programozási nyelv - Wikipedia](https://hu.wikipedia.org/wiki/Python_(programoz%C3%A1si_nyelv))
- [OpenCV Tutorial: A Guide to Learn OpenCV](https://www.pyimagesearch.com/2018/07/19/opencv-tutorial-a-guide-to-learn-opencv/)
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
- [Tutorial: Python Web Scraping Using BeautifulSoup (by DataQuest)](https://www.dataquest.io/blog/web-scraping-tutorial-python/)
- [Python Data Science Handbook (Jake VanderPlas)](https://jakevdp.github.io/PythonDataScienceHandbook/)
- [Introduction to Deep Neural Networks with Keras and Tensorflow](https://github.com/leriomaggio/deep-learning-keras-tensorflow)
- [Jupyter notebooks for the code samples of the book "Deep Learning with Python"](https://github.com/fchollet/deep-learning-with-python-notebooks)
- [CS228 Python Tutorial](https://github.com/kuleshov/cs228-material/blob/master/tutorials/python/cs228-python-tutorial.ipynb)
- [Deep Learning a gyakorlatban Python és LUA alapon](https://github.com/BME-SmartLab-Education/vitmav45/blob/master/01/03-LUA-alapok-compiled.ipynb)
- [Getting Started With Testing in Python (by RealPython)](https://realpython.com/python-testing/)
- [Coursera Machine Learning course by Andrew Ng](https://www.coursera.org/learn/machine-learning)
- [Virtuális környezet használata Python 3.5+ -ben](https://arato.inf.unideb.hu/szathmary.laszlo/pmwiki/index.php?n=Py3.Virtualenv)
- [What Is Pip? A Guide for New Pythonistas](https://realpython.com/what-is-pip/)
- [Pipenv & Virtual Environments](https://docs.python-guide.org/dev/virtualenvs/)
