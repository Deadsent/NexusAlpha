# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.

label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg hanger

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    q "Hey you!"

    "You hear a voice behind you. It’s clear, rung like a bell in an empty workshop. Angry, too. You turn to see a woman wearing a flight suit and a scowl that could strip the paint off a frame."
    d annoyed "You're the new recruit, right?"

    menu:
        "Obviously.":
            y "Uh, yeah?"
            $ devah_affection += 1

        "Well that's a suspicious way to introduce yourself.":
            y "Who's asking?"

        "Quick! Feign ignorance!":
            y "Who?"
            $ devah_affection -= 1

        "Oh. Pretty lady!":
            y "Woah. Hi."

    d annoyed "Oh for the love of..."

    "A sudden surge of realization. The chevrons on her shoulder. The flight suit. The fact that she’s wearing a name tag. This is Devah, known by her fellow Cat contractors as Angel."
    
    "She was supposed to be next in line for a Hound contract. But now you have one and she doesn’t. She knows you know. You can see it in her eyes. She’s firing a professional-level glare right at you."

    d annoyed "I had something good here before you showed up. Prospects."

    show d neutral at left
    menu:
        "Empathize.":
            y "I'm sorry."
            $ devah_affection -= 1
            $ choice_option = 1
            jump devah_choice_one
            
        "Hey! Why is she going off at you?!":
            y "That's not my fault!"
            $ choice_option = 2
            jump devah_choice_one

        "Dig deeper.":
            y "This isn’t about the contract, is it?"
            $ devah_affection -= 1
            $ choice_option = 3
            jump devah_choice_one

        "That's capitalism, baby!":
            y "I'm just here to do my job."
            $ devah_affection += 1
            $ choice_option = 4
            jump devah_choice_one

label response:
    d annoyed "Don't you dare get too comfortable in that cockpit."

    "She leans in close. She’s not all that much taller than you but she moves like she’s thirty feet tall. Consequences of being a pilot probably. It’s hard to tell. It’s hard to tell because she’s really close and her face is right up in yours and...{i}oh god oh man oh jeez{/i}"

    d angry "I’m going to fight for what’s mine, you hear me? If you can’t prove you’re worthy of the contract, I’m going to do it for you and nobody’s even going to remember your name."

    "Her voice is a low growl. For a Cat, she’s definitely got the whole canine thing down. You swallow and she backs off."

    d neutral "Just in case, though, what is your name?"

    python:
        name = renpy.input("What is your name?")
        name = name.strip() or "Amara"

    mc "It's [name]."
#    menu:
#        "Hit The Gym":
#            jump workout
#        "Train In The Simulations":
#            jump simulations
#        "Study":
#            jump study
        
    return
