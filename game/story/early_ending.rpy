label calculate_early_ending:

    if spooks_encountered == 0:
        call party_ending

    else:
        call getting_lost

    return


label party_ending:

    scene bg stacy with dissolve

    "You finally arive at Stacy's house."

    "It is full of people and covered in halloween decorations."

    show bianca normal at left3
    with dissolve
    show bradley normal at right3
    with dissolve

    by "We made it. Time to have some fun."

    b "Yeah"

    show tyrone normal at center3
    with dissolve

    t "Oh yeah! Time for some party!"
    t "Go Butchers!"
    
    hide tyrone normal with dissolve
    
    "Tyrone rushes forward"

    show robert normal at center3
    with dissolve

    r "It was nice to walk with you nerds."
    t "Where is my keg?"
    r "Shit. I'm coming!"

    hide robert normal with dissolve
    
    "Robert joins Tyrone"

    show helen normal at center3
    with dissolve

    h "Yeah. It was nice talk to you guys. Time for some fun right?"

    by "Yeah"

    hide helen normal with dissolve

    "She heads into house."

    by "I guess we have finally some time to chill out."

    b "Oh yeah. Thats the thing I need the most. Lets go!"

    hide bradley normal with dissolve

    "You look around and you see a cat you saw earlier. It pays no attention to you."

    b "You're the chill one cat!"

    b "Hey Bradley! Wait!"

    hide bianca normal with dissolve

    "You spend rest of the night partying with only thing you have to worry about being an tomorrow's hangover."

    "But that's something future Bianca should worry about."

    "The End."


    return