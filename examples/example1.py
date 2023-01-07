from NumericalAnalysis.analysor import Analysor


def scoring_function_multiplication(a,b):
    return  a * b

def score_function_addition(a,b):
    return a + b

if __name__ == "__main__":
    analysor = Analysor()
    params_dict = {"a" : [i/100 for i in range(0,100 +1)],# define range value for your parameter a
                   "b" : range(-20,20,3) # range value for parameter b
                   }
    analysor.add_function(scoring_function_multiplication,params_dict)
    analysor.add_function(score_function_addition,params_dict)
    analysor.compute()# it will compute product of every possible value for a and b gived before
    analysor.draw_linear_2D_graph() # it will draw and save fig in "./graph" directory

