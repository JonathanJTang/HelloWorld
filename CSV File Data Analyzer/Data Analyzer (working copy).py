import csv
import math
import turtle
import time
#import copy

class SurveyEntry:
    courseDictKeyStr = ["WhyChoseCourse", "LikeMath", "LikeCourse", "CourseDifficulty", "WhenStudy", "LengthStudy", "TimeSpent", "Grade"]
    
    def __init__(self,entryID):
        self.ID = entryID  #An unique int to match this survey entry to the excel file
        #self.name = None  #Will be string
        self.currentGrade = None  #Will be int
        self.birthYear = None  #Will be int
        self.gender = None  #Will be a char: M or F

        self.incentiveChoice = None  #Will be string
        self.hardestThingAboutMath = None  #Will be string

        self.parentsExpectWellMath = None  #Will be one of four ints: 1 to 4
        self.parentsThinkMathImportant = None  #Will be one of four ints: 1 to 4
        self.friendsLikeMath = None  #Will be one of four ints: 1 to 4
        self.friendsDoWellMath = None  #Will be one of four ints: 1 to 4
        self.iLookForwardMathClass = None  #Will be one of four ints: 1 to 4
        self.iAnxiousMath = None  #Will be one of four ints: 1 to 4
        self.iWorryMathMark = None  #Will be one of four ints: 1 to 4

        '''In each (enabled) course's data dictionary, there will be:
        grX???WhyChoseCourse   #An int from 1 to 5, or string (representing 'other')
        grX???LikeMath   #An int from 1 to 10
        grX???LikeCourse   #An int from 1 to 10
        grX???CourseDifficulty   #An int from 1 to 10
        grX???WhenStudy   #An int from 1 to 4, or string (represent 'other')
        grX???LengthStudy   #An int from 1 to 6
        grX???TimeSpent   #An int from 1 to 6
        grX???Grade   #An int from 1 to 6'''

        self.gr9MPMData = None
        self.gr10MPMData = None
        self.gr11MCRData = None
        self.gr12MHFData = None
        self.gr12MDMData = None
        
        # Debug
        #print(self.__dict__)

    def __str__(self):
        separator = "| "  #could be changed to '\n'
        basicInfoStr = "ID{0}: {1},{2},{3}; {4} {5} {6} {7} {8} {9} {10}".format(self.ID,self.currentGrade,self.birthYear,self.gender, \
                                        self.parentsExpectWellMath, self.parentsThinkMathImportant, self.friendsLikeMath, \
                                        self.friendsDoWellMath, self.iLookForwardMathClass, self.iAnxiousMath, self.iWorryMathMark)
        if self.gr9MPMData != None:
            gr9MPMStr = "{0}, {1} {2} {3}, {4} {5} {6}, {7}".format(self.gr9MPMData[courseDictKeyStr[0]], self.gr9MPMData[courseDictKeyStr[1]], \
                                                                 self.gr9MPMData[courseDictKeyStr[2]], self.gr9MPMData[courseDictKeyStr[3]], \
                                                                 self.gr9MPMData[courseDictKeyStr[4]], self.gr9MPMData[courseDictKeyStr[5]], \
                                                                 self.gr9MPMData[courseDictKeyStr[6]], self.gr9MPMData[courseDictKeyStr[7]])
        else:
            gr9MPMStr = "No Grade 9 MPM Info"
            
        if self.gr10MPMData != None:
            gr10MPMStr = "{0}, {1} {2} {3}, {4} {5} {6}, {7}".format(self.gr10MPMData[courseDictKeyStr[0]], self.gr10MPMData[courseDictKeyStr[1]], \
                                                                 self.gr10MPMData[courseDictKeyStr[2]], self.gr10MPMData[courseDictKeyStr[3]], \
                                                                 self.gr10MPMData[courseDictKeyStr[4]], self.gr10MPMData[courseDictKeyStr[5]], \
                                                                 self.gr10MPMData[courseDictKeyStr[6]], self.gr10MPMData[courseDictKeyStr[7]])
        else:
            gr10MPMStr = "No Grade 10 MPM Info"
            
        if self.gr11MCRData != None:
            gr11MCRStr = "{0}, {1} {2} {3}, {4} {5} {6}, {7}".format(self.gr11MCRData[courseDictKeyStr[0]], self.gr11MCRData[courseDictKeyStr[1]], \
                                                                 self.gr11MCRData[courseDictKeyStr[2]], self.gr11MCRData[courseDictKeyStr[3]], \
                                                                 self.gr11MCRData[courseDictKeyStr[4]], self.gr11MCRData[courseDictKeyStr[5]], \
                                                                 self.gr11MCRData[courseDictKeyStr[6]], self.gr11MCRData[courseDictKeyStr[7]])
        else:
            gr11MCRStr = "No Grade 11 MCR Info"
            
        if self.gr12MHFData != None:
            gr12MHFStr = "{0}, {1} {2} {3}, {4} {5} {6}, {7}".format(self.gr12MHFData[courseDictKeyStr[0]], self.gr12MHFData[courseDictKeyStr[1]], \
                                                                 self.gr12MHFData[courseDictKeyStr[2]], self.gr12MHFData[courseDictKeyStr[3]], \
                                                                 self.gr12MHFData[courseDictKeyStr[4]], self.gr12MHFData[courseDictKeyStr[5]], \
                                                                 self.gr12MHFData[courseDictKeyStr[6]], self.gr12MHFData[courseDictKeyStr[7]])
        else:
            gr12MHFStr = "No Grade 12 MHF Info"
            
        if self.gr12MDMData != None:
            gr12MDMStr = "{0}, {1} {2} {3}, {4} {5} {6}, {7}".format(self.gr12MDMData[courseDictKeyStr[0]], self.gr12MDMData[courseDictKeyStr[1]], \
                                                                 self.gr12MDMData[courseDictKeyStr[2]], self.gr12MDMData[courseDictKeyStr[3]], \
                                                                 self.gr12MDMData[courseDictKeyStr[4]], self.gr12MDMData[courseDictKeyStr[5]], \
                                                                 self.gr12MDMData[courseDictKeyStr[6]], self.gr12MDMData[courseDictKeyStr[7]])
        else:
            gr12MDMStr = "No Grade 12 MDM Info"
        extraInfoStr = "chose {0}, thought hardest was {1}".format(self.incentiveChoice,self.hardestThingAboutMath)
        return basicInfoStr + separator + gr9MPMStr + separator + gr10MPMStr + separator + gr11MCRStr \
               + separator + gr12MHFStr + separator + gr12MDMStr + separator + extraInfoStr

    def valueOf(self,columnNameStr):
        """A 'resolver': returns the desired instance attribute"""
        pass



