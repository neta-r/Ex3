from unittest import TestCase
from random import seed, randrange, random
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo

class test_GraphAlgo(TestCase):

    def graph_creator(self, num_of_nodes: int, num_of_ed: int):
        seed(1)
        graph = DiGraph()
        i = 0
        while i < num_of_nodes:
            graph.add_node(i)
            i = i + 1
        while graph.e_size() < num_of_ed:
            rnd = randrange(0, num_of_nodes)
            rnd2 = randrange(0, num_of_nodes)
            rnd3 = random()
            graph.add_edge(rnd, rnd2, rnd3 * 100)
        return graph

    def test_shortest_path(self):
        graph = self.graph_creator(10, 20)
        algo_g = GraphAlgo(graph)
        ans = (28.415936669394814, [3, 4])
        # direct path
        self.assertEqual(ans, algo_g.shortest_path(3, 4))
        graph.add_edge(3, 2, 9)
        graph.add_edge(2, 4, 9)
        ans = (18, [3, 2, 4])
        # longer but cheaper path
        self.assertEqual(ans, algo_g.shortest_path(3, 4))
        ans = (0, [])
        self.assertEqual(ans, algo_g.shortest_path(3, 3))
        graph.remove_edge(3, 2)
        graph.remove_edge(2, 4)
        graph.remove_node(8)
        ans = (float('inf'), [])
        # no path
        self.assertEqual(ans, algo_g.shortest_path(1, 7))
        # non existed node
        self.assertEqual(ans, algo_g.shortest_path(81, 7))
        self.assertEqual(ans, algo_g.shortest_path(7, 81))