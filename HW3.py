import sys
import Person


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
                    gList.append(x)
                    x.assigned = True

    elif line == "3":
        pass
    elif line == "4":
        pass
    elif line == "5":
        pass

    line = input("Choose an option:")

