![Pythonarium](../../PythonariumLogo.png)

<p align="right"><sup><a href="02_base_syntax.md">Előző fejezet</a> | <a href="README.md">Tartalom</a></sup></p>

# Haladó Python

Ebben a részben az összetett adatokkal való műveletekről lesz szó, továbbá megismerjük a Python vezérlő utasításait.

## Adattípusok

A Python 3-ban minden adattípus objektumként van kezelve. Ezen belül lehetséges, hogy egy típus megváltoztatható (mutable), és nem megváltoztatható (immutable). A megváltoztathatóság azt jelenti, hogy az adott típusú objektum értéke megváltozhat anélkül, hogy az `id()`-ja megváltozna. Ha az objektum megváltoztathatatlan, akkor van egy fix értéke. Ha egy másik értéket szeretnénk tárolni ugyanazon a néven (vagyis ugyanabban a változóban), akkor egy másik objektumot hoz létre a rendszer. Fontos szerepük van az ilyen objektumoknak azokban az esetekben, amikor egy állandó hash értékre van szükség, pl. a szótár (dictionary, `dict`) típusú objektumok kulcsainál.

Egy másik fontos fogalom a hash-elhetőség. Egy objektum hash-elhető, ha van egy hash értéke, ami nem változik meg az objektum élettartama során (szükséges, hogy az objektumnak legyen egy `__hash__()` nevű metódusa), és összehasonlításra lehet használni (szükséges egy `__eq__()` nevű metódus is). Az egyező objektumok hash értékének azonosnak kell lennie.

A Python 3-ban a következő adattípusokat használhatjuk:
- logikai típus: `bool`: igaz/hamis értékkel (`True`/`False`)
- numerikus típusok
  - `int`: egész szám
  - `float`: lebegőpontos szám
  - `complex`: komplex szám
  - `decimal.Decimal`: decimális típus a Decimal modul segítségével
- `iterator`: iterátor típus; `generator`: generátor típus
- szekvenciális típusok: 
  - `list`: lista 
  - `array.array`: tömb, az `array` modul implementálja
  - `tuple`: n db elemet tartalmazó, nem megváltoztatható adatszerkezet
  - `range`: egész számokból álló számtani sorozat
- `str`: szöveges adattípus
- bináris szekvenciális típusok:
  - `bytes`: byte-okból álló, nem megváltoztatható sorozat
  - `bytearray`: a `bytes` objektum megváltoztatható változata
  - `memoryview`: lehetővé teszi objektumok belső adatának elérését Pythonban
- halmaz típusok:
  - `set`: hash-elhető objektumok nem sorrendezett gyűjteménye. Megváltoztatható, és hash-elhető a `set`.
  - `frozenset`: A `set` nem megváltoztatható változata
- "mapping" típus: `dict`: kulcs-érték párokat tároló típus, "szótár". Egy hash-elhető értéket leképez egy tetszőleges objektumra. Megváltoztatható adatszerkezet.

Megváltoztathatóság szempontjából a következőképpen néznek ki a Python adattípusok:


| Típus (osztály) | Megváltoztatható |
|-----------------|------------------|
| bool            | nem              |
| int             | nem              |
| decimal.Decimal | nem              |
| float           | nem              |
| complex         | nem              |
| list            | igen             |
| array.array     | nem              |
| tuple           | nem              |
| range           | nem              |
| str             | nem              |
| bytes           | nem              |
| bytesarray      | igen             |
| memoryview      | igen             |
| set             | igen             |
| frozenset       | nem              |
| dict            | igen             |


Egy adatelem, változó típusát a type utasítással lehet lekérdezni:

```
>>> a = 2
>>> b = 123.45
>>> c = 'something'
>>> d = 'today is Wednesday' == 'something'
>>> a
2
>>> b
123.45
>>> c
'something'
>>> d
False
>>> type(a)
<class 'int'>
>>> type(b)
<class 'float'>
>>> type(c)
<class 'str'>
>>> type(d)
<class 'bool'>
>>> type(type(a))
<class 'type'>
```

## Függvények

Függvényeket a `def` kulcsszóval lehet definiálni.

```python
def print_welcome():
  print("Welcome!")
  
print_welcome()
```
Kimenet:

```
Welcome!
```

A függvények első részében egy (egy- vagy többsoros) opcionális dokumentációt lehet elhelyezni. A függvény paramétereit a név utáni zárójelben soroljuk fel.

```python
def square_plus_3(x):
    """
    Return the number's square incremented by 3
    """
    return x*x+3

print(square_plus_3(4))
```

