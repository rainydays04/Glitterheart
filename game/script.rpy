# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define mc = Character("Hana")
define t = Character("Ms.Melissa")
define c = Character("Cynthia")

image bg classroom = im.Scale("classroom.png",1920,1080)
image bg empty = im.Scale("empty.png",1920,1080)
image bg dorm = im.Scale("dormRoom.png",1920,1080)
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg empty

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.
    mc "Girls come to Glitterheart Academy to learn the art of magic, service, and beauty."
    mc "I always felt behind, but isnt that what everyone feels?"
    mc "I think today was a reminder. I am behind."

    scene bg classroom
    show Melissa
    mc "I don't see why I wasn't given an assignment for the month"
    t "Look Hana, your effort is there, but lacking in results. Your not ready to be given an assignment."
    mc "I could still take a simple one. Community service, teacher's assistant-"
    t "Fine. I'll give you an assignment. Give me an essay why you want to be a Glitterheart."
    mc "That's it?"
    t "Yes. Now go."
    hide Melissa with dissolve
    scene bg dormRoom with fade
    show Cynthia
    





    return
