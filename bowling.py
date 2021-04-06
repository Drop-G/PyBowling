ball_1 = 0
ball_2 = 0
ball_3 = 0
ball_4 = 0
ball_5 = 0
ball_6 = 0
ball_7 = 0
ball_8 = 0
ball_9 = 0
ball_10 = 0
ball_11 = 0
ball_12 = 0
ball_13 = 0
ball_14 = 0
ball_15 = 0
ball_16 = 0
ball_17 = 0
ball_18 = 0
ball_19 = 0
ball_20 = 0




frame_counter = 0
num_pins = 0
num_frames = int()
user_name = str()
PINS = 0
SCORE_TOTAL = 0
FRAMES = 0

FRAME_1 = 0
FRAME_2 = 0
FRAME_3 = 0
FRAME_4 = 0
FRAME_5 = 0
FRAME_6 = 0
FRAME_7 = 0
FRAME_8 = 0
FRAME_9 = 0
FRAME_10 = 0

SCORE_TOTAL_ONE = 0
SCORE_TOTAL_TWO = 0
SCORE_TOTAL_THREE = 0
SCORE_TOTAL_FOUR = 0
SCORE_TOTAL_FIVE = 0
SCORE_TOTAL_SIX = 0
SCORE_TOTAL_SEVEN = 0
SCORE_TOTAL_Eight = 0
SCORE_TOTAL_NINE = 0
SCORE_TOTAL_TEN = 0





#  - - - - - - - - - - -


# Greet
print("\nHello, there! We're about to start bowling.\n")
user_name = input("First, let's add your name to the score board!\
 type your first\nname and then hit enter! ")

# Game set-up
game_type = input('What game are we playing?\n Type "Nine" for [Nine-Pins]\
Type "Ten" for [10-Pins] ')
if ( game_type == 'nine'.lower() ) or ( game_type == '9' ):
    PINS = 9
    FRAMES = 7
elif ( game_type == 'ten'.lower() ) or ( game_type == '10' ):
    PINS = 10
    FRAMES = 11
elif ( (game_type != '9') or (game_type != 'nine') ) or ( (game_type != '10') or (game_type != 'ten') ):
    print("Something went wrong. Please choose which game you'd like to play")
    game_type = input('What game are we playing?\n Type "Nine" for [Nine-Pins]\
    Type "Ten" for [10-Pins] ')


if (PINS == 9) or (PINS == 10):
# 1
    while FRAME_1 == 0:
        print('\t**FRAME ONE**')
        ball_1 = int( input('How many pins were knocked down? ') )
        while ( ball_1 < 0 ) or ( ball_1 > PINS ):
            print('That is an invalid value.')
            ball_1 = int(input('Enter a positive nonzero number: '))
        if ball_1 == PINS:
            print(f'Wow, { user_name }! You got a STRIKE!')
            FRAME_1 = ball_1
        elif ball_1 != PINS:
            num_pins = ( PINS - ball_1 )
            print(f'Way to go! There are { num_pins } pins left')

            ball_2 = int( input('How many pins were knocked down? ') )
            while ( ball_2 < 0 ) or ( ball_2 > num_pins ):
                print( 'That is an invalid value.' )
                ball_2 = int( input( 'Enter a positive nonzero number: ' ))
        elif ( ball_1 == 0 ) and ( ball_2 == 0 ):
            print( f'Too bad, { user_name }, open frame.' )
        elif FRAME_1 == PINS:
            FRAME_1 = ( ball_1 + ball_2 )
            print(f'Wow, { user_name }! You got a SPARE!')

        FRAME_1 = (ball_1 + ball_2)
        SCORE_TOTAL_ONE = SCORE_TOTAL_ONE + FRAME_1
        print(f'Your score for this frame is { FRAME_1 }')
# 2
    while FRAME_2 == 0:
        print('\t**FRAME TWO**')
        ball_3 = int( input('How many pins were knocked down? ') )
        while ( ball_3 < 0 ) or ( ball_3 > PINS ):
            print('That is an invalid value.')
            ball_3 = int(input('Enter a positive nonzero number: '))
        if ball_3 == PINS:
            print(f'Wow, { user_name }! You got a STRIKE!')
            FRAME_2 = ball_3
        elif ball_3 != PINS:
            num_pins = ( PINS - ball_3 )
            print(f'Way to go! There are { num_pins } pins left')
            ball_4 = int( input('How many pins were knocked down? ') )
            while ( ball_4 < 0 ) or ( ball_4 > num_pins ):
                print( 'That is an invalid value.' )
                ball_4 = int( input( 'Enter a positive nonzero number: ' ))
        elif ( ball_4 == 0 ) and ( ball_4 == 0 ):
            print( f'Too bad, { user_name }, open frame.' )
        elif FRAME_2 == PINS:
            FRAME_2 = ( ball_3 + ball_4 )
            print(f'Wow, { user_name }! You got a SPARE!')

        FRAME_2 = (ball_3 + ball_4)
        SCORE_TOTAL_TWO = SCORE_TOTAL_ONE + FRAME_2
        print(f'Your score for this frame is { FRAME_2 }')

