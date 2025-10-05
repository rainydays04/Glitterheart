# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#characters
define mc = Character("Hana")
define t = Character("Ms.Melissa")
define c = Character("Cynthia")
#backgrounds
image bg classroom = im.Scale("classroom.png",1920,1080)
image bg empty = im.Scale("empty.png",1920,1080)
image bg dorm = im.Scale("domRoom.png",1920,1080)


# character images
image Melissa = im.Scale("Melissa.png",1000,1000)
image Hana = im.Scale("Hana.png",1000,1000)
image Cynthia = im.Scale("Cynthia.png",1000,1000)

#relationship points
default Cynthia_points = 0
default discovery_points = 0
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
    show Hana at left
    mc "I don't see why I wasn't given an assignment for the month"
    show Melissa at right
    hide Hana
    t "Look Hana, your effort is there, but lacking in results. Your not ready to be given an assignment."
    hide Melissa
    show Hana at left
    mc "I could still take a simple one. Community service, teacher's assistant-"
    show Melissa at right
    hide Hana
    t "Fine. I'll give you an assignment. Give me an essay why you want to be a Glitterheart."
    hide Melissa
    show Hana at left
    mc "That's it?"
    show Melissa at right
    hide Hana
    t "Yes. Now go."
    hide Melissa with dissolve
    
    scene bg dorm with fade
    hide Hana
    mc "I share a dorm with Cynthia. She is practically perfect. I wonder how her day went."
    show Cynthia at right
    c "Hey Hana! How was class?"
    hide Cynthia
    show Hana at left
    mc "Great, oh where are you headed?"
    show Cynthia
    hide Hana
    c "Preparing for my assignement. I just got a tier 2 assignment! Patroling a village nearby"
    menu:
        "Congratulate her":
            hide Cynthia
            show Hana at left
            mc "Really? Great job Cynthia!"
            show Cynthia at right
            hide Hana
            c "Thanks! Do you want anything from the village?"
            $ Cynthia_points += 20
            menu:
                "Yes please!":
                    hide Cynthia
                    show Hana at left
                    mc "Maybeee a bracelet?"
                    show Cynthia at right
                    hide Hana
                    c "I'll make sure to get you one!"
                "No thanks":
                    hide Cynthia
                    show Hana at left
                    mc "Um no thanks, I'm good."
                    show Cynthia at right
                    hide Hana
                    c "Aw, alright"
        "Act indifferent":
            hide Cynthia
            show Hana at left
            mc "Oh, tha's nice."
            show Cynthia at right
            hide Hana
            c "Yeah.... Do you want anything from the village?"
            $ Cynthia_points -= 10
    hide Cynthia with moveoutright
    show Hana
    mc "Tier 2 already...I should really start up on my assigment."
    mc "..."
    mc "Why did I join Glitter Heart...?"
    #help??what are these options
    menu:
        "To become stronger":
            mc "My powers were weak back them, I want to become strong"
        "To look good":
            mc "Kids often bullied me for my looks...my weakness. I want to change that"
        "To escape my old life":
            mc "I hated the village. Im glad im free from it"
    mc "Let me write that down"

    jump classroom_scene
label classroom_scene:
    scene bg classroom with fade
    show Hana at left





    





    return
