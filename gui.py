'''This creates the Yahtzee gui, which communicates with the Yahtzee class
CS108 Final Project
11/23/2016
Nate Herder (ndh7)
'''

from tkinter import *
from yahtzee import *

class App:
    
    def __init__(self, window):
        self._game = Yahtzee()
        self.pressed_buttons = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        
        #make the three main frames---------------------------------------------------------------------
        frame0 = Frame(window)
        frame0.pack(side=TOP)
        
        frame1 = Frame(window)
        frame1.pack(side=TOP)
        
        frame2 = Frame(window)
        frame2.pack(side=TOP)
        
        frame3 = Frame(window)
        frame3.pack(side=TOP)
        
        
        
        logo = PhotoImage(file='yahtzeepic.png')
        image_label = Label(frame0, image=logo)
        image_label.image = logo
        image_label.pack(side=TOP)
        
        
        
        #roll button----------------------------------------------------------------------------------
        roll_button = Button(frame1, text='Roll Dice', command=self.new_roll)
        roll_button.grid(row=1, column=1, sticky=E)
        
        
        
        #dice roll label 1----------------------------------------------------------------------------
        self.dice1 = IntVar()
        dice1_roll_label = Label(frame1, textvariable=self.dice1, width = 1)
        dice1_roll_label.grid(row=1, column=2, sticky=W)
        
        #dice roll label 2----------------------------------------------------------------------------
        self.dice2 = IntVar()
        dice2_roll_label = Label(frame1, textvariable=self.dice2, width = 1)
        dice2_roll_label.grid(row=1, column=3, sticky=W)
         
        #dice roll label 3----------------------------------------------------------------------------
        self.dice3 = IntVar()
        dice3_roll_label = Label(frame1, textvariable=self.dice3, width = 1)
        dice3_roll_label.grid(row=1, column=4, sticky=W)
         
        #dice roll label 4----------------------------------------------------------------------------
        self.dice4 = IntVar()
        dice4_roll_label = Label(frame1, textvariable=self.dice4, width = 1)
        dice4_roll_label.grid(row=1, column=5, sticky=W)
         
        #dice roll label 5----------------------------------------------------------------------------
        self.dice5 = IntVar()
        dice5_roll_label = Label(frame1, textvariable=self.dice5, width = 1)
        dice5_roll_label.grid(row=1, column=6, sticky=W)
        
        
        
        #hold label-----------------------------------------------------------------------------------
        hold_label = Label(frame1, text='Hold:')
        hold_label.grid(row=2, column=1, sticky=E)
        
        #hold checkbox for dice 1---------------------------------------------------------------------
        self.check_hold_dice1 = IntVar()
        hold_dice1 = Checkbutton(frame1, variable=self.check_hold_dice1)
        hold_dice1.grid(row=2, column=2, sticky=E)
        
        #hold checkbox for dice 2---------------------------------------------------------------------
        self.check_hold_dice2 = IntVar()
        hold_dice2 = Checkbutton(frame1, variable=self.check_hold_dice2)
        hold_dice2.grid(row=2, column=3, sticky=E)
        
        #hold checkbox for dice 3---------------------------------------------------------------------
        self.check_hold_dice3 = IntVar()
        hold_dice3 = Checkbutton(frame1, variable=self.check_hold_dice3)
        hold_dice3.grid(row=2, column=4, sticky=E)
        
        #hold checkbox for dice 4---------------------------------------------------------------------
        self.check_hold_dice4 = IntVar()
        hold_dice4 = Checkbutton(frame1, variable=self.check_hold_dice4)
        hold_dice4.grid(row=2, column=5, sticky=E)
        
        #hold checkbox for dice 5---------------------------------------------------------------------
        self.check_hold_dice5 = IntVar()
        hold_dice5 = Checkbutton(frame1, variable=self.check_hold_dice5)
        hold_dice5.grid(row=2, column=6, sticky=E)
        
        
        
        #label upper section of score card-------------------------------------------------------------
        upper_section_label = Label(frame2, text='UPPER SECTION:')
        upper_section_label.grid(row=3, column=1, sticky=W)
        
        
        
        #Aces button-----------------------------------------------------------------------------------
        self.aces_score_button = Button(frame2, text='Aces', command=self.score_aces, state=ACTIVE)
        self.aces_score_button.grid(row=4, column=1, sticky=E)
        
        #Twos button-----------------------------------------------------------------------------------
        self.twos_score_button = Button(frame2, text='Two\'s', command=self.score_twos, state=ACTIVE)
        self.twos_score_button.grid(row=4, column=2, sticky=W)
        
        #Threes button---------------------------------------------------------------------------------
        self.threes_score_button = Button(frame2, text='Three\'s', command=self.score_threes, state=ACTIVE)
        self.threes_score_button.grid(row=4, column=3, sticky=W)
    
        #Fours button----------------------------------------------------------------------------------
        self.fours_score_button = Button(frame2, text='Four\'s', command=self.score_fours, state=ACTIVE)
        self.fours_score_button.grid(row=4, column=4, sticky=W)    
    
        #Fives button----------------------------------------------------------------------------------
        self.fives_score_button = Button(frame2, text='Five\'s', command=self.score_fives, state=ACTIVE)
        self.fives_score_button.grid(row=4, column=5, sticky=W)
        
        #Sixes button----------------------------------------------------------------------------------
        self.sixes_score_button = Button(frame2, text='Sixes', command=self.score_sixes, state=ACTIVE)
        self.sixes_score_button.grid(row=4, column=6, sticky=W)
        
        
        
        #upper section total label---------------------------------------------------------------------
        upper_total_label = Label(frame2, text='Upper Total:')
        upper_total_label.grid(row=5, column=1, sticky=W)
        
        #display total of the upper---------------------------------------------------------------------
        self.u_score = IntVar()
        display_upper_score = Label(frame2, textvariable=self.u_score)
        display_upper_score.grid(row=5, column=2, sticky=W)
        
        #display bonus label if bonus is reached-------------------------------------------------------
        self.bonus = StringVar()
        bonus_label = Label(frame2, textvariable=self.bonus)
        bonus_label.grid(row=5, column=3, columnspan=2, sticky=W)
        
        
        
        #lower section label---------------------------------------------------------------------------
        lower_section_label = Label(frame3, text='LOWER SECTION:')
        lower_section_label.grid(row=6, column=1, sticky=W)
        
        
        
        #three of a kind button------------------------------------------------------------------------
        self.three_of_kind_button = Button(frame3, text='3 of a Kind', command=self.score_three_of_kind, state=ACTIVE)
        self.three_of_kind_button.grid(row=7, column=1, sticky=E)
        
        #four of a kind button-------------------------------------------------------------------------
        self.four_of_kind_button = Button(frame3, text='4 of a Kind', command=self.score_four_of_kind, state=ACTIVE)
        self.four_of_kind_button.grid(row=7, column=2, sticky=W)
        
        #full house button-----------------------------------------------------------------------------
        self.full_house_button = Button(frame3, text='Full House', command=self.score_full_house, state=ACTIVE)
        self.full_house_button.grid(row=7, column=3, sticky=W)
        
        #small straight button-------------------------------------------------------------------------
        self.small_straight_button = Button(frame3, text='Sm. Straight', command=self.score_small_straight, state=ACTIVE)
        self.small_straight_button.grid(row=7, column=4, sticky=W)
        
        #large straight button-------------------------------------------------------------------------
        self.large_straight_button = Button(frame3, text='Lg. Straight', command=self.score_large_straight, state=ACTIVE)
        self.large_straight_button.grid(row=7, column=5, sticky=W)
        
        #yahtzee button--------------------------------------------------------------------------------
        self.yahtzee_button = Button(frame3, text='Yahtzee', command=self.score_yahtzee, state=ACTIVE)
        self.yahtzee_button.grid(row=7, column=6, sticky=W)
        
        #chance button---------------------------------------------------------------------------------
        self.chance_button = Button(frame3, text='Chance', command = self.score_chance, state=ACTIVE)
        self.chance_button.grid(row=7, column=7, sticky=W)
        
        
        
        #lower section total label---------------------------------------------------------------------
        lower_total_label = Label(frame3, text='Lower Total:')
        lower_total_label.grid(row=8, column=1, sticky=W)
        
        #display total of the lower--------------------------------------------------------------------
        self.l_score = IntVar()
        display_lower_score = Label(frame3, textvariable=self.l_score)
        display_lower_score.grid(row=8, column=2, sticky=W)
        
        
        
        #total label-----------------------------------------------------------------------------------
        grand_total_label = Label(frame3, text='GRAND TOTAL:')
        grand_total_label.grid(row=9, column=1, sticky=W)
        
        #total label where score will be displayed
        self.grand_total = IntVar()
        grand_total_score_label = Label(frame3, textvariable=self.grand_total)
        grand_total_score_label.grid(row=9, column=2, sticky=W)
        
        
        #new game buttom-------------------------------------------------------------------------------
        new_game_button = Button(frame3, text='New Game', command = self.new_game)
        new_game_button.grid(row=10, column=1, sticky=W)
        
        #high score button-----------------------------------------------------------------------------
        highscore_button = Button(frame3, text='Highscore', command = self.display_highscore)
        highscore_button.grid(row=10, column=7, sticky=W)
         
        #highscore display-----------------------------------------------------------------------------
        self.high_score = IntVar()
        highscore_label = Label(frame3, textvariable=self.high_score)
        highscore_label.grid(row=10, column=8, sticky=W)
        
        
        
    def new_roll(self):
        '''roll the dice, and tell the yahtzee game which dice the user wants to hold'''
        hold_list =[0, 0, 0, 0, 0]
        if self.check_hold_dice1.get() == 1:
            hold_list[0] = 1
        if self.check_hold_dice2.get() == 1: 
            hold_list[1] = 1
        if self.check_hold_dice3.get() == 1:
            hold_list[2] = 1
        if self.check_hold_dice4.get() == 1:
            hold_list[3] = 1
        if self.check_hold_dice5.get() == 1:
            hold_list[4] = 1
        
        self._game.roll_dice(hold_list)
        
        dice_list = self._game.get_dice()
        self.dice1.set(dice_list[0])
        self.dice2.set(dice_list[1])
        self.dice3.set(dice_list[2])
        self.dice4.set(dice_list[3])
        self.dice5.set(dice_list[4])

        self.enable_unused_buttons()
    
    def score_aces(self):
        '''score the number of aces rolled'''
        self._game.count_dice(1)
        self.u_score.set(self._game.get_upper_total())
        self.grand_total.set(self._game.get_grand_total())
        
        self.pressed_buttons[0] = 1
        self.disable_all_buttons()
        self.bonus_display()
        self._game.reset_roll_count()
        self.reset_holds()
        self.empty_roll_slots()
        
    def score_twos(self):
        '''score the number of twos rolled'''
        self._game.count_dice(2)
        self.u_score.set(self._game.get_upper_total())
        self.grand_total.set(self._game.get_grand_total())
        
        self.pressed_buttons[1] = 1
        self.disable_all_buttons()
        self.bonus_display()
        self._game.reset_roll_count()
        self.reset_holds()
        self.empty_roll_slots()
        
    def score_threes(self):
        '''score the number of threes rolled'''
        self._game.count_dice(3)
        self.u_score.set(self._game.get_upper_total())
        self.grand_total.set(self._game.get_grand_total())
        
        self.pressed_buttons[2] = 1
        self.disable_all_buttons()
        self.bonus_display()
        self._game.reset_roll_count()
        self.reset_holds()
        self.empty_roll_slots()
        
    def score_fours(self):
        '''score the number of fours rolled'''
        self._game.count_dice(4)
        self.u_score.set(self._game.get_upper_total())
        self.grand_total.set(self._game.get_grand_total())
        
        self.pressed_buttons[3] = 1
        self.disable_all_buttons()
        self.bonus_display()        
        self._game.reset_roll_count()
        self.reset_holds()
        self.empty_roll_slots()
        
    def score_fives(self):
        '''score the number of fives rolled'''
        self._game.count_dice(5)
        self.u_score.set(self._game.get_upper_total())
        self.grand_total.set(self._game.get_grand_total())
        
        self.pressed_buttons[4] = 1
        self.disable_all_buttons()
        self.bonus_display()        
        self._game.reset_roll_count()
        self.reset_holds()
        self.empty_roll_slots()
        
    def score_sixes(self):
        '''score the number of sixes rolled'''
        self._game.count_dice(6)
        self.u_score.set(self._game.get_upper_total())
        self.grand_total.set(self._game.get_grand_total())
        
        self.pressed_buttons[5] = 1
        self.disable_all_buttons()
        self.bonus_display()
        self._game.reset_roll_count()
        self.reset_holds()
        self.empty_roll_slots()
        
        
    
    def score_three_of_kind(self):
        '''score a three of a kind'''
        self._game.count_three_of_Kind()
        self.l_score.set(self._game.get_lower_total())
        self.grand_total.set(self._game.get_grand_total())
        
        self.pressed_buttons[6] = 1
        self.disable_all_buttons()
        self._game.reset_roll_count()
        self.reset_holds()
        self.empty_roll_slots()
        
    def score_four_of_kind(self):
        '''score a four of a kind'''
        self._game.count_four_of_kind()
        self.l_score.set(self._game.get_lower_total())
        self.grand_total.set(self._game.get_grand_total())
        
        self.pressed_buttons[7] = 1
        self.disable_all_buttons()
        self._game.reset_roll_count()
        self.reset_holds()
        self.empty_roll_slots()
        
    def score_full_house(self):
        '''score a full house'''
        self._game.count_full_house()
        self.l_score.set(self._game.get_lower_total())
        self.grand_total.set(self._game.get_grand_total())
        
        self.pressed_buttons[8] = 1
        self.disable_all_buttons()
        self._game.reset_roll_count()
        self.reset_holds()
        self.empty_roll_slots()
        
    def score_small_straight(self):
        '''score a small straight'''
        self._game.count_small_straight()
        self.l_score.set(self._game.get_lower_total())
        self.grand_total.set(self._game.get_grand_total())
        
        self.pressed_buttons[9] = 1
        self.disable_all_buttons()
        self._game.reset_roll_count()
        self.reset_holds()
        self.empty_roll_slots()
        
    def score_large_straight(self):
        '''score a large straight'''
        self._game.count_large_straight()
        self.l_score.set(self._game.get_lower_total())
        self.grand_total.set(self._game.get_grand_total())
        
        self.pressed_buttons[10] = 1
        self.disable_all_buttons()
        self._game.reset_roll_count()
        self.reset_holds()
        self.empty_roll_slots()
        
    def score_yahtzee(self):
        '''score a yahtzee'''
        self._game.count_yahtzee()
        self.l_score.set(self._game.get_lower_total())
        self.grand_total.set(self._game.get_grand_total())
        
        self.pressed_buttons[11] = 1
        self.disable_all_buttons()
        self._game.reset_roll_count()
        self.reset_holds()
        self.empty_roll_slots()
    
    def score_chance(self):
        '''score a chance'''
        self._game.count_chance()
        self.l_score.set(self._game.get_lower_total())
        self.grand_total.set(self._game.get_grand_total())
        
        self.pressed_buttons[12] = 1
        self.disable_all_buttons()
        self._game.reset_roll_count()
        self.reset_holds()
        self.empty_roll_slots()
         
    
    
    def display_highscore(self):
        '''reveal the highest ever score when this button is pressed'''
        self._game.set_highscore()
        self.high_score.set(self._game.get_high_score())
    
    def bonus_display(self):
        '''display message to user telling them they got a bonus'''
        if self._game.get_upper_total() >= 63:
            self.bonus.set("+35 bonus!")
    
    def reset_holds(self):
        '''reset the check marks after the user score their dice so that all the dice will roll again'''
        self.check_hold_dice1.set(0)
        self.check_hold_dice2.set(0)
        self.check_hold_dice3.set(0)
        self.check_hold_dice4.set(0)
        self.check_hold_dice5.set(0)
        
    def empty_roll_slots(self):
        '''make the dice roll labels blank after user scores their dice, to let them know to roll again'''
        self.dice1.set('')
        self.dice2.set('')
        self.dice3.set('')
        self.dice4.set('')
        self.dice5.set('')
        
    def disable_all_buttons(self):
        '''disable buttons after users scores to force them to roll again'''
        self.aces_score_button.config(state=DISABLED)
        self.twos_score_button.config(state=DISABLED)
        self.threes_score_button.config(state=DISABLED)
        self.fours_score_button.config(state=DISABLED)
        self.fives_score_button.config(state=DISABLED)
        self.sixes_score_button.config(state=DISABLED)
        self.three_of_kind_button.config(state=DISABLED)
        self.four_of_kind_button.config(state=DISABLED)
        self.full_house_button.config(state=DISABLED)
        self.small_straight_button.config(state=DISABLED)
        self.large_straight_button.config(state=DISABLED)
        self.yahtzee_button.config(state=DISABLED)
        self.chance_button.config(state=DISABLED)
 
    def enable_unused_buttons(self):
        '''give the user back the buttons they still have to play in order to complete the game'''
        if self.pressed_buttons[0] == 0:
            self.aces_score_button.config(state=ACTIVE)
        if self.pressed_buttons[1] == 0:
            self.twos_score_button.config(state=ACTIVE)
        if self.pressed_buttons[2] == 0:
            self.threes_score_button.config(state=ACTIVE)
        if self.pressed_buttons[3] == 0:
            self.fours_score_button.config(state=ACTIVE)
        if self.pressed_buttons[4] == 0:
            self.fives_score_button.config(state=ACTIVE)
        if self.pressed_buttons[5] == 0:
            self.sixes_score_button.config(state=ACTIVE)
        if self.pressed_buttons[6] == 0:
            self.three_of_kind_button.config(state=ACTIVE)
        if self.pressed_buttons[7] == 0:
            self.four_of_kind_button.config(state=ACTIVE)
        if self.pressed_buttons[8] == 0:
            self.full_house_button.config(state=ACTIVE)
        if self.pressed_buttons[9] == 0:
            self.small_straight_button.config(state=ACTIVE)
        if self.pressed_buttons[10] == 0:
            self.large_straight_button.config(state=ACTIVE)
        if self._game.get_yahtzee_press() == 0:
            self.yahtzee_button.config(state=ACTIVE)
        if self.pressed_buttons[12] == 0:
            self.chance_button.config(state=ACTIVE)
            
    
    def new_game(self):
        '''reset internal data, make buttons usable again, and reset the roll labels'''   
        self.pressed_buttons = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self._game.reset_game()
        self.empty_roll_slots()
        self.reset_holds()
        self.bonus.set('')
        self.u_score.set('')
        self.l_score.set('')
        self.grand_total.set('')
        self.aces_score_button.config(state=ACTIVE)
        self.twos_score_button.config(state=ACTIVE)
        self.threes_score_button.config(state=ACTIVE)
        self.fours_score_button.config(state=ACTIVE)
        self.fives_score_button.config(state=ACTIVE)
        self.sixes_score_button.config(state=ACTIVE)
        self.three_of_kind_button.config(state=ACTIVE)
        self.four_of_kind_button.config(state=ACTIVE)
        self.full_house_button.config(state=ACTIVE)
        self.small_straight_button.config(state=ACTIVE)
        self.large_straight_button.config(state=ACTIVE)
        self.yahtzee_button.config(state=ACTIVE)
        self.chance_button.config(state=ACTIVE)
        
        
        
if __name__ == '__main__':
    root = Tk()
    root.title("Yahtzee")
    app = App(root)
    root.mainloop()