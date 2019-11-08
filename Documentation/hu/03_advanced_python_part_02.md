![Pythonarium](../../PythonariumLogo.png)

<p align="right"><sup><a href="03_advanced_python_part_01.md">Előző fejezet</a> | <a href="README.md">Tartalom</a></sup></p>

# Haladó Python - Második rész

TODO

## Összetett adattípusok - folytatás

TODO

### `bytes`: bináris szekvenciális típus, byte-okból álló, nem megváltoztatható sorozat

TODO

### `bytearray`: bináris szekvenciális típus, a `bytes` objektum megváltoztatható változata

TODO

### `memoryview`: bináris szekvenciális típus, lehetővé teszi objektumok belső adatának elérését Pythonban

TODO

### `set`: halmaz típus, hash-elhető objektumok nem sorrendezett gyűjteménye. Megváltoztatható, és hash-elhető a `set`.

TODO

### `frozenset`: halmaz típus, a `set` nem megváltoztatható változata

TODO

### `dict`: kulcs-érték párokat tároló szótár típus

A `dict` típussal egy hash-elhető értéket le lehet képezni egy tetszőleges objektumra. Megváltoztatható adatszerkezet.

TODO

## Iterátorok és generátorok

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

## Referenciák

- [Mutable vs Immutable Objects in Python (megha mohan)](https://medium.com/@meghamohan/mutable-and-immutable-side-of-python-c2145cf72747)
- [Built-in Types - Python documentation](https://docs.python.org/3/library/stdtypes.html)
- [PEP 3137 -- Immutable Bytes and Mutable Buffer](https://www.python.org/dev/peps/pep-3137/)
- [Python - Functions](https://www.tutorialspoint.com/python/python_functions.htm)
- [Python filter()](https://www.programiz.com/python-programming/methods/built-in/filter)
- [Decorators in Python](https://www.datacamp.com/community/tutorials/decorators-python)

<p align="right"><sup><a href="03_advanced_python_part_01.md">Előző fejezet</a> | <a href="README.md">Tartalom</a></sup></p>
