#OOP Principles
# Encapsulation

class BadBankAccount:
    def __init__(self, balanceq):
        self.balance = balanceq


account = BadBankAccount(0.0)
account.balance = -1
print(account.balance)

class BankAccount:
    def __init__(self):
        self._balance = 0.0


    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit amoun must e positive")
        self._balance += amount

    def withdraw (self, amouunt):
        if amouunt <= 0:
            raise ValueError("withdraw amoun must e positive")



        








# #static vs. instance method example 
# class BankAccount:
#     MIN_BALANCE = 100

#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         # here we create the protectetd balance
#         self._balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#             print(f"{self.owner}'s newbalance ${self._balance}")
#         else:
#             print("charge your balance")

#     def _is_valid_amount(self, amount):
#         return amount > 0
    
#     def __log_transaction(self, trns_type, amount ):
#         print(f"Logging {trns_type} of $ {amount}. new balance: $ {self._balance}")


#     @staticmethod
#     def is_valid_interest_rate(rate):
#         return 0 <= rate <= 5
    

# account = BankAccount("paratsoo", 500)
# account.deposit(10)

# print(BankAccount.is_valid_interest_rate(3))
# print(BankAccount.is_valid_interest_rate(10))
        













# ///////////////////////////////////////////////////////////

# class User:
#     user_count = 0

#     def __init(self, username, email):
#         self.username = username
#         self.email = email
#         User.user_count += 1

#     def display_user(self):
#         print(f"username: {self.username}, email: {self.email}")


# user1 = User("parastoo", "p@gmail.com")
# user2 = User("sara", "s@gmail.com")

# print(User.user_count)
# print(user2.user_count)
# print(user2.user_count)


# ///////////////////////////////////////////////////////////
# class User :
#     def __init__(self, username, email, password):
#         self.username = username
#         self._email = email
#         self.password = password

#     @property
#     def email(self):
#         print("Email accessed")
#         return self._email

# # sett property
#     @email.setter
#     def email(self, new_emailx):
#         if "@" in new_emailx:
#              self._email = new_emailx


    

#     # def get_email(self):
#     #     return self._email
    
#     # def set_email(self, new_email):
#     #     if "@" in new_email:
#     #         self._email = new_email
#     #     self._email 

        
# user1 = User("paratsoo", " pst@gmail.com", "***")
# print(user1.email)



#     # def get_email(self):
#     #     return self._email
#     # def clean_email(self):
#     #     return self._email.lower().strip()

#     # def hi(self, user): 
#     #     print(f"Sending message to {user.username}: Hi {user.username},its {self.username}")

# # print(user1._email)
# # print(user1.clean_email())

# # print(user1._email)
# # user1.email="tedr"
# # print(user1.eamil)
# # user2 = User("weeda", "weeda@gmail.com", "123")
# # user1.hi(user2)

# # //////////////////////////////////////////////////////////

# # class Person :
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age

# #     def greet(self):
# #         print(f"hi, my name is {self.name} and {self.age} years old")

# # person1 = Person("parastoo", 26)
# # person1.greet()

# # person2 = Person("Bob", 77)
# # person2.greet()

# # //////////////////////////////////////////////////////////

# # class Dog:
# #     def __init__(self, namex,breedx, owner):
# #         self.name = namex
# #         self.breed = breedx
# #         self.owner = owner

# #     def bark (self):
# #         print("whoof whoof")


# # class Owner:
# #     def __init__(self, nameq, addressq, contactq):
# #         self.name = nameq
# #         self.address = addressq
# #         self.phone_num = contactq


# # owner1 = Owner( "Denny", "122 s div", "88-99")
# # dog1 = Dog("kiki", "Iranian", owner1)
# # print(dog1.owner.name)

# # owner2 = Owner("p1", "44 e av", "77-66")
# # dog2 =Dog("psto", "German", owner2)
# # print(dog2.owner.name)

# # owner3 = Owner("namMe", "AddressMe", "ContactMe")
# # dog3 = Dog("test1", "BreedMe", owner3)
# # print(dog3.owner.address)