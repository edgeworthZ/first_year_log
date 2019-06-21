#Name: Nutawut Naprom
#Lang: Python

MAP_PATH = 'Map'

import csv

def GetPopulation(csvList, areaDict, rowStart, rowEnd, colStart, colEnd):
    sumPop = 0
    sumArea = 0
    for i in range(rowStart, rowEnd):
        for j in range(colStart, colEnd):
            if(len(csvList[i][j]) > 0):
                sumPop += int(csvList[i][j])*10000
                sumArea += 10
    areaDict['sumPop'] += sumPop
    areaDict['sumArea'] += sumArea
    return areaDict

def GetNorth(csvList):
    areaDict = {'sumPop':0,'sumArea':0}
    areaDict = GetPopulation(csvList, areaDict, 0, 11, 0, 13)
    areaDict = GetPopulation(csvList, areaDict, 11, 17, 0, 5)
    return areaDict

def GetCentral(csvList):
    areaDict = {'sumPop':0,'sumArea':0}
    areaDict = GetPopulation(csvList, areaDict, 11, 17, 5, 13)
    areaDict = GetPopulation(csvList, areaDict, 17, 33, 0, 13)
    return areaDict

def GetEast(csvList):
    areaDict = {'sumPop':0,'sumArea':0}
    areaDict = GetPopulation(csvList, areaDict, 5, 31, 13, len(csvList[0]))
    return areaDict

def GetSouth(csvList):
    areaDict = {'sumPop':0,'sumArea':0}
    areaDict = GetPopulation(csvList, areaDict, 33, len(csvList), 0, len(csvList[0]))
    return areaDict

with open(MAP_PATH+'/thailand_cencus.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csvList = list(csv_reader)
    countryDict = {}
    countryDict['North'] = GetNorth(csvList)
    countryDict['Central'] = GetCentral(csvList)
    countryDict['East'] = GetEast(csvList)
    countryDict['South'] = GetSouth(csvList)
    print(countryDict)
    sumDict = {}
    for key, val in countryDict.items():
        sumDict[key] = val['sumPop']
    maxArea = max(sumDict, key=sumDict.get)
    maxAreaDensity = countryDict[maxArea]['sumPop']/countryDict[maxArea]['sumArea']
    print(f'{maxArea} is the area with the most population, with the density of {maxAreaDensity:.2f} citizen/square kilometre.')
    
