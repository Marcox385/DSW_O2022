# IS727272 - Iterator
# Sesión 23 - 11.11.22
from collections.abc import Iterable, Iterator
from enum import Enum

class IteradorConcreto(Iterator):
    class Tipo(Enum):
        KEY_0 = 0