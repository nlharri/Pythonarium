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
- `dict`: kulcs-érték párokat tároló szótár típus. Egy hash-elhető értéket leképez egy tetszőleges objektumra. Megváltoztatható adatszerkezet.

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

Ha a függvény definíciójának argumentumlistájában van egy `**kwargs` argumentum (itt igazából a név elején szereplő `**` a lényeg, a `**kwargs` elnevezés csak egy elterjedt szokás, de nem kell feltétlenül így hívni), akkor ez az argumentum azokat a kulcsszavas argumentumokat fogja tartalmazni, amik nem szerepelnek a formális argumentumlistájában.

Például az előbbi függvényt így is definiálhatjuk:

```python
def rectangle_area(**kwargs):
    print("a={}".format(kwargs["a"]))
    print("b={}".format(kwargs["b"]))
    return kwargs["a"] * kwargs["b"]

rectangle_area(a=4, b=3)
```

```
>>> rectangle_area(a=4, b=3)
a=4
b=3
12
```

Viszont ilyenkor meg kell adni a nevet:

```
>>> rectangle_area(3, 4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: rectangle_area() takes 0 positional arguments but 2 were given
```

Ha a függvény felhívásakor nem adunk meg minden paramétert, de a függvényen belül használjuk, akkor is hibát dob a rendszer:

```
>>> rectangle_area(a=4)
a=4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in rectangle_area
KeyError: 'b'
```

Tehát az ilyen esetet le kell védeni megfelelő hibakezeléssel.

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

Az alábbi függvény az argumentumokban megadott, tetszőleges mennyiségű számot szorozza össze. Legalább két argumentumot meg kell adni, a többi opcionális.

```python
def multiply_numbers(n1, n2, *n):
    result = n1*n2
    for i in n:
        result*=i
    return result

print(multiply_numbers(1,2,3,4,5))
print(multiply_numbers(5,10,12,74,331))

print(multiply_numbers(2)) # error
```

```
>>> print(multiply_numbers(1,2,3,4,5))
120
>>> print(multiply_numbers(5,10,12,74,331))
14696400
>>> 
>>> print(multiply_numbers(2)) # error
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: multiply_numbers() missing 1 required positional argument: 'n2'
```

#### Kulcsszavas argumentumok és nem kulcsszavas arguentumok együttes használata

Lehetőség van rá, hogy kulcsszavas és nem kulcsszavas arguentumokat egyszerre használjunk a függvényben. Az alábbi függvényben `*args` néven elérhetők a nem kulcsszavas argumentumok, és `**kwargs` néven elérhetők a további kulcsszavas argumentumok. Az `*args`nak minding meg kell előznie a `**kwargs` argumentumot.

```python
def number_mapper(one, two, *args, **kwargs):
    print("one: {}".format(one))
    print("two: {}".format(two))
    for arg in args:
        print(arg)
    for key in kwargs.keys():
        print("{}: {}".format(key, kwargs[key]))

number_mapper("1", "2", "3", "4", "5", six="6", seven="7", eight="8")
```

```
>>> number_mapper("1", "2", "3", "4", "5", six="6", seven="7", eight="8")
one: 1
two: 2
3
4
5
six: 6
seven: 7
eight: 8
```

### Lambda függvények, anonim függvények

A Pythonban a `lambda` kulcsszóval lehet anomim függvényeket definiálni, melyek egyetlen utasításból állnak. azért anonim függvény, mert sok esetben nincs külön elnevezése. Az alábbi példában a `multiplier` nevű függvény, melynek egy paramétere van (`n`), egy lambda függvényt ad vissza. A lambda függvénynek egyetlen paramétere van (`a`), és a visszatérési értéke ezen paraméter (`a`) értékének, és a `multiplier` függvény hívásakor megadott paraméter (`n`) értékének a szorzata.

Tehát, ha a `multiplier` függvényt 3-as értékkel, mint paraméterrel hívjuk, akkor kapunk egy olyan, egy paraméterrel rendelkező függvényt, amit felhívva a megadott paraméter 3-szorosát adja vissza.

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

A lambda függvények másik tipikus alkalmazása az úgynevezett funkcionális programozás témakörével kapcsolatos. Az alábbi példáról még részletesebben lesz szó később. Ebben az alfejezetben csak annyit jegyzünk meg, hogy a filter függvény első paraméterében megadott lambda anonim függvény `bool` típussal tér vissza, és `False` értékkel, ha a lambda függvény paraméterében megadott `a` szám értéke pozitív, és `True` értékkel, amennyiben negatív. 

```python
numbers_negative = list(filter(lambda a : a < 0, range(-10,10)))
print(numbers_negative)
```

```
>>> print(numbers_negative)
[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
```

## Dekorátorok

A Pythonban a dekorátorok (decorators) olyan függvények, amikkel egy már meglévő objektumot lehet kibővíteni anélkül, hogy az eredeti objektumot megváltoztatnánk. Általában azelőtt hívódnak fel, mielőtt az eredeti funkció meghívódik.

Nagyon fontos megérteni, hogy a Pythonban minden objektum. A függvények is, ami azt jelenti, hogy a függvényeket át lehet adni paraméterként más függvényeknek, lehet függvény egy másik függvény visszatérési értéke, lehet módosítani egy függvényt, lehet egy változónévhez rendelni függvényt. 

Példaként először vegyük az alábbi függvényt, ami a megadott szám négyzetét adja vissza:

```python
def square_of_x(x):
    return x**2

square_of_x(2)
square_of_x(-2)
```

```
>>> square_of_x(2)
4
>>> square_of_x(-2)
4
```

Tegyük fel, hogy ez a függvény már korábban rendelkezésünkre állt, viszont arra van szükségünk, hogy csak a pozitív számok négyzetét számoljuk ki. Negatív esetben pedig a négyzet ellentettjére van szükségünk. Tehát valami ilyesmire:

```python
def square_of_x_special(x):
    if (x>0):
        return x**2
    else:
        return -(x**2)

square_of_x_special(2)
square_of_x_special(-2)
```

```
>>> square_of_x_special(2)
4
>>> square_of_x_special(-2)
-4
```

Tehát el is készítettük az új függvényünket. De mi a helyzet akkor, ha ezt a már meglévő függvényünk segítségével szeretnénk elkészíteni Éredemes észrevenni, hogy a `square_of_x_special()` függvény újraimplementálja a `square_of_x()` függvényt. Ez most egy egyszerű példa, de ha a `square_of_x()` függvény bonyolult, akkor nem biztos, hogy le akarjuk másolni az egészet egy másik függvény belsejébe, hiszen az kód-duplikálást eredményez, és ha később változtatni kell rajta, akkor már két helyen kell kijavítani ugyanazt. Ez nem az amit mi szeretnénk. Ezért szeretnénk újrahasználni a már létező funkciót. Ezt a példát dekorátor alkalmazásával is meg lehet oldani.

Korábban már láttunk példát arra, hogy egy függvény visszaadott egy másik függvényt eredményként. A dekorátorok alkalmazásakor is ezt a lehetőséget fogjuk használni. Előtte viszont egy kis kitérőként néhány szó az általam beágyazott függvényeknek nevezett konstrukcióról (aminek az eredeti megnevezése _nested functions_).

### Beágyazott függvények (_nested functions_)

Lehetséges függvényeket definiálni függvényeken belül.

```python
def multiply_by_six(x):
    def multiply_by_two(y):
        return y*2
    return multiply_by_two(x)*3

multiply_by_six(7)
multiply_by_six(-8)
```

```
>>> multiply_by_six(7)
42
>>> multiply_by_six(-8)
-48
```

A `multiply_by_two()` függvényt nem lehet a `multiply_by_six()` függvényen kívülről elérni.

```
>>> multiply_by_two(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'multiply_by_two' is not defined
```

A belső függvény viszont hozzáfér az őt tartalmazó függvény szintjén elérhető változókhoz. Az alábbi példában az előbbihez hasonlóan először kettővel, majd hárommal szorzunk, így a végeredmény az eredeti szám hatszorosa lesz. Viszont előtte kiírja a program, hogy mi fog történni. (Ezért egy külön változóban tároljuk el a `multiply_by_two_print()` hívás eredményét (`mul_two`), majd a saját számításunk eredményét is (`result_mul_three`), és utána történik a kiírás. A `multiply_by_two_print()` függvényen belül is hasonlót figyelhetünk meg.)

```python
def multiply_by_six_print(x):
    message = "I multiply {} by {}, result: {}"
    def multiply_by_two_print(y):
        result_mul_two = y*2
        print(message.format(y, 2, result_mul_two))
        return result_mul_two
    mul_two = multiply_by_two_print(x)
    result_mul_three = mul_two*3
    print(message.format(mul_two, 3, result_mul_three))
    return result_mul_three

multiply_by_six_print(7)
multiply_by_six_print(-8)
```

```
>>> multiply_by_six_print(7)
I multiply 7 by 2, result: 14
I multiply 14 by 3, result: 42
42
>>> multiply_by_six_print(-8)
I multiply -8 by 2, result: -16
I multiply -16 by 3, result: -48
-48
```

Függvények utazhatnak paraméterként is, és visszatérési értékként is, ahogy azt már korábban láttuk.

### Dekorátorok használata

Visszatérve a dekorátorokhoz, az alábbi példában a fentebb említett `square_of_x_special()` függvényt valósítom meg a `square_of_x()` függvény és dekorátorok segítségével. Ebben a példában a dekorátor függvény a `square_of_x_special()`, és definiáltam a `square_of_x()` "dekorált" változatát `square_special` néven.

```python
def square_of_x(x):
    return x**2

def square_of_x_special(function):
    def wrapper(x):
        if x > 0:
            return function(x)
        else:
            return -function(x)
    return wrapper

square_special = square_of_x_special(square_of_x)

square_special(2)
square_special(-2)
```

```
>>> square_special(2)
4
>>> square_special(-2)
-4
```

Egy alternatív megoldás a `square_special = square_of_x_special(square_of_x)` sor helyett az alábbi. Ebben az esetben megcseréltem a `square_of_x()` és a `square_of_x_special()` definiálásának sorrendjét.

```python
def square_of_x_special(function):
    def wrapper(x):
        if x > 0:
            return function(x)
        else:
            return -function(x)
    return wrapper

@square_of_x_special
def square_of_x(x):
    return x**2

square_of_x(2)
square_of_x(-2)
```

```
>>> square_of_x(2)
4
>>> square_of_x(-2)
-4
```

## Listák és egyéb összetett adattípusok

## Iterátorok

## Beépített könyvtárak

## Vezérlő utasítások (control flow)

### Elágazások: `if` utasítás

### Ciklusok: `for` utasítás, `range` használata

#### A `break`, `continue` és `else`

Az alábbi példában vegyük észre, hogy az `else` utasítás a `for`ral egy szinten van, és nem az `if`fel van egy szinten. 

```python
def getDivider(n):
    for x in range(2,n):
        if n % x == 0:
            divider = x
            break
    else:
        divider = 0
    return divider

for n in range(2,10):
    divider = getDivider(n)
    if divider != 0:
        print("{} = {} * {}".format(n, divider, int(n/divider)))
    else:
        print("{} is a prime number.".format(n))
```

```
2 is a prime number.
3 is a prime number.
4 = 2 * 2
5 is a prime number.
6 = 2 * 3
7 is a prime number.
8 = 2 * 4
9 = 3 * 3
```

#### A `pass` utasítás

## Objektum-orientáltság

## Referenciák

- [Mutable vs Immutable Objects in Python (megha mohan)](https://medium.com/@meghamohan/mutable-and-immutable-side-of-python-c2145cf72747)
- [Built-in Types - Python documentation](https://docs.python.org/3/library/stdtypes.html)
- [PEP 3137 -- Immutable Bytes and Mutable Buffer](https://www.python.org/dev/peps/pep-3137/)
- [Python - Functions](https://www.tutorialspoint.com/python/python_functions.htm)
- [Python filter()](https://www.programiz.com/python-programming/methods/built-in/filter)
- [Decorators in Python](https://www.datacamp.com/community/tutorials/decorators-python)

<p align="right"><sup><a href="02_base_syntax.md">Előző fejezet</a> | <a href="README.md">Tartalom</a></sup></p>
