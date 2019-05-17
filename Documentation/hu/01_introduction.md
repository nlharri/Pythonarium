# Bevezető

Ebben a fejezetben megismerkedhetsz a Python programozási nyelv történetével, és az első lépésekkel, hogy elkezdhesd megtanulni a nyelvet. 

## A Python programozási nyelv története

A Python egy általános célú, nagyon magas szintű programozási nyelv, melyet Guido van Rossum holland programozó kezdett el fejleszteni 1989 végén, majd hozott nyilvánosságra 1991-ben. A nyelv tervezési filozófiája az olvashatóságot és a programozói munka megkönnyítését helyezi előtérbe a futási sebességgel szemben.

## Motiváció

A Python nyelv használata nagyon széleskörű. Általános programozási nyelvként könnyen tanulható és az egyik legsokoldalúbban alkalmazható programozási nyelv. Néhány fontosabb alkalmazási területe:
- általános szkriptnyelv rendszeradminisztrációs, automatizálási feladatokra
- parancssori alkalmazások fejlesztésére hatékonyan használható
- felhasználói felületek létrehozásának támogatása 
- külön területként említhető a weboldalak szisztematikus letöltése, feldolgozása, a webscraping
- webes alkalmazások fejlesztése
- adatbányászat, adattudomány, hatékony adatfeldolgozás és adatvizualizáció
- mesterséges intelligencia, neurális hálózatok definiálása és tanítása, gépi tanuló algoritmusok 
- képfeldolgozás, gépi látás
- számítógépes grafika, vizuális effektusok generálásakor a pipeline fejlesztéséhez is hatékonyan használható

A lista nem teljes, de jól látható, hogy milyen széleskörűen használható nyelv.

## Telepítés

A Python legfrissebb változata jelen dokumentum írásának idején a 3.7.3 verzió. Linux és macOS operációs rendszerek alatt valószínűleg meg alapból telepítve van egy Python verzió. Windows-hoz külön lehet letölteni és telepíteni.

A Python nyelvnek két változata van, a Python3 és a Python2. A Python3 olyan újításokat tartalmaz, ami miatt visszafelé nem kompatibilis. Én ebben a könyvben Python3-at használok, és ennek a telepítését ajánlom az Olvasónak is.

