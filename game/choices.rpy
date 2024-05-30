default choice_option = 0

label devah_choice_one:
    if choice_option == 1:
        hide d neutral
        d annoyed "Keep your pity. I’m not interested. I’m interested in that contract. And I’m not interested in sharing it with someone who can’t even stand up for themselves."
        $ choice_option = 0
        jump response

    elif choice_option == 2:
        hide d neutral
        d neutral "No. But it’s your responsibility now, buttercup. Own up to it, or fuck off."
        $ choice_option = 0
        jump response

    elif choice_option == 3:
        hide d neutral
        d angry "What the f– Yes it is! Who the fuck do you think you are?"
        $ choice_option = 0
        jump response

    else:
        hide d neutral
        d neutral "Yeah. Good. I’m glad you realize that. I’m here to do that job too, and I’m going to do it better than you."
        $ choice_option = 0
        jump response


