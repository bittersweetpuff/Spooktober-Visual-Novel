
define dad = Character("Father")
define mom = Character("Mother")

label opening_scene:

    "Friday, October 31th"

    "Halloween"

    "You reach your home after a long day in school."

    menu:
        "You start searching for keys in your pockets but instead of keys you find:"

        "A couple of hairpins.":
            "A couple of hairpins that are usually very usefull to pick some basic locks, but are no use for your house's door"
            call increase_trickery

        "Make-up kit.":
            "Your make-up kit you always try to keep close in case of emergency, but sadly you can't open door with it"
            call increase_charm

    "Suddenly, door open and you see your father, dressed in rather formal attire. He looks at you worried."

    dad "You're late Bianca. I was afraid something may have happened to you."

    b "Sorry dad, I forgot to call you..."

    dad "About what?"
    
    menu:
        b "About..."
        

        "my volleyball training":
            b "My volleyball training took longer than expected. Way longer. Out coach is dead serious on us doing well this season."
            dad "Go Ladybugs!"
            b "...yeah..."
            call increase_fitness

        "the charity meeting":
            b "Charity meeting took longer than usual."
            dad "Charity meeting?"
            b "You remember when I told you that we are in charge of this year's annual bake sale?"
            dad "Yeah. What are you raising money for?"
            b "Mr. Norton's house burned down a few weeks ago, so we are trying to help in any way possible."
            dad "That's very kind of you."
            b "Thanks dad!"
            call increase_empathy
        
        "falling asleep in library":
            b "I kinda fell asleep in library."
            dad "Really?"
            b "Yeah. I was suposed to just do my homework asignment but I guess my body needed some rest after this whole week of exams."
            dad "I'm sure you passed them with flying colours after studing this much."
            b "I hope so."
            call increase_smarts

    dad "Anyway. There is a pumpkin pie from your grandma in a fridge in case you get hungry"

    b "Are you going somewhere?"
    
    dad "Don't you remember? I'm taking your mom to the theatre tonight."

    b "Ooo... A halloween date! That's really nice of you daddy!"

    dad "I'm afraid the play have nothing to do with halloween, but your mom..."

    "You can hear the footsteps of high heeled boots as your mom enters the room. Similar to dad she is dressed quite elegant."

    dad "...insisted"

    mom "Oh come on Frank, I'm sure you'll love it."

    dad "If you say so."

    mom "Im glad you're back Bianca. We realized that you forgott a keys so we couldn't leave without you coming back."

    b "Thanks mom."

    mom "Oh, you're welcome. Lucky, we should be there on time. Unlike the last time..."

    menu:
        "I guess mom is talking about THAT last time":

            "I'm sorry im not faster"





