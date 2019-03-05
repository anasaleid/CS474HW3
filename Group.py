import Person

class Group:
    numGroups = 0
    def __init__(self, id = numGroups, listOfPeople = None):
        self.id = id
        Group.numGroups += 1
        self.listOfPeople = listOfPeople


    def validate(self):
        list = ["firstName", "lastName", "id"]
        for x in self.listOfPeople:
            x.Person.validate(list)

        if len(self.listOfPeople) < 3:
            print("Group has" +len(self.listOfPeople) + " people, less than 3")
        elif len(self.listOfPeople) > 5:
            print("Group has" + len(self.listOfPeople) + " people, more than 5")