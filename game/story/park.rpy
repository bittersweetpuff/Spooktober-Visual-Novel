label park_sounds:
    scene
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
            call meeting_robert
        
        "That's weird. Let's check it out.":
            b "Yeah. That seems weird."
            "You head towards the source of the sound."

            call park_spook
    return


label park_spook:

    $ spooks_encountered = spooks_encountered +1

    "All 3 of you start making your way through bushes. However you don't find a source of weird sounds."

    h "Let's look around."

    by "I dont think we will find anything here."

    h "Oh, come on. Just keep your eyes open."

    hide helen normal
    with dissolve

    by "Well, I may as well do that."

    hide bradley normal
    with dissolve

    "You also start looking around but nothing catches your attention."

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
    call meeting_robert
    return
        

