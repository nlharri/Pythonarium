# Bevezetés a Python nyelv szintaxisába

Ebben a fejezetben a Python nyelv alap szintakszisáról olvashatsz.

## Hello World! program

Az alábbi példa egy egyszerű Hello World! példaprogram, amely kiírja a képernyőre, hogy Hello World!

[Python Hello World example](https://repl.it/@nlharri/PythonHelloWorld)

(A továbbiakban ehhez hasonló, böngészőből futtatható példaprogramokat is fogok használni. A fenti ablakban a futtatás gombra kattintva elindítható a program, az ablak alsó részén látszik a futtatás eredménye. Az is látható, hogy Python 3.6.1 verziót használunk.)



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
