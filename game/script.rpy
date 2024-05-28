# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define A = Character("Antimony", image = "antimony")
define a = Character ("Aaliyah", image = "aaliyah")
define D = Character("Diana", image = "diana")
define d = Character("Devah", image = "devah")
define e = Character("Epoc", image = "epoc")
define H = Character("Handler", image = "handler")
define h = Character("Hex", image = "hex")
define n = Character("Nexus Alpha", image = "nexus_alpha")
define r = Character("Reefdancer", image = "reefdancer")
define w = Character("Wardog", image = "wardog")
define mc = Character("[name]")


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

    
    d concerned "Hey rookie!"

    mc "Who are you?"

    d "You think you're hot shit just because you're the new Hound?"

    menu:
        "Placate her.":
            jump choice_placate

        "Be Cocky":
            jump choice_cocky

    label choice_placate:
        $ placate = True

        mc "I just applied at the right time."

        hide devah neutral

        show devah cocky

        d "Yeah. Yeah that's right. Cause you're not better than me."

        jump choice_placateDone

    label choice_cocky:
        $ cocky = True

        mc "I mean yeah. I'm a Hound, and what are you?"

        hide devah neutral
        show devah angry

        d "About to break your nose."

        jump choice_cockyDone

    label choice_placateDone:
        "You catch the pilot giving you the stink eye for the rest of the day."

        return

    label choice_cockyDone:
        "You wake up in the infirmary with cotton in your nose."

        return
