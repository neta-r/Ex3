from random import seed
from random import random
from unittest import TestCase
from DiGraph import DiGraph
from random import randrange


class TestDiGraph(TestCase):

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

    def test_add_edge(self):
        graph = self.graph_creator(10, 20)
        # connect existing nodes with no edges between them
        graph.add_edge(9, 0, 60)
        self.assertEqual(graph.e_size(), 21)
        graph.add_edge(1, 3, 60)
        self.assertEqual(graph.e_size(), 22)
        graph.add_edge(3, 5, 60)
        self.assertEqual(graph.e_size(), 23)
        # connect existing nodes with exiting edge between them
        graph.add_edge(1, 2, 60)
        self.assertEqual(graph.e_size(), 23)
        graph.add_edge(3, 4, 60)
        self.assertEqual(graph.e_size(), 23)
        graph.add_edge(5, 1, 60)
        self.assertEqual(graph.e_size(), 23)
        # connect non existing nodes
        graph.add_edge(90, 1, 60)
        self.assertEqual(graph.e_size(), 23)
        graph.add_edge(5, 56, 60)
        self.assertEqual(graph.e_size(), 23)
        graph.add_edge(-5, 115, 60)
        self.assertEqual(graph.e_size(), 23)
        # connect a node to itself
        graph.add_edge(5, 5, 60)
        self.assertEqual(graph.e_size(), 23)
        graph.add_edge(9, 9, 60)
        self.assertEqual(graph.e_size(), 23)

    def test_add_node(self):
        graph = self.graph_creator(10, 20)
        # adding existing nodes
        graph.add_node(5)
        self.assertEqual(graph.v_size(), 10)
        graph.add_node(6)
        self.assertEqual(graph.v_size(), 10)
        graph.add_node(9)
        self.assertEqual(graph.v_size(), 10)
        # adding non existing nodes
        graph.add_node(59)
        self.assertEqual(graph.v_size(), 11)
        graph.add_node(20)
        self.assertEqual(graph.v_size(), 12)
        graph.add_node(-5)
        self.assertEqual(graph.v_size(), 13)

    def test_remove_node(self):
        graph = self.graph_creator(10, 20)
        # remove existing node
        self.assertTrue(graph.remove_node(3))
        self.assertEqual(graph.v_size(), 9)
        self.assertEqual(graph.e_size(), 15)
        self.assertFalse(3 in graph.nodes.keys())
        self.assertTrue(graph.remove_node(1))
        self.assertEqual(graph.v_size(), 8)
        self.assertEqual(graph.e_size(), 10)
        self.assertFalse(1 in graph.nodes.keys())
        # remove non exiting node
        self.assertFalse(graph.remove_node(3))
        self.assertEqual(graph.v_size(), 8)
        self.assertEqual(graph.e_size(), 10)
        self.assertFalse(graph.remove_node(59))
        self.assertEqual(graph.v_size(), 8)
        self.assertEqual(graph.e_size(), 10)

    def test_remove_edge(self):
        graph = self.graph_creator(10, 20)
        # remove an existing edge
        graph.remove_edge(5, 1)
        self.assertEqual(graph.v_size(), 10)
        self.assertEqual(graph.e_size(), 19)
        self.assertFalse(graph.get_node(5).get_ni().__contains__(9))
        self.assertFalse(graph.get_node(9).get_c_tome().__contains__(5))
        graph.remove_edge(7, 8)
        self.assertEqual(graph.v_size(), 10)
        self.assertEqual(graph.e_size(), 18)
        self.assertFalse(graph.get_node(7).get_ni().__contains__(8))
        self.assertFalse(graph.get_node(8).get_c_tome().__contains__(7))
        # remove a non existing edge
        graph.remove_edge(7, 8)
        self.assertFalse(graph.get_node(7).get_ni().__contains__(8))
        self.assertFalse(graph.get_node(8).get_c_tome().__contains__(7))
        # remove a non existing edge from a non existing node
        graph.remove_edge(59, 8)
        self.assertFalse(graph.get_node(7).get_ni().__contains__(8))
        self.assertFalse(graph.get_node(8).get_c_tome().__contains__(7))

    def test_get_node(self):
        graph = self.graph_creator(10, 20)
        # getting existing nodes
        self.assertIsNotNone(graph.get_node(5))
        self.assertIsNotNone(graph.get_node(8))
        self.assertIsNotNone(graph.get_node(0))
        # trying to getting non existing nodes
        try:
            graph.get_node(59)
            # we shouldn't get to the line below
            self.fail()
        except:
            print("you passed the test")
        graph.remove_node(8)
        try:
            graph.get_node(8)
            # we shouldn't get to the line below
            self.fail()
        except:
            print("you passed the test")

    def test_get_all_v(self):
        graph = self.graph_creator(10, 20)
        n = []
        for nd in graph.nodes.values():
            n.append(nd)
        for nd in n:
            self.assertIn(nd, graph.get_all_v().values())
        nd2 = graph.get_node(5)
        graph.remove_node(5)
        self.assertNotIn(nd2, graph.get_all_v().values())


    def test_all_in_edges_of_node(self): #להשלים
        graph = self.graph_creator(5, 6)
        g = DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_edge(1, 0, 4)
        g.add_edge(0, 2, 4)
        g.add_edge(0, 3, 4)
        g.add_edge(4, 0, 4)
        g.add_edge(2, 0, 4)
        g.add_edge(1, 4, 4)
        for i in range(5):
            f = graph.all_in_edges_of_node(i).keys()
            p = g.all_in_edges_of_node(i).keys()
            for k in f:
                self.assertIn(k, p)

    def test_all_out_edges_of_node(self):
        graph = self.graph_creator(5, 6)
        g = DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_edge(1, 0, 4)
        g.add_edge(0, 2, 4)
        g.add_edge(0, 3, 4)
        g.add_edge(4, 0, 4)
        g.add_edge(2, 0, 4)
        g.add_edge(1, 4, 4)
        for i in range(5):
            f = graph.all_out_edges_of_node(i).keys()
            p = g.all_out_edges_of_node(i).keys()
            for k in f:
                self.assertIn(k, p)

    def test_v_size(self):
        graph = self.graph_creator(10, 20)
        num = graph.v_size()
        self.assertEqual(10, graph.v_size())
        graph.remove_node(8)
        num = num-1
        self.assertEqual(num, graph.v_size())
        graph.remove_node(5614) # doesn't exist
        self.assertEqual(num, graph.v_size())
        graph.remove_node(8) # should not exist
        self.assertEqual(num, graph.v_size())

    def test_e_size(self):
        graph = self.graph_creator(10, 20)
        num = graph.e_size()
        self.assertEqual(20, graph.e_size())
        graph.remove_node(8)
        num = num-7
        self.assertEqual(num, graph.e_size())
        graph.remove_node(5614)  # doesn't exist
        self.assertEqual(num, graph.e_size())
        graph.remove_node(8)  # should not exist
        self.assertEqual(num, graph.e_size())

    def test_get_mc(self):
        graph = self.graph_creator(10, 20)
        num = graph.get_mc()
        graph.remove_edge(7, 8)
        num = num+1
        self.assertEqual(num, graph.get_mc())
        graph.remove_node(5)
        num = num+5
        self.assertEqual(num, graph.get_mc())
        graph.remove_node(5)
        self.assertEqual(num, graph.get_mc())
        graph.add_node(8915)
        num = num + 1
        self.assertEqual(num, graph.get_mc())
        graph.add_node(8915)
        self.assertEqual(num, graph.get_mc())

