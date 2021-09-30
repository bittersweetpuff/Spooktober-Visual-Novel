
define dad = Character("Father")
define mom = Character("Mother")

label opening_scene:
    scene bg outside with dissolve

    "Friday, October 31th"

    "Halloween"

    "You reach your home after a long day in school."

    menu:
        "You start searching for keys in your pockets but instead of keys you find:"

        "A couple of hairpins.":
            "A couple of hairpins that are usually very usefull to pick some basic locks, but are no use for your house's door"
            call increase_trickery from _call_increase_trickery

        "Make-up kit.":
            "Your make-up kit you always try to keep close in case of emergency, but sadly you can't open door with it"
            call increase_charm from _call_increase_charm

    "Suddenly, door open and you see your father, dressed in rather formal attire. He looks at you worried."

    dad "You're late Bianca. I was afraid something may have happened to you."

    b "Sorry dad, I forgot to call you..."

    
    menu:
        dad "About what?"
        

        "My volleyball training":
            b "My volleyball training took longer than expected. Way longer. Out coach is dead serious on us doing well this season."
            dad "Go Ladybugs!"
            b "...yeah..."
            call increase_fitness from _call_increase_fitness

        "The charity meeting":
            b "Charity meeting took longer than usual."
            dad "Charity meeting?"
            b "You remember when I told you that we are in charge of this year's annual bake sale?"
            dad "Yeah. What are you raising money for?"
            b "Mr. Norton's house burned down a few weeks ago, so we are trying to help in any way possible."
            dad "That's very kind of you."
            b "Thanks dad!"
            call increase_empathy from _call_increase_empathy
        
        "Falling asleep in library":
            b "I kinda fell asleep in library."
            dad "Really?"
            b "Yeah. I was suposed to just do my homework asignment but I guess my body needed some rest after this whole week of exams."
            dad "I'm sure you passed them with flying colours after studing this much."
            b "I hope so."
            call increase_smarts from _call_increase_smarts

    dad "Anyway. There is a pumpkin pie from your grandma in a fridge in case you get hungry"

    b "Are you going somewhere?"
    
    dad "Don't you remember? I'm taking your mom to the theatre tonight."

    b "Ooo... A halloween date! That's really nice of you daddy!"

    dad "I'm afraid the play have nothing to do with halloween, but your mom..."

    "You can hear the footsteps of high heeled boots as your mom enters the room. Similar to dad she is dressed quite elegant."

    dad "...insisted"

    mom "Oh come on Frank, I'm sure you'll love it."

    dad "If you say so."

    mom "Im glad you're back Bianca. We realized that you've forgotten the key so we couldn't leave without you coming back."

    b "Thanks mom."

    mom "Oh, you're welcome. Lucky, we should be there on time. Unlike the last time..."

    b "Last time?"

    

    

    menu:
        mom "Don't you remember? We missed our flight becouse you were just not ready."

        "The zipper on my bag was stuck":
            b "Mom, I've told you so many times. The zipper on my bag was stuck and it took me a really long time to fix it."
            mom "And by fixing it you mean tearing your bag apart?"
            b "..."
            b "..kinda."
            call decrease_trickery from _call_decrease_trickery

        "Im not that fast":
            b "Okay mom. I've told you so many times. I have many talents, sadly speed is not one of them."
            mom "Well I can see that honey"
            b "..."
            b "...nevermind"
            call decrease_fitness from _call_decrease_fitness

            
    mom "Oh don't be upset sweetheart. I was just messing with you."

    b "Good job on ruining my self esteem."

    mom  "Bianca... please..."

    b "Im not joking mom. My self esteem is as dead as it gets."

    dad "Honey, we'll be late. Let's go. Im sure Bianca also could use some rest."

    b "Have fun guys!"

    "After your parents leave you head to the kitchen, finish grandma's pumpkin pie and go upstairs to your room."

    call room_scene from _call_room_scene

    return


label room_scene:

    scene bg room with dissolve

    "You enter your room, throw yourself on bed."

    b "Damn, that was a long week."

    scene bg phone with dissolve

    "You hear your phone buzzing. You quickly check it out just to see a text from Bradley"

    "\"Sup' Bianca. You home?\""

    "You quickly text him back \"Yeah... btw how are you? I haven't seen you in the school today.\""

    "\"Well... something came up. Im fine tho\" - he texts you back almost instantly"

    "\"Good to know\" - you type back"

    "Now when you think of it, Bradley is last person who would skip the school for any other reason than severe illness."

    "You hear message notification again."

    "\"Anyway, you heard about party at Stacy Glow's place? Her parents are out for a weekend so she is throwing a halloween party. Wonna come?\""

    "You answer: \"I'd love too but my parents kinda don't want me to go to parties after the last time.\""

    "You got a response almost instantly."

    menu:
        "\"What hapened last time?\""

        "\"I took some bad internet advice on not getting drunk\"":
            "\"I took some bad internet advice on not getting drunk and it... well didn't work as intended. I should've known better. So yeah. Im kinda dumb.\" - you reply"
            "Bradley anwserws: \"Well yeah, that sucks\""
            call decrease_smarts from _call_decrease_smarts

        "\"Shouldn't have been hitting on others when drunk.\"":
            "\"Shouldn't have been hitting on others when drunk. That was so cringe. I don't really want to embarrass myself again\" - you reply"
            "Bradley anwserws: \"Oh... nothing's worse than booze endorsed heartbreak\""
            "\"More like booze endorsed meltdown.\""
            call decrease_charm from _call_decrease_charm

        "\"I got really mean while drunk.\"":
            "\"I got really mean while drunk and I don't want to ruin any more friendships because of that.\" - you reply"
            "Bradley anwserws: \"That's the tough one to handle.\""
            call decrease_empathy from _call_decrease_empathy

    "But to be honest, you feel like going to a party is a good idea. At least it is some way to unwind after this whole week."

    "You quickly text Bradley: \"Okay... I guess a little party never killed nobody. I'll get ready in like... 10 minutes.\""

    "\"Ok, I'll be waiting in front of your house\" - you get as reply."

    "\"Great. See you there\" - you type back and throw your phone into your bag. You change your clothes and do your best to fix your hair."

    scene bg room with dissolve

    "After a chaotic 20 minutes you look in a mirror."

    show bianca normal at center1
    with dissolve

    b "Looking good girl!"

    "You hear a doorbell ringing. It must be Bradley. You grab your bag and leave your house."

    call meeting_bradley from _call_meeting_bradley

    return




