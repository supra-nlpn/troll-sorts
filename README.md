# TrollSorts

[![PyPI version](https://badge.fury.io/py/troll-sorts.svg)](https://badge.fury.io/py/troll-sorts)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

A Python library containing innovative (and highly unconventional) sorting algorithms designed to challenge traditional paradigms of data organization.

---

## Table of Contents

- [Installation](#installation)
- [Algorithms](#algorithms)
- [Usage](#usage)
- [Command Line Interface](#command-line-interface)
- [License](#license)

---

## Installation

You can install `troll-sorts` directly via pip:

```bash
pip install troll-sorts
```

*For local engineering and development:*

```bash
pip install .
```

---

## Algorithms

Our suite currently includes four distinct sorting paradigms:

- **Communist Sort**: Wealth redistributed equally
- **Capitalist Sort**: All wealth to the top 1%
- **Island Sort**: Strictly less than 18
- **Six-Seven Sort**: Just 6-7

---

## Usage

Integrating `troll-sorts` into your workflow is straightforward.

```python
from troll_sorts import communist_sort, capitalist_sort, island_sort, six_seven_sort

# Sample unorganized data representing arbitrary values
arr = [10, 25, 4, 30, 15, 8]

# Apply the Communist Sort paradigm
print("Communist:", communist_sort(arr))
# Output: [15, 15, 15, 15, 15, 15]

# Apply the Capitalist Sort paradigm
print("Capitalist:", capitalist_sort(arr))
# Output: [0, 0, 0, 92, 0, 0]

# Apply the Island Sort paradigm
print("Island:", island_sort(arr))
# Output: [4, 8, 10, 15]

# Apply the Six-Seven Sort paradigm
print("Six-Seven:", six_seven_sort(arr))
# Output: [6, 7, 6, 7, 6, 7]
```

## Command Line Interface

The package also includes an executable module providing a terminal welcome animation.

```bash
trollsorts
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

