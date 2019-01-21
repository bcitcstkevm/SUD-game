"""
SUD Game- COMP 1510 Assignment 1
"""

# Kevin Mark
# A01067248
# November 09, 2018

# imports
from character import Char
from game import Game


def main():
    # initialize
    player_1 = Char()
    new_game = Game(player_1)
    new_game.set_player_name()

    # Game starts here

    ascii_art = """                                 #,,             &.                            
                                 ,((.(((((((((#%&%#                            
                                 &&((,#((#((((((###%                           
                                %%#%(((.&%%#((%######*                         
                 ((#%.         (%#%%&@&&%%&&%/*.*#####& #,                     
                 %(((((((#%    %%%%% .. %.... /*****..,.,                      
                 #(((((((((((%%&&&%%.  #######****/*(****                      
                &%%%%%%%%%&&%&&@&&&*/(((#@#@@#,*.*///*/.                     
               #%%%#%%%%((%%&%% %&&&&@**///**@(,@(**///(,*                     
              *%#%#(((((%&&%%& *..,/(&%@**,,,,*&*%#/(/((#                      
         ./%#(((((((((%%#((#.    .#(#@ #% .,,,,*@/&&/((/                       
./%%((((((((((((((((#(((((.  ( . .%*(&,/#, .**/(,&(/%(*                        
#%%%%%%%%*,(&&%(((((((((#   #.. .*%*/%&@#%  *(###(,,                           
%%%%%%#               # *# ....***%/*#&%&   (/**                             
#%%%%%.              #.....,,****/%((#%%&%&@%...(                              
%%%%%%*          #...,,*****,(,*#%(%#%%#%%& ((                               
%%%%%%#   *#,  .,****////((/*   ###%%%%&%%&&&&&                                
%%%#%%%*.,**    ,(#((**&/*       ./&%%%%%%%%%@.* ,(                          
%%###/, /(*    **#(%(((/#&(((/(,.,,*//#%%&&%%##&////(.                         
%##%. ..      ,*#/./.,(//@@&/ ,(%%%%#//(((((((%##*(((%(&*                      
##%,,. ((((#  ..#*#(%(//(@ /*        &%%.((/ .*##/,. (#,.((%,  """

    print(ascii_art)
    print("Welcome to PCR's SUD")
    new_game.print_scenario()
    print('You can move by typing north, south, east, or west. Type "quit" anytime to exit and save')

    new_game.game_loop()

    print("Thank you for playing PCR's SUD. Credit for game story goes to games Overwatch and Runescape")


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