# 3
    while FRAME_3 == 0:
        print('\t**FRAME THREE**')
        ball_5 = int( input('How many pins were knocked down? ') )
        while ( ball_5 < 0 ) or ( ball_5 > PINS ):
            print('That is an invalid value.')
            ball_5 = int(input('Enter a positive nonzero number: '))
        if ball_5 == PINS:
            print(f'Wow, { user_name }! You got a STRIKE!')
            FRAME_3 = ball_5
        elif ball_5 != PINS:
            num_pins = ( PINS - ball_5 )
            print(f'Way to go! There are { num_pins } pins left')
            ball_6 = int( input('How many pins were knocked down? ') )
            while ( ball_6 < 0 ) or ( ball_6 > num_pins ):
                print( 'That is an invalid value.' )
                ball_6 = int( input( 'Enter a positive nonzero number: ' ))
        elif ( ball_6 == 0 ) and ( ball_6 == 0 ):
            print( f'Too bad, { user_name }, open frame.' )
        elif FRAME_3 == PINS:
            FRAME_3 = ( ball_5 + ball_6 )
            print(f'Wow, { user_name }! You got a SPARE!')

        FRAME_3 = (ball_5 + ball_6)
        SCORE_TOTAL_THREE = SCORE_TOTAL_TWO + FRAME_3
        print(f'Your score for this frame is { FRAME_3 }')
#4
    while FRAME_4 == 0:
        print('\t**FRAME FOUR**')
        ball_7 = int( input('How many pins were knocked down? ') )
        while ( ball_7 < 0 ) or ( ball_7 > PINS ):
            print('That is an invalid value.')
            ball_7 = int(input('Enter a positive nonzero number: '))
        if ball_7 == PINS:
            print(f'Wow, { user_name }! You got a STRIKE!')
            FRAME_4 = ball_7
        elif ball_7 != PINS:
            num_pins = ( PINS - ball_5 )
            print(f'Way to go! There are { num_pins } pins left')
            ball_8 = int( input('How many pins were knocked down? ') )
            while ( ball_8 < 0 ) or ( ball_8 > num_pins ):
                print( 'That is an invalid value.' )
                ball_8 = int( input( 'Enter a positive nonzero number: ' ))
        elif ( ball_8 == 0 ) and ( ball_8 == 0 ):
            print( f'Too bad, { user_name }, open frame.' )
        elif FRAME_4 == PINS:
            FRAME_4 = ( ball_7 + ball_8 )
            print(f'Wow, { user_name }! You got a SPARE!')

        FRAME_4 = (ball_7 + ball_8)
        SCORE_TOTAL_FOUR = SCORE_TOTAL_THREE + FRAME_4
        print(f'Your score for this frame is { FRAME_4 }')
# 5
    while FRAME_5 == 0:
        print('\t**FRAME FIVE**')
        ball_9 = int( input('How many pins were knocked down? ') )
        while ( ball_9 < 0 ) or ( ball_9 > PINS ):
            print('That is an invalid value.')
            ball_9 = int(input('Enter a positive nonzero number: '))
        if ball_9 == PINS:
            print(f'Wow, { user_name }! You got a STRIKE!')
            FRAME_5 = ball_9
        elif ball_9 != PINS:
            num_pins = ( PINS - ball_9 )
            print(f'Way to go! There are { num_pins } pins left')
            ball_10 = int( input('How many pins were knocked down? ') )
            while ( ball_10 < 0 ) or ( ball_10 > num_pins ):
                print( 'That is an invalid value.' )
                ball_10 = int( input( 'Enter a positive nonzero number: ' ))
        elif ( ball_10 == 0 ) and ( ball_10 == 0 ):
            print( f'Too bad, { user_name }, open frame.' )
        elif FRAME_5 == PINS:
            FRAME_5 = ( ball_9 + ball_10 )
            print(f'Wow, { user_name }! You got a SPARE!')

        FRAME_5 = (ball_9 + ball_10)
        SCORE_TOTAL_FIVE = SCORE_TOTAL_FOUR + FRAME_5
        print(f'Your score for this frame is { FRAME_5 }')
