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

    "Few minutes after leaving a trap field you encounter another obstacle."

    show tyrone normal at right2
    with dissolve

    t "Are we being serious here?"

    show bianca normal at left2
    with dissolve

    b "Whats wrong?"

    "You don't need to wait for answer. You find yourself in front of a barb wire fence."

    t "Are we really gonna go through this shit?"

    b "Im afraid we may need to."

    t "What kind of weird torture porn bullshit it is."

    hide tyrone normal with dissolve

    show bradley normal at right2
    with dissolve

    by "I'll go first."

    hide bradley normal with dissolve

    "Bradley slowly but surely makes his way through barb wire."

    "Lucky wires are not really dense."

    show helen normal at right2
    with dissolve

    h "I guess Im next."

    h "Come on Helen... you can do this."

    hide helen normal with dissolve

    "Helen takes her time but finally makes her way through with no scratch."

    if robert_alive == True:

        show robert normal at right2
        with dissolve

        r "Ugh... gimmie a break."

        hide robert normal with dissolve

        "In spite of hurt leg, Robert manages to get through."

    show tyrone normal at right2
    with dissolve

    t "Okay Bianca, you're next."

    b "I guess."

    hide tyrone normal with dissolve
    hide bianca normal with dissolve

    "You take a deep breath and start to crawl through barb wire."

    b "And I could've stayed home."

    "It feels like eternity, but finally you are on the other side."

    "You look at Tyrone on the other side of fence."

    b "Okay big guy. Be careful."

    "Tyrone start making his way through. Suddenly he stops and yells."

    "You see him slowly getting tangled in barb wire."

    show tyrone normal at center1
    with dissolve

    "He start panicking."

    t "Shit, shit, shit..."

    b "Tyrone. Calm down. You are making it worse."

    define barb_diff = 4

    menu:
        t "It hurts!"

        "<CHARM> \"Don't worry. Im here. Just slowly come to me.\"":
            b "Don't worry. Im here. Just slowly come to me."
            "Tyrone lookes at you..."
            if stats.stats["charm"] >= barb_diff:
                "<SUCCESS> ...and manages to get through."
                b "Im proud of you big boy."
                "In spite of his wounds he smiles."
                t "Thanks for calming me down Bianca."
                b "No problem."
            
            else:
                "<FAILURE> ...and tries to get through."
                "He only makes it worse and starts panicing."
                $ tyrone_alive = False
        
        "<SMARTS> Take a look at barb wire.":
            if stats.stats["smarts"] >= 3:
                "<SUCCESS> You manage to find a path that should be easier for Tyrone to get through."
                "You think you can guide him through it."
                $ barb_diff = 3
            else:
                "<FAILURE> But you can't find any easier way."
            menu:
                b "Tyrone..."

                "<CHARM> \"Don't worry. Im here. Just slowly come to me.\"":
                    b "Don't worry. Im here. Just slowly come to me."
                    "Tyrone lookes at you..."
                    if stats.stats["charm"] >= barb_diff:
                        "<SUCCESS> ...and manages to get through using easier path."
                        b "Im proud of you big boy."
                        "In spite of his wounds he smiles."
                        t "Thanks for calming me down Bianca."
                        b "No problem."
                    else:
                        "<FAILURE> ...and tries to get through."
                        "He only makes it worse and starts panicing."
                        $ tyrone_alive = False

    if tyrone_alive == False:
        b "Shit, Tyrone. Stop moving."
        "Tyrone breathes heavily."
        b "You're stuck. We'll get help. Just stay calm."

        t "Don't tell me you're gonna leave me here."

        b "What else can we do?"

        "He looks terrified but finally nods."

        t "Okay Bianca. My life is in your hands."

        hide tyrone normal with dissolve

        "You and the rest continue walking with a swift pace leaving Tyrone behind."

    else:

        t "My whole body hurts."

        b "I'm not surprised."

        "You and the rest continue walking with a swift pace."

    call bridge

    return


