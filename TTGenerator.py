connectives = ["not", "and", "or", "implies"] #bicon idk
vars = ["P", "Q", "R"]
valid = True

statement = input("Enter a statement: ")

words = statement.split()

variables = []
connectivesUsed = []



#reads variables and connectives
for word in words:
 if word.isalpha() and word in vars:  
  variables.append(word)
 elif word in connectives:  
  connectivesUsed.append(word)
 else:
  print("invalid syntax detected")
  valid = False
        #it does nothing yet tamad ako eh
        
 for word1, word2 in zip(words, words[1:]):
    if valid:
     if word1 in vars and word2 in vars:
         print("Invalid Statement")
         valid = False
         break
     if word1 in connectives and word2 in connectives and word2 != "not":
         print("Invalid Statement")
         valid = False
         break
     if words[-1] in connectives:
         print("Invalid Statement")
         valid = False
         break
        

if valid: #(tab niyo yung sa baba)
 conCount = 0
 varCount = 0

#reads logic
 while varCount < len(variables) or conCount < len(connectivesUsed):
     if conCount < len(connectivesUsed) and connectivesUsed[conCount] == "not":
         print(connectivesUsed[conCount] + " ")#to be substituted with actual logi 
         print(variables[varCount] + " ")
         conCount += 1
         varCount += 1
     elif varCount < len(variables) and varCount <= conCount:
         print(variables[varCount] + " ")#to be substituted with actual logic
         varCount += 1
    
     if conCount < len(connectivesUsed):
         print(connectivesUsed[conCount] + " ")#to be substituted with actual logic
         conCount += 1 
    
