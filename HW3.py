import sys
import Person
import Group

line = input("Choose an option:")
pList = []
gList = []

while line != "-1":
    if line == "0":
        print('''
        On -1, end the loop.
        On 0, output what each number does
        On 1, create a new Person. Ask for the first and last name.
        On 2, create a new group, populated by existing Person objects. Loop while outputting the names of people
        who have not been assigned to a group and ask for the ids of the people to add.
        On 3, allow the user to modify an existing group. Ask the user which group they wish to modify. Then ask
        whether they are trying to add or remove members to/from the group. Then, interactively allow the user to add
        Page 2 of 2
        or remove as many users as they want by offering a list of available choices and having the user select which
        member to interact with.
        On 4, validate all existing groups, as well as all people to check that they have a group.
        On 5, output each group’s number and members.
        ''')
    elif line == "1":
        first = input("What is the person's first name?")
        last = input("What is the person's last name?")
        p = Person.Person(None, first, last, {})
        pList.append(p)

    elif line == "2":
        selected = 0
        newGroup = Group.Group(None, None)
        while selected != "-1":
            for x in pList:
                if x.assigned is False:
                    pId = x.attributes["id"]
                    first2 = x.attributes["firstName"]
                    last2 = x.attributes["lastName"]
                    print(str(pId) + " " + str(first2) + " " + str(last2))
            selected = input("Which person would you like to add to the new group? (-1 to finish adding people) :")
            for x in pList:
                if str(x.attributes["id"]) == selected:
                    newGroup.listOfPeople.append(x)
                    x.assigned = True

        gList.append(newGroup)

    elif line == "3":
        groupID = input("Which group would you like to modify?")
        addOrRemove = input("would you like to ADD or Remove members?")
        selectedGroup = gList[0]
        selectedPerson = 0
        for x in gList:
            if str(x.id) == groupID:
                selectedGroup = x
        if addOrRemove == "ADD":
            while selectedPerson != "-1":
                for x in pList:
                    if x.assigned is False:
                        print(str(x.attributes["id"]) + " " + str(x.attributes["firstName"]) + " " + str(x.attributes["lastName"]))
                selectedPerson = input("Which person would you like to add from the group? (-1 to finish):")
                if selectedPerson == "-1":
                    break
                else:
                    for x in pList:
                        if str(x.attributes["id"]) == selectedPerson:
                            selectedGroup.listOfPeople.append(x)
        elif addOrRemove == "REMOVE":
            while selectedPerson != "-1":
                for x in selectedGroup.listOfPeople:
                    print(str(x.attributes["id"]) + " " + str(x.attributes["firstName"]) + " " + str(x.attributes["lastName"]))
                selectedPerson = input("Which person would you like to add from the group? (-1 to finish):")
                if selectedPerson == "-1":
                    break
                else:
                    for x in selectedGroup.listOfPeople:
                        if str(x.attributes["id"]) == selectedPerson:
                            selectedGroup.listOfPeople.remove(x)
                            x.assigned = False
    elif line == "4":
        list = ["firstName", "lastName", "id"]
        for x in pList:
            x.validate(list)
        for x in gList:
            x.validate()
    elif line == "5":
        for x in gList:
            print("Group " + str(x.id))
            for y in x.listOfPeople:
                print(str(y.attributes["firstName"]) + " " + str(y.attributes["lastName"]))

    line = input("Choose an option:")

