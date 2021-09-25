label meeting_bradley:
    scene

    "You lock you house's door and see Bradley in a driveway."

    
    show bradley normal at right2
    with dissolve

    by "Hey Bianca. Looking good!"

    show bianca normal at left2
    with dissolve

    b "Thanks."

    b "I was worried about you. Really. You are like... the last person on earth to miss school."

    by "I was feeling really sick. But not Im okay."

    b "Well that's a relief."

    b "Lucky with your results you'll get to med school with no problem even if you completely ditch school."

    by "Thanks... by the way, I kinda forgot. What major are you aiming to study?"

    b "Haven't I told you?"

    by "I don't think so."

    menu:
        b "Well..."

        "Astrophysics":
            b "Astrophisics major would be neat."
            by "Nice"
            call increase_smarts

        "Cyber security":
            b "Cyber security would be neat. I could use some of my XSS skills."
            by "Nice"
            call increase_trickery

        "Drama":
            b "Drama major would be a dream come true."
            by "Nice"
            call increase_charm

        "Diplomacy":
            b "Diplomacy major would be neat."
            by "Nice"
            call increase_empathy

        "Just getting sports scholarship would be nice":
            b "Too be honest... Just getting sports scholarship would be nice."
            by "That would be cool."
            call increase_fitness

    b "But really. I thought I've already told you that."

    by "Then I must have forgotten"

    by "There is just too much stuff on my head right now."

    b "Oh..."

    b "If you need my help..."

    by "Don't worry Bianca. I can manage. Thanks."

    "You start walking towards Stacy's house."

    by "The fastest way would be through the park and a piece of forest"

    b "O... forest in an evening on Halloween. Thats so..."

    menu:
        by "What?"

        "Spooky":
            b "Spooooooky!"
            by "It will get us into right mood."
            b "Yeah!"

        "Irresponsable":
            b "Irresponsable."
            by "Aren't you to old for that stuff?"
            b "Im just being carefull."

    b "Anyway..."

    b "You said you've been forgetting stuff lately?"

    by "Not really. Just a lot of stuff on my head."

    b "Oh. I just hoped you would forget some of the more embarrassing moments from my life."

    by "Haha..."

    menu:
        by "Like?"

        "Not making to the team in eight grade":
            b "That one time I failed tryouts."
            by "Oh... this one. This one I sadly remember. "
            if stats.stats['fitness'] >= 4:
                by "Luckly you improved so much over years."
            else:
                by "That was a long time ago. Don't worry about it."
            b "Yeah, but I still have a lot of training ahead of me."
            call decrease_fitness

        "Calling Maggie a toad.":
            b "Calling Maggie a toad in like... third grade"
            by "Oh, that was a messy one."
            b "Yeah. That was meant. Didn't knew she had this weird skin disease."
            b "Gosh... sometimes Im so mean."
            call decrease_empathy

        "Destroying our school project.":
            b "Destroying our school project last year."
            by "How could I forget that."
            b "Hell, I wish I had a firmer grip."
            call decrease_trickery

        "Losing in knowledge quiz.":
            b "Losing in knowlege quiz"
            by "But that was a long time ago, right?"
            b "Yeah but still. Should've studied more."
            call decrease_smarts

        "Crying after I didn't get what i wanted for birthday.":
            b "Crying after I didn't get what i wanted for birthday."
            by "Oh come on."
            b "No... that was my sixth birthday and people still think Im spoiled child who can't behave herself."
            call decrease_charm
    
    by "Girl, if that is your most embarrassing secret you are a lucky one."

    b "Haha! Maybe you're right."
    

        

    return