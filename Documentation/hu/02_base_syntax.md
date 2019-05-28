![Pythonarium](../../PythonariumLogo.png)

<p align="right"><sup><a href="01_introduction.md">Előző fejezet</a> | <a href="README.md">Tartalom</a></sup>

# Bevezetés a Python nyelv szintaxisába

Ebben a fejezetben a Python nyelv alap szintakszisáról olvashatsz.

## Hello World! program

Az alábbi példa egy egyszerű Hello World! példaprogram, amely kiírja a képernyőre, hogy Hello World!

[Python Hello World example](https://repl.it/@nlharri/PythonHelloWorld)

(A továbbiakban ehhez hasonló, böngészőből futtatható példaprogramokat is fogok használni. A fenti ablakban a futtatás gombra kattintva elindítható a program, az ablak alsó részén látszik a futtatás eredménye. Az is látható, hogy Python 3.6.1 verziót használunk. Az ablak alsó része a Python interpreter.)

A fenti példaprogramban a `print` egy beépített függvény a Pythonban. Ez a függvény arra szolgál, hogy szövegeket írjunk ki a képernyőre (konzolra). További információt erről a függvényről a Python interpreterből kérhetünk:

```python
help(print)
```

Ennek hatására a megjelenő szöveg:

```
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
```

A paraméterátadás lehetőségeiről a későbbiekben lesz szó részletesen.

## A Python interpreter

Az alábbiakban a Python interpretert fogom használni néhány egyszerű műveletre. Néhány adattípus már most is előkerül, de ezekről részletesen lesz szó később. A példákban a `>>>` karaktersorozat a prompt. A prompt utáni részt kell begépelni az interpreterbe, hogy végrehajtsa az utasítást. Az alatta lévő sorban a Python kiírja a végrehajtás eredményét. (A végrehajtás az ENTER gombbal történik.)

### Számológép

Ha csak egyszerű matematikai műveleteket írunk be, akkor az egész úgy működik, mint egy számológép.

```
>>> 4+5+6
15
>>> 3*5
15
>>> 12*2
24
>>> 20/7
2.857142857142857
>>> 20//7
2
>>> 20%7
6
```

A `/` az osztás művelet, a `//` pedig az egészosztás. A `%` művelet a maradékos osztás maradékát adja meg.

### Típusok

A Pythonban a következő egyszerű típusúak lehetnek a változóink. A típusokról a későbbiekben még lesz szó, de az alábbi példák megértéséhez fontos, hogy lássuk, milyen típusok lehetnek. Vannak összetett adattípusok is, amikről később szintén lesz szó.

* Egész szám (integer)

* Lebegőpontos szám (float)

* Komplex szám (complex)

* Karakterláncok (string)

* Igaz/hamis logikai érték (boolean)

### Karakterláncok (stringek)

Változóknak `=` jellel lehet értéket adni. A változó típusa futás során dől el, nem kell megadni értékadáskor, vagy előre definiálni a változót, és futás közben más típusú adatot is adhatok a változónak. Az egész dinamikus. A Pythonban egyébként mindent objektumként kezel a rendszer, erről a későbbiekben még lesz szó.

Karakterláncok definiálása az aposztróf vagy idézőjel karakterekkel lehetséges. Ezek használatának részleteiről az "Idézőjelek szerepe" alfejezetben olvashatsz. A `+` karakterrel össze lehet kapcsolni karaktersorozatokat.

```
>>> gepjarmu_marka = 'BMW'
>>> gepjarmu_tipus = '118i'
>>> gepjarmu_megnevezes = gepjarmu_marka + ' ' + gepjarmu_tipus
>>> gepjarmu_megnevezes
'BMW 118i'
```

Ha egymás mellé írunk sztringliterálokat szóközzel elválasztva, akkor azokat is összekapcsolja a Python. Viszont ez változókkal nem működik.

```
>>> a = 'abcd' 'efgh'
a = 'abcd' 'efgh'
>>> a
'abcdefgh'
>>> b = 'ijkl'
b = 'ijkl'
>>> c = a b
  File "<stdin>", line 1
    c = a b
          ^
SyntaxError: invalid syntax
>>> c = b 'zzz'
  File "<stdin>", line 1
    c = b 'zzz'
              ^
SyntaxError: invalid syntax
```

Stringeknél a `'` karakterek közé kell tenni a string tartalmát. Viszont mi van, ha magát a `'` karaktert akarjuk beletenni a stringbe? Több lehetőségünk is van. Az alábbi listában a stringek definiálásának a lehetőségeit láthatod:

* `"` karakter használata:

```
>>> title = "Python Developer's Guide"
>>> title
"Python Developer's Guide"
```

* `'` karakter használata:

```
>>> title = 'Python Developers Guide'
>>> title
'Python Developer's Guide'
```

* "escape sequence" használata: ezek speciális karaktersorozatok, amelyekkel megváltoztathatjuk az utánuk következő karakter(ek) jelentését. Tipikus példák: `\'`, `\"`, `\n`, `\\` - ezek jelentése sorrenben: `'` karakter, `"` karakter, újsor karakter, `\` karakter.

```
>>> title = 'Python Developer\'s Guide'
>>> title
"Python Developer's Guide"
>>> title = 'Python\nDeveloper\'s\nGuide"
>>> print(title)
Python
Developer's
Guide
>>> quote = "\"When words fail, music speaks.\"\n - Shakespeare"
>>> print(quote)
"When words fail, music speaks."
 - Shakespeare
```

* `"""` vagy `'''` karaktersorozat használata: Ebben az esetben az utána levő karaktersorozat újsorok szempontjából egy az egyben úgy kerül bele a stringbe, ahogy látjuk. Tehát az újsorjelek benne lesznek. Láthatjuk azt is az alábbi példából, hogy ha csak simán beírjuk a változó nevét az interpreterbe, és nem a print függvényt használjuk, akkor másként jelenik meg a string. A `"""` vagy `'''` karaktersorozat használata esetén is történik escape sequence helyettesítés.

```
>>> quote = """
... "An investment in knowledge pays the best interest"
...  - Benjamin Franklin"""
>>> print(quote)
"An investment in knowledge pays the best interest"
 - Benjamin Franklin
>>> quote
'\n"An investment in knowledge pays the best interest"\n - Benjamin Franklin'
>>> a = """
... a\n
... b\n
... """
>>> print(a)
a
b
>>> a
'\na\n\nb\n\n'
```

* "raw" sztringliterál definiálása: `r''`: ez egy olyan string, amiben pontosan a megadott karakterek vannak, tehát nincsen escape sequence helyettesítés.

```
>>> rawstring = r'\"this is\nmy\rawsting\"'
>>> print(rawstring)
\"this is\nmy\rawsting\"
>>> rawstring
'\\"this is\\nmy\\rawsting\\"'
```

* unicode sztringliterál használata: `u''`

```
>>> cat = u"\U0001F431"
>>> print(cat)
🐱
```

Stringekkel sokféle műveletet végezhetünk. Az alábbiakban néhány példát láthatunk erre.

```
>>> my_str = "Hello World!"
>>> my_str.isalnum()
False
>>> my_str.isalpha()
False
>> my_str.upper()
'HELLO WORLD!'
>>> my_str.lower()
'hello world!'
>>> my_str.islower()
False
>>> my_str.isupper()
False
>>> my_str.lower().islower()
True
>>> my_str.upper().isupper()
True
```

Amint látható, a fenti függvényeket a string változón (objektumon) hívtuk meg. Némely közülük igaz/hamis értékkel tér vissza (`boolean`). A fenti példákból az is látszik, hogy az `upper()` és `lower()` függvények egy új stringet hoznak létre. A stringműveletekről részletesen a referencia dokumentációban olvashatunk.

[string - Common string operations](https://docs.python.org/3/library/string.html)

### Boolean értékek

A boolean típus igaz (`True`) vagy hamis (`False`) értéket vehet fel. Az alábbi példákban a `==` és `!=` operátorokat használjuk két érték egyenlőségének eldöntésére.

```
>>> 1==2
False
>>> 1==1
True
>>> 1!=1
False
>>> a = (1==2)
>>> b = (2==2)
>>> a
False
>>> b
True
>>> a == b
False
>>> a != b
True
```

### Komplex számok

A Python beépítetten támogatja a komplex számokat.

```
>>> a = 1 + 2j
>>> b = 3 + 4j
>>> c = a + b
>>> c
(4+6j)
```

Később még lesz szó a csomagokról, viszont itt érdemes megjegyezni, hogy van egy cmath nevű beépített csomag, amivel komplex számok kezelését támogatja a Python.

```
>>> import cmath
>>> cmath.sqrt(-1)
1j
```

### Tömbök

Tömbök (array) vagy másnéven listák (list) definiálására a `[` és `]` karakterek használhatók. A tömb egy adott elemét is megcímezhetjük így. Az elemek indexelése 0-tól kezdődik.

```
>>> allatok = ['nyúl', 'kacsa', 'liba', 'teknős', 'viziló'] 
>>> allatok[2]
'liba'
```

Az összetett adattípusokról később még lesz szó részletesen.

## Azonosítók

A Python azonosítók olyan nevek, amelyekkel azonosítunk változókat, függvényeket, osztályokat, modulokat és egyéb objektumokat. Az azonosító az angol ABC betűiből (kis és nagybetűk külön számítanak, a Python case sensitive), `_` karakterből, és számjegyekből állhat. Csak betűvel vagy `_` karakterrel kezdődhet. A Python nem engedi speciális karakterek használatát, mint például a `@`, `$` vagy `%`.

```
>>> valtozo1 = 12
>>> VALTOZO1 = 23
>>> valtozo1
12
>>> VALTOZO1
23
```

## Foglalt szavak

Az alábbi táblázat a Python foglalt szavait tartalmazza. Ezek a szavak a Python nyelvben speciális jelentéssel bírnak, emiatt nem használhatók azonosítóként. A Python nyelv foglalt szavai csak kisbetűket tartalmaznak.

```
|----------|--------|---------|--------|-------|--------|
| and      | def    | exec    | if     | not   | return |
|----------|--------|---------|--------|-------|--------|
| assert   | del    | finally | import | or    | try    |
|----------|--------|---------|--------|-------|--------|
| break    | elif   | for     | in     | pass  | while  |
|----------|--------|---------|--------|-------|--------|
| class    | else   | from    | is     | print | with   |
|----------|--------|---------|--------|-------|--------|
| continue | except | global  | lambda | raise | yield  |
|----------|--------|---------|--------|-------|--------|
```

Amennyiben foglalt szóval szeretnénk egy változót elnevezni, akkor szintaktikai hibát kapunk.

```
>>> for = 123
for = 123
  File "<stdin>", line 1
    for = 123
        ^
SyntaxError: invalid syntax
>>> For = 123
>>> return = a
  File "<stdin>", line 1
    return = a
           ^
SyntaxError: invalid syntax
```

## Sorok és bekezdés

## Többsoros utasítások

## Idézőjelek szerepe

## Megjegyzések elhelyezése a kódban

## Üres sorok használata

## Felhasználói bemenet feldolgozása

## Több utasítás egy sorban

## Parancssori argumentumok

A Pythonban a `sys.argv` tömb stringeket tartalmaz, amelyek a Python interpreter indításakor használt paramétereket tartalmazzák. Soha nem lehet üres. 

A Python interpreter felhívása során a parancssori argumentumokat átadása és feldolgozása szempontjából a következő eseteket különböztetjük meg:

* Interpreter indítása egy script file-lal: a `sys.argv` tömb első eleme a script file neve, a további elemei az script fájl nevét követő argumentumok. (Ha script nélkül indítjuk az interpretert, akkor a `sys.argv[0]` üres string lesz. 

* Script név helyett `-` karakter használata: ezáltal a Python interpreter a standard inputról veszi az utasításokat amiket futtat. Ebben az esetben a `sys.argv[0]` értéke `-` lesz. 

* Script név helyett `-c parancs` használata: `sys.argv[0]` értéke `-c` lesz, és az ezután megadott argumentumokat is tartalmazza a `sys.argv`, tehát ezeket a `parancs` utasításnak kell feldolgoznia. 

# Befejezés

Köszönöm a figyelmet. A következő részben mélyebben beleássuk magunkat a Python világába.

<p align="right"><sup><a href="01_introduction.md">Előző fejezet</a> | <a href="README.md">Tartalom</a></sup>
