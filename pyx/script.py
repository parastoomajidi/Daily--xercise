class User :
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def hi(self, user): 
        print(f"Sending message to {user.username}: Hi {user.username},its {self.username}")


# p = Hi("username", "user@gmail.com", "***")
# User.hi()

user1 = User("paratsoo", "pst@gmail.com", "***")
user2 = User("weeda", "weeda@gmail.com", "123")

user1.hi(user2)




# //////////////////////////////////////////////////////////

# class Person :
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print(f"hi, my name is {self.name} and {self.age} years old")

# person1 = Person("parastoo", 26)
# person1.greet()

# person2 = Person("Bob", 77)
# person2.greet()

# //////////////////////////////////////////////////////////

# class Dog:
#     def __init__(self, namex,breedx, owner):
#         self.name = namex
#         self.breed = breedx
#         self.owner = owner

#     def bark (self):
#         print("whoof whoof")


# class Owner:
#     def __init__(self, nameq, addressq, contactq):
#         self.name = nameq
#         self.address = addressq
#         self.phone_num = contactq


# owner1 = Owner( "Denny", "122 s div", "88-99")
# dog1 = Dog("kiki", "Iranian", owner1)
# print(dog1.owner.name)

# owner2 = Owner("p1", "44 e av", "77-66")
# dog2 =Dog("psto", "German", owner2)
# print(dog2.owner.name)

# owner3 = Owner("namMe", "AddressMe", "ContactMe")
# dog3 = Dog("test1", "BreedMe", owner3)
# print(dog3.owner.address)