# 6
    while FRAME_6 == 0:
        print('\t**FRAME SIX**')
        ball_11 = int( input('How many pins were knocked down? ') )
        while ( ball_11 < 0 ) or ( ball_11 > PINS ):
            print('That is an invalid value.')
            ball_11 = int(input('Enter a positive nonzero number: '))
        if ball_11 == PINS:
            print(f'Wow, { user_name }! You got a STRIKE!')
            FRAME_11 = ball_11
        elif ball_11 != PINS:
            num_pins = ( PINS - ball_11 )
            print(f'Way to go! There are { num_pins } pins left')
            ball_12 = int( input('How many pins were knocked down? ') )
            while ( ball_12 < 0 ) or ( ball_12 > num_pins ):
                print( 'That is an invalid value.' )
                ball_12 = int( input( 'Enter a positive nonzero number: ' ))
        elif ( ball_12 == 0 ) and ( ball_12 == 0 ):
            print( f'Too bad, { user_name }, open frame.' )
        elif FRAME_6 == PINS:
            FRAME_6 = ( ball_11 + ball_12 )
            print(f'Wow, { user_name }! You got a SPARE!')

        FRAME_6 = (ball_11 + ball_12)
        SCORE_TOTAL_SIX = SCORE_TOTAL_FIVE + FRAME_6
        print(f'Your score for this frame is { FRAME_6 }')

if PINS == 10:
# 7
    while FRAME_7 == 0:
        print('\t**FRAME SEVEN**')
        ball_13 = int( input('How many pins were knocked down? ') )
        while ( ball_13 < 0 ) or ( ball_13 > PINS ):
            print('That is an invalid value.')
            ball_13 = int(input('Enter a positive nonzero number: '))
        if ball_13 == PINS:
            print(f'Wow, { user_name }! You got a STRIKE!')
            FRAME_13 = ball_13
        elif ball_13 != PINS:
            num_pins = ( PINS - ball_13 )
            print(f'Way to go! There are { num_pins } pins left')
            ball_14 = int( input('How many pins were knocked down? ') )
            while ( ball_14 < 0 ) or ( ball_14 > num_pins ):
                print( 'That is an invalid value.' )
                ball_14 = int( input( 'Enter a positive nonzero number: ' ))
        elif ( ball_14 == 0 ) and ( ball_14 == 0 ):
            print( f'Too bad, { user_name }, open frame.' )
        elif FRAME_7 == PINS:
            FRAME_7 = ( ball_13 + ball_14 )
            print(f'Wow, { user_name }! You got a SPARE!')

        FRAME_7 = (ball_13 + ball_14)
        SCORE_TOTAL_SEVEN = SCORE_TOTAL_SIX + FRAME_7
        print(f'Your score for this frame is { FRAME_7 }')

# 8
    while FRAME_8 == 0:
        print('\t**FRAME EIGHT**')
        ball_15 = int( input('How many pins were knocked down? ') )
        while ( ball_15 < 0 ) or ( ball_15 > PINS ):
            print('That is an invalid value.')
            ball_15 = int(input('Enter a positive nonzero number: '))
        if ball_15 == PINS:
            print(f'Wow, { user_name }! You got a STRIKE!')
            FRAME_8 = ball_15
        elif ball_15 != PINS:
            num_pins = ( PINS - ball_15 )
            print(f'Way to go! There are { num_pins } pins left')
            ball_16 = int( input('How many pins were knocked down? ') )
            while ( ball_16 < 0 ) or ( ball_16 > num_pins ):
                print( 'That is an invalid value.' )
                ball_16 = int( input( 'Enter a positive nonzero number: ' ))
        elif ( ball_16 == 0 ) and ( ball_16 == 0 ):
            print( f'Too bad, { user_name }, open frame.' )
        elif FRAME_8 == PINS:
            FRAME_8 = ( ball_15 + ball_16 )
            print(f'Wow, { user_name }! You got a SPARE!')

        FRAME_8 = (ball_15 + ball_16)
        SCORE_TOTAL_EIGHT = SCORE_TOTAL_SEVEN + FRAME_8
        print(f'Your score for this frame is { FRAME_8 }')
