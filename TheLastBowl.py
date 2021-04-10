# Program bowling

# Declare constants
NUMBER_OF_FRAMES = 10
NUMBER_OF_PINS = 10

# Declare Variable types (EVERY variable used)
frame_1_ball_1 = int()
frame_1_ball_2 = int()
frame_2_ball_1 = int()
frame_2_ball_2 = int()
frame_3_ball_1 = int()
frame_3_ball_2 = int()
frame_4_ball_1 = int()
frame_4_ball_2 = int()
frame_5_ball_1 = int()
frame_5_ball_2 = int()
frame_6_ball_1 = int()
frame_6_ball_2 = int()
frame_7_ball_1 = int()
frame_7_ball_2 = int()
frame_8_ball_1 = int()
frame_8_ball_2 = int()
frame_9_ball_1 = int()
frame_9_ball_2 = int()
frame_10_ball_1 = int()
frame_10_ball_2 = int()

frameTotal = int()
gameTotal = int()
frameNumber = int()
pins = int()
ball_1 = int()
ball_2 = int()

prompt = str()

frame_1_ball_1 = 0
frame_1_ball_2 = 0
frame_2_ball_1 = 0
frame_2_ball_2 = 0
frame_3_ball_1 = 0
frame_3_ball_2 = 0
frame_4_ball_1 = 0
frame_4_ball_2 = 0
frame_5_ball_1 = 0
frame_5_ball_2 = 0
frame_6_ball_1 = 0
frame_6_ball_2 = 0
frame_7_ball_1 = 0
frame_7_ball_2 = 0
frame_8_ball_1 = 0
frame_8_ball_2 = 0
frame_9_ball_1 = 0
frame_9_ball_2 = 0
frame_10_ball_1 = 0
frame_10_ball_2 = 0

frameTotal = 0
gameTotal = 0
frameNumber = 0

for frame in range( NUMBER_OF_FRAMES ):

    pins = NUMBER_OF_PINS
    ball_1 = 0
    ball_2 = 0
    frameNumber = frame + 1
    print( "Frame", frameNumber, "Game Total: ", gameTotal )

    # first ball: be sure it's a valid number of pins
    prompt = "Ball 1"
    prompt += " (this ball must be between 0 and " + str( pins ) + ": "
    ball_1 = int( input( prompt ) )
    while ( (ball_1 > pins) or (ball_1 < 0) ):
        ball_1 = int( input( prompt ) )
    #} while
        
    pins -= ball_1

    # there's no second ball if all pins have been knocked down
    if (pins > 0):
        
        # first ball: be sure it's a valid number of pins
        prompt = "Ball 2"
        prompt += " (this ball must be between 0 and " + str( pins ) + ": "
        ball_2 = int( input( prompt ) )
        while ( (ball_2 > pins) or (ball_2 < 0)
                and ( ( ball_1 + ball_2 ) > NUMBER_OF_PINS ) ):
            ball_2 = int( input( prompt ) )
        #} while
                
        pins -= ball_2

    else:
        ball_2 = 0
        
    #} if

    frameTotal = ball_1 + ball_2

    if ( ball_1 == NUMBER_OF_PINS ):
        print( "*** you got a STRIKE!" )
        
    elif( frameTotal == NUMBER_OF_PINS ):
        print( "*** you got a SPARE!" )
        
    else:
        print( ".... too bad, open frame" )
        
    #} if
    
    # Update the total game score
    gameTotal += frameTotal

    # assign the ball scores to the frame variables for printing at the end
    if (frameNumber == 1):
        frame_1_ball_1 = ball_1
        frame_1_ball_2 = ball_2

    elif (frameNumber == 2):
        frame_2_ball_1 = ball_1
        frame_2_ball_2 = ball_2

    elif (frameNumber == 3):
        frame_3_ball_1 = ball_1
        frame_3_ball_2 = ball_2

    elif (frameNumber == 4):
        frame_4_ball_1 = ball_1
        frame_4_ball_2 = ball_2

    elif (frameNumber == 5):
        frame_5_ball_1 = ball_1
        frame_5_ball_2 = ball_2

    elif (frameNumber == 6):
        frame_6_ball_1 = ball_1
        frame_6_ball_2 = ball_2

    elif (frameNumber == 7):
        frame_7_ball_1 = ball_1
        frame_7_ball_2 = ball_2

    elif (frameNumber == 8):
        frame_8_ball_1 = ball_1
        frame_8_ball_2 = ball_2

    elif (frameNumber == 9):
        frame_9_ball_1 = ball_1
        frame_9_ball_2 = ball_2

    elif (frameNumber == 10):
        frame_10_ball_1 = ball_1
        frame_10_ball_2 = ball_2
    else:
        print( "Can't Happen" )
    #} if

#} for
        
# Print the header line.
print( format( "Frame", ">5" ),
       format( "Ball 1", ">7" ), format( "Ball 2", ">7" ),
       format( "Frame Total", ">12" ), format( "Game Total", ">12" ) )

frameTotal = 0
gameTotal = 0

# Print all the frame scores
for frame in range( NUMBER_OF_FRAMES ):
    
    frameNumber = frame + 1
    
    # assign the ball scores to the frame variables for printing at the end
    if (frameNumber == 1):
        ball_1 = frame_1_ball_1
        ball_2 = frame_1_ball_2

    elif (frameNumber == 2):
        ball_1 = frame_2_ball_1
        ball_2 = frame_2_ball_2

    elif (frameNumber == 3):
        ball_1 = frame_3_ball_1
        ball_2 = frame_3_ball_2

    elif (frameNumber == 4):
        ball_1 = frame_4_ball_1
        ball_2 = frame_4_ball_2

    elif (frameNumber == 5):
        ball_1 = frame_5_ball_1
        ball_2 = frame_5_ball_2

    elif (frameNumber == 6):
        ball_1 = frame_6_ball_1
        ball_2 = frame_6_ball_2

    elif (frameNumber == 7):
        ball_1 = frame_7_ball_1
        ball_2 = frame_7_ball_2

    elif (frameNumber == 8):
        ball_1 = frame_8_ball_1
        ball_2 = frame_8_ball_2

    elif (frameNumber == 9):
        ball_1 = frame_9_ball_1
        ball_2 = frame_9_ball_2

    elif (frameNumber == 10):
        ball_1 = frame_10_ball_1
        ball_2 = frame_10_ball_2
    else:
        print( "Can't Happen" )
    #} if

    frameNumber = frame + 1
    frameTotal = ball_1 + ball_2
    gameTotal += frameTotal

    print( format( frameNumber, ">5" ),
           format( ball_1, ">7" ), format( ball_2, ">7" ),
           format( frameTotal, ">12" ), format( gameTotal, ">12" ) )

#} for

# Print the final score in a nice, friendly way.
print( "Your final score is: ", gameTotal )
print( "Hope you enjoyed yourself.  Come back soon." )

# End Program
