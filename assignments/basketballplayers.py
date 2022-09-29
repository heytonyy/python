class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.age = dict['age']
        self.position = dict['position']
        self.team = dict['team']
    
    def print_player_info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nPosition: {self.position}\nTeam: {self.team}")
        print("----")

    @classmethod
    def get_team(cls, team_list):
        class_new_team = []
        for player in team_list:
            class_new_team.append(Player(player))
        return class_new_team

# data
kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}
    
# Create your Player instances here!
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

# Player List
new_team = []
players = [kevin, jason, kyrie]

print("-----------------")

for player in players:
    new_team.append(Player(player))
    Player(player).print_player_info()

print("-----------------")

# using class method
new_team_class_method = Player.get_team(players)
for player in new_team_class_method:
    player.print_player_info()

print("-----------------")
