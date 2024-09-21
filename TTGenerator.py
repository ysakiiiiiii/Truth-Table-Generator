connectives = ["not", "and", "or", "implies"] #bicon idk

statement = input("Enter a statement: ")

words = statement.split()

variables = []
connectivesUsed = []

for word in words:
    if word.isalpha() and word not in connectives:  
        variables.append(word)
    elif word in connectives:  
        connectivesUsed.append(word)
        
conCount = 0
varCount = 0

#fck this logic
while varCount < len(variables) or conCount < len(connectivesUsed):
    if conCount < len(connectivesUsed) and connectivesUsed[conCount] == "not":
        print(connectivesUsed[conCount] + " ")
        print(variables[varCount] + " ")
        conCount += 1
        varCount += 1
    elif varCount < len(variables) and varCount <= conCount:
        print(variables[varCount] + " ")
        varCount += 1
    
    if conCount < len(connectivesUsed):
        print(connectivesUsed[conCount] + " ")
        conCount += 1 
    
        
