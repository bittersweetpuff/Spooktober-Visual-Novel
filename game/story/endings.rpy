label calculate_ending:
    scene bg deepforest with dissolve

    if helen_alive and robert_alive and tyrone_alive:
        call good_ending from _call_good_ending
    else:
        if helen_alive or robert_alive or tyrone_alive:
            call bad_ending from _call_bad_ending
        else:
            call worst_ending from _call_worst_ending
    return


    label good_ending:

        "You continue your walk through the woods in search of help."

        show tyrone normal at left3
        with dissolve

        t "Yo! Check this out!"

        "He points at a light in a night."

        "Bradley seems woried"

        show bradley normal at right3
        with dissolve

        show bianca normal at center3
        with dissolve

        b "Brad? You ok?"

        by "I have a bad feeling about it."

        b "This can be our only help. Come on."

        hide tyrone normal with dissolve
        hide bianca normal with dissolve

        "You join Tyrone, Helen and Robert as they go in lights direction."

        by "Hey, guys wait!"

        hide bradley normal with dissolve

        scene bg witchhosue

        "Together you reach a lonely house in the woods. Only source of light comes from one of the windows."

        "You start knocking."

        b "Anybody there? We need help!"

        "There is no answer but your knocking pushes door open."

        "You enter the weird house."

        scene bg yaga with dissolve

        "Walls are covered in strange symbols and floor is full of coal."

        b "Okay this place is messed up."

        h "Yeah."

        "You don't see any sign of life here but find a door to the backyard."

        scene bg grave with dissolve

        "You leave the house and then you see it..."

        "... a freshly dug grave."

        "You start feeling really weird, but instead of running away you take a look inside."

        "and then you see Bradley's body."

        "You manage to silence your scream."

        r "But it doesent make any sense. The nerd is right here..."

        "All four of you look at Bradley. Who starts to smile."

        show witch normal at center1
        with dissolve

        w "I guess you know my little secret now."

        w "I hoped you won't make it here. But since you did it I guess all that is left is..."

        hide witch normal with dissolve

        "He does not finish as Helen kicks him in his calf throwing him off balance."

        h "Take this you demon bitch!"

        w "Wai..."

        "Tyrone does not wait as he tackles the demon to the ground and starts hitting him with his fist."

        t "YOU. GOD. DAMN. SON. OF. THE. BITCH. I. WILL. KILL. YOU!"

        "Robert slowly grabs the beer keg he has been carrying all the time and lifts it above supposed Bradleys head."

        r "Heads up, bitch!"

        "He drops keg on monsters head. As it hits him demon explodes into black goo splashing all over you."

        "It take you a couple minutes to realize what happened."

        "Your phone service is back and now when you look around, you see familiar path."

        "It feels like all that has happened was just some kind of bad dream."

        "The only thing making all those memories real is Bradley's body in a grave."
        
        
        scene bg end1 with dissolve

        "You are shocked."

        "You hear Tyrone calling police but you don't care."

        "You stand over your best friend's grave and start crying."

        b "I'm sorry."

        b "I hope now... at least you will rest in peace."

        scene black with dissolve

        centered "{size=+30}{font=Gothic_Birthday_Cake.ttf}The End{/font}{/size}"

        return



    label bad_ending:
        "You almost run through the woods in search of help."

        "And then, suddenly you see a light in a night."

        "You rush forward to the source of the light leaving your companions."

        b "I'll check this up!"

        "You hear them saying something but you are to focused on making it to the source of light."

        scene bg witchhosue

        "You reach a house in a middle of a forest."

        "You start knocking."

        b "Anybody there? We need help!"

        "There is no answer but your knocking pushes door open."

        "You enter the weird house."

        scene bg yaga with dissolve

        "Walls are covered in strange symbols and floor is full of coal."

        b "Okay this place is messed up."

        "You don't see any sign of life here but find a door to the backyard."

        scene bg grave with dissolve

        "You leave the house and then you see it..."

        "... a freshly dug grave."

        "You start feeling really weird, but instead of running away you take a look inside."

        "and then you see Bradley's body."

        "You manage to silence your scream as you hear someone standing behind you."

        w "I guess you finally found out."

        "You turn around"

        show witch normal at center1
        with dissolve

        b "Who... what are you?"

        w "Oh Bianca. I'm your dear friend. Don't you see?"

        "You look around"

        define count = 0

        if robert_alive:
            b "Robert?"
            $ count += 1
        if tyrone_alive:
            b "Tyrone?"
            $ count += 1
        if helen_alive:
            b "Helen?"
            $ count += 1

        w "Hahaha!"

        if count == 1:
            if helen_alive:
                w "She won't hear you."
                w "I took care of her."
            else:
                w "He won't hear you."
                w "I took care of him."

        else:
            w "They won't hear you."
            w "I took care of them."
        
        b "You monster!"

        w "Call me what you want sweetheart. Now it's your turn."

        hide bradley curse with dissolve

        scene bg end3 with dissolve

        "He smiles as he gets closer"


        "You start running away."

        "Then, your scream tears down a silence of the night."

        

        scene black with dissolve

        centered "{size=+30}{font=Gothic_Birthday_Cake.ttf}The End{/font}{/size}"

        return




    label worst_ending:
        "Now it's just you and Bradley. He seems surprisingly calm."

        show bradley normal at right2
        with dissolve

        show bianca normal at left2
        with dissolve

        b "How can you be this calm?!"

        by "Bianca calm down!"

        b "How can I calm down!"
        b "You saw what happened to them. We need to find help! NOW!"

        "And then, suddenly you see a light in a night."

        hide bianca normal with dissolve

        by "Really?"

        hide bradley normal with dissolve

        "You rush forward to the source of the light leaving Bradley behind."

        scene bg witchhosue

        "The light turn out to be coming from a window of a lonely house in a woods."

        "You immediately dash to the door and start knocking."
        
        b "Anybody there? We need help!"

        "There is no answer but your knocking pushes door open."

        "You enter the weird house."

        scene bg yaga with dissolve

        "Walls are covered in strange symbols and floor is full of coal."

        b "Okay this place is messed up."

        "You don't see any sign of life here but find a door to the backyard."

        scene bg grave with dissolve

        "You leave the house and then you see it..."

        "... a freshly dug grave."

        "You start feeling really weird, but instead of running away you take a look inside."

        "and then you see Bradley's body."

        "You manage to silence your scream as you hear someone standing behind you."

        w "I guess you finally found out."

        "You turn around"

        show witch normal at center1
        with dissolve

        b "Who... what are you?"

        w "Oh Bianca. I'm your dear friend. Don't you see?"

        b "Sh.. shut up! He's dead! You KILLED HIM!"

        w "I may have just gently pushed him to the other side. Nothing more."

        b "You son of the bitch"

        w "Watch your language young lady."

        b "Shut up! You killed him. You lured us into all those traps!"

        w "You are truly as smart as Bradley thought of you."

        b "What do you want, freak?"

        w "I have told you already. I just want to talk. But it may be a really long talk."

        w "One you may never live long enought to withness the end of."

        hide bradley curse with dissolve

        scene bg end2 with dissolve

        "He smiles as he gets closer"

        

        "Then, your scream tears down a silence of the night."

        

        scene black with dissolve

        centered "{size=+30}{font=Gothic_Birthday_Cake.ttf}The End{/font}{/size}"

        return

