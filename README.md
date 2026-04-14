# TrollSorts

A Python library containing troll sorting algorithms.

## Installation

```bash
pip install .
```

## Algorithms

- **Communist Sort**: Wealth redistributed equally
- **Capitalist Sort**: All wealth to the top 1%
- **Island Sort**: Strictly less than 18
- **Six-Seven Sort**: Just 6-7

## Usage

```python
from troll_sorts import communist_sort, capitalist_sort, island_sort, six_seven_sort

arr = [10, 25, 4, 30, 15, 8]

print(communist_sort(arr)) # [15, 15, 15, 15, 15, 15]
```
