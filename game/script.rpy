# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#characters
define mc = Character("Hana")
define t = Character("Ms.Melissa")
define c = Character("Cynthia")
define l = Character("Luna")
define s = Character("Sophie")
define i = Character("Isla")
define idk = Character("???")

#backgrounds
image bg classroom = im.Scale("classroom.png",1920,1080)
image bg empty = im.Scale("empty.png",1920,1080)
image bg dorm = im.Scale("domRoom.png",1920,1080)
image bg library = im.Scale("library.png",1920,1080)
image bg village = im.Scale("village.png",1920,1080)
image bg dorm2 = im.Scale("histDorm.png",1920,1080)

# character images
image Melissa = im.Scale("Melissa.png",1000,1000)
image Hana = im.Scale("Hana.png",1000,1000)
image Cynthia = im.Scale("Cynthia.png",1000,1000)

#relationship points
default Cynthia_points = 0
default discovery_points = 0
default meet_luna = False
default meet_sophia = False
default Sophia_points = 0
default meet_isla= False
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
            hide Hana
            show bg empty with fade
            show bg village with fade
            #dialouge about her friends or like girls from the village bullying her
            #then fade back to her like...stuff
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
            #flashbck family sneaking her books scene
            mc "They gave me everything I needed to achieve my dreams. I want to make them proud."
    mc "Ill write about that for my essay, hopefully its good enough."
    narrator "After working on her essay for a while, the sun begins to set"
    mc "{i}yawn{/i} its getting late"
    mc "Well this essay looks good anyway, I'll turn it in tomorrow and maybe I'll be given a real assignment"
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
    t "..."
    if discovery_points == 5:
        t "hmm... proving others wrong is always a good motivator. Spite can be powerful. But is that all you want?"
        t "You become a Luminara to protect others, not to spite a girl from your 7th years."
    if discovery_points == 8:
        t "Learning is always noble, you will always learn regardless of what you are doing no matter where you are in life."
        t "But become a Luminara is not just learning, it about teaching, protecting. It is about action with magic, not knowledge of."
    if discovery_points == 3:
        t "hmm...I see."
        t "I understand your family must be  very important to, especially with how much they helped you get here."
        t "But becoming a Luminara should not just be to repay someone. It is your future, your life. You must want it for yourself."
        t "Being a luminara is a lifelong commitment, not just a way to repay someone."
    t "Your getting somewhere, Hana. But I need you to think deeper. Why did you join Glitterheart Academy? Why do you want to become a Luminara?"
    t "I want you to write a new essay, take your time with it. It isnt due until next month. I expect a thorough answer by then."
    hide Melissa
    show Hana
    mc "...Yes I understand. Thank you Ms.Melissa."
    hide Hana with moveoutleft
    hide Melissa with fade
    scene bg empty with fade
    jump act_2
    return

label act_2:
    scene bg library with fade 
    show Hana with moveinleft
    mc "Perhaps here I can find some inspiration. History books maybe or perhaps some literature."
    menu:
        "Look at history books":
            $ discovery_points -= 2
            $ meet_sophia = True
            #add image or animation of her going through history books
            mc "I never really enjoyed history. Lots of dates and names to remember."
            mc "..."
            mc "But knowing the past is important, seeing how it effects current day and all."
            narrator "From the other side of the shelf, Hana hears someone snickering. A cheery know-it-all voice jeering between the books."
            idk "It is! History is one of the most important subjects you can learn!"
            narrator "From the side of the shelf, a girl with curly brown and glasses steps out, a pile of books in hand"
            #add image of sophie
            narrator "The short girl reaches her hand out to Hana with a bright smile, struggling to balance the books in one hand"
            s "Hi Hi! Sophie! It's rare to find someone ACTAUALLY interested in history around here!"
            narrator "To say her enthusiasm is overwhelming would be an understatement.Hana shakes Sophie's hand"
            mc "Hana, first year. I don't really like history all that much really"
            #frowning face
            s "Ah well, what are you looking for?"
            mc "Just some content for an essay I need to write"
            s "On what?"
            #hana being slightly embarrased
            mc "Just for the reason I joined Glitterheart in the first place"
            s "Oh so the big questions."
            #thinking face before answering
            s "I like to imagine people's reasons reveal themselves over time, like in history books. There is not only the aftermath, but the add-up"
            s "I personally joined to learn about the history of magic. I want to become a scholar who preserves the history of magic for future generations"
            mc "That's kinda cool"
            mc "I thought most people who came to Glitterheart wanted to become Luminaras"
            s "Just because the school produces many alum who later become Luminaras does not mean that is is the only path."
            s "There are many roles that serve society and often you just have to find how your own interest play into that"
            mc "And I'm assuming history and become a scholar is your way of serving society?"
            s "Society and myself"
            mc "I see"
            s "I can show you more of what I do if you want? I usually hang out with a study group at the cafe"
            mc "I'll see if I can come by"
            s "Alright!"
            narrator "Sophie stumbles off, moving side to side to ensure none of her books fall"        
        "Look at fiction books":
            $ discovery_points += 5
            #add image or animation of her going through fiction books
            mc "Oh look at this."
            mc "I used to love reading this book as a kid. It's about a young ballerina who went into the real version of the Swan Lake ballet."
            mc "I almost wanted to go into ballet after reading this."
            #introduce new character who likes ballet and introduces herself
            #idea her is for her to be a friend an mayb
            $ meet_luna = True
            narrator "You hear someone clearing their throat."
            idk "Sorry, hi. I couldn't help but ovehear you mention ballet?"
            narrator "Hana looks over to the see a girl with blonde hair and green eyes, towering slightly over her, but still managing to look so meek"
            mc "Oh, yeah I was just looking through some books. I used to love dancing as a kid"
            narrator "The girl's eyes light up"
            idk "I love ballet! I'm Luna, by the way. I have been trying to start a dance club here, but I haven't gotten enough interest to get it started. "
            narrator "Hana shakes the Luna's hand"
            mc "I'm Hana. I thought you only needed interest to create club if it can connect to Tier missions or skill?"
            l "That's the thing most people don't know. Dancing is a skill, it improves balance, flexibility, and strength. Many Luminaras practice dance to assist in magical control"
            mc "Really? I never knew that, had I known I would have gotten into dance sooner"
            narrator "Luna smiled brightly, leaning forward"
            l "Well, if you still want to try, I already have the room reserved. You can come by after class today?"
            mc "You know what, sure why not"
            l "Great, see then!"
            #luna leaves the scene
            narrator "Luna waves goodbye and skips off down the aisle of the library"
            
        "Look at poetry books":
            $ discovery_points += 3

            mc "Poetry huh? Maybe if I write poetically enough, I'll get off the hook a bit more"
            mc "Never read much though and oh- I think I know that author"
            narrator "Hana attempts jumping to the top shelf to grab a book, but it slips from her grasp"
            #animation of her finding some poetry books, a book falling
            idk "Careful!"
            narrator "To her suprise, no book hits her head. Instead it is a shrill voice from behind her"
            #show Isla
            $ meet_isla = True
            narrator "Hana turns around and sees a brunette with green eyes, frozen midway through a karate chop motion. The book Hana was trying to reach for now having flown across the isle"
            idk "We have stools you know?"
            narrator "She looked as some would say 'thoroughly pissed' "
            mc "Sorry, I was just in such a rush I didn't see them"
            narrator "Hana looks over at the girl and sees a name tag that read {i}Isla{/i}"
            i "Well now you know for next time"
            narrator "An awkward silence falls upon the two"
            mc "So...do you volunteer here?"
            i "I am part of the library committee"
            mc "We have one of those?"
            narrator "Isla crosses her arms and rolls here eyes"
            i "Yes, but the school doesn't advertise it nearly enough"
            mc "Ah, I see. So what do you guys do?"
            narrator "Her eyes sparkle slightly as she uncrosses her arms, standing straighter as she begins to speak"
            i "We order all the books for the library here. Curate them, organize them, and set up events like book sales then donate them to kids"
            narrator "Hana looks up to her with slight intrigue"
            mc "How many people are in it?"
            narrator "She shifts back and forth, biting the inside of her cheek"
            i "Like...3, but we're really efficent"
            mc "I could join if you li-"
            i "YES"
            i "Sorry, im just...really exicted. Meet me here at lets say...16:00?"
            mc "Sure things"
            #isla leave right
            narrator "Isla skips of happily behind the library counter"
    mc "My essay isn't due for a month, so why not spend some time"
    mc "I think I cling to Cynthia to much, meeting new people will be good for me"
    show bg empty with fade

    if meet_luna == True:
        #library
    if meet_isla == True:
        #dance room
    if meet_sophia== True:
        show bg dorm2 with fade
        #show sofia
        #slide in hana
        narrator "When Hana walks into the room, she sees Sofia sitting in the center of her room, surrounded by books, papers scatted across her bed"
        mc "Sorry for walking in without invite"
        narrator "She doesnt even look up from her work as she responds"
        s "No no its fine, sit anywhere. Just finishing up a thought"
        menu:
            "Where should Hana sit?"

            "Bed":
                narrator "Hana goes to sit on the bed which has a pile of books and papers are the foot of it, on the wall there are sticky notes hand written"
                menu:
                    "What to inspect first?"

                    "Sticky notes":
                        #see sofia's notes and what she does in a day
                        #menu on
                    "Books":
                        #not history books but lots of shojo manga like magical girls stuff
                    "Paper":
                        #drawings and sketches of a art
            "Desk":
                narrator "Hana takes a seat at the desk by the window. Cleaner then the rest of the room, it neatly has a letter set on the table and a folder for all her classwork"
                menu:
                    "Ask about mission":
                    "Ask about letter set":


            "Floor":
                narrator "Hana looks around the room and decides that it would be better to sit next to her prospective friend"
                narrator "Sophia looks up and smiles at her"
                s "It wont take long, here, look"
                narrator "She holds up a timeline map of the most notable alumni from Glitterheart, not only Luminaras but scholars, writers, and artists"
                mc "Wow, I don't know about half these people"
                s "Oooohh you definetly know them. See this one wrote the Stars before Time and this one acted in Lilie Deception"
                mc "You're kidding..."
                narrator "Sophia shakes her head, and pulls out what seems to be a box of books from behind her"
                s "These are all the past yearbooks, feel free to look through them. I've scrapbooked some so that"
                mc "Is that how you got all this information?"
                s "Yes, and more. There used to be so many clubs in Glitterheart, but once more alumni started to become notable Luminaras well..."
                s "They allocated more resources to their Lumins program and less to other possible paths"
                mc "That actually sucks"
                s "Yeah, but there are many students working around here to fix that, I'm doing my part"
                mc "..."
                mc "You know I never thought of exploring paths outside of being a Luminara"
                s "Many people don't, but I think you should know its not the only option"
                mc "Yeah"
                narrator "Hana and Sophia scramble on the floor, exchanging books and information for hours"
                #if i have the time maybe add menu for which books she reads
                mc "It's almost curfew, I should head out."
                s "Oh"
                s "Oh well, do you wanna bring some books back?"
                menu:
                    "Yes":
                        mc "Yes please"
                        $ Sophia_points+=5
                        narrator "Sophia scrambles and passes over three books to Hana"
                        s "See how you like these and you can always come back "
                        mc "Wow, this a lot, thank you Sophia."
                        s "Of course, see you later"
                        
                        

                    "No":
                        $ Sophia_points-=3
                        mc "Oh no that's alright, thank you though"
                        narrator "Sophia looks a bit sad when told this, but manages a small grateful smile. Hana can't help but feel a bit guilty"
                        s "That's ok! you probably have a lot to carry already with assignments and classes. See you around then?"
                mc "See you"
                hide mc with moveoutleft

        show bg empty with fade

        





    return
            
       
    




