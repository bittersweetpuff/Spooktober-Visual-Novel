label meeting_helen:
    scene bg parking with dissolve
    "You reach parking lot located next to the park you need to go through."

    "You see a girl standing next to the fence. She looks familiar."

    show bianca normal at left3
    with dissolve

    b "Hey, Brad. Is that Helen?"

    show bradley normal at right3
    with dissolve

    by "Helen?"

    b "Don't you know her?"

    by "I don't think so."

    b "Well, thats Helen... Helen Kul I think. She usually hangs out on a side and draws."

    by "An artsy kind?"

    b "You can say that."

    "The girl seems to have noticed you and approaches you."

    show helen normal at center3
    with dissolve

    h "Good evening"

    b "Hey Helen."

    by "Sup'"

    h "What are you guys up to?"

    b "We're going on a party at Stacy's place."

    h "Oh, same here. I was just trying to figure out what's the fastest way there."

    b "I didn't knew you guys were friends."

    h "We used to date back in 10th grade. Now we are just friends but still like to hang out together some times."

    by "That's kinda lovely."


    menu:
        h "Yeah. She is really nice"

        "<CHARM> She must have been stupid to break up with you.":
            b "She must have been stupid to break up with you."
            if stats.stats['charm'] >= 4:
                h "<SUCCESS> Oh... don't say that"
                "Helen blushes."
                h "It wasn't anything serious or anything."
            else:
                h "<FAILURE> I don't think so. We just didn't really fit together."
                h "It wasn't anything serious or anything."
        "Good to know.":
            b "That's good to know."

    h "So since we are going on the same party..."

    menu:
        h "Can we all go together."

        "Sure":
            b "Sure, why not."
        "Bradley?":
            b "Bradley, what to you think?"
            by "Sure, why not. Welcome to the team Helen."

    h "Nice!"

    hide bradley normal
    with dissolve
    hide helen normal
    with dissolve
    hide bianca normal
    with dissolve

    "As you start walking Helen approaches you."

    show bianca normal at left2
    with dissolve

    show helen normal at right2
    with dissolve

    h "How are you doing Bianca?"

    b "Kinda okay... I guess."

    h "Heard you had hell of a week."

    b "Well it wasnt THAT bad."

    "You start laughing."

    b "How about you?"

    h "It's fine. Finished my art project..."

    h "...although I spilled ink all over my bed sheets while doing so."

    b "Ouch..."

    h "Anyway... didn't knew you were hanging out with little mister perfect over here."

    "She points at Bradley."

    b "Oh, we are friends since we were like three."

    h "Wow. That's really cute."

    "You smile. Even though you and Bradley are friends for such a long time, you usually hang out with different people."

    if stats.stats["smarts"] <= 3:

        h "You just don't really look like someone like who would hang out with library dwellers like he."
    
    else:

        h "Now when I think of it you are kinda similar."

    "Bradley, stops and squeezes in between you."

    show bianca normal at left3
    with move

    show helen normal at right3
    with move

    show bradley normal at center3
    with dissolve

    by "What are you guys talking about?"

    h "Nothing."

    menu:
        "He looks at you."

        "<CHARM> About how cute you are.":

            b "We were talking about how cute you are."
            if stats.stats["charm"] >= 3:
                by "<SUCCESS> Oh..."
                "Bradley looks disoriented"
                h "Oh yeah. You're such a cutie pie."
                "Both of you start laughing. Bradley is even more mixed up."
                by "Well... um... thanks... I guess."
                
            else:
                by "<FAILURE> Bianca. Stop!"
                b "Oh come on. I was just messing with you."
                by "Whatever."

        "I was telling Helen about you.":
            b "I was telling Helen how long you and I know each other."
            h "Yeah, I didn't realize you guys are friends."
            by "Well now you know."

    hide bradley normal
    with dissolve
    hide helen normal
    with dissolve
    hide bianca normal
    with dissolve

    "You continue walking in silence as you enter park."

    call park_sounds

    return


    


