class Dog:
    def __init__(self, namex,breedx, owner):
        self.name = namex
        self.breed = breedx
        self.owner = owner

    def bark (self):
        print("whoof whoof")


class Owner:
    def __init__(self, nameq, addressq, contactq):
        self.name = nameq
        self.address = addressq
        self.phone_num = contactq


owner1 = Owner( "Denny", "122 s div", "88-99")
dog1 = Dog("kiki", "Iranian", owner1)
print(dog1.owner.name)

owner2 = Owner("p1", "44 e av", "77-66")
dog2 =Dog("psto", "German", owner2)
print(dog2.owner.name)

owner3 = Owner("namMe", "AddressMe", "ContactMe")
dog3 = Dog("test1", "BreedMe", owner3)
print(dog3.owner.address)