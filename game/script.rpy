# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.

label start:
    python:
        name = renpy.input("What is your name?")
        name = name.strip() or "Amara"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg hanger

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    menu:
        "Hit The Gym":
            jump workout
        "Train In The Simulations":
            jump simulations
        "Study":
            jump study
        
    return
