label park_sounds:
    scene bg park with dissolve
    "As you walk through the park Helen starts looking around."

    show helen normal at center1
    with dissolve

    h "You guys hear that as well?"

    "You don't hear anything besides the sound of wind moving trees and bushes."

    show helen normal at right2
    with move

    show bradley normal at left2
    with dissolve

    

    menu:
        by "She's right. I also hear that."

        "It's just a wind guys.":
            show helen normal at right3
            with move
            show bradley normal at left3
            with move
            show bianca normal at center3
            with dissolve
            b "Guys, chill out. It's just a wind. I know it is halloween but we don't need to be scared of every single sound of nature."

            by "Well..."
            h "If you say so."

            "You continue walking through park."

            hide bradley normal
            with dissolve
            hide helen normal
            with dissolve
            hide bianca normal
            with dissolve
            call meeting_robert from _call_meeting_robert
        
        "That's weird. Let's check it out.":
            b "Yeah. That seems weird."
            "You head towards the source of the sound."

            call park_spook from _call_park_spook
    return


label park_spook:

    $ spooks_encountered = spooks_encountered +1

    "All 3 of you start making your way through bushes. However you don't find the source of weird sounds."

    h "Let's look around."

    by "I don't think we will find anything here."

    h "Oh, come on. Just keep your eyes open."

    hide helen normal
    with dissolve

    by "Well, I may as well do that."

    hide bradley normal
    with dissolve

    "You also start looking around but nothing catches your attention."

    scene bg cloth with dissolve

    "Then you see a piece of dark clothing laying in one of the bushes."

    menu:
        "However it's really hard to reach."

        "<TRICKERY> Try to reach it.":
            if stats.stats["trickery"] >= 4:
                "<SUCCESS> You manage to grab a cloth and pull it out of bushes."
                "It turns out to be a t-shirt. Suprisingly similar to the one Bradley is wearing."
                b "Guys! Come here!"
                show helen normal at right3
                with dissolve
                show bradley normal at left3
                with dissolve
                show bianca normal at center3
                with dissolve
                h "Have you found something."
                b "Just this T-shirt."
                "You show it to Bradley. He seems worried."
                by "They are kinda popular after all."
                b "Yeah, somebody may have just thrown it away here."
                h "Since that's all we found maybe better go to this party already."
                b "Yeah, lets go."
            else:
                "<FAILURE> You try to grab a cloth but only and up scratching yourself."
                b "Crap"
                show helen normal at right3
                with dissolve
                show bradley normal at left3
                with dissolve
                show bianca normal at center3
                with dissolve
                h "Have you found something."
                b "Nothing. I scratched  the shit out of my hand through."
                by "You okay?"
                b "I'll survive."
                h "Since we haven't found anything maybe better go to this party already."
                b "Yeah, lets go."

        "Leave it be":
            "You leave the cloth in bushes."
            show helen normal at right3
            with dissolve
            show bradley normal at left3
            with dissolve
            show bianca normal at center3
            with dissolve
            h "Have you found something."
            b "Nothing."
            h "Since we haven't found anything maybe better go to this party already."
            b "Yeah, lets go."

    hide bradley normal
    with dissolve
    hide helen normal
    with dissolve
    hide bianca normal
    with dissolve

    scene bg park with dissolve
    call meeting_robert from _call_meeting_robert_1
    return

label meeting_robert:
    "As you make your way through the park you hear somebody running through bushes."
    "Suddenly he jumps out one of the bushes in front of you and crushes into you."

    show robert normal at center1
    with dissolve

    r "Hey! Watch out!"

    "You pick yourself up."
    show robert normal at right2
    with move

    show bianca normal at left2
    with dissolve

    menu:
        b "Excuse me? You are the one who crushed into me."

        "You should watch out dude.":
            b "You should be the one watching out dude."
            r "Oh shut up."

        "<CHARM> Buy me a dinner first.":
            b "You have to buy me a dinner first if you want to go that way."
            if stats.stats["charm"] == 5:
                r "<SUCCESS> Uhm.. well.. whaaa?"
                "He turns red instantly."

            else:
                r "<FAILURE> Yeah yeah. Really funny. Shut up."
                b "Oh..."

    show robert normal at right3
    with move

    show bianca normal at center3
    with move

    show helen normal at left3
    with dissolve

    h "Well well well... who do we have here if not Robert Woodley himself."

    r "Quit it nerd."

    h "Oh come on. Aren't you too \"cool\" and \"independent\" to go on halloween parties?"

    r "And who said Im going to the party, huh?"

    h "And what else would you be doing here?"

    r "You have a point."

    b "Helen, you know this dork."

    r "Hey!"

    h "Kinda. That's Robert. We're at the same class."

    b "How have I never met you?"

    r "Dunno. We go to the big school I guess."

    h "Plus he is kind of a loner."

    r "I prefer a term \"sigma male\""

    b "..."

    h "..."

    by "..."

    "You, Helen and Bradley burst into laugh."

    hide helen normal
    with dissolve

    r "Hey, stop laughing"

    b "Sorry... sorry..."

    "You continue to laugh."

    r "HEY!"

    b "Okay... sorry. You're the first person I know that used this term not ironically."

    r "Whatever..."

    menu:
        b "Oh don't be mad Robert."

        "Im Bianca":
            b "My name is Bianca, that's Bradley."
            r "Whatever..."

        "<EMPATHY> Let's start again. Hi! My name is Bianca.":
            b "Let's start again. Hi! My name is Bianca and that's Bradley. Helen you already know."

            if stats.stats["empathy"] >= 3:
                r "<SUCCESS> Well... Hi! Im Robert."
                "He shakes your hand."

            else:
                r "<FAILURE> Whatever..."

    
    b "So, since we already know each other, why wont you join us."

    r "Why?"

    b "We're going on the same party."

    r "..."

    b "So? Wonna join?"

    r "..."

    r "...yeah. Whatever."

    hide robert normal
    with dissolve
    
    hide bianca normal
    with dissolve

    "You leave a park and take shortcut through the forest."

    call forest_screams from _call_forest_screams

    return
        

