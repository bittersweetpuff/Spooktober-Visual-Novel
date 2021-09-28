label forest_screams:
    scene bg forest with dissolve

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

    "You continue your walk through the forest."

    show bradley normal at left2
    with dissolve

    by "Damn, what an evening."
    by "At this point I'm wondering what will happend next."

    show bianca normal at right2
    with dissolve
    if spooks_encountered == 0:
        b "Oh, It isn't so bad."
        b "Sure, some weird stuff is happening around us but nothing special."
        b "You're just worring to much."
        by "Maybe you're right."

    else:
        b "Yeah... too many spooky shit for one night if you ask me."
        by "Good to feel that I'm not alone in that thought."

    b "Bradley, I'm really worried about you. Really. If you need to talk, we can ditch this party and just hang out somewhere."
    by "Thanks, but that would be stupid. At the end of the day, I was the one that dragged you here."
    b "Oh come on... thanks to dragging me here. I needed it."
    "Bradley's mood seems to getting better and better every second."

    h "HEY BIANCA. COME HERE."
    "Helen Is waving at you, showing you to come to her."
    hide bradley normal
    with dissolve
    hide bianca normal
    with dissolve

    show robert normal at right3
    with dissolve

    show helen normal at left3
    with dissolve

    r "Come on. How many people am I gonna encounter tonight?"
    h "Stop whining."
    r "And out of all people it have to be this dickhead?"
    h "Shut up, Robert."
    show bianca normal at center3
    with dissolve
    b "Hey, what's up?"
    "Helen points her finger at a silhouette sitting next to one of the threes."
    "You see a tall guy sitting next to the beer keg and drinking from a can of light beer."
    b "Is that..."
    r "...Tyrone McNamara. Yeah. Biggest damn idiot in the whole school. Probably becouse of brain damage he suffered while playing football or something."
    h "Is there someone you don't hate?"
    r "Shut up."
    "Helen rolls her eyes."
    b "Oh come on Robbie. I know him. He's not that bad."
    hide bianca normal with dissolve
    r "Don't tell me she'll invite him to join as well."
    h "Well, she is a social butterfly afterall."

    hide robert normal with dissolve
    hide helen normal with dissolve

    show tyrone normal at right2
    with dissolve

    t "Why am I the one carrying this."

    show bianca normal at left2
    with dissolve

    b "Oh, poor unfortunate soul. Who made you do this?"

    t "Oh shit! Bianca!"

    "Tyrone throws half finished beer can in bushes."

    b "Tell me big guy. Does your coach know you drink this stuff?"

    "You point at bushes."

    t "Oh come on girl. That's just a beer. Everybody is drinking that."

    b "You got point, but not everybody is Cloudvale High Butchers running back."

    t "Oh..."

    "Tyrone seems happy about that comment."

    b "I think I may be worried about our star player. Right?"

    t "Haha! Yeah girl. You should be."

    "He stops laughing and looks at you with serious face."

    menu:
        t "You won't report me to the coach, right?"

        "<CHARM> I have a soft spot for bad boys":
            b "I have a soft spot for bad boys you know?"
            if stats.stats["charm"] >= 2:
                t "<SUCCESS> Damn girl, you're a lucky one."
                t "You have one right here."
                b "Im flattered."
            else:
                t "<FAILURE> Ugh.. I have no idea what are you talking about."
                b "..."
                b "Whatever..."

        "Maybe":
            b "Maybe..."
            t "Oh come on. Don't be such a bitch."
            b "Chill out. We are going on a party. I was joking."
            t "Oh..."
            "Tyrone seems confused."
        
    t "So you guys are going to Stacy's as well?"
    b "What else would be doing in a forest this late."
    t "I have no idea what weird hobbies you guys have."
    "He points at Robert."
    t "Especially this guy."
    hide bianca normal with dissolve

    show robert normal at left2
    with dissolve

    r "Shut up!"

    t "Chill out my dude. There's no reason to be upset you know? Grab this."

    "Tyrone puts keg in Robert's arms."

    t "We're almost there. I think you can manage."

    hide tyrone normal with dissolve

    r "Wha.. Hey..."
    r "..."
    r "...whatever."

    hide robert normal with dissolve

    call forest_silhouette

    return

