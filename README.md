# Algorithm for generating simple quasigroups on given ones

## Summary

Implementation of an algorithm for obtaining a simple quasigroup from a given quasigroup.

## Usage of [quasigroup.py](quasigroup.py)

The algorithm is contained in the file [quasigroup.py](quasigroup.py). Dry run of this file will show an example on quasigroup from file [ex_2.txt](ex_2.txt) with printing of intermediate steps.

### Initialization

The quasigroup is stored in the structure Quasigroup, which can be initialized with

* **size** - size of quasigroup. Not necessary if the quasigroup is specified from a file
* **file** - file name. If not specified, will generate $\mathbb{Z}_n$
* **from_1** - kind of quasigroup. Required if the quasigroup is specified from a file. Default: *true*
* **mark** - mark for quasigroup. The mark which will be printed. Default: *Q*

### Methods

The following main methods can be applied to the structure

* `Quasigroup.create_simple`. Return the simple quasigroup by the algorithm.
* `Quasigroup.all_in_one`. Also return simple quasigroup. Slightly optimized version
* `__str__(Quasigroup)`. Representation of a group in the form of a multiplication table. With mark `Quasigroup.mark`.
* `Quasigroup.random_alteration`. Random shuffling of rows and columns, rearranging elements.
* `Quasigroup.export`. Write quasigroup in file, given as **file_name** as argument

## Usage of [main.py](main.py)

This part was mainly written in the needs of paper on quasigroups. Therefore, it may be a little useless for a direct launch. But it can be used as an example :)

The sqlite database is used to store the results. `matplotlib` is used for plotting.
