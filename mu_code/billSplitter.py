# Write your code here :-)
import pprint

def billSplitter() :
    print('How many people are you splitting between?')
    numPeople = int(input())
    people = {}
    names = []
    for i in range(1 , numPeople + 1) :
        print('Enter the person ' + str(i) + '\'s name')
        name = input()
        people.setdefault(name,{})
        names.append(name)

    for name , receipt in people.items() :
        print ('Enter ' + name + '\'s sole expenses. Type \"Q" once you are done. \nItem Name/Q:')
        itemName = input()

        while itemName != 'Q' :
            receipt.setdefault('Total', 0)
            receipt.setdefault(itemName, 0)
            print ('Price of ' + itemName + ': ')
            itemPrice = float(input())
            receipt[itemName] += itemPrice
            receipt['Total'] += itemPrice
            print ('Item Name/Q:')
            itemName = input()


    for i in range(numPeople) :
        for j in range (i + 1, numPeople) :
            print ('Enter ' + names [i] + ' and ' + names[j] + '\'s shared expenses. Type \"Q" once you are done. \nItem Name/Q:')
            itemName = input()
            while itemName != 'Q' :
                people[names[i]].setdefault(itemName, 0)
                people[names[j]].setdefault(itemName, 0)
                print ('Price of ' + itemName + ': ')
                itemPrice = float(input())
                people[names[i]][itemName] += itemPrice/2
                people[names[j]][itemName] += itemPrice/2
                print ('Item Name/Q:')
                itemName = input()


    print ('Enter all shared expenses. Type \"Q" once you are done. \nItem Name/Q:')
    itemName = input()
    while itemName != 'Q' :
        for i in range(numPeople) :
            people[names[i]].setdefault(itemName, 0)

        print ('Price of ' + itemName + ': ')
        itemPrice = float(input())

        for i in range(numPeople) :
            people[names[i]][itemName] += itemPrice/float(numPeople)
        print ('Item Name/Q:')
        itemName = input()

    pprint.pprint(people)
    total = 0
    for name, receipt in people.items() :
        total += receipt['Total']
    print('The total is: ' + str(total))




billSplitter()







