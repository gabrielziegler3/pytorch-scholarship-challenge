import numpy as np

def perceptron(x1, x2):
    weight1 = np.float64(3)
    weight2 = np.float64(4)
    bias = np.float64(-10)
    learning_rate = np.float64(0.1)
    i = 0

    while True:
        result = weight1 * x1 + weight2 * x2 + bias
        result = round(result, 1)
        weight1 = round(weight1, 1)
        weight2 = round(weight2, 1)
        bias = round(bias, 1)
        print("{} * x1 + {} * x2 {} = 0".format(weight1, weight2, bias))
        print("result", result)

        if result >= 0.0:
            print("Done with {} iterations".format(i))
            break

        weight1 += learning_rate
        weight2 += learning_rate
        bias += learning_rate
        i += 1

if __name__ == '__main__':
    perceptron(1, 1)
