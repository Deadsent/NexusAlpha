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

default mc_piloting = 1
default mc_physique = 1
default mc_shooting = 1
default mc_wit = 1
default mc_charm = 1

default mc_piloting_counter = 0
default mc_physique_counter = 0
default mc_shooting_counter = 0
default mc_wit_counter = 0
default mc_charm_counter = 0

default antimony_affection = 0
default aaliyah_affection = 0
default devah_affection = 0
default diana_affection = 0
default epoc_affection = 0
default hex_affection = 0
default nexusAlpha_affection = 0

label workout:
    if mc_physique_counter < 4:
        $ mc_physique_counter += 1
        "You got in a good workout"
        return
    else:
        $ mc_physique_counter = 0
        $ mc_physique += 1
        "Your physique is now [mc_physique]!"
        return

label simulations:
    if mc_piloting_counter < 4:
        $ mc_piloting_counter += 1
        "You practiced hard!"
        return
    else:
        $ mc_piloting_counter = 0
        $ mc_piloting += 1
        "Your piloting is now [mc_piloting]!"
        return

label study:
    if mc_wit_counter < 4:
        $ mc_wit_counter += 1
        "You studied hard!"
        return
    else:
        $ mc_wit_counter = 0
        $ mc_wit += 1
        "Your wit is now [mc_wit]!"
        return

label range:
    if mc_shooting_counter < 4:
        $ mc_shooting_counter += 1
        "You practiced hard!"
        return
    else:
        $ mc_shooting_counter = 0
        $ mc_shooting += 1
        "Your shooting is now [mc_shooting]!"
        return