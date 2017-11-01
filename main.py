from collections import Counter
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time

#https://pythonprogramming.net/testing-visualization-and-conclusion/?completed=/basic-image-recognition-testing/


# Average the pixels of the given array - if any pixels brighter than avg, make it plain white otherwise, plain black.
def threshold(imageArray) :
    balanceAr = []
    newAr = imageArray
    from statistics import mean
    for eachRow in imageArray:
        for eachPix in eachRow:
            # 0 - 3 b.c we want to ignore the alpha field
            avgNum = mean(eachPix[:3])
            balanceAr.append(avgNum)

    balance = mean(balanceAr)
    if len(imageArray[0][0]) == 4:
        for eachRow in newAr:
            for eachPix in eachRow:
                if mean(eachPix[:3]) > balance:
                    eachPix[0] = 255
                    eachPix[1] = 255
                    eachPix[2] = 255
                    eachPix[3] = 255
                else:
                    eachPix[0] = 0
                    eachPix[1] = 0
                    eachPix[2] = 0
                    eachPix[3] = 255
    else :
        for eachRow in newAr:
            for eachPix in eachRow:
                if mean(eachPix[:3]) > balance:
                    eachPix[0] = 255
                    eachPix[1] = 255
                    eachPix[2] = 255
                else:
                    eachPix[0] = 0
                    eachPix[1] = 0
                    eachPix[2] = 0
    return newAr

# example of using the threshold method
def normalize(file):
    i = Image.open(file)
    iar = np.array(i)

    #print(len(iar))
    iar = threshold(iar)

    # fig = plt.figure()
    # ax1 = plt.subplot2grid((8,6),(0,0), rowspan=4, colspan=3)
    # ax2 = plt.subplot2grid((8,6),(4,0), rowspan=4, colspan=3)

    plt.imshow(iar)
    # ax1.imshow(iar1)
    # ax2.imshow(iar2)

    plt.show()

# create a flat file database to refer to for the detect function
def createExamples():
    numberArrayExamples = open('numArEx.txt','a')
    numbersWeHave = range(1,10)
    for eachNum in numbersWeHave:
        #print eachNum
        for furtherNum in numbersWeHave:
            # you could also literally add it *.1 and have it create
            # an actual float, but, since in the end we are going
            # to use it as a string, this way will work.
            print(str(eachNum)+'.'+str(furtherNum))
            imgFilePath = 'images/numbers/'+str(eachNum)+'.'+str(furtherNum)+'.png'
            ei = Image.open(imgFilePath)
            eiar = np.array(ei)
            eiarl = str(eiar.tolist())

            print(eiarl)
            lineToWrite = str(eachNum)+'::'+eiarl+'\n'
            numberArrayExamples.write(lineToWrite)


def detect(filePath):
    matchedAr = []
    loadExamps = open('numArEx.txt', 'r').read()
    loadExamps = loadExamps.split('\n')

    i = Image.open(filePath)
    iar = np.array(i)
    iarl = iar.tolist()

    inQuestion = str(iarl)

    for eachExample in loadExamps:
        try:
            splitEx = eachExample.split('::')
            currentNum = splitEx[0]
            currentAr = splitEx[1]

            eachPixEx = currentAr.split('],')
            eachPixInQ = inQuestion.split('],')

            x = 0

            while x < len(eachPixEx):
                if eachPixEx[x] == eachPixInQ[x]:
                    matchedAr.append(int(currentNum))

                x += 1
        except Exception as e:
            print(str(e))

    print(matchedAr)
    x = Counter(matchedAr)
    print(x)
    graphX = []
    graphY = []

    ylimi = 0

    for eachThing in x:
        graphX.append(eachThing)
        graphY.append(x[eachThing])
        ylimi = x[eachThing]

    fig = plt.figure()
    ax1 = plt.subplot2grid((4, 4), (0, 0), rowspan=1, colspan=4)
    ax2 = plt.subplot2grid((4, 4), (1, 0), rowspan=3, colspan=4)

    ax1.imshow(iar)
    ax2.bar(graphX, graphY, align='center')
    plt.ylim(400)

    xloc = plt.MaxNLocator(12)
    ax2.xaxis.set_major_locator(xloc)

    plt.show()


normalize('data/2.1.jpg')

