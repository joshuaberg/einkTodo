#!/usr/bin/env python3

import csv


#main fuction for testing
def main():
    addToList(content = "hi")
    addToList(content = "inserted", position = 8)


#ADDS ITEM TO LIST
def addToList(content, position = 999, sub = 0):

    #put contents into list
    with open('todo.csv','r') as csvfile:
        file  = csv.reader(csvfile,delimiter = ',')
        data = list(file)    

    #find number of items in current list
    filelen = len(data)


    if position > filelen:
        #print to end of the file

        #build the injected item for the todo list
        injection = [content, sub]
        data.append(injection)

        #write the new csv file
        with open('todo.csv', 'w') as csvfile:
            write = csv.writer(csvfile)
            write.writerows(data)

    else:
        #print to specified location

        #build the injected item for the todo list
        injection = [content, sub]
        data.insert(position - 1 , injection )

        #write the new csv file
        with open('todo.csv', 'w') as csvfile:
            write = csv.writer(csvfile)
            write.writerows(data)



#REMOVE ITEM FROM LIST
def removeFromList(content, position = 999, sub = 0):






if __name__== "__main__":
    main()


