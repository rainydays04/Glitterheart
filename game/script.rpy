# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define mc = Character("Hana")
define t = Character("Ms.Melissa")
define c = Character("Cynthia")

image bg classroom = "classroom.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg classroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show 

    # These display lines of dialogue.
    mc "Hello, world!"

    return
