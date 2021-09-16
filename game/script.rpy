# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

define c = Character("Chad")


# The game starts here.

label start:
    call initialize

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    $ outp =  stats.Output

    menu:
        "[outp]"
        "Life is good" :
            call yes
        "Killed the wife":
            call no

    call increase_smarts

    call increase_charm

    call increase_trickery

    call increase_empathy

    call increase_fitness


    call decrease_smarts

    call decrease_charm

    call decrease_fitness

    call decrease_trickery

    call decrease_empathy
    call decrease_empathy
    call decrease_empathy
    call decrease_empathy
        
    $ outp =  stats.Output

    "[outp]"

    return

    label yes:

        c "Yeah it kinda goes"

        return

    label no:

        c "Fock ya ya cunt!"

        return

    

