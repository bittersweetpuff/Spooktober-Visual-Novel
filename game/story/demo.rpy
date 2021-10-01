screen hello_world():
        text "Hello, World." size 40
label demo:


    "Ok so this is a test"


    centered "{size=+20}{font=Gothic_Birthday_Cake.ttf}The End{/font}{/size}"

    

    "You see Bradley in front of you"

    show bradley normal at center1

    by "O hey Bianca, didnt see you there" 

    by "I've Been waitning for you for quite long now... "

    show bianca normal at left2
    show bradley normal at right2


    menu:
        by "what took you so long?"

        "I was dressing up":
            b "I was dressing up. It takes time you know"

        "I was taking a shower":
            b "I was taking shower after training."

    by "Oh, nevermind... we have a party to go to."

    by "Oh, is that Helen?"

    hide bianca
    hide bradley

    show bianca normal at left3:
  
    show bradley normal at right3:

    show helen normal at center3: 


    h "Hey Guys"

    by "Hey Helen, how are you?"

    menu:
        h "Doing quite good, how about you Bianca?"

        "Good":
            b "Good"

        "Hungry":
            b "Im hungry..."



