import readMnist
if __name__ == "__main__":
    data, labels = readMnist.readMnist()
    readMnist.showImage(data[0])
    # currData, currLabels = readMnist.genMnistDigits([0,1],500,data,labels)
    print("e")
