'''
Author: Celine Podgornik
Date: 26 April 2017

Description:
This program simulates combat for a simple Role Playing Game.
'''

import random

class Fighter():

    def __init__(self, name):
        '''
        This function sets a name attribute to the name of the parameter and
        sets a hit_points attribute to 10. 
    
        Parameters:
        self
        name: a string representing the name of a player.
    
        Returns:
        None.
        '''
    
        self.name = name
        self.hit_points = 10
        return None
        
    def __repr__(self): 
        '''
        This function returns a string showing a players name and the hit_points 
        assocated with that player.
    
        Parameters:
        self.
    
        Returns:
        a string showing a players name and the hit_points assocated with that player.
        '''
    
        result = self.name + ' (HP: ' + str(self.hit_points) + ')'
        return result
        
    def take_damage(self, damage_amount):
        '''
        This function decreases the hit_points attribute by the damage_amount, checks
        to see if a player has died (if the hit_points attribute is 0 or less), then prints
        out either a messages indicating the player has died or how many hit points the 
        player has remaining. 
        
        Parameters:
        self.
        damage_amount: an integer that represents the number of hit points of damage 
        inflicted on a player. 
        
        Returns:
        None.
        '''
    
        self.hit_points -= damage_amount
        if self.hit_points <= 0:
            print('\tAlas, ' + self.name + ' has fallen!')
        else:
            print('\t' + self.name + ' has ' + str(self.hit_points) + ' hit points remaining.')
        return None

    def attack(self, other):
        '''
        This function first prints the name of the playing attacking and the player being attacked and 
        then determines whether the attack hits (if a randomly generated number is 12 or greater). If the 
        attack hits, a random integer is generated representing the amount of damage inflicted. Then the
        amount of damage is printed and the take_damage method is called on the victim, passing it the
        amount of damage inflicted. If the attack misses, a message indicting that the attack missed is printed.
        
        Parameters:
        self.
        other: the fighter instance being attacked by the self instance. 
        
        Returns:
        None.
        '''
    
        print(self.name + ' attacks ' + other.name + '!')
        hits = random.randrange(1,21)
        if hits > 11:
            amount = random.randrange(1,7)
            print('\tHits for ' + str(amount) + ' hit points!')
            other.take_damage(amount)
        else:
            print('\tMisses!')
        return None
    
    def is_alive(self):
        '''
        This function checks to see if a player is alive. 
        
        Parameters:
        self.
        
        Returns:
        True if the hit_points attribute is greater than 0.
        False otherwise. 
        '''
    
        if self.hit_points > 0:
            return True
        return False
        
def combat_round(player1, player2):
    '''
    This function determines which of the two players attacks first by generating a
    random integer.
    
    Parameters:
    player1: an instance of the first player. 
    player2: an instance of the second player.
    
    Returns:
    None.
    '''
    
    player1_num = random.randrange(1,7)
    player2_num = random.randrange(1,7)
    if player1_num == player2_num:
        print('Simultaneous!')
        player1.attack(player2)
        player2.attack(player1)
    elif player1_num > player2_num:
        player1.attack(player2)
        if player2.is_alive():
            player2.attack(player1)
    else:
        player2.attack(player1)
        if player1.is_alive():
            player1.attack(player2)
    return None    
        
#==========================================================
def main():
    '''
    When this file is run, first two instances of the Fighter class are created. Then
    in a while loop the following happens: the round number is printed, each of the
    fighters information is printed, the function is paused until a user presses enter,
    and the combat function is called to simulate a single round of combat. Once a player 
    has died (the is_alive method returns False), the while loop is exited and a message
    indicating the battle has ended is printed followed by each of the fighters information. 
    '''
    
    player1 = Fighter(input('Enter name of player 1: '))
    player2 = Fighter(input('Enter name of player 2: '))
    i = 1
    while True:
        print('='*19 + ' ROUND ' + str(i) + ' ' + '='*19)
        print(player1)
        print(player2)
        input('Enter to fight!')
        combat_round(player1, player2)
        if not player1.is_alive() or not player2.is_alive():
            break
        i += 1
    print()
    print('The battle is over!')
    print(player1)
    print(player2)
        
if __name__ == '__main__':
    main()
