#Tokenize string text into a list of type int delineated by " ".
def split_line(text):    
  listOfInts = text.split()
  listOfInts[0]=int(listOfInts[0])
  print("length of list: "+str(listOfInts[0]))
  myRange=range(1,listOfInts[0]+1)          
  for n in myRange:
    listOfInts[n]=int(listOfInts[n])
    print("item "+str(n)+": "+str(listOfInts[n])+", type: "+str(type(listOfInts[n])))
  return listOfInts

#Add together all int values in list except the first.
def add(myList):
  total=0
  myRange=range(1,myList[0]+1)
  for n in myRange:
    total+=myList[n]
  return total

print ("sum: "+str(add(split_line("3 4 15 432"))))