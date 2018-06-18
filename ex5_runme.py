import readMnist
import numpy as np
import GradientDescentMethods

if __name__ == "__main__":

    a = np.random.rand(5,5)
    print()


    data, labels = readMnist.readMnist()
    readMnist.showImage(data[0])
    currData, currLabels = readMnist.genMnistDigits([0,1],500,data,labels)

    # replace 0 with -1
    currLabels [currLabels == 0] = -1
    # add column of 1
    ones_col = np.repeat(1, len(currData))
    # currLabels = np.hstack((currLabels, ones_col))

    # SGD with batches of 5, 50, 150
    GradientDescentMethods.SGD(currData,currLabels,150,1,5)
    GradientDescentMethods.SGD(currData,currLabels,150,1,50)
    GradientDescentMethods.SGD(currData,currLabels,150,1,150)

    # GD algorithm with 150 iterations
    GradientDescentMethods.GD(currData,currLabels,150,1,150)



    print("e")
