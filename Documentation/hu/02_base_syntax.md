# Bevezetés a Python nyelv szintaxisába

Ebben a fejezetben a Python nyelv alap szintakszisáról olvashatsz.

## Hello World! program

Az alábbi példa egy egyszerű Hello World! példaprogram, amely kiírja a képernyőre, hogy Hello World!

[Python Hello World example](https://repl.it/@nlharri/PythonHelloWorld)

(A továbbiakban ehhez hasonló, böngészőből futtatható példaprogramokat is fogok használni. A fenti ablakban a futtatás gombra kattintva elindítható a program, az ablak alsó részén látszik a futtatás eredménye. Az is látható, hogy Python 3.6.1 verziót használunk.)

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
