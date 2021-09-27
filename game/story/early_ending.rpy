label calculate_early_ending:

    if spooks_encountered == 0:
        call party_ending

    else:
        call getting_lost

    return


label party_ending:

    "You arive at Stacy's house"

    "The end"

    return