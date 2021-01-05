from unittest import TestCase
from random import seed, randrange, random
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
from Node import Node


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

    def test_save_and_load(self):
        graph = self.graph_creator(10, 20)
        algo_g = GraphAlgo(graph)
        algo_g.save_to_json("testing.txt")
        algo_g2 = GraphAlgo()
        algo_g2.load_from_json("testing.txt")
        self.assertEqual(algo_g.graph, algo_g2.graph)
        algo_g.graph.remove_node(5)
        self.assertNotEqual(algo_g.graph, algo_g2.graph)

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

    def test_connected_component(self):
        graph = self.graph_creator(10, 20)
        algo_g = GraphAlgo(None)
        ans = []
        self.assertEqual(ans, algo_g.connected_component(89))
        algo_g = GraphAlgo(graph)
        # non exiting node
        self.assertEqual(ans, algo_g.connected_component(89))
        ans = [2]
        self.assertEqual(ans, algo_g.connected_component(2))
        ans = [6, 8, 7, 0]
        self.assertEqual(ans, algo_g.connected_component(6))
        ans = [9]
        self.assertEqual(ans, algo_g.connected_component(9))
        graph.add_edge(3, 6, 7)
        ans = [3, 6, 8, 7, 0]
        self.assertEqual(ans, algo_g.connected_component(3))

    def test_connected_components(self):
        graph = self.graph_creator(10, 20)
        algo_g = GraphAlgo(None)
        ans = []
        self.assertEqual(ans, algo_g.connected_components())
        algo_g = GraphAlgo(graph)
        ans = [[9], [2], [1, 4], [3], [6, 8, 7, 0], [5]]
        self.assertEqual(ans, algo_g.connected_components())
        graph.add_edge(3, 6, 7)
        ans = [[9], [2], [1, 4], [3, 6, 8, 7, 0], [5]]
        self.assertEqual(ans, algo_g.connected_components())
        graph.add_edge(9, 2, 7)
        ans = [[9, 2], [1, 4], [3, 6, 8, 7, 0], [5]]
        self.assertEqual(ans, algo_g.connected_components())
        graph.add_edge(2, 1, 7)
        ans = [[9, 2, 1, 4], [3, 6, 8, 7, 0], [5]]
        self.assertEqual(ans, algo_g.connected_components())
        graph.add_edge(1, 5, 7)
        ans = [[8, 6, 3, 5, 9, 2, 1, 4, 7, 0]]
        self.assertEqual(ans, algo_g.connected_components())

    def test_plot_graph(self):
        # graph = self.graph_creator(10, 20)
        # Node.set_pos(graph.nodes.get(2), 2, 5)
        # Node.set_pos(graph.nodes.get(8), 8, 7.41)
        # Node.set_pos(graph.nodes.get(1), 10, 10)

        algo_g = GraphAlgo()
        algo_g.load_from_json("../data/A2")
        algo_g.plot_graph()
