from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple, Optional

class Station:
    def __init__(self, idx: str, name: str, line: str):
        self.idx = idx
        self.name = name
        self.line = line
        self.neighbors: List[Tuple["Station", int]] = [] # (Station, time) tuples

        