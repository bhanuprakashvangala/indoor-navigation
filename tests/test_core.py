import math
import tempfile
from pathlib import Path
import unittest
from navigation import shortest_path

class RouteTests(unittest.TestCase):
    def test_shortest_path_and_zero_cycle(self):
        graph = {'a': {'b': 0, 'c': 9}, 'b': {'a': 0, 'c': 2}, 'c': {}}
        self.assertEqual(shortest_path(graph, 'a', 'c'), {'distance': 2, 'path': ['a','b','c']})
        self.assertEqual(shortest_path(graph, 'a', 'a')['path'], ['a'])

    def test_invalid_edges_and_unreachable(self):
        for weight in (-1, math.nan, math.inf):
            with self.assertRaises(ValueError):
                shortest_path({'a': {'b': weight}, 'b': {}}, 'a', 'b')
        with self.assertRaisesRegex(ValueError, 'No route'):
            shortest_path({'a': {}, 'b': {}}, 'a', 'b')
