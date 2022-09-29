from ninja import Ninja
from pets import Cat,Squirrel

owners = []

owners.append( Ninja("Tony", "Aiello", "Cat Nip", "Dry Food", Cat("Sol")) )
owners.append( Ninja("Trevor", "Corson", "Nuts", "Nuts", Squirrel("Ted")) )

##############
##############

print(" ")
print(">>> Welcome to the pet playground! <<<")
print(" ")
print("The current pet owners in the playground are: ")
for owner in owners:
    print(f"    {owner.first_name} {owner.last_name}")
print(" ")
print("These are the types of pets in the playground:")
for owner in owners:
    print(f"    {owner.pet.type}")
print(" ")
print("Look at the owners take care of their pets!")
print(" ")
for owner in owners:
    owner.feed(owner.pet_food)
    owner.walk()
    owner.bathe()
    print(" ")
print(" ")
print("Thanks for visiting the playground! Bring your pet here next time!")
print(" ")
print(" ")

##############
##############
