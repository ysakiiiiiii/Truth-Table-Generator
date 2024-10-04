

connectives = ["~", "^", "⌄", "->", "<->"] 
vars = ["P", "Q", "R"]
matchingBrackets = {"(": ")", "{": "}", "[": "]"}  
firstVar = []
secondVar = []
thirdVar = []

rowCount = 0
valid = True  # Glinobal ko kase para same sa lahat na ng fucking functions

def userInput():
    statement = input("Enter a statement: ").upper()
    words = statement.split()
    checkParentheses(words)
    syntaxChecker(words)

def checkParentheses(words):
    global valid  # Idineclare ko para mamodify dito sa function yung tang-inang global var na yon
    stackParentheses = []  
    for word in words: 
        if word in matchingBrackets.keys():  
            stackParentheses.append(word)  
        elif word in matchingBrackets.values():  
            if stackParentheses and matchingBrackets[stackParentheses[-1]] == word:  
                stackParentheses.pop()  
            else:
                print("Invalid Statement: Unmatched closing parenthesis") 
                valid = False
                return False  

    if not stackParentheses:  
        print("Parentheses are balanced.")
    else:
        print("Parentheses are not balanced.")
        valid = False


def syntaxChecker(words):
    global valid  
    variables = [] # pagstore'n t variables nga nausar
    connectivesUsed = [] #pagstore'n t connectives nga nausar
    parenthesesUsed = [] #pagstore'n t parentheses nga nausar

    # Syntax check for variables, connectives, and parentheses
    for word in words:
        if word.isalpha() and word in vars:  
            variables.append(word)
        elif word in connectives: 
            connectivesUsed.append(word)
        elif word in matchingBrackets.keys() or word in matchingBrackets.values():
            parenthesesUsed.append(word)
        else:
            print("Invalid syntax detected.")
            valid = False
            return

    #To check syntax din by Basilio
    for word1, word2 in zip(words, words[1:]):
        if word1 in vars and word2 in vars:
            print("Invalid Statement: Two variables cannot be adjacent.")
            valid = False
            return
        if word1 in connectives and word2 in connectives and word2 != "not":
            print("Invalid Statement: Two connectives cannot be adjacent.")
            valid = False
            return
        if words[-1] in connectives:
            print("Invalid Statement: The last word cannot be a connective.")
            valid = False
            return

    if valid:
        uniqueVars = set(variables)  # set function para iremove yung duplicates na vars
        varPopulator(uniqueVars)  # ipopulate ang var based sa count ng unique vars to compute the rows
        readLogic(variables, connectivesUsed)

def varPopulator(uniqueVars):
    n = len(uniqueVars)  # exponent determiner base sa uniq na variable kanina
    global rowCount 
    rowCount = 2 ** n    # Number ng row sa truth table...tama tong formula dbaaaaaaaa 2^n?

    if n == 3:

        for i in range(rowCount): # alam niyo na to from 0 to 7 kung n = 3 and rowCount is 8
            firstVar.append("True" if (i // 4) % 2 == 0 else "False")  # nakafloor division yan ha...ieevaluate lang kung true or false tas iaappend sa first var and same din sa iba 
            secondVar.append("True" if (i // 2) % 2 == 0 else "False") # wag ko na explain ha, alam kong magaling kayo
            thirdVar.append("True" if i % 2 == 0 else "False")      


    if n == 2:

        for i in range(rowCount):
            firstVar.append("True" if (i // 2) % 2 == 0 else "False") 
            secondVar.append("True" if (i % 2) == 0 else "False") 

    if n == 1: #prinepare ko na to para sa mga kupal na mag-eenter ng p and not p etc

        for i in range(rowCount):
            firstVar.append("True" if (i % 2) == 0 else "False")  



def readLogic(variables, connectivesUsed):

    print("Test")
    # conCount = 0
    # varCount = 0
    # while varCount < len(variables) or conCount < len(connectivesUsed):
    #     if conCount < len(connectivesUsed) and connectivesUsed[conCount] == "not":
    #         print(connectivesUsed[conCount] + " " + variables[varCount])
    #         conCount += 1
    #         varCount += 1
    #     elif varCount < len(variables) and varCount <= conCount:
    #         print(variables[varCount] + " ")
    #         varCount += 1
    #     if conCount < len(connectivesUsed):
    #         print(connectivesUsed[conCount] + " ")
    #         conCount += 1

def printFuckingTable():    
    if rowCount == 8:
        print(f"{'P':<10} {'Q':<10} {'R':<10}")  # string formatting based kay w3schools 
        print('-' * 30) 
        for i in range(len(firstVar)):
            print(f"{firstVar[i]:<10} {secondVar[i]:<10} {thirdVar[i]:<10}")

    elif rowCount == 4:
        print(f"{'P':<10} {'Q':<10}") 
        print('-' * 20)  
        for i in range(len(firstVar)):
            print(f"{firstVar[i]:<10} {secondVar[i]:<10}")

    elif rowCount == 2:
        print(f"{'P':<10}") 
        print('-' * 10)
        for i in range(len(firstVar)):
            print(f"{firstVar[i]:<10}")



# Entry point ng putang-inang user
userInput()
printFuckingTable()
