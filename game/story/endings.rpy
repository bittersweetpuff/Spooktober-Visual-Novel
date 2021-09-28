label calculate_ending:

    if helen_alive and robert_alive and tyrone_alive:
        "Good ending"
    else:
        if helen_alive or robert_alive or tyrone_alive:
            "Bad ending"
        else:
            call worst_ending
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

        "The light turn out to be coming from a window of a lonely house in a woods."

        "You immediately dash to the door and start knocking."
        
        b "Anybody there? We need help!"

        "There is no answer but you're knocking pushes door open."

        "You enter weird house."

        "Walls are covered in strange symbols and floor is full of coal."

        b "Okay this place is messed up."

        "You don't see any sign of life here but find door to the backyard."

        "You leave house and then you see it..."

        "... freshly dug grave."

        "You start feeling really weird, but instead of running away you take a look inside."

        "And than you see Bradley's body."

        "You manage to silence your scream as you hear someone standing behind you."

        w "I guess you finally found out."

        "You turn around"

        show witch normal at center1
        with dissolve

        b "Who... what are you?"

        w "Oh Bianca. Im your dear friend. Don't you see?"

        b "Sh.. shut up! He's dead! You KILLED HIM!"

        w "I may have just gently pushed him to the other side. Nothing more."

        b "You son of the bitch"

        w "Watch your language young lady."

        b "Shut up! You killed him. You lured us into all those traps!"

        w "You are truly as smart as Bradley thought of you."

        b "What do you want, freak?"

        w "I have told you already. I just want to talk. But it may be a really long talk."

        w "One you may never live long enought to withness the end of."

        "He smiles as he gets closer"

        "Then, your scream tears down a silence of the night."

        hide bradley curse with dissolve

        "The end."

