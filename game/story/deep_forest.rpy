label trap_field:

    "Bradley leeds the way and in spite of being lost, he seems confident about direction he was going."

    "It seems that will to get out of the forest really kicked in."

    "You catch up to him."

    show bradley normal at right2
    with dissolve

    show bianca normal at left2
    with dissolve

    b "Are you ok?"

    by "It depends."

    by "Not gonna lie, getting lost was not something I had planned for today."

    menu:
        "He seems stressed out."

        "<EMPATHY> Try to comfort him.":
            "You pat his back."
            b "Don't worry. We'll be fine."

            if stats.stats["empathy"] >= 3:
                by "<SUCCESS> I hope so."
                by "Thanks for staying calm."
            else:
                by "<FAILURE> Sorry Bianca, but you're not helping."
                b "Sorry."

        "Don't say nothing":
            b "..."

    hide bianca normal with dissolve
    hide bradley normal with dissolve

    "As you continue to walking you come across an old sign."

    "\"Warning! Bear traps!\""

    show helen normal at right3
    with dissolve

    show robert normal at left3
    with dissolve

    r "Ah shit."

    show bianca normal at center3
    with dissolve

    b "Whats wrong."

    r "Bear traps."

    b "Is that the only way?"

    h "It seems so."

    b "Just be careful."

    h "I have a bad feeling about it."

    b "Whats wrong."

    h "I've never seen a bear caught in a bear trap."

    h "It seems only stupid teenagers in horror movies fall into them."

    b "We're lucky then."

    h "Why?"

    b "We're not stupid."

    h "Oh..."

    "You turn to the rest of the team."

    b "Ok guys. Just be careful and watch your step."

    hide helen normal with dissolve
    hide robert normal with dissolve
    hide bianca normal with dissolve

    "You carefuly make your way through the trap field."

    "There is a lot of old traps covered in rust lying around."

    define trap_diff = 4

    "Suddenly you hear a loud noise and few seconds later you hear Robert screaming."

    r "Shit! My leg!"

    "You see him lying on a ground with his leg caught in one of the traps."

    "Helen and Tyrone look like they are about to run with help."

    b "WATCH OUT!"

    "You point at rest of traps lying around and slowly make your way to robert."
    
    show robert normal at center1
    with dissolve

    b "You okay buddy?"

    r "Nice joke."

    "You examine a trap. It's old but solid, and Robert moving his leg only makes it worse."

    b "Robert."

    menu:
        r "What?"

        "<EMPATHY> Try to calm him down":
            b "Robert, please. Calm down. You're only make it worse."
            if stats.stats["empathy"] >= 3:
                "<SUCCESS> Robert stops moving and calms down."
                $ trap_diff -= 1
            else:
                r "<FAILURE> Easier said than done."

            menu:
                r "What now smartass?"

                "<TRICKERY> Try to open trap.":
                    if stats.stats["trickery"] >= trap_diff:
                        "<SUCCESS> It takes a couple of minutes but you manage to open trap."
                        "Robert breathes heavily."
                        r "Thanks... Bianca."
                    else:
                        "<FAILURE> Not only you can't open the trap. You jammed a lock."
                        r "Shit it hurts!"
                        $ trap_diff += 1
                        menu:
                            b "Sorry!"

                            "<FITNESS> Try to force trap open.":
                                if stats.stats["fitness"] >= trap_diff:
                                    "<SUCCESS> You manage to force it open"
                                    "Robert breathes heavily."
                                    r "Thanks... Bianca."
                                else:
                                    "<FAILURE> Trap won't open."
                                    "Robert screams in pain"
                                    $ robert_alive = False
                
                "<FITNESS> Try to force trap open.":
                    if stats.stats["fitness"] >= trap_diff:
                        "<SUCCESS> You manage to force it open"
                        "Robert breathes heavily."
                        r "Thanks... Bianca."
                    else:
                        "<FAILURE> Trap won't open."
                        "Robert screams in pain"
                        menu:
                            b "Calm down"

                            "<TRICKERY> Try to open trap.":
                                if stats.stats["trickery"] >= trap_diff:
                                    "<SUCCESS> It takes a couple of minutes but you manage to open trap."
                                    "Robert breathes heavily."
                                    r "Thanks... Bianca."
                                else:
                                    "<FAILURE> Not only you can't open the trap. You jammed a lock."
                                    r "Shit it hurts!"
                                    $ robert_alive = False

        "<TRICKERY> Try to open trap.":
            if stats.stats["trickery"] >= trap_diff:
                "<SUCCESS> It takes a couple of minutes but you manage to open trap."
                "Robert breathes heavily."
                r "Thanks... Bianca."
            else:
                "<FAILURE> Not only you can't open the trap. You jammed a lock."
                r "Shit it hurts!"
                $ trap_diff += 1
                menu:
                    b "Sorry!"

                    "<FITNESS> Try to force trap open.":
                        if stats.stats["fitness"] >= trap_diff:
                            "<SUCCESS> You manage to force it open"
                            "Robert breathes heavily."
                            r "Thanks... Bianca."
                        else:
                            "<FAILURE> Trap won't open."
                            "Robert screams in pain"
                            $ robert_alive = False      


        "<FITNESS> Try to force trap open.":
            if stats.stats["fitness"] >= trap_diff:
                "<SUCCESS> You manage to force it open"
                "Robert breathes heavily."
                r "Thanks... Bianca."
            else:
                "<FAILURE> Trap won't open."
                "Robert screams in pain"
                menu:
                    b "Calm down"

                    "<TRICKERY> Try to open trap.":
                        if stats.stats["trickery"] >= trap_diff:
                            "<SUCCESS> It takes a couple of minutes but you manage to open trap."
                            "Robert breathes heavily."
                            r "Thanks... Bianca."
                        else:
                            "<FAILURE> Not only you can't open the trap. You jammed a lock."
                            r "Shit it hurts!"
                            $ robert_alive = False      


    if robert_alive == True:
        b "Okay get up buddy and lets go!"
        hide robert normal with dissolve
        "You help him stand and slowly you leave bear trap field."
        r "Thanks Bianca. Thanks for saving me."
        b "Save it for later."
        "You meet with the rest of the team and continue looking for way out."
    else:
        b "Robert, listen to me."
        b "I can't open it, the mechanism is messed up."

        b "You dont seem to bleed. Just stay calm. We'll get help"

        r "Hey don't leave me!"

        b "And how else are we supposed to help you?"

        "Robert seems worried."

        r "Okay, fine. Just please. Be quick."

        b "Don't worry."

        hide robert normal with dissolve

        "You meet with the rest of the team and continue looking for way out."

        b "We need to get help. Fast."

    "Worried and stressed you continue walking deeper and deeper into the unknown."
    
    call barbwire

    return


label barbwire:

    return