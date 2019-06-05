![Pythonarium](../../PythonariumLogo.png)

<p align="right"><sup><a href="02_base_syntax.md">Előző fejezet</a> | <a href="README.md">Tartalom</a></sup></p>

# Haladó Python

Ebben a részben az összetett adatokkal való műveletekről lesz szó, továbbá megismerjük a Python vezérlő utasításait.

## Adattípusok

A Python 3-ban a következő adattípusokat használhatjuk:
- logikai típus: `bool`: igaz/hamis értékkel (`True`/`False`)
- numerikus típusok
  - `int`: egész szám
  - `float`: lebegőpontos szám
  - `complex`: komplex szám
- `iterator`: iterátor típus; `generator`: generátor típus
- szekvenciális típusok: 
  - `list`: lista (vagy tömb)
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

Egy objektum hash-elhető, ha van egy hash értéke, ami nem változik meg az objektum élettartama során, és összehasonlításra lehet használni.

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

Kimenet: 

```
5
14
28
60
```

## Paraméterek, paraméter-átadás függvényeknek

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

## Dekorátorok

## Listák és egyéb összetett adattípusok

## Iterátorok

## Beépített könyvtárak

## Vezérlő utasítások (control flow)

## Objektum-orientáltság

## Referenciák

<p align="right"><sup><a href="02_base_syntax.md">Előző fejezet</a> | <a href="README.md">Tartalom</a></sup></p>
