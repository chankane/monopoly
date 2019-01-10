from player import Player

class Room:

    def __init__(self):
        self.members = []
    
    def add_member(self, player):
        self.members.append(player)
    
    def get_members(self):
        return self.members
    
    def disp(self, screen, size):
        for player in self.members:
            player.disp(screen, size)