label forest_screams:
    scene

    "Bradley aproaches you."

    show bradley normal at left2
    with dissolve

    by "Why are we hanging out with this asshole?"

    show bianca normal at right2
    with dissolve

    b "Why not?"

    by "You don't have to take evey single person with you."

    b "Yeah. I don't have to... but I can."

    "Bradley seems to be worried."

    b "What's wrong?"

    by "I just hoped we could talk while we go to the party."

    b "We can talk now!"

    "Bradley points at Helen and Robert walking in front of you."

    b "Oh right."

    b "Is that something important? You seem worried."

    by "Oh, it's nothing, really. Just wanted to talk to you face to face."

    b "Don't worry. Im sure we'll find a while to..."

    "As you speak you hear a loud scream."

    by "What the hell was that?"

    show bradley normal at left3
    with move

    hide bianca normal
    with dissolve

    show robert normal at center3
    with dissolve

    r "You guys heard that?"

    show helen normal at right3
    with dissolve

    h "Someone was screaming."

    by "Yeah heard that too."

    menu:
        h "What's going on?!"

        "Chill. That's just people freaking out over halloween.":
            b "Chill out guys. It's halloween today. People are probably just making pranks."
            h "You sure. That sounded quite serious."
            by "Bianca may be right. Let's not worry about it."
            r "Yeah let's go."

            hide helen normal
            with dissolve
            hide robert normal
            with dissolve
            hide bradley normal
            with dissolve

            call meeting_tyrone

        "Let's check it out!":
            b "Yeah, that was weird. Let's chceck it out."
            hide helen normal
            with dissolve
            hide robert normal
            with dissolve
            by "Hey guys, wait for me!"
            hide bradley normal
            with dissolve

            call tracks_spook


    return

label tracks_spook:
    $ spooks_encountered = spooks_encountered + 1
    "You start looking for a source of scream with no effect."
    show helen normal at center1
    with dissolve
    h "Let's split up!"
    hide helen normal
    with dissolve
    "No matter how stupid it sounded, it seemed like a only idea that made sense."
    "After couple minutes of looking for something you found some strange tracks on ground."
    b "Hey guys! Come check it out!"
    "You can hear rest of the guys getting closer."
    show bradley normal at center3
    with dissolve
    by "You found something Bianca?"
    show helen normal at left3
    with dissolve
    show robert normal at right3
    with dissolve
    b "Just some tracks"
    menu:
        r "They look kinda weird."

        "<SMARTS> Examine the tracks.":
            "You take a closer look at the tracks"

            if stats.stats["smarts"] >= 4:
                b "<SUCCESS> You will not like this guys."
                "Bradley seems worried."
                r "What's wrong with them?"
                b "It seems like someone was draging something really heavy. Something or someone."
                "Robert and Helen also started looking worried."
            else:
                b "<FAILURE> I have no idea what they are."
                by "Oh... maybe that's better"

        "Just go.":
            b "We are not some kind of trackers of something. And I don't hear any more screaming."
            h "Yeah, that was probably some drunk idiot pretending to be a ghost."
                    


    b "You know what guys? The better we reach Stacy's house the better."
    r "Yeah."
    by "You're right"
    h "It's not far from here."
    b "Let's go then."
    hide helen normal
    with dissolve
    hide robert normal
    with dissolve
    hide bradley normal
    with dissolve
    call meeting_tyrone
    return

label meeting_tyrone:
    return