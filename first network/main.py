import numpy as np

def f(x):
    return 1 if x > 0.5 else 0

def go(params):
    W1 = [0, 0.2, 0.2]
    W2 = [1, 0.2,-0.6]

    weight1 = np.array([W1,W2])
    weight2 = np.array([-1, 1])

    sum = np.dot(weight1, params)
    res = np.array([f(x) for x in sum])

    sum2 = np.dot(weight2, res)
    res2 = f(sum2)
    return res2

print(f"Result of NeuralNet: {go([0,0,0])}")