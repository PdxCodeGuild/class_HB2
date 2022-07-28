class Player:
    '''
    '   A class to represent each player
    '   Attributes: name and color
    '''

class Game:
    '''
    '   A connect four game object.
    '   Attributes: game board (7x6 2D nested list)
    '   Methods:
    '           get_height(position) returns int of how many pieces occupy a column
    '           move(player,position) adds a player token to a column after figuring out the current height of the column
    '           calc_winner(): returns True if four in a row are found
    '           is_full(): returns true if all board positions are occupied
    '           is_game_over(): returns true if the game is over (a winnder is found or the board is full)
    '           play_turn(): function that plays one turn
    '           play(): function that plays whole game, given two player
    '           recursive_chip_checker(): recurisvely checks in all directions to find if theres a connect 4
    '''

if __name__ == '__main__':
    # if this module is run directly, this code will run
    # if the module is imported into another, it won't run

    game = Game()
    with open('1 Python/docs/class_code_examples/connect-four-moves.txt', 'r') as moves:

        for move_num, line in enumerate(moves):
            print(line)
            col_to_play = int(line.strip()) - 1
            player = 'Y' if move_num % 2 != 0 else 'R'
            game.play_turn(player, col_to_play)
            # OPTIONAL/BONUS: print board after each turn
            game.is_game_over() # could be called w/in play_turn, or in a different order

