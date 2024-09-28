def checkParentheses(words , valid):
    stackParentheses = []        #stack for parentheses, temporary storage ng parenthesis
    for word in words: 
       if word in matchingBrackets.keys():  #if word is in the keys of matchingBrackets, it means it is an opening parenthesis
         stackParentheses.append(word)   #append the opening parenthesis to the stack
       if word in matchingBrackets.values():   #if word is in the values of matchingBrackets, it means it is a closing parenthesis
        if stackParentheses and matchingBrackets[stackParentheses[-1]] == word:  #check if the closing parenthesis matches the last opening parenthesis in the stack
            stackParentheses.pop()     #if it matches mapopop yung opening parenthesis sa stack. mababawasan yung stack hanggang may partner sya
        else:
            print("Invalid Statement: Unmatched closing parenthesis" ) 
            return False  

    if not stackParentheses:  #if the stack is empty, it means all parentheses are balanced
        print("Parentheses are balanced.")
    else:
        print("Parentheses are not balanced.")
        valid = False
   
 
connectives = ["~", "^", "⌄", "->","<->"] #bicon idk
vars = ["P", "Q", "R"]
matchingBrackets = {"(": ")", "{": "}", "[": "]"}  # dictionary for matching brackets, parang pinagpapartner lang neto yung mga brackets. parang ganto sya "key": "value" so every key is may corresponding na value. ginamit ko sya para easy yung pagcheck ng matching ng brackets
#kapag nagprint tayo ng matchingBrackets["("] lalabas yung ")" so parang ganito yung logic nya matchingBrackets["key"] = "value" so pag tinawag mo yung key, lalabas yung value then vice versa kapag tinawag value lalabas yung key
valid = True


statement = input("Enter a statement: ").upper()
words = statement.split()
checkParentheses(words , valid)
variables = []
connectivesUsed = []
parenthesesUsed = []

#reads variables and connectives
for word in words:
 if word.isalpha() and word in vars:  
  variables.append(word)
 elif word in connectives: 
  connectivesUsed.append(word)
 elif word in matchingBrackets.keys() or word in matchingBrackets.values():
  parenthesesUsed.append(word)
 else:
  print("invalid syntax detected")
  valid = False
  
        #it does nothing yet tamad ako eh
   #________________________________________________________     
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
 while varCount < len(variables) or conCount < len(connectivesUsed) :
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
