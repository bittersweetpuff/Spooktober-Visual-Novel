# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("Bianca")
define by = Character("Bradley")
define h = Character("Helen")


image bianca normal = "images/characters/bianca.png"
image bradley normal = "images/characters/bradley.png"
image helen normal = "images/characters/helen.png"


# The game starts here.

label start:
    call inintialize_variables from _call_inintialize_variables

    #call demo

    #call opening_scene from _call_opening_scene

    call meeting_bradley
    
    return

label inintialize_variables:
    call initialize from _call_initialize
    define spooks_encountered = 0
    define robert_statatus = "away"
    define tyrone_statatus = "away"
    define helen_statatus = "away"
    return
