class Person:
   def _init_(self, name, birthdate):
    self.name=name
    self.birthdate=birthdate

persons=[]

for i in range(3):
  name = input("Enter your Name: ")
  birthdate = input("Enter your Birthdate: ") 
  persons.append(Person(name, birthdate))

for person in persons:
    print(person.name, "was born on", person.birthdate)


