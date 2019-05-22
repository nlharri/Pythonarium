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

### Boolean értékek

### Komplex számok

### Tömbök

Tömbök (array) vagy másnéven listák (list) definiálására a `[` és `]` karakterek használhatók. A tömb egy adott elemét is megcímezhetjük így. Az elemek indexelése 0-tól kezdődik.

```
>>> allatok = ['nyúl', 'kacsa', 'liba', 'teknős', 'viziló'] 
>>> allatok[2]
'liba'
```

Az összetett adattípusokról később még lesz szó részletesen

## Azonosítók

## Foglalt szavak

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

## Befejezés

Köszönöm a figyelmet. A következő részben mélyebben beleássuk magunkat a Python világába.
