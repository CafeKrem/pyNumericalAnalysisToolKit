import unittest

from numericalAnalysis.analysor import Analysor


def fct_1(x):
    return x + 1


def fct_2( x):
    return x * 2

class AnalysorTest(unittest.TestCase):
    def test_instanciation(self):
        fct = lambda x: x**2
        input_dict = {fct : {"x" : range(0,10)}}
        analysor = Analysor(input_dict)
        self.assertDictEqual(analysor._functions,input_dict)
        self.assertEqual(["x"],analysor._param_names)

    def test_no_argument_instanciation(self):
        analysor = Analysor()
        self.assertDictEqual(analysor._functions, {})
    def test_add_function(self):
        fct = lambda x: x + 1
        analysor = Analysor()
        analysor.add_function(fct, {"x" : range(1,100)})
        self.assertDictEqual(analysor._functions, {fct : {"x" : range(1,100)}})

    def test_compute_function(self):
        fct = lambda x: x +1
        fct2 = lambda  x: x*2
        fct_dict = {"x" : [1,2,3]}
        analysor = Analysor()
        analysor.add_function(fct,fct_dict)
        analysor.add_function(fct2,fct_dict)
        # action
        analysor.compute()
        self.assertListEqual([fct(x) for x in fct_dict["x"]],list(analysor._result[fct][analysor._target_name]))
        self.assertListEqual([fct2(x) for x in fct_dict["x"]],list(analysor._result[fct2][analysor._target_name]))


    def test_draw_linear_2D_graph(self):
        fct_dict = {"x": [1, 2, 3]}
        analysor = Analysor()
        analysor.add_function(fct_1, fct_dict)
        analysor.add_function(fct_2, fct_dict)
        # action
        analysor.compute()
        analysor.draw_linear_2D_graph()

if __name__ == '__main__':
    unittest.main()
