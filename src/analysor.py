from itertools import product

from pandas import DataFrame


class Analysor:

    def __init__(self,functions_dictionary=None,target_name="target"):
        if functions_dictionary is None:
            self._functions = {}
        else:
            self._functions = functions_dictionary
        self._result = { fct : None for fct in self._functions.keys()}
        self._target_name = target_name


    def add_function(self, function, parameters_range: dict):
        self._functions[function] = parameters_range

    def _param_product(self,d):
            return (dict(zip(d.keys(), values)) for values in product(*d.values()))
    def compute(self):
        for fct,parameters_range in self._functions.items():
            contents = []
            for d in self._param_product(parameters_range):
                res = fct(**d)
                line = {**d,self._target_name: res}
                contents.append(line)
            self._result[fct] = DataFrame(contents)