# 9
    while FRAME_9 == 0:
        print('\t**FRAME NINE**')
        ball_17 = int( input('How many pins were knocked down? ') )
        while ( ball_17 < 0 ) or ( ball_17 > PINS ):
            print('That is an invalid value.')
            ball_17 = int(input('Enter a positive nonzero number: '))
        if ball_17 == PINS:
            print(f'Wow, { user_name }! You got a STRIKE!')
            FRAME_17 = ball_17
        elif ball_17 != PINS:
            num_pins = ( PINS - ball_17 )
            print(f'Way to go! There are { num_pins } pins left')
            ball_18 = int( input('How many pins were knocked down? ') )
            while ( ball_18 < 0 ) or ( ball_18 > num_pins ):
                print( 'That is an invalid value.' )
                ball_18 = int( input( 'Enter a positive nonzero number: ' ))
        elif ( ball_18 == 0 ) and ( ball_18 == 0 ):
            print( f'Too bad, { user_name }, open frame.' )
        elif FRAME_9 == PINS:
            FRAME_9 = ( ball_17 + ball_18 )
            print(f'Wow, { user_name }! You got a SPARE!')

        FRAME_9 = (ball_17 + ball_18)
        SCORE_TOTAL_NINE = SCORE_TOTAL_EIGHT + FRAME_9
        print(f'Your score for this frame is { FRAME_9 }')
# 10
    while FRAME_10 == 0:
        print('\t**FRAME TEN**')
        ball_19 = int( input('How many pins were knocked down? ') )
        while ( ball_19 < 0 ) or ( ball_19 > PINS ):
            print('That is an invalid value.')
            ball_19 = int(input('Enter a positive nonzero number: '))
        if ball_19 == PINS:
            print(f'Wow, { user_name }! You got a STRIKE!')
            FRAME_10 = ball_19
        elif ball_10 != PINS:
            num_pins = ( PINS - ball_19 )
            print(f'Way to go! There are { num_pins } pins left')
            ball_20 = int( input('How many pins were knocked down? ') )
            while ( ball_20 < 0 ) or ( ball_20 > num_pins ):
                print( 'That is an invalid value.' )
                ball_20 = int( input( 'Enter a positive nonzero number: ' ))
        elif ( ball_20 == 0 ) and ( ball_20 == 0 ):
            print( f'Too bad, { user_name }, open frame.' )
        elif FRAME_10 == PINS:
            FRAME_10 = ( ball_19 + ball_20 )
            print(f'Wow, { user_name }! You got a SPARE!')

        FRAME_10 = (ball_19 + ball_20)
        SCORE_TOTAL_TEN = SCORE_TOTAL_NINE + FRAME_10
        print(f'Your score for this frame is { FRAME_2 }')

if PINS == 9:
    game_summary = print(f'GAME SCORE\tFRAME\tBALL 1\tBALL 2\tFRAME TOTAL\n\
        {SCORE_TOTAL_ONE}\t  {1}\t  {ball_1}\t  {ball_2}\t     {FRAME_1}\n\
        {SCORE_TOTAL_TWO}\t  {2}\t  {ball_3}\t  {ball_4}\t     {FRAME_2}\n\
        {SCORE_TOTAL_THREE}\t  {3}\t  {ball_5}\t  {ball_6}\t     {FRAME_3}\n\
        {SCORE_TOTAL_FOUR}\t  {4}\t  {ball_7}\t  {ball_8}\t     {FRAME_4}\n\
        {SCORE_TOTAL_FIVE}\t  {5}\t  {ball_9}\t  {ball_10}\t     {FRAME_5}\n\
        {SCORE_TOTAL_SIX}\t  {6}\t  {ball_11}\t  {ball_12}\t     {FRAME_6}\n')
elif PINS == 10:
    game_summary = print(f'GAME SCORE\tFRAME\tBALL 1\tBALL 2\tFRAME TOTAL\n\
        {SCORE_TOTAL_ONE}\t  {1}\t  {ball_1}\t  {ball_2}\t     {FRAME_1}\n\
        {SCORE_TOTAL_TWO}\t  {2}\t  {ball_3}\t  {ball_4}\t     {FRAME_2}\n\
        {SCORE_TOTAL_THREE}\t  {3}\t  {ball_5}\t  {ball_6}\t     {FRAME_3}\n\
        {SCORE_TOTAL_FOUR}\t  {4}\t  {ball_7}\t  {ball_8}\t     {FRAME_4}\n\
        {SCORE_TOTAL_FIVE}\t  {5}\t  {ball_9}\t  {ball_10}\t     {FRAME_5}\n\
        {SCORE_TOTAL_SIX}\t  {6}\t  {ball_11}\t  {ball_12}\t     {FRAME_6}\n\
        {SCORE_TOTAL_SEVEN}\t  {7}\t  {ball_13}\t  {ball_14}\t     {FRAME_7}\n\
        {SCORE_TOTAL_EIGHT}\t  {8}\t  {ball_15}\t  {ball_16}\t     {FRAME_8}\n\
        {SCORE_TOTAL_NINE}\t  {9}\t  {ball_17}\t  {ball_18}\t     {FRAME_9}\n\
        {SCORE_TOTAL_TEN}\t  {10}\t  {ball_19}\t  {ball_20}\t     {FRAME_10}\n')