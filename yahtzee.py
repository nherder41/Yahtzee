'''This contains the class needed in order to run Yahtzee
CS108 Final Project
11/23/2016
Nate Herder (ndh7)
'''
import random


class Yahtzee:
     

    def __init__(self):
        self.upper_score = 0
        self.lower_score = 0
        self.grand_total_score = 0
        
        self.highscore = 0
        self.roll_count = 0
        self.yahtzee_count = 0
        self.yahtzee_press = 0
        self.bonus_count = 0
        
        self.roll_list = [0, 0, 0, 0, 0]
            
    def get_dice(self):
        '''access the current dice values'''
        return self.roll_list
    
    def roll_dice(self, hold_list):
        '''set the dice in the roll list to a random integer 1-6 only if the dice is not being held'''
        if self.roll_count < 3:        
            for dice in range(5):
                if hold_list[dice] == 0:
                    self.roll_list[dice] = random.randint(1, 6)    
        self.roll_count += 1
         
         
         
    def count_dice(self, number):
        '''this will properly score aces through sixes, updates the upper total, and check to see if the user earned a bonus'''
        for dice in self.roll_list:
            if dice == number:
                self.upper_score += number
        if self.upper_score >= 63:
            if self.bonus_count == 0:
                self.upper_score += 35
                self.bonus_count += 1
        self.compute_grand_total()
        self.check_highscore()
        
    def count_three_of_Kind(self):
        '''makes sure the roll_list has three dice wtih the same value, if so it awards the user points'''
        sum_of_dice = sum(self.roll_list)
        for i in range(1,7):
            if self.roll_list.count(i) >= 3:
                self.lower_score += sum_of_dice
        self.compute_grand_total()
        self.check_highscore()
        
    def count_four_of_kind(self):
        '''makes sure the roll_list has four dice with the same value, if so it awards the user points'''
        sum_of_dice = sum(self.roll_list)
        for i in range(1,7):
            if self.roll_list.count(i) >= 4:
                self.lower_score += sum_of_dice
        self.compute_grand_total()
        self.check_highscore()
        
    def count_full_house(self):
        '''makes sure that the dice values in roll_list truly are a full house, if so it awards the user points'''
        tally_list = [0, 0, 0, 0, 0, 0]
        for dice in self.roll_list:
            if dice == 1: 
                tally_list[0] += 1
            if dice == 2: 
                tally_list[1] += 1
            if dice == 3: 
                tally_list[2] += 1
            if dice == 4: 
                tally_list[3] += 1
            if dice == 5: 
                tally_list[4] += 1
            if dice == 6: 
                tally_list[5] += 1
        if 3 in tally_list and 2 in tally_list:
            self.lower_score += 25
        
        self.compute_grand_total()
        self.check_highscore()
        
    def count_small_straight(self):
        '''makes sure the values in roll_list fits one of the three possible options to receive points for a small straight'''
        st1 = [1, 2, 3, 4]
        st2 = [2, 3, 4, 5]
        st3 = [3, 4, 5, 6]
        count = 0
        for i in range(5):
            if self.roll_list[i] in st1:
                count +=1
                if count == 4:
                    self.lower_score += 30
        for i in range(5):
            if self.roll_list[i] in st2:
                count +=1
                if count == 4:
                    self.lower_score += 30
        for i in range(5):
            if self.roll_list[i] in st3:
                count +=1
                if count == 4:
                    self.lower_score += 30
        
        self.compute_grand_total()
        self.check_highscore()
        
    def count_large_straight(self):
        '''makes sure the values in roll_list fits one of the two possible options to receive points for a large straight'''
        st1 = [1, 2, 3, 4, 5]
        st2 = [2, 3, 4, 5, 6]
        sorted_dice = sorted(self.roll_list)
        if (sorted_dice == st1) or (sorted_dice == st2):
            self.lower_score += 40
        
        self.compute_grand_total()
        self.check_highscore()
        
    def count_yahtzee(self):
        '''makes sure all the dice values in roll_list are the same and awards the user points'''
        tally_list = [0, 0, 0, 0, 0, 0]
        for dice in self.roll_list:
            if dice == 1: 
                tally_list[0] += 1
            if dice == 2: 
                tally_list[1] += 1
            if dice == 3: 
                tally_list[2] += 1
            if dice == 4: 
                tally_list[3] += 1
            if dice == 5: 
                tally_list[4] += 1
            if dice == 6: 
                tally_list[5] += 1
        if 5 in tally_list:
            if self.yahtzee_count == 0:
                self.lower_score += 50
            else:
                self.lower_score += 100
            self.yahtzee_count += 1
        else:
            self.yahtzee_press += 1
        
        self.compute_grand_total()
        self.check_highscore()
        
    def count_chance(self):
        '''sums up all the dice in the roll_list and awards the user points'''
        self.lower_score += sum(self.roll_list)
        
        self.compute_grand_total()
        self.check_highscore()
    
    
    
    def get_upper_total(self):
        '''accessor for the upper score'''
        return self.upper_score
        
    def get_lower_total(self):
        '''accessor for the lower score'''
        return self.lower_score
        
    def get_grand_total(self):
        '''calculates and returns the grand total'''
        return self.grand_total_score
    
    def get_high_score(self):
        '''accessor for the highest score'''
        return self.highscore
    
    def get_yahtzee_press(self):
        '''accessor for the highest score'''
        return self.yahtzee_press
    
    
    
    def compute_grand_total(self):
        '''compute the grand total score'''
        self.grand_total_score = self.upper_score + self.lower_score
    
    def set_highscore(self):
        '''read from the stats file to see what the all time highscore is and display it in the gui'''
        score = []
        with open('stats.txt', 'r') as f:
            for line in f.readlines():
                score.append(line)
            self.highscore = score[0]
         
    def check_highscore(self):
        '''check to see if the grand total is greater than the stored high score'''
        if int(self.grand_total_score) > int(self.highscore):
            with open('stats.txt', 'w') as f:
                f.write(str(self.grand_total_score))
            self.highscore = self.grand_total_score
        
    def reset_roll_count(self):
        '''resets the roll count so the user can have another three rolls'''
        self.roll_count = 0
    
    def get_yahtzee_count(self):
        '''keeps track of the number of yahtzee rolled by the user throughout the game'''
        return self.yahtzee_count
    
    def reset_game(self):
        '''resets scores, the yahtzee count, and the dice values in the roll_list'''
        self.reset_roll_count()
        self.upper_score = 0
        self.lower_score = 0
        self.grand_total_score = 0
        self.yahtzee_count = 0
        self.yahtzee_press = 0
        self.bonus_count = 0
        self.roll_list = [0, 0, 0, 0, 0]

     
        