label bridge:

    "Not a long time after making it through a barbed wire fence you hear the sound of running water."

    "You come across a river with a couple of planks that create a primitive bridge."

    "Unsurprisingly the \"bridge\" does not look stable at all."

    show bradley normal at right2
    with dissolve
    show bianca normal at left2
    with dissolve

    by "Bianca, take a look."

    "He points at riverbed."

    by "Thats a good 4 meter fall."

    b "Yeah... and current looks strong."

    b "We need to be really careful while passing."

    by "Ladies first."

    b "Shut up."

    hide bradley normal with dissolve
    hide bianca normal with dissolve

    "You take deep breath and start walking on a bridge."

    "Wood produces an unsettling sound when you step on it."

    b "Don't break, don't break."

    "After couple seconds you are on the other side."

    show bianca normal at left2
    with dissolve

    "You look at rest."

    if robert_alive == True:
        "Robert, slowly, makes it through."

        show robert normal at right2
        with dissolve

        r "I'm not leaving home for next week after we get out of this damn forest."

        b "Same here mate."

        hide robert normal with dissolve

    if tyrone_alive == True:
        "Tyrone does not wait any longer and just rushes through the bridge."

        "When he makes it to the other side starts breathing heavily."

        show tyrone normal at right2
        with dissolve

        t "Im done with this shit B."

        b "Well I can see that."

        hide tyrone normal with dissolve

        if robert_alive == True:
            "He stands next to Robert."

        else:
            "He watches others pass."

        "Bradley makes it through with little to no problem."

        show bradley normal at right2
        with dissolve

        by "Watch out Helen. It feels like it's about to snap."

        "Helen, pale as a ghost, starts making her way through bridge."

        "She stops in a middle and starts shaking. Then she gets on all fours."

        hide bianca normal with dissolve
        hide bradley normal with dissolve

        "You stand on the other side of the bridge."

        show helen normal at center1
        with dissolve

        h "Shit... I can't. It'll break."

        b "Shut up and come here Helen. Don't you dare to panic."

        "You see cracks in planks."

        define bridge_diff = 4

        menu:
            h "Bianca... I can't."

            "<CHARM> Come on Helen. You are almost here... Be brave.":
                call helen_charm_check
                menu:
                    "..."

                    "<TRICKERY> <LIE> The bridge wont break":
                        call helen_trickery_check

                        menu:
                            "..."

                            "Just come to me.":
                                call come_to_me


                    "Just come to me.":
                        call come_to_me


            "<TRICKERY> <LIE> The bridge wont break":
                call helen_trickery_check

                menu:
                    "..."

                    "<CHARM> Come on Helen. You are almost here... Be brave.":
                        call helen_charm_check
                        menu:
                            "..."

                            "Just come to me.":
                                call come_to_me
                    

                    "Just come to me.":
                        call come_to_me



            "Just come to me.":
                call come_to_me


    if helen_alive == True:
        "Both of you are lying on a ground breathing heavily."

        h "That was close."

        b "Lets get out of here."

        b "Yeah"

        "Bradley helps you get up and together you continue looking for a way out."

    else:

        b "No... Helen!"

        "You feel Bradley's hand on your shoulder."

        by "You can't help her now. Let's go."

        "Still in shock you stand up and continue looking for a way out."

    
    call calculate_ending


    return


label helen_charm_check:
    b "Come on Helen. You are almost here... Be brave."
    "You reach your hand to her."

    if stats.stats["charm"] >= 3:
        $ bridge_diff -= 1
        "<SUCCESS> Helen seems to be calming down."
    else:
        "<FAILURE> Helen is still panicking."
    
    return

label helen_trickery_check:
    b "Helen, It just look like it's about to break."
    b "You will be fine. Trust me."

    if stats.stats["trickery"] >= 4:
        $ bridge_diff -= 1
        "<SUCCESS> Helen seems to be calming down."
    else:
        h "<FAILURE> STOP LYING!"
        $ bridge_diff += 1
        "Helen seems to panicing more."
    
    return

label come_to_me:
    b "Just come to me..."
    b "On three"
    b "One"
    b "Two"
    b "THREE!"

    hide helen normal with dissolve

    menu:
        "Helen jumps to you in a second that bridge snaps under her."

        "<FITNESS> CATCH HER":
            if stats.stats["fitness"] >= bridge_diff:
                "<SUCCESS> You grab her hand and pull her on your side of riverbank."
            else:
                "<FAILURE> You miss her hand by couple centimeters."
                h "Fu...."
                "You see her falling into dark water."
                b "HELEN!"
                b "HELEN!"
                "No response."
                $ helen_alive = False
    return




