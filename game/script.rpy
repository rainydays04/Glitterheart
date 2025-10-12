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
image bg danceRoom = im.Scale("dance.png",1920,1080)

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
default isla_points = 0
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
            s "I can show you more of what I do if you want? My dorm is in the east wing and you can swing by after classes"
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

    if meet_isla == True:
        show bg library with fade
        narrator "The library is not exactly empty when Hana walks in, but it's enought to calm her mind down from the hectic day"
        narrator "Isla is behind the counter, books floating around her under her control as Hana approaches"
        menu:
            "Wait for her to finish":
                narrator "Hana waits there patiently for Hana to notice her presence. In the quiet of the library, Isla's humming is loud enough to make out"
                narrator "After a few minutes, Isla looks up at Hana, smiling as she notices her"
                i "Hey! You made it, I wasn't sure you were gonna show."
                mc "I wanted to check out the committee and you know, meet others. And talk to you more of course"
                i "Of course of course. The rest are on their assignments at the moment. Many are Tier 2 and 3 up so they went out as soon as assignment came out yesterday"
                mc "Ah I see"
                menu :
                    "Ask about her assignment"
                    "Yes":
                        mc "What about your assignment for this month?"
                        i "..."
                        narrator "She does a small spin, arms out gesturing to the room, the library"
                        i "This, currating spell books for teachers for this class semester. Helping students with books"
                        mc "I thought that this was for volunteering?"
                        i "It is, but it's my assignment for the month and probably the rest of the semester too since I spend so much time here "
                        mc "But, will you ever get higher tier assignments?"
                        i "I will, actually I'm still on track to be a Luminara"
                        mc "How is that if you don't go on missions?"
                        narrator "She gives Hana a mischevious look as she reaches for her phone and shows her an email"
                        i "ok, im not suppose to tell anyone this, but there are several people, missions even, that involve transferring top secret books"
                        mc "Oh my-"
                        i "STARS I KNOW"
                        $ discovery_points+=5

                    "No":
                        mc "So you're doing all this by yourself? Let me help"
                        i "It's alright, I do it alone most days"
                        mc "Well now you have me"
                        narrator "Hana takes a stack of books and begins organizing them to which Isla bows slightly to show her gratitude"
                    
            "Say Hi to her":
                $ isla_points +=3
                narrator "Hana taps her shoulder"
                mc "Hi, Isla"
                i "Ah! Oh my stars you scared me"
                mc "Oh- sorry sorry"
                i "It is alright, honestly. It's just rare  for someone to talk to me in the libarary especially at the beginning of the month"
                mc "What about the other committee members?"
                i "They are often out on their missions, second and third tiers"
                menu :
                    "Ask about her assignment"
                    "Yes":
                        mc "What about your assignment for this month?"
                        i "..."
                        narrator "She does a small spin, arms out gesturing to the room, the library"
                        i "This, currating spell books for teachers for this class semester. Helping students with books"
                        mc "I thought that this was for volunteering?"
                        i "It is, but it's my assignment for the month and probably the rest of the semester too since I spend so much time here "
                        mc "But, will you ever get higher tier assignments?"
                        i "I will, actually I'm still on track to be a Luminara"
                        mc "How is that if you don't go on missions?"
                        narrator "She gives Hana a mischevious look as she reaches for her phone and shows her an email"
                        i "ok, im not suppose to tell anyone this, but there are several people, missions even, that involve transferring top secret books"
                        mc "Oh my-"
                        i "STARS I KNOW"
                        $ discovery_points+=5

                    "No":
                        mc "So you're doing all this by yourself? Let me help"
                        i "It's alright, I do it alone most days"
                        mc "Well now you have me"
                        narrator "Hana takes a stack of books and begins organizing them to which Isla bows slightly to show her gratitude"
                i "Anyways, you said you had an interest in the committee?"
                mc "Yeah, and also spending time at the library more"
                i "Oh yeah, I've seen you studying here a lot. Late nights too. You spend a lot of time in the training grounds too, correct?"
                mc "Ah yes,"
                #embarred look hana
                i "Well, hopefully the library committee is not too much strife on you. We get a few perks too"
                mc "Oh?"
                i "We can choose the books ordered. Say I want to get the newest book by my favorite author. I could get it for a certain section and keep a copy for myself. "
                i "Only one book though for every order, which we make offical order like that every few weeks."
                mc " Oh I see"
                i "What books are you intested in?"
                menu:
                    "Romance":
                        mc "Oh I like romance books"
                        i "Oh I don't read much romance books, but I do know a few good recommendations."
                        mc "Oh yeah, I just like seeing those connections between people you know. Especailly in young adult"
                        mc "Though it boggles me how people have time for that"
                        narrator "Isla walks over with a pile of books, looking up at her"
                        i "For what?"
                        mc "I mean like putting time into a whole romantic relationship"
                        i "Well, I think if you really love someone you find time for them."
                        mc "But during your school years?"
                        i "Well everyone does it to some extent. Maybe not for a person"
                        i "I find time for reading between studying and found a way to involve what I love with what I want to do"
                        mc "Oh... Intresting"
                        i "Well, what do you love doing?"
                        mc "Well um.."
                        mc "Reading every now and then, but most of it has been for school lately"
                        i "Well maybe you should get back to it, just for what you wanna do"
                        mc "gosh I had not have had time for romance novels in quite a bit"
                        narrator "Isla hands over a pileof romance novels"
                        i "I've been meaning to explore more genres, right? So uh, I have a list of romance books that maybe we could read together. Book club kinda vibe"
                        mc "i'd love that yeah. Reading these together and checking back up with each other?"
                        i "Yes yes. Here we could do..."
                        $ isla_points +=10
                        $ discovery_points +=10
                        narrator "They two chose out a book and planned to pic"
                    "Horror":
                        mc "I like horror novels, I like the thrill"
                        i "My poor heart could not handle that"
                        mc "Oh I could give you some reccomendations, albeit it has been a while since I read anything really"
                        i "Sure, I always want to try something new"
                        $ isla_points +=8
                        $ discovery_points+=5
                        narrator "Isla and Hana spent several hours conversing about different horror novel. Isla warming up to the genre"
            
                    "Classics":
                        mc "I'm into the classics"
                        i "Me too! Gosh I absolutely love Janie Heartwell's work"
                        mc "I have actually been meaning to get into more of her work."
                        i "I could definetly you show you!"
                        mc "I'd love that"
                        narrator "Isla introduced Hana to several books, going through different classics"
                    narrator "The sun starts to set and students begin to leave"
                    i "Oh my we've been here for hours"
                    mc "Oh right, I should head back to my dorm"
                    i "Yeah same"
                    narrator "Isla begins to clean up"
                    i "I'll see you around?"
                    mc "Yeah, see you"
    if meet_luna == True:
        show bg danceRoom with fade
        narrator "The music room is dusty from disuse,instruments pushes aside. Luna is in the centre dancing in front of the mirror to a hip-hop song."
        menu:
            "Watch her":
                narrator "Hana leans against the door nonchalantly, crossing her arms as she watches Luna, mesmerized by her movements"
                narrator "Once the music stops, Luna is panting and staring down at the floor, already tired from all her physical efforts"
                mc "Wow"
                narrator "Luna looks over in Hana's direction and smiles"
                l "Enjoying the show?"
                mc "Yeah, well your a good dancer"
                l "So are you"
                mc "You haven't even seen me dance before?"
                l "I don't need to see you dance to know your a good dancer"
                narrator "She summons a simple spell, one that causes the lights to dim and strings of light show in parts of the room"
                mc "What is this"
                l "Tier 3 spell magic. Honing magic from when you dance. It focuses your magic"
                mc "Woah"
                l "Neat right? I've been having the magic fill the room during dances. Each dance produces a different kind of magic"
                narrator "She takes the newest looking string and brings it over to show. It is pink and firey"
                l "Learn to feel it, learn to hone it by producing it "
                mc "So wait let me get this straight. You have the physical form of the magic by..dancing?"
                l "Exactly. Think like making a potion"
            "Join her":
                narrator "After observing the general beat and rhythm. Hana steps forward quietly, her reflection next to Luna's in the mirror"
                
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
                        narrator "The sticky notes are full of reminders or mini diary entries from the day. Notes like Sophia's favorite class"
                        narrator "Sophia picks up on Hana leaning in on the sticky notes"
                        $ Sophia_points-=2
                        s "Hey, those are private."
                        narrator "Hana jolts back in shock"
                        mc "Sorry, I didn't know. They just seem so interesting. What are they notes on?"
                        narrator "Sophia ponders a bit and then sits up"
                        s "I like to write down my favorite thing about everyday. Helps me stay in the present and not the past"
                        mc "That's really thoughtful"
                        s "Yeah..."
                        narrator "Sophia shifts over on the floor indicating that she is ready to talk"

                    "Books":
                        narrator "As Hana sits at the foot of Sophia's bed, Hana sees a pile of books there"
                        narrator "As Hana looks through the books, expecting them to be another pile of history books, it seems as though they are instead Manga"
                        mc "Hm..."
                        narrator "Hana flips through them  as she waits for Sophia to finish her work"
                        s "..."
                        s "Oh are you looking at my books?"
                        $ Sophia_points += 2
                        mc "Oh yeah, sorry they just seemed so intersting"
                        mc "Why do you have so much manga if I may ask?"
                        narrator "Sophia perks up at the question"
                        s "They are what made me want to study history in the first place. All the same genre over the same years and even better we see that play out in OUR world. Really how luck are we?"
                        mc "I never thought of it like that"
                        s "Well the more you know"
            "Desk":
                narrator "Hana takes a seat at the desk by the window. Cleaner then the rest of the room, it neatly has a letter set on the table and a folder for all her classwork"
                menu:
                    "Ask about mission":
                        mc "Hey, I never asked, but your level got their assignments for the month, correct?"
                        s "Yeah, I got a tier 3 assignment. I am partnering with a local university team to help with their mana study for prospective Luminaras at that level "
                        mc "I didn't know there was such an assignment, thought it was being put into those teams to be that"
                        s "They adjust based on level and interst. Again, most only got the Luminara route"
                    "Ask about letter set":
                        mc "Your letter set is really pretty, you use it a lot?"
                        $ Sophia_points+=4
                        s "Oh yeah, I write to my parents a lot. Keep them upto date with my studies"
                        mc "That is so sweet"



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
        mc "It's almost curfew, I should head out."
        s "Oh"
        s "Oh well, do you wanna bring some books back?"
        menu:
            "Yes":
                mc "Yes please"
                $ Sophia_points+=5
                $ discovery_points+=3
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