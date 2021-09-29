# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("Bianca")
define by = Character("Bradley")
define h = Character("Helen")
define r = Character("Robert")
define t = Character("Tyrone")
define w = Character("Bradley?")


image bianca normal = "images/characters/bianca.png"
image bradley normal = "images/characters/bradley.png"
image helen normal = "images/characters/helen.png"
image robert normal = "images/characters/robert.png"
image tyrone normal = "images/characters/tyrone.png"
image witch normal = "images/characters/witch.png"

image bg room = "images/backgrounds/bg_room.png"
image bg parking = "images/backgrounds/bg_parking.png"
image bg outside = "images/backgrounds/bg_outside.png"
image bg park = "images/backgrounds/bg_park.png"
image bg forest = "images/backgrounds/bg_las_01.png"
image bg deepforest = "images/backgrounds/bg_las_02.png"
image bg witchhosue = "images/backgrounds/bg_chata.png"
image bg stacy = "images/backgrounds/bg_end_01.png"
image bg wire = "images/backgrounds/bg_druty.png"
image bg cat = "images/backgrounds/bg_kot.png"
image bg traps = "images/backgrounds/bg_pulapka.png"
image bg river = "images/backgrounds/bg_rzeka.png"
image bg scarecrow = "images/backgrounds/bg_strach.png"
image bg cloth = "images/backgrounds/bg_ubranie.png"
image bg yaga = "images/backgrounds/baba_jaga_inside.png"

# The game starts here.

label start:
    call inintialize_variables from _call_inintialize_variables

    #call demo

    #call opening_scene from _call_opening_scene

    call cat_sighted
    #call park_sounds
    #call forest_screams
    return

label inintialize_variables:
    call initialize from _call_initialize
    define spooks_encountered = 0
    define robert_alive = True
    define tyrone_alive = True
    define helen_alive = True
    return