A Python3 miértjéről ebben a cikkben tájékozódhatsz (angolul): [STOP USING PYTHON 2: WHAT YOU NEED TO KNOW ABOUT PYTHON 3](https://hackaday.com/2018/08/15/stop-using-python-2-what-you-need-to-know-about-python-3/)

### Windows

Windowshoz a Python legfrissebb változata letölthető a [Python Software Foundation](https://www.python.org/downloads/) weboldalról. Telepítés után a Start Menüből indítható a Python shell.

![Python in Windows Start Menu](./assets/Python_in_Windows_Start_Menu.png "Python in Windows Start Menu")

### Linux

Linux operációs rendszer alatt többnyire már telepítve van egy Python verzió. Az aktuális telepített Python verzió lekérdezéséhez a következő parancsot használd:

```
python --version
python3 --version
```

![Python in Linux](./assets/Python_in_Linux.png "Python in Linux")

Amint látható, a python3-at külön paranccsal lehet elérni.

### macOS

macOS operációs rendszer alatt telepítve van egy Python verzió. A legfrissebb, macOS Mojave változat a Python 2.7-et tartalmazza alapból. 

![Python in macOS](./assets/Python_in_macOS.png "Python in macOS")


A Python 3 telepítésére többfajta módszer létezik. Amit én használtam, az a HomeBrew nevű csomagkezelő használata. Ehhez először a HomeBrew-t kell telepíteni:

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

majd pedig a HomeBrew segítségével a Pythont:

```
brew install python3
```

## Python shell

A Python interpretált nyelv. Ez azt jelenti, hogy a Python nyelven írt programot megírás után az interpreter futtatja. Nincs szükség olyan fordításra (compiling), melynek során a programnyelven írt programot egy futtatható állománnyá alakítjuk, amelyet az operációs rendszer és a processzor már közvetlenül értelmezni tudna.

Python programok futtatása a Python interpreterrel lehetséges.

### Python programok futtatása 

A következő lehetőségek állnak rendelkezésre:

- a Python program futtatása (pl. ```program.py```) a következő paranccsal: ```python program.py``` vagy ```python3 program.py```

- Python shell: a ```python``` vagy ```python3``` paranccsal indítható a terminal alkalmazásból (Windows operációs rendszeren PowerShell-ből)

- IPython: Interactive Python - ez egy parancsértelmező amely többfajta programozási nyelvet támogat, de eredetileg Pythonhoz fejlesztették ki. Sokfajta funkciót támogat, úgymint type introspection (változók és objektumok vizsgálata futási időben), parancsok tabulátor billentyűvel történő kiegészítése, illetve az eddig kiadott utasítások közötti visszakereshetőség (history).

## Csomagkezelés: ```pip```

Mi is az a ```pip```? A ```pip``` a Python standard csomagkezelője. Arra jó, hogy segítségével telepíthessünk és kezelhessünk olyan Python csomagokat, amik nem részei a Python alapkönyvtárának. Más programozási környezetből már ismerős lehet a koncepció, mint pl. JavaScript esetén az ```npm``` csomagkezelő, vagy Ruby esetében a ```gem```. 

A Python programozási nyelv Standard Könyvtára [Python Standard Library](https://docs.python.org/3/py-modindex.html) már nagyon sok alapvető csomagot tartalmaz, amelyek segítségével alkalmazások széles körét fejleszthetjük. Ugyanakkor a Python nyelvnek nagyon aktív közössége van, akik újabb és újabb csomagokat készítenek. Ezek a csomagok sok esetben a Pythonban már egy meglévő funkció vagy csomag használatát teszik egyszerűbb, például újabb interfészekkel.

Ezek a csomagok a [Python Package Index](https://pypi.org)-en kerülnek publikálásra.

Az alábbi példában telepítünk egy csomagot, a ```requests``` nevűt, amelynek a segítségével weboldalakat tudunk letölteni. Ugyanezt a funkciót a Python Standard Library csomagjaival is meg tudjuk valósítani, de a ```requests``` csomag jóval egyszerűbb, könnyebben használható interfészt nyújt.

```
pip install requests
```

A parancs kiadásának eredménye:

```
```

itt kell folytatni!!!

## Virtuális környezet: ```virtualenv```

A ```virtualenv``` egy Python csomag, amivel virtuális környezetet lehet létrehozni a Python projektünk számára. Tulajdonképpen létrehoz egy külön könyvtárat a Python projektünkhöz, és ez a könyvtár az összes külső függőséget (külső könyvtárakat, amiket a projektünk használ) tartalmazni fogja. 

A ```virtualenv``` telepítése ```pip``` segítségével:

```
pip install virtualenv
```

Majd a telepítés eredményének ellenőrzése a ```virtualenv``` verziójának lekérdezésével:

```
virtualenv --version
```

### Virtuális környezet létrehozása

Ehhez létre kell hoznunk egy új könyvtárat a projektünk számára, majd ezt a könyvtárat kijelölni a virtuális környezet számára.

```
mkdir MyNewPythonProjectVenv
virtualenv -p python3 MyNewPythonProjectVenv
```

Ezek után a ```MyNewPythonProjectVenv/bin``` könyvtár tartalmazni fogja a Python fordítót. Ahhoz, hogy ezt a virtuális környezetet használni tudjuk, vagyis ezen a virtuális környezeten belül kezdjünk el dolgozni, a következő parancsot kell kiadni:

```
source MyNewPythonProjectVenv/bin/activate
```

Innentől kezdve, ha telepítünk egy csomagot a ```pip```-pel, akkor az ebben a virtuális környezetben fog települni. Például a ```numpy``` csomag telepítése:

```
pip install --upgrade numpy
```

### Jelenleg telepített Python csomagok listája

Ha szeretnénk később ugyanezt a virtuális környezetet létrehozni, ugyanezekkel a telepített csomagokkal, például egy másik gépen, akkor szükségünk van arra a listára, hogy milyen csomagjaink lettek telepítve. Erre szolgál a következő parancs (a virtuális környezetből kell kiadni):

```
pip freeze > requirements.txt
```

Ez létrehozza a ```requirements.txt``` filet, ami tartalmazni fogja a csomagok listáját. Innentől kezdve ha telepíteni szeretnénk ezeket a csomagokat, azt megtehetjük ezzel a paranccsal:

```
pip install -r requirements.txt
```

## Python program futtatása online

Python kód online futtatására is van lehetőség, például az alábbiak:
- [Repl.it](https://repl.it) - én ezt tartom a legjobbnak egyszerű Python programok futtatására
- [Google Colab](https://colab.research.google.com/) - ez leginkább tudományos számításokhoz, gépi tanulás témakörében használható jól. Beépített GPU támogatással nagy számítási igényű modelleket is lehet tanítani vele.
- [Tutorialspoint online Python](https://www.tutorialspoint.com/execute_python_online.php)

## Kódszerkesztők, Integrált Fejlesztői Környezetek (IDE-k)

Az általam használt kódszerkesztő a [Visual Studio Code](https://code.visualstudio.com/). Egyéb kódszerkesztők és Integrált Fejlesztői Környezetek:
- [Atom editor](https://atom.io)
- [PyCharm](https://www.jetbrains.com/pycharm/)
- [IDLE](https://docs.python.org/3/library/idle.html)