label forest_silhouette:

    "The party continues its journey through the woods."

    show helen normal at left3
    with dissolve

    h "It kinda feels like D&D session if you ask me."

    show bianca normal at center3
    with dissolve

    b "Why?"

    h "You know... Group of characters, recruiting new party members..."

    b "Where are the enemies them?"

    h "They should show up soon. We're probably gonna face some rats sooner or later."

    b "Ugh... I hate rats."

    h "Oh come on. Rats are cool."

    show tyrone normal at right3
    with dissolve

    t "Yo guys. Have you seen that?"

    "He points at darkness between trees."

    h "I don't see anything."

    b "Me neither."

    menu:
        t "I swear I saw someone."

        "Just ignore it":
            b "Maybe, but we are almost there. Lets ignore it and just go to this party."
            b "Im tierd."

            hide bianca normal with dissolve
            hide helen normal with dissolve

            t "But I really..."
            t "Uh.. nevermind."

            hide tyrone normal with dissolve

            call calculate_early_ending

        "Lets check it out.":
            b "Well, if you say so... lets check it. Out."

            hide bianca normal with dissolve
            hide tyrone normal with dissolve

            h "I'll wait with Robert and Bradley!"

            hide helen normal with dissolve

            call effigy_spook

    return

label effigy_spook:

    $ spooks_encountered = spooks_encountered+1

    "You and Tyrone looking for mysterious person he saw."

    show bianca normal at left2
    with dissolve

    b "Are you sure it was here?"

    show tyrone normal at right2
    with dissolve

    t "Yeah. For sure."

    b "Let's just search around and don't make the rest wait for too long."

    t "Good idea girl."

    hide tyrone normal with dissolve
    hide bianca normal with dissolve

    "You look around with no result."

    "Finally you find something that may have looked like a human silhouette."

    show bianca normal at left2
    with dissolve

    "You look at a human sized effigy, looking similar to a scarecrow. It has dark hairs, blue jacket, black t-shirt and white scarf."

    b "Okay, thats super spooky."

    "You hear Tyrone yelling."

    t "YO!"

    t "ANYBODY HERE?"

    b "Tyrone! Shut up and come here."

    show tyrone normal at right2
    with dissolve

    "Tyrone joins you and looks at a scarecrow"

    t "What the..."

    b "Yeah... who would put scarecrow in a middle of the forest?"

    t "I have no idea... really."

    t "Maybe someone dumped unwanted halloween decoration here."

    b "I would love to belive that but look at it's clothing."

    t "Oh shit! It looks like..."

    b "Exactly."

    t "Better return to the rest."

    b "Yeah. The faster we get out of this forest the better."

    hide tyrone normal with dissolve
    hide bianca normal with dissolve

    "You return to Helen and the rest."

    "Bradley approaches you."

    show bradley normal at left2
    with dissolve

    by "Have you found anything?"

    show bianca normal at right2
    with dissolve

    b "Yeah, just some weird human sized doll. Creepy but nothing to write home about."

    by "Thats great to know. Now come on. We're gonna be late."

    by "... Is something wrong? You seem worried."

    b "It's nothing Im just..."

    menu:
        by "Huh?"

        "It looked like you":
            b "This weird scarecrow, doll or whatever thingy looked just like you."

            by "What do you mean."

            b "It was you size, had your clothes... that was really weird."

            "Bradley's face turned pale in a second."

            b "Don't worry. It was just a scarecrow. Lets go!"

        "Nothing, really":

            b "Nothing, really."

            by "Are you sure?"

            b "Yeah. Let's go"

            "Bradley seems relieved."

    hide bradley normal with dissolve
    hide bianca normal with dissolve

    call getting_lost

    return


label getting_lost:
    scene bg deepforest with dissolve
    "After a couple minutes of walking there is no end to the forest."

    show tyrone normal at left3 with dissolve

    t "Are you guys sure we are on a right track?"

    show helen normal at right3 with dissolve

    h "Yeah..."

    h "But let me check map really quick."

    "She pulls up her phone."

    h "Really? Now?"

    show robert normal at center3 with dissolve

    r "What's wrong?"

    h "My battery has run out."

    r "Great. I forgot my phone."

    t "Let me check mine."

    "Tyrone pulls up his phone"

    t "What the hell..."

    h "What's wrong?"

    t "No service. No GPS... what the hell is going on..."

    hide robert normal with dissolve

    show bianca normal at center3 with dissolve

    h "How is your phone Bianca?"

    "You check up your phone..."

    "...It has no service, nor GPS signal."

    b "Same as Tyrone's"

    "You look at Bradley. He check his phone."

    by "Same here."

    b "Great. Are we really lost?"

    h "Oh don't worry. This forest is not that big."

    h "At some point we will get out."

    b "That's not something I was hoping for."

    b "My parents will be so pissed off."

    t "No need to panic. People know we are coming to the party. If we don't show up they will probably start looking for us."

    "He looks at Robert."

    t "At least they will look for some of us."

    hide helen normal with dissolve
    show bradley normal at right3 with dissolve

    by "Im gonna agree with the big guy here. There is no reason to panic. Just continue walking."

    hide bradley normal with dissolve

    "Bradley starts walking down the path."

    t "I guess there is no point not to."

    hide tyrone normal with dissolve

    "Tyrone goes after Bradley. The rest follows them."

    b "I guess that's the best shot."
    
    hide bianca normal with dissolve

    call trap_field


    return