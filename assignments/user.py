class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    def display_info(self):
        print(f"User Info: \n  First Name: {self.first_name} \n  Last Name: {self.last_name} \n  Email: {self.email} \n  Age: {self.age} \n  Rewards Member: {self.is_rewards_member} \n  Gold Card Points: {self.gold_card_points}")
        return self
    def enroll(self):
        if not self.is_rewards_member:
            self.is_rewards_member = True
            self.gold_card_points = 200
        else:
            print("Already a rewards member.")
        return self
    def spend_points(self, amount):
        if (self.gold_card_points - amount) > 0:
            self.gold_card_points -= amount
        else:
            print("Sorry, you don't have enough points")
        return self
    
user1 = User('Tony', 'Aiello', 'mraiello3@gmail.com', 31)
user1.display_info().enroll().spend_points(50).display_info()

user2 = User('Sol', 'the cat', 'catsHaveNoEmail1@gmail.com', 4)
user2.display_info().enroll().spend_points(80).display_info()

user3 = User('Luna', 'the cat', 'catsHaveNoEmail2@gmail.com', 4)
user3.display_info().spend_points(40).display_info()