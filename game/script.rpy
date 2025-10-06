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
    mc "To become Luminaras, the protectors of the realm."
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
            c "Yeah.... I'll leave you to your assignment then."
            $ Cynthia_points -= 10
    hide Cynthia with moveoutright
    show Hana
    mc "sigh"
    mc "Tier 2 already...I should really start up on my assigment."
    mc "..."
    mc "Why did I join Glitter Heart...?"
    #help??what are these options
    menu:
        "To prove the girls from my village wrong":
            #gain 5 discovery points
            #add a flashback scene later
            $ discovery_points += 5
            mc "The girls in my village used to make fun of how my looks, my skill. Coming here, perhaps I could prove them wrong"
        "To learn more about magic":
            #gain 8 discovery points
            $ discovery_points += 8
            #flashback to learning about magic for the first time
            mc "Magic has protected my villages for centeries. Perhaps I could help them, or someone like me from ever expereincing what I did..."
        "To make my family proud":
            #gain 3 discovery points
            $ discovery_points += 3
            #flashbck family sneaking her books scene lwk
            mc "They gave me everything I needed to achieve my dreams. I want to make them proud."
    mc "Ill write about that for my essay, hopefully its good enough."
    hide Hana with moveoutleft
    scene bg empty with fade
        
    scene bg classroom with fade
    show Melissa at right
    t "You finished this quickly Hana"
    hide Melissa
    show Hana at left
    mc "Yes, I wanted to prove to you I could take on the assignment"
    show Melissa at right
    hide Hana
    t "You know assignments, regardless of what they are, are meant to take time and effort."
    t "Well if your rushing this assignment, I'll just grade it right here and now."
    if discovery_point == 5:
        t "hmm... proving others wrong is always a good motivator. Spite can be powerful. But is that all you want?"
        t "You become a Luminara to protect others, not to spite a girl from your 7th years."
    if discovery_point == 8:
        t "..."
        t "Learning is always noble, you will always learn regardless of what you are doing no matter where you are in life."
        t "But become a Luminara is not just learning, it about teaching, protecting. It is about action with magic, not knowledge of."
    if discovery_point == 3:
        t "hmm...I see."
        t "I understand your family must be  very important to, especially with how much they helped you get here."
        t "But becoming a Luminara should not just be to repay someone. It is your future, your life. You must want it for yourself."
        t "Being a luminara is a lifelong commitment, not just a way to repay someone."
    t "Your getting somewhere, Hana. But I need you to think deeper. Why did you join Glitterheart Academy? Why do you want to become a Luminara?"
    hide Melissa
    







    





    return