```
19
```

Több paramétert is definiálhatunk:

```python
import math

def distance_of_two_points(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

print(distance_of_two_points(2,3,4,5))
```

```
2.8284271247461903
```

### Paraméterek, paraméter-átadás függvényeknek

Egy Python függvényt a következőképpen lehet felhívni:
- Kötelező (required) argumentumok: ezeket kötelező megadni, és olyan sorrendben kell szerepelniük, ahogyan definiáltuk őket. A felhíváskor megadott argumentumok száma meg kell, hogy egyezzen a definíciókor megadott argumentumok számával.
- Kulcsszavas (keyword) argumentumok: a híváskor az argumentum neve alapján azonosítja a rendszer, hogy melyik argumentumnak milyen értéket vesz fel. Ez lehetővé teszi, hogy kihagyjunk argumentumokat (amelyeknek van alapértelmezett értéke, lást alapértelmezett argumentumok), illetve hogy különböző sorrendben hívjuk adjuk meg az argumentumokat, mint amilyen sorrendben a definíciónál szerepel.
- Alapértelmezett (default) argumentumok: ezek olyan argumentumok, amik felvesznek egy alapértelmezett értéket, amennyiben felhíváskor nincsen megadva az argumentum.
- Változó hosszúságú (variable length) argumentumlista: vannak esetek, amikor nem tudjuk előre pontosan megmondani a függvény definíciójakor, hogy hány db argumentumra van szükség. Ezekben az esetekben a függvény utolsó argumentuma egy `tuple` típusú változó, amelyben a további argumentumok vannak felsorolva. Ez a `tuple` üres, ha nincsenek további argumentumok.

Az alábbiakben ezekre mutatok példákat:

#### Kötelező argumentumok

Az alábbi függvénynél kötelező megadni az egyetlen argumentumot.

```python
def plus2mul2(x):
    x+=2
    return x*2

n = 5
plus2mul2(n)
plus2mul2(n)
print(n)
print(plus2mul2(n))

print(plus2mul2(12))
print(plus2mul2(plus2mul2(12)))
```

```
>>> n = 5
>>> plus2mul2(n)
14
>>> plus2mul2(n)
14
>>> print(n)
5
>>> print(plus2mul2(n))
14
>>> print(plus2mul2(12))
28
>>> print(plus2mul2(plus2mul2(12)))
60
```

#### Kulcsszavas argumentumok

Az alábbi függvényben a paraméterek neve `a` és `b`. 

```python
def rectangle_area(a,b):
    print("a={}".format(a))
    print("b={}".format(b))
    return a*b

rectangle_area(a=4, b=3)
rectangle_area(3, 4)
```

```
>>> rectangle_area(a=4, b=3)
a=4
b=3
12
>>> rectangle_area(3, 4)
a=3
b=4
12
```

#### Alapértelmezett argumentumok

Az alábbi függvénynél az `x` argumentum alapértelmezett `0` értéket kap, tehát ha nem adjuk meg, az olyan, mintha `0`-t adtunk volna meg.

```python
def plus2mul2(x=0):
    x+=2
    return x*2

plus2mul2()
plus2mul2(0)
n = 5
plus2mul2(n)
```

```
>>> plus2mul2()
4
>>> plus2mul2(0)
4
>>> n = 5
>>> plus2mul2(n)
14
```

#### Változó hosszúságú argumentumlista



### Lambda függvények

```python
def multiplier(n):
  return lambda a : a * n

tripler = multiplier(3)
print(tripler(12))
print(multiplier(4)(12))
multiply_by_48 = multiplier(48)
print(multiplier(4)(multiplier(4)(12)))
print(multiply_by_48(10))
```

```
5
14
28
60
```

## Dekorátorok

## Listák és egyéb összetett adattípusok

## Iterátorok

## Beépített könyvtárak

## Vezérlő utasítások (control flow)

## Objektum-orientáltság

## Referenciák

- [Mutable vs Immutable Objects in Python (megha mohan)](https://medium.com/@meghamohan/mutable-and-immutable-side-of-python-c2145cf72747)
- [Built-in Types - Python documentation](https://docs.python.org/3/library/stdtypes.html)
- [PEP 3137 -- Immutable Bytes and Mutable Buffer](https://www.python.org/dev/peps/pep-3137/)
- [Python - Functions](https://www.tutorialspoint.com/python/python_functions.htm)

<p align="right"><sup><a href="02_base_syntax.md">Előző fejezet</a> | <a href="README.md">Tartalom</a></sup></p>
