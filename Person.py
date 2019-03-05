class Person:
    numPeople = 1
    def validate(self, listOfAttributes):
        if not listOfAttributes:
            if self.assigned is False:
                print(self.name + " does not have an assigned group.")
        else:
            for x in listOfAttributes:
                if x in self.dictionary:
                    pass
                else:
                    print("Attribute " + x + " is missing")

    def __init__(self, id = numPeople, firstName = None, lastName = None, dict= None):
        if not dict:
            self.attributes = {}
        else:
            self.attributes = dict
        self.attributes["firstName"] = firstName
        self.attributes["lastName"] = lastName
        self.attributes["id"] = Person.numPeople
        self.assigned = False
        Person.numPeople += 1