class DataAnalyzer:
    courseDictKeyStrs = ["WhyChoseCourse", "LikeMath", "LikeCourse", "CourseDifficulty", "WhenStudy", "LengthStudy", "TimeSpent", "Grade"]
    surveyEntryAttributeColumnIndexDict = {"ID":0, "currentGrade":1, "birthYear":2, "gender":3, "parentsExpectWellMath":4, "parentsThinkMathImportant":5, \
                                     "friendsLikeMath":6, "friendsDoWellMath":7, "iLookForwardMathClass":8, "iAnxiousMath":9, "iWorryMathMark":10, \
                                     "gr9MPMWhyChoseCourse":11, "gr9MPMLikeMath":12, "gr9MPMLikeCourse":13, "gr9MPMCourseDifficulty":14, \
                                     "gr9MPMWhenStudy":15, "gr9MPMLengthStudy":16,  "gr9MPMTimeSpent":17, "gr9MPMGrade":18, \
                                     "gr10MPMWhyChoseCourse":19, "gr10MPMLikeMath":20, "gr10MPMLikeCourse":21, "gr10MPMCourseDifficulty":22, \
                                     "gr10MPMWhenStudy":23, "gr10MPMLengthStudy":24,  "gr10MPMTimeSpent":25, "gr10MPMGrade":26, \
                                     "gr11MCRWhyChoseCourse":27, "gr11MCRLikeMath":28, "gr11MCRLikeCourse":29, "gr11MCRCourseDifficulty":30, \
                                     "gr11MCRWhenStudy":31, "gr11MCRLengthStudy":32,  "gr11MCRTimeSpent":33, "gr11MCRGrade":34, \
                                     "gr12MHFWhyChoseCourse":35, "gr12MHFLikeMath":36, "gr12MHFLikeCourse":37, "gr12MHFCourseDifficulty":38, \
                                     "gr12MHFWhenStudy":39, "gr12MHFLengthStudy":40,  "gr12MHFTimeSpent":41, "gr12MHFGrade":42, \
                                     "gr12MHFWhyChoseCourse":43, "gr12MHFLikeMath":44, "gr12MHFLikeCourse":45, "gr12MHFCourseDifficulty":46, \
                                     "gr12MHFWhenStudy":47, "gr12MHFLengthStudy":48,  "gr12MHFTimeSpent":49, "gr12MHFGrade":50, 
                                     "incentiveChoice":51, "hardestThingAboutMath":52}
    
    
    def __init__(self, surveyEntriesList, turtleScreenObj, turtleTurtleObj):
        self.data = []
        self.readDataFromSurveyEntriesList(surveyEntriesList)
        #self.numEntries = len(self.data)
        #Set up screen object and turtle object used for displaying graphs
        self.wn = turtleScreenObj
        self.wn.setworldcoordinates(-50,-50,self.wn.window_width()-50,self.wn.window_height()-50)
        self.turtle = turtleTurtleObj
        self.turtle.shape("circle")
        self.turtle.shapesize(0.5)
        self.turtle.speed(0)
        self.turtle.penup()
        self.turtle.hideturtle()
        
    def readDataFromSurveyEntriesList(self, surveyEntriesList):
        for surveyEntry in surveyEntriesList:
            row = []
            row.append(surveyEntry.ID)
            row.append(surveyEntry.currentGrade)
            row.append(surveyEntry.birthYear)
            row.append(surveyEntry.gender)
    
            row.append(surveyEntry.parentsExpectWellMath)  #Will be one of four ints: 1 to 4
            row.append(surveyEntry.parentsThinkMathImportant)  #Will be one of four ints: 1 to 4
            row.append(surveyEntry.friendsLikeMath)  #Will be one of four ints: 1 to 4
            row.append(surveyEntry.friendsDoWellMath)  #Will be one of four ints: 1 to 4
            row.append(surveyEntry.iLookForwardMathClass)  #Will be one of four ints: 1 to 4
            row.append(surveyEntry.iAnxiousMath)  #Will be one of four ints: 1 to 4
            row.append(surveyEntry.iWorryMathMark)  #Will be one of four ints: 1 to 4
            
            for courseName in ["9MPM", "10MPM", "11MCR", "12MHF", "12MDM"]:
                keyName = "gr" + courseName + "Data"
                if surveyEntry.__dict__[keyName] == None:
                    for i in range(8):  #Append None 8 times, since there's no data for this course
                        row.append(None)
                else:
                    for courseDictKeyStr in self.courseDictKeyStrs:
                        row.append(surveyEntry.__dict__[keyName][courseDictKeyStr])
            
            row.append(surveyEntry.incentiveChoice)  #Will be string
            row.append(surveyEntry.hardestThingAboutMath)  #Will be string
            
            self.data.append(row)
        
        for line in self.data:
            print(line)
    
    def readDataFromCSVFile(self, csvFileObj):
        pass
    
    def columnBreakdown(self, columnNameStr, dataInclusionList=[]):
        """Calculates and prints mean, median, and mode"""
        actualN = 0
        sumAllAnswers = 0
        allAnswers = []
        answerFreqs = {}
        maxFreq = 0
        modeList = []
        
        columnIndex = self.surveyEntryAttributeColumnIndexDict[columnNameStr]
        if columnIndex == None:
            raise ValueError("{0} not a valid column name".format(columnNameStr))
        
        for entry in range(len(self.data)):
            answer = self.data[entry][columnIndex]
            if answer == None:
                continue
            else:
                actualN += 1
                if answer in answerFreqs.keys():
                    answerFreqs[answer] += 1  #Increment already-created entry
                else:
                    answerFreqs[answer] = 1  #Create new entry
                try:
                    sumAllAnswers += answer
                except:  #If answer is not a numeric type, then mean won't work
                    pass
                allAnswers.append(answer)
        
        #Find mode
        for key,value in answerFreqs.items():
            if value > maxFreq:  #Item with higher frequency found, replace all previous "modes" in modeList
                maxFreq = value
                modeList = [key]
            elif value == maxFreq:  #Item with same frequency found as highest frequency, add this mode to modeList
                modeList.append(key)
        #Find median
        allAnswers.sort()
        # Note that allAnswers is accessed with indices from 0 to actualN-1
        if actualN % 2 == 0:  #If actualN is even:
            median = simplifyNumber( (allAnswers[actualN // 2 - 1] + allAnswers[actualN // 2]) /2)  #Median is average of middle two values
        else:  #If actualN is odd:
            median = allAnswers[actualN // 2]  #Median is the center value
        #Find Q1, Q3 by finding where Q1 and Q3 lie, and then averaging the 
        q1 = simplifyNumber( (allAnswers[math.floor(25/100*(actualN+1)) - 1] + allAnswers[math.ceil(25/100*(actualN+1)) - 1]) / 2)
        q3 = simplifyNumber( (allAnswers[math.floor(75/100*(actualN+1)) - 1] + allAnswers[math.ceil(75/100*(actualN+1)) - 1]) / 2)
        #Find IQR (interquartile range)
        iqr = q3-q1
        #Find range
        maxAnswer = allAnswers[actualN-1]
        minAnswer = allAnswers[0]
        answerRange = maxAnswer - minAnswer
        # Five number summary
        fiveNumberSummary = [minAnswer, q1, median, q3, maxAnswer]
        #Find mean and standard deviation
        try:
            mean = round(sumAllAnswers / actualN,4)
            sumDeviationSquared = 0
            for x in allAnswers:
                sumDeviationSquared += (x - mean)**2
            stdDev = round( (sumDeviationSquared/(actualN - 1))**0.5,  4)
        except:
            mean = "N/A due to data type"
            stdDev = "N/A due to data type"
        print("{0}: n={1}, mean={2}, median={3}, mode={4}, stdDev={6}, fiveNumberSummary={7}, IQR={8}, answer distribution={5}".format(columnNameStr,actualN,mean,median,modeList,answerFreqs,stdDev,fiveNumberSummary,iqr))
        
        #Display info on screen with turtle
        """self.turtle.setpos(x,y)
        self.turtle.write()"""
      
    
    def returnCorrelationCoefficient(self, xColumnIndex, yColumnIndex, dataInclusionList=[]):
        """dataInclusionList is a list of conditions that need to be
            for entries to be included in the data analysis. The list
            contains (key,desiredState) tuples where key is in self.a"""
        actualN = 0  #It's not len(self.data) as some entries could be invalid
        sumX = 0.0
        sumY = 0.0
        sumXY = 0.0
        sumXSquared = 0.0
        sumYSquared = 0.0
        skipEntry = False
        for entry in range(len(self.data)):
            x = self.data[entry][xColumnIndex]
            y = self.data[entry][yColumnIndex]
            if x == None or y == None:
                continue
            for conditionKeyStr,desiredState in dataInclusionList:
                columnIndex = self.surveyEntryAttributeColumnIndexDict.get(conditionKeyStr)
                if columnIndex == None:  #conditionKeyStr is not a key in the dict
                    continue
                if self.data[entry][columnIndex] != desiredState:
                    skipEntry = True
            if skipEntry:
                skipEntry = False
                continue
            actualN += 1
            sumX += x
            sumY += y
            sumXY += x*y
            sumXSquared += x**2
            sumYSquared += y**2
            
        r = (actualN*sumXY - sumX*sumY) / (( (actualN*sumXSquared - sumX**2)*(actualN*sumYSquared - sumY**2) )**0.5)
        return actualN,r
    
    def displayScatterPlot(self,xColumnIndex, yColumnIndex, dataInclusionList=[]):
        """A test idea. Parameters: screen wn, turtle t
            dataInclusionList"""
        printedValues = []
        updateFrequency = 10
        currentTimeElapsed = 0
        self.wn.tracer(updateFrequency,delay=1)
        scaleFactor = (self.wn.window_width() * 0.75) // 10  #Assuming that window_width is smaller than window_height
        #Draw axes
        self.turtle.setpos(0,0)
        self.turtle.pendown()
        self.turtle.setpos(0,(10+1)*scaleFactor)
        self.turtle.penup()
        self.turtle.setpos(0,0)
        self.turtle.pendown()
        self.turtle.setpos((10+1)*scaleFactor,0)
        self.turtle.penup()
        skipEntry = False
        
        #Draw the dots
        for entry in range(len(self.data)):
            x = self.data[entry][xColumnIndex]
            y = self.data[entry][yColumnIndex]
            if x == None or y == None:
                continue
            for conditionKeyStr,desiredState in dataInclusionList:
                columnIndex = self.surveyEntryAttributeColumnIndexDict.get(conditionKeyStr)
                if columnIndex == None:
                    continue
                if self.data[entry][columnIndex] != desiredState:
                    skipEntry = True
            if skipEntry:
                skipEntry = False
                continue
            #Scale x and y to numbers that can be displayed on the screen
            xCoord = x*scaleFactor
            yCoord = y*scaleFactor
            #print(xValue,yValue)
            printedValues.append((x,y))
            t0 = time.perf_counter()
            self.turtle.setpos(xCoord,yCoord)
            self.turtle.stamp()
            t1 = time.perf_counter()
            currentTimeElapsed += (t1-t0) #Everything involving time here seems like a lot of calculations, but the program apparently handles it in a reasonable amount of time 
            if currentTimeElapsed > 0.5: #more than 0.5 seconds
                updateFrequency += 5 #update after more number of frames have passed
                self.wn.tracer(updateFrequency,delay=1)
                currentTimeElapsed = 0
        print(printedValues)
        n,r = self.returnCorrelationCoefficient(xColumnIndex, yColumnIndex, dataInclusionList)
        self.turtle.setpos(0,-30)
        self.turtle.write("n = {0}, r = {1:.4f}".format(n,r), move=True,align="left",font=("Arial",26,"bold"))
        print("n = {0}, r = {1:.7f}".format(n,r))
            
    def clearScreen(self):
        self.turtle.clear()

def returnDataFieldIndiceDictionary(lineList):
    indexDict = {} #A dictionary that matches a column with its index in lineList
    enabledColumns = []
    for index in range(len(lineList)):
        columnName = lineList[index]
        if columnName == "":
            continue
            #indexDict[index] = None  #The column doesn't have any information related to this program
        else:
            indexDict[index] = columnName #For data display/visualization purposes
            enabledColumns.append(index)
    return indexDict,enabledColumns
    """Find a way to determine which set of things is from which grade"""

def simplifyNumber(number):
    """If number is a float representation of an integer, return it upgraded to int.
        Else return number unchanged
        Assumes parameter number is an int or float"""
    if (number // 1) != number:  #Is this method valid?
        #Then number is a decimal
        return number
    else:  #Then number is an int
        return int(number)

def returnFirstNumber(answerStr):
    """Returns an int or float, depending on the number"""
    numStr = ""
    for c in answerStr:
        if c.isnumeric() or c == ".":  #This assumes that a period will only occur as the decimal sign in answerStr
            numStr += c
        else:
            break
    output = float(numStr)
    return simplifyNumber(output)


if __name__ == "__main__":
    surveyEntriesList = []
    opinionToInt = {"SD": 1,  "D": 2,  "A":3,  "SA":4}
    courseDictKeyStr = ["WhyChoseCourse", "LikeMath", "LikeCourse", "CourseDifficulty", "WhenStudy", "LengthStudy", "TimeSpent", "Grade"]
    firstPrint = True
    filename = "Raw Data-Rearranged (working copy).csv"
    
    #Build surveyEntriesList (Should change this to an actual 2D array? or make it a class?)
    with open(filename,"r") as csvfile:
        dataReader = csv.reader(csvfile)
        lineNo = 0
        for line in dataReader:
            #print(lineNo,line)
            lineNo += 1
            if lineNo == 1:
                continue #Skip line 1
            elif lineNo == 2:
                dataFieldIndices,enabledColumns = returnDataFieldIndiceDictionary(line)
                continue
            
            if firstPrint:
                print("dataFieldIndices is:", dataFieldIndices)
                print("enabledColumns is:", enabledColumns)
                firstPrint = False
                
            #The rest of the csv file would be actual survey results
            entry = SurveyEntry(lineNo)
            #enabledColumns[0] is name/ID
            entry.currentGrade = int(line[enabledColumns[1]])
            entry.birthYear = int(line[enabledColumns[2]])
            entry.gender = line[enabledColumns[3]]
            #enabledColumns[4] is choice of food
            entry.parentsExpectWellMath = opinionToInt[line[enabledColumns[5]]]
            entry.parentsThinkMathImportant = opinionToInt[line[enabledColumns[6]]]
            entry.friendsLikeMath = opinionToInt[line[enabledColumns[7]]]
            entry.friendsDoWellMath = opinionToInt[line[enabledColumns[8]]]
            entry.iLookForwardMathClass = opinionToInt[line[enabledColumns[9]]]
            entry.iAnxiousMath = opinionToInt[line[enabledColumns[10]]]
            entry.iWorryMathMark = opinionToInt[line[enabledColumns[11]]]
            #enabledColumns[12] is hardestThingAboutMath
            #enabledColumns[13] is emotionalRating

            enabledColumnIndex = 13
            for courseNo,courseName in enumerate(["9MPM", "10MPM", "11MCR", "12MHF", "12MDM"]):
                NACount = 0
                currentHeader = "gr" + courseName
                currentDictName = currentHeader+"Data"
                entry.__dict__[currentDictName] = {}
                for n in range(8):
                    enabledColumnIndex += 1
                    answer = line[enabledColumns[enabledColumnIndex]]
                    if answer == "N/A":
                        NACount += 1
                    else:
                        if answer == "NoAnswer":
                            entry.__dict__[currentDictName][courseDictKeyStr[n]] = None
                        else:
                            entry.__dict__[currentDictName][courseDictKeyStr[n]] = returnFirstNumber(answer)  #For now, only choose first answer in multi-choice answers
                    if NACount >= 2:
                        entry.__dict__[currentDictName] = None
                        enabledColumnIndex = 13 + (courseNo+1)*8  #Move index to 1 place before start of next course's info
                        break
                    
            print(entry)
            surveyEntriesList.append(entry)  
    csvfile.close()
    
    screen = turtle.Screen()
    turtle = turtle.Turtle()
    surveyDataAnalyzer = DataAnalyzer(surveyEntriesList,screen,turtle)
    for columnNameStr in ["parentsExpectWellMath","parentsThinkMathImportant","friendsLikeMath","friendsDoWellMath","iLookForwardMathClass","iAnxiousMath","iWorryMathMark"]:
        surveyDataAnalyzer.columnBreakdown(columnNameStr)

    #for num in [0,1,2,3,4]:
    for num in [2]:  #Gr 11 math
        for xColumn, yColumn in [(14+num*8,13+num*8),(14+num*8,12+num*8),(13+num*8,12+num*8)]:
            surveyDataAnalyzer.displayScatterPlot(xColumn, yColumn,[("currentGrade",12)])
            time.sleep(2)
            surveyDataAnalyzer.clearScreen()
            surveyDataAnalyzer.displayScatterPlot(xColumn, yColumn,[("currentGrade",11)])
            time.sleep(2)
            surveyDataAnalyzer.clearScreen()
    
    screen.bye()
