# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("{color=#ff0000}Ren{/color}")
define a = Character("{color=#008000}Amelia{/color}")
define y = Character("{color=#ffd700}Yosef{/color}")
define d = Character("{color=#800080}Donovan{/color}")
define o = Character("{color=#fd5d10}Olive{/color}")
define n = Character("{color=#0064ff}Noel{/color}")

define m = Character("{color=#c0c0c0}Mr. Adams{/color}")
define b = Character("{color=#c0c0c0}Elizabeth{/color}")

define e = Character(" ")
define q = Character("{color=#c0c0c0}???{/color}")

define v = Character(" ", kind=nvl)

transform midleft:
    xalign 0.25
    yalign 1.0

transform midright:
    xalign 0.75
    yalign 1.0

transform farleft:
    xalign 0.0
    yalign 1.0

transform farright:
    xalign 1.0
    yalign 1.0

transform qleft:
    xalign 0.35
    yalign 1.0

transform qright:
    xalign 0.7
    yalign 1.0

transform offleft:
    xalign -0.5
    yalign 1.0

transform slidefarleft:
    #xalign 1.0 yalign 1.0
    linear 1.0 xalign 0.0

transform slidefarright:
    #xalign 1.0 yalign 1.0
    linear 1.0 xalign 1.0

transform slideqleft:
    #xalign 1.0 yalign 1.0
    linear 1.0 xalign 0.35

transform slideqright:
    #xalign 1.0 yalign 1.0
    linear 1.0 xalign 0.7

transform slideoffleft:
    #xalign 1.0 yalign 1.0
    linear 1.0 xalign -0.5

transform slidecenter:
    #xalign 1.0 yalign 1.0
    linear 1.0 xalign 0.5

# The game starts here.

label start:

    $ rp = 0
    $ ap = 0
    $ yp = 0
    $ dp = 0
    $ op = 0
    $ np = 0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    stop music fadeout 1

    scene bg gray
    with Dissolve(1.0)

    label enter_name:

        python:
            name = renpy.input("Enter your name:")
            name = name.strip() or "Jackie"

    menu name:
        e "Is the name [name] okay?"

        "Yes":

            menu:
                e "Would you like to know about accessibility options?"

                "Yes":

                    e "Press Shift + A to open the accessibility menu. From there, you can change the text font, activate text-to-speech, and adjust other options."

                    e "For a full list of controls, see the Help section in the menu."

                "No":

                    e "For a full list of controls, see the Help section in the menu."

            e "This game is a work in progress. As such, certain scenes are currently unfinished and may not flow in a coherent manner. Anything currently established in this build of the game is subject to change in the future."

        "No":

            jump enter_name

    menu:
        e "DEVELOPER SKIPS - Choose a part to skip to."

        "Intro Part 1":

            jump intropart1

        "Intro Part 2":

            play music "lazyafternoon.mp3" fadeout 1

            scene bg studio1

            show ren rd at farleft

            show olive rc at qleft

            show donovan ld at qright

            show noel ld at farright

            jump intropart2

        "Intro Part 3":

            scene bg studio1

            show amelia rh at qleft

            show olive ld at qright

            show yosef ld at farright

            jump intropart3

        "Day 2 Start":

            jump day2start

        "CEO Lobby Scene":

            jump ceo_meeting

    label intropart1:

    #Introduction - SCENE START

    show bg black
    with Dissolve(1.0)

    pause .5

    e "A video game tester."

    e "Job description: Responsible for playing video games to test their functionality, identify any bugs or glitches, and report to the game developers. The role is critical to the development process, as testers help developers to create a high-quality video game."

    e "This is the job you applied for, and today is your very first day."

    play music "lazyafternoon.mp3" fadeout 1

    show bg street1
    with Dissolve(1.0)

    e "The company you are working for is Nomina Games, an independent game publisher."

    e "Nomina has put out some of the most highly regarded indie games of the last decade. In the eyes of many, it is a rather prestigious publisher."

    menu:
        e "As you walk in the direction of their office, you feel..."

        "Confident!":

            e "As you assertively stride along, you finally approach your destination..."

        "Anxious...":

            e "As you sheepishly shuffle along, you finally approach your destination..."

    show bg entrance4
    with Dissolve(1.0)

    e "Nomina Games Headquarters..."

    e "You wonder what kind of workplace awaits you behind those doors."

    #e "Only one way to find out!"

    show bg lobby2
    with Dissolve(1.0)

    e "As you walk inside and approach the desk, the secretary greets you."

    show elizabeth ld
    with Dissolve(.5)

    q "Good afternoon. How may I help you?"

    menu:
        e "She greets you politely, but doesn't seem that interested in what you have to say..."

        "I'm the new game tester. Today is my first day.":

            q "Oh, right. My boss mentioned you would be here today."

    b "My name is Elizabeth, and I work the front desk here at Nomina."

    e "She checks her computer screen."

    b "So you're [name]..."

    b "Let's see...ah, so you'll be working with that new team..."

    b "...Good, you finished all your paperwork online. That saves me a lot of trouble."

    b "Once you clock in, you'll want to head upstairs and to the left, to room 214. The building's not super big, so it shouldn't be too hard to find."

    show elizabeth lh
    with Dissolve(.2)

    b "Have fun!"

    e "She sends you off with a smile, and then returns to her work."

    scene bg door3
    with Dissolve(1.0)

    e "You head upstairs and approach the room marked 214. The door is closed, but the room appears to be occupied."

    e "Through the window you can see two people, one wearing red and one wearing purple. They are both sitting at computers, facing opposite each other. You knock on the door..."

    play sound "knockingsound.mp3"

    "Both look towards the door. The one in red gets up to greet you."

    q "Are you our new tester? Come on in!"

    e "The young man beckons you inside."

    show bg studio1
    with Dissolve(1.0)

    show ren rd
    with Dissolve(.5)

    q "Hey there!"

    r "My name's Ren, and I'm a programmer here. What's your name?"

    e "You introduce yourself."

    r "[name]? That's a cool name, but I bet you hear that a lot."

    r "So [name], what do you think of this studio space? These PCs are pretty state of the art. It's a bit overkill for the type of game we're making right now, but they're cool regardless!"

    menu:
        e "There are a dozen or so computers lined up on the desks. They all have a sleek, modern look to them."

        "These look pretty sweet!":

            $ rp += 1
            r "Right? I might have to take some design cues from these for my own PC. {color=#ff0000}+1{/color}"

            r "Anyways, I should let Donovan introduce himself."

        "It's like I've stepped into the future...":

            $ rp += 1
            r "Yeah, that's the popular look for PCs these days. The future is now, as they say! {color=#ff0000}+1{/color}"

            r "Anyways, I should let Donovan introduce himself."

        "They just seem like computers to me.":

            show ren rc
            with Dissolve(.2)

            r "Hmm. I guess that's how most people see them."

            r "Donovan feels the same way."

            show ren rd
            with Dissolve(.2)

    #Change Donovan's intro animations?

    e "You turn your head towards the guy in purple, who has been completely silent until now."

    show ren at slidefarleft

    pause .5

    show donovan ld at qright
    with Dissolve(.2)

    d "My name's Donovan. I'm the writer for our game."

    e "He sits there in awkward silence for a moment, then turns around and goes back to his work."

    hide donovan
    with Dissolve(.2)

    #Change "man!"

    r "Don't sell yourself so short, man! You're the one who came up with the whole pitch for our game, right? That basically makes you the creative director, or some other fancy title!"

    show donovan ld at qright
    with Dissolve(.2)

    d "...I guess so."

    hide donovan ld
    with Dissolve(.2)

    menu:
        r "Psh. Some first impression that was..."

        "What kind of game are we working on, anyway?":

            r "Wait, you don't know? You weren't told when you applied, or when you were interviewed?"

    r "Huh. I guess someone didn't do their job correctly..."

    r "Well, maybe we should wait to give you the lowdown until the others are back. Are the girls still on their lunch break?"

    show donovan ld at qright
    with Dissolve(.2)

    d "They said they were going to that cafe across the street."

    q "We're baaack! And we brought croissants!"

    e "Two young women walk through the doorway, one of them holding a box of pastries."

    show olive rd at offleft
    #with Dissolve(.5)

    show olive at slideqleft

    #show noel?

    pause .5

    q "You guys hungry?..."

    q "Woah! Who are you?"

    e "You introduce yourself to her."

    q "You're the new game tester? I forgot you'd be here today!"

    o "I'm Olive, and my orange-haired friend here is Noel! She's an artist."

    show noel ld at farright
    with Dissolve(.5)

    n "Orange-haired friend? Is that what I am to you?"

    o "You're much more to me than just that! Your hair is just your defining feature, that's all."

    n "I-is that true? I didn't know that's how people thought of me..."

    show noel ls
    with Dissolve(.2)

    e "Noel looks at the floor, embarrassed..."

    show noel ld
    with Dissolve(.2)

    n "L-like Olive said, I also make art!"

    menu commissions:
        n "I'm actually still going to school for art. What I do here is just commission work."

        "Commission work? What's that?":

            show noel lh1
            with Dissolve(.2)

            $ np += 1
            n "Basically, it's when someone online pays me to make a piece of art for them. It's how a lot of digital artists make a living. {color=#0064ff}+1{/color}"

            o "And her art gets exposure, since her clients usually like to post it online for everyone to see!"

            o "Though she has gotten some really, REALLY weird requests before. There was this one time-"

            show noel ld
            with Dissolve(.2)

            n "A-Anyway!"

            n "Now that we're all here, we should probably get back to work."

            r "Hold on. [name] still hasn't been briefed about what we're making."

            o "Huh?"

        "What kind of art do you like to make?":

            n "I usually like to draw, but playing around in digital art programs can also be fun."

            n "I like designing characters, though drawing scenery can also be relaxing."

            show noel lh2
            with Dissolve(.2)

            $ np += 1
            e "She smiles at you, seemingly appreciative of your interest. {color=#0064ff}+1{/color}"

            show noel ld
            with Dissolve(.2)

            n "Well, now that we're all here, we should probably get back to work."

            r "Hold on. [name] still hasn't been briefed about what we're making."

            o "Huh?"

        "Cool. Now, about the game we're making...":

            n "..."

            show noel ls
            with Dissolve(.2)

            e "Noel looks towards the floor again with a sad expression..."

            show noel ld
            with Dissolve(.2)

    show olive rc
    with Dissolve(.2)

    label intropart2:

    o "Wait, you mean you don't know anything about the game? How did that happen?"

    r "Apparently, they aren't telling new hires about the games they're paid to work on..."

    show olive rd
    with Dissolve(.2)

    o "Huh. That's not a mistake I would make! Probably..."

    #r "Well, I'm going to go use the restroom, and then we can talk about the game."

    #n "Why don't we all take a quick breather? I could use a break."

    #r "You just got back from lunch..."

    #o "Meeting new people takes a lot out of her. Don't you remember how exhausted she was by the end of her first day?"

    #n "Do we have to talk about this now?"

    #e "..."

    #e "You decide to excuse yourself and step outside for a moment..."

    #scene bg black
    #with Dissolve(1.0)

    #pause .5

    #play music "lostparadise.mp3" fadeout 1

    #e "Now might be a good time to save your game and take a short break."

    #pause 1.0

    #e "After a quick breather, everyone returns to the studio."

    #show bg studio1
    #with Dissolve(1.0)

    #play music "passingtime.mp3" fadeout 1

    #show ren rd at farleft
    #with Dissolve(.2)

    #show olive rd at qleft
    #with Dissolve(.2)

    #show donovan ld at qright
    #with Dissolve(.2)

    #show noel ld at farright
    #with Dissolve(.2)

    #r "Was that enough break time for everyone?"

    #n "I'll manage."

    o "Oh! Don't forget about the croissants we brought back!"

    e "Remembering the box Olive brought in, everyone grabs a pastry."

    menu:
        r "Alright, now we can tell you about the game, [name]."

        "Let's hear it.":

            r "Since you're the one who came up with the premise, why don't you do the honors, Donovan?"

            d "...Uh, sure."

            stop music fadeout 1

            hide ren
            with Dissolve(.2)

            hide olive
            with Dissolve(.2)

            hide noel
            with Dissolve(.2)

            hide donovan
            with Dissolve(.2)

            #show bg studio1dim
            #with Dissolve(1.0)

            nvl show dissolve

            pause .5

            play music "wintervillage.mp3"

            v "The game we're developing is called The Lonely Star. It is a story-driven adventure game."

            v "You play as a young child, who spends their days playing in the woods near their home."

            v "One day, the child ventures farther from home than usual, and discovers a strange new place that they have never seen before."

            v "Knowing that they have strayed too far from home, the child turns around and goes back the way they came."

            v "However, they soon get lost and cannot find their way home."

            v "Just when the child is about to lose all hope, they hear a soft, calming voice speaking to them."

            v "The voice guides them to a small pond at the foot of a hill. The child looks into the pond, and floating on the surface of the water are small, glowing stars."

            v "The child leans down and touches one of the stars. Another voice comes from it."

            v "The voice is of someone making a wish."

            v "The child reaches into the water and touches more of the stars. All of them, with different voices, repeat various wishes."

            v "The guiding voice from before then tells the child that in order to find a way home, they must grant the wishes spoken by the floating stars."

            v "But who did those wishes belong to, and how would the child make them come true?"

            v "Determined to make it back home, the child sets out to meet the people of this mysterious place and make their wishes reality."

            v "Along the way, perhaps the child will learn more about this strange new place they have wandered into, and find out what it really means to grant people's wishes..."

            nvl hide dissolve

            stop music fadeout 1

            #pause .5

            #show bg studio1
            #with Dissolve(1.0)

            show donovan ld at qright
            with Dissolve(1.0)

            d "...So yeah. That's what I have written for the synopsis so far."

            play music "lazyafternoon.mp3" fadeout 1

            show olive rd at qleft
            with Dissolve(.2)

            show noel ld at farright
            with Dissolve(.2)

            show ren rd at farleft
            with Dissolve(.2)

            n "I-I really like that setup. You're a good storyteller, Donovan."

            show donovan lh
            with Dissolve(.2)

            d "...Thanks."

            e "Donovan ever-so-slightly smiles."

            show donovan ld
            with Dissolve(.2)

        "Actually, I just remembered... (skip story summary)":

            r "Oh, so you WERE given information about The Lonely Star? I guess we don't need to explain too much, then."

    r "Basically, it's an adventure game where you explore a town and get to know the characters who live in it. The goal of the game is to solve the problems of these characters, which are first shown to the player through the wishing stars."

    o "And it has a positive message about communication and learning to understand people better!"

    o "That's what you told us, right Donovan?"

    d "...Yes."

    r "It's not the type of thing that you'd typically think of when you picture a video game, but it's a project that all of us think is pretty neat. Nomina's CEO is pretty invested in it, too."

    menu:
        r "What do you think about it, [name]?"

        "It seems pretty ambitious.":

            d "Does it really? I guess it kind of is in some ways."

            d "It's not a super ground-breaking game, concept wise."

        "The premise is interesting. What's the game inspired by?":

            n "That's something I've been meaning to ask as well."

        "Eh, I was hoping I'd get to test an FPS or something...":

            show ren rc
            with Dissolve(.2)

            r "Oh. Well, sorry to disappoint, I guess."

            show ren rd
            with Dissolve(.2)

            r "Maybe you'll like the game once you start playing it."

            n "Oh, I just remembered..."

            n "I've been meaning to ask you this, Donovan: What was your idea for this game inspired by? Any book or movies, or other video games?"

    show donovan lh
    with Dissolve(.2)

    d "Actually, the idea for The Lonely Star was inspired by a similar adventure game from the 90's called Crescent, which was-"

    o "Hmm...Crescent..."

    o "Like a croissant!"

    e "Olive holds up a half-eaten croissant."

    show donovan ld
    with Dissolve(.2)

    show noel lh2
    with Dissolve(.2)

    e "Donovan doesn't react at all to Olive's keen observation."

    stop music fadeout 1

    e "Suddenly, you hear a knock at the door."

    play sound "knockingsound.mp3"

    pause .5

    show noel ld
    with Dissolve(.2)

    q "I'm not interrupting anything, am I?"

    e "A man in a suit stands in the doorway. Two other people you've never seen before stand behind him."

    play music "passingtime.mp3" fadeout 1

    #hide ren

    #hide olive

    hide donovan
    with Dissolve(.2)

    show ren ld at slideqleft
    #with Dissolve(.2)

    show olive ld at slideqright
    #with Dissolve(.2)

    show gerald rd at offleft
    #with Dissolve(.5)

    pause .5

    show gerald at slidefarleft

    pause 1.0

    n "Hello, sir."

    o "Hi there, sir!"

    q "Haven't I told you guys? There's no need to call me sir. Just call me Mr. Adams. Or Gerald, even!"

    e "The man looks in your direction."

    q "You must be [name], our new tester! Good to finally meet you in person."

    m "I'm Gerald Adams, the CEO and founder of Nomina."

    menu:
        m "In case you don't remember, I was the one who conducted your interview online. We never saw each other's faces, though."

        "The pleasure is mine. *shake his hand*":

            e "You reach your right hand out, and Mr. Adams shakes it."

            show gerald rh
            with Dissolve(.2)

            m "Wow, proper business etiquette! You love to see it."

        "That was you? I thought I was talking to a chatbot...":

            show gerald rh
            with Dissolve(.2)

            m "Ha! You thought I was an AI? That's funny."

            m "Hmm...Using AI for interviews..."

            m "I should look into that idea. Well, I'll probably have Beth look into it..."

    q "Pardon me, Gerald..."

    e "One of the people standing behind Mr. Adams steps forward."

    hide ren
    with Dissolve(.2)

    #pause .5

    show amelia rd at offleft

    show amelia at slideqleft

    pause 1.0

    show amelia ld
    with Dissolve(.5)

    q "You said that you and the new tester never saw each other's faces during the interview? What kind of an interview is that?"

    show gerald rd
    with Dissolve(.2)

    m "A modern interview, that's what kind!"

    m "Younger people these days are under a lot of stress when they're being asked all these questions by someone they barely know. They struggle to maintain eye contact, as well."

    m "With an interview that's only over text, the interviewee feels a lot less pressure. I give them as much time as they need to answer my questions."

    q "Interesting...I didn't know that was a thing."

    e "The other person behind Mr. Adams abruptly steps forward."

    hide noel
    with Dissolve(.2)

    show yosef ra at offleft

    show yosef at slidefarright

    pause 1.0

    show yosef la
    with Dissolve(.5)

    q "Forgive me, Gerald, but that idea is absurd to me!"

    q "How can you have a job interview without face-to-face interaction? The whole point of one is to find out if the person can effectively communicate with others in a shared work environment!"

    q "What you're describing doesn't make any sense to me!"

    show olive lc
    with Dissolve(.2)

    show yosef lc
    with Dissolve(.2)

    q "..."

    q "...Sorry, I flew off the handle a bit there."

    m "You're allowed to have your own opinions, Yosef."

    m "I may or may not take those opinions into consideration, but you're allowed to have them nonetheless."

    m "Though I would appreciate it if you kept your voice down."

    show yosef ld at farright
    with Dissolve(.2)

    q "...Right. I'll make sure to work on that..."

    o "Um, sir? Did you need us for something?"

    m "Hm? Oh, right!"

    m "I came here to greet [name], as well as introduce you to these two."

    e "Mr. Adams gestures towards the woman in green."

    m "This is Amelia. As of today, she will be working on the marketing for The Lonely Star."

    show amelia rh
    with Dissolve(.2)

    a "I look forward to getting to know all of you, along with the game you're making."

    e "Mr. Adams gestures towards the man in yellow."

    m "...And my friend here with no indoor voice is Yosef. He's in charge of the budget for the game."

    e "Yosef approaches you, takes your hand, and shakes it firmly. He then goes around the room and does the same to everyone else."

    y "It's great to meet all of you! I'll help in any way I can!"

    m "While they won't officially be members of your team, you should expect them to consult with you quite often about how the game will be advertised and budgeted."

    a "The game is called The Lonely Star, correct? Gerald filled us in on some of the details."

    a "It's not the most marketable title I've heard, but anything can be made appealing to customers if you put the right spin on it."

    y "And I'm here to make sure that you guys don't bankrupt the company!"

    y "Nomina may be a well-respected name, but I've learned from my time here so far that they aren't made of money!"

    show gerald rc
    with Dissolve(.2)

    m "This uh, isn't really the best time or place to be discussing the company's enterprise value, Yosef..."

    #show gerald rd
    #with Dissolve(0.2)

    m "Well, I'll let you all get further acquainted. I've got work to do..."

    show gerald lc
    with Dissolve(.2)

    show olive ld
    with Dissolve(.5)

    o "Bye, sir!"

    m "..."

    show gerald at slideoffleft
    #with Dissolve(.5)

    pause .5

    hide gerald

    label intropart3:

    play music "gainingtraction.mp3" fadeout 1

    pause 1.0

    y "So, you know Amelia and I now. What does everyone else do here?"

    show amelia rd at slidefarleft

    #pause 1.0

    #show amelia ld
    #with Dissolve(.2)

    pause .5

    show ren rd at qleft
    with Dissolve(.2)

    r "I'm Ren, and I'm the programmer for The Lonely Star."

    a "Are you the only programmer for the game? That sounds like a lot of work."

    show ren ld
    with Dissolve(.2)

    r "It is, but it's rewarding in it's own way. To me, there isn't much that's more satisfying than fixing broken code."

    show ren lc
    with Dissolve(.2)

    r "Though I can't say it doesn't wear on me sometimes, staring at numbers all day."

    show yosef lc
    with Dissolve(.2)

    y "I can defenitely relate..."

    show olive lh
    with Dissolve(.2)

    show ren rd
    with Dissolve(.2)

    show yosef ld
    with Dissolve(.2)

    o "I'm Olive! I do audio stuff for the game!"

    show amelia rc
    with Dissolve(.2)

    a "Audio...stuff?"

    hide ren
    with Dissolve(.2)

    show noel rd at qleft
    with Dissolve(.2)

    n "She's the sound designer for the game."

    show amelia rd
    with Dissolve(.2)

    a "I see. What does that entail?"

    show olive ld
    with Dissolve(.2)

    o "Hmm...I work on sound mixing, making sure everything sounds like it should, that kind of thing."

    y "Are you writing the music for the game?"

    show olive ls
    with Dissolve(.2)

    o "...No."

    e "Olive's enthusiasm seems to have disappeared."

    n "I-I'm Noel. I'm making the art for The Lonely Star."

    show olive ld
    with Dissolve(.2)

    y "You're an artist? Good to see that they haven't replaced you with a computer program yet!"

    show noel rc
    with Dissolve(.2)

    n "Y-yeah, I'm...also glad that hasn't happened..."

    show amelia rh
    with Dissolve(.2)

    a "You must be a talented artist if you've managed to make it your job. Do you mind if I take a look at it some time?"

    show noel lh1
    with Dissolve(.2)

    n "N-no, I don't mind..."

    e "..."

    hide noel
    with Dissolve(.2)

    show amelia rd
    with Dissolve(.2)

    show donovan ld at qleft
    with Dissolve(.5)

    d "..."

    o "Psst...Donovan, I think they're waiting for you to say something."

    d "Hm? Oh..."

    d "I'm the writer for The Lonely Star."

    d "..."

    d "...And my name's Donovan."

    hide yosef
    with Dissolve(.2)

    show ren ld at farright zorder 2
    with Dissolve(.2)

    r "Man, you're hopeless..."

    r "Not only is he writing the story, he's also the one who came up with the whole idea for the game."

    a "Is that right?"

    show donovan ln zorder 2
    with Dissolve(.2)

    d "Yep. I pitched the idea to Mr. Adams, and he was way more into it than I thought he would be."

    d "...But even though I'm the sole writer, I want it to be a collaborative effort. I'd like to get ideas from everybody, so it's not just MY game, but OUR game."

    menu:
        d "Especially from you, [name], since you're the one who's going to play it and help improve it the most."

        "Sounds fun!":

            show donovan lh
            with Dissolve(.2)

            $ dp += 1
            d "...Glad you think so. {color=#800080}+1{/color}"

        "I hope you're not expecting too much from me...":

            show donovan lh
            with Dissolve(.2)

            d "Heh. No need to worry about it that much."

            $ dp += 1
            d "Just keep your feedback honest. That's all we're asking. {color=#800080}+1{/color}"

        "Are you trying to get me do your job?":

            d "What? N-no..."

            show donovan ls
            with Dissolve(.2)

            e "He looks away from you."

            a "I think he's just open to any creative input you might have. That's all."

            show donovan ln
            with Dissolve(.2)

            d "Y-yeah..."

            show donovan lh
            with Dissolve(.2)

            d "Thank you."

    o "Woah, you made him smile a little bit! I can't believe it!"

    o "I've never been able to get him to do that before..."

    r "I think he finds you socially intimidating."

    show olive rd
    with Dissolve(.2)

    o "Me, intimidating? No way!"

    show olive rw
    with Dissolve(.2)

    o "I'm as innocent as can be!"

    show olive rd zorder 2
    with Dissolve(.2)

    a "Do they always talk about you as if you're not in the room with them?"

    show donovan ln zorder 2
    with Dissolve(.2)

    d "Yeah..."

    show yosef ld zorder 1:
        xalign 0.6
        yalign 1.0
    with Dissolve(.5)

    play music "passingtime.mp3" fadeout 1

    y "Well, Amelia, I think that we'll fit pretty well into this group dynamic."

    y "You can spend time with the shy ones, while I hang out with the fun people!"

    show olive ld zorder 2
    with Dissolve(.2)

    show amelia ra
    with Dissolve(.2)

    a "Yosef! Behave yourself."

    a "We're here to do our jobs, not to make friends."

    show amelia rc zorder 1
    with Dissolve(.2)

    a "...Not that I'm opposed to making friends."

    show olive rd
    with Dissolve(.2)

    o "When he said fun people, he had to have been talking about us, right Ren!? Maybe [name], too."

    r "Heh, I'm interested to see how this plays out..."

    r "For now, why don't we all take a look at the game together? [name] can play it for the first time."

    show amelia rd
    with Dissolve(.2)

    #show donovan at slidecenter

    show noel rd at left zorder 2:
        xalign 0.15
        yalign 1.0
    with Dissolve(.5)

    n "That's a good idea."

    show noel rs
    with Dissolve(.2)

    n "N-new people will be looking at my art...That makes me nervous."

    show noel rd
    with Dissolve(.2)

    menu:
        r "Just keep in mind that the game is still in pretty early development. You ready to play?"

        "Born ready!":

            show ren lh
            with Dissolve(.2)

            r "That's what I like to hear!"

        "I guess so...":

            r "Love the enthusiasm!"

            y "I think that was sarcasm."

            a "I think we all know what sarcasm sounds like, Yosef..."

    r "Alright, I'll go ahead and boot up the most recent build..."

    stop music fadeout 1

    scene bg black
    with Dissolve(1.0)

    e "You and the team spend the rest of the work day playing The Lonely Star and going over its development plans."

    e "The current build is pretty simple, but it has a lot of potential."

    e "With a team like this working on it, only time will tell how the final product will turn out..."

    #Introduction - SCENE END

    scene bg black
    with Dissolve(1.0)

    #pause .5

    play music "lostparadise.mp3" fadeout 1

    e "Now might be a good time to save your game and take a short break."

    pause 1.0

    stop music fadeout 1

    label day2start:

    scene bg lobby2
    with Dissolve(1.0)

    play music "lazyafternoon.mp3" fadeout 1

    e "The next day..."

    show elizabeth ld
    with Dissolve(.5)

    q "Good morning."

    q "You're [name], right?"

    e "You confirm that your name is in fact [name]."

    show elizabeth lh
    with Dissolve(.2)

    q "Good, I got it right."

    menu:
        q "Do you happen to remember my name?"

        "Eliza.":

            show elizabeth ld
            with Dissolve(.2)

            b "It's Elizabeth, actually..."

            b "My family members call me Eliza."

            b "You can just stick with Elizabeth for now."

        "Liz.":

            show elizabeth ld
            with Dissolve(.2)

            b "It's Elizabeth, actually..."

            show elizabeth lc
            with Dissolve(.2)

            b "Have you, uh, heard someone who works here call me by that name?"

            b "There are only a few specific people who call me that..."

            b "You can just stick with Elizabeth for now."

            show elizabeth ld
            with Dissolve(.2)

        "Beth.":

            show elizabeth ld
            with Dissolve(.2)

            b "It's Elizabeth, actually..."

            b "Did Mr. Adams refer to me as Beth?"

            b "I only let friends call me that."

            b "Since we just met, you can stick with Elizabeth for now. No offense."

        "Elizabeth":

            b "Thank you! No one ever remembers my name on their second day."

    b "Well, I should let you head upstairs and get to work. You've got a game to test, right?"

    scene bg black
    with Dissolve(1.0)

    e "You spend the morning playtesting and giving feedback to the team."

    scene bg studio1
    with Dissolve(1.0)

    e "Eventually, you decide to take your lunch break. Everyone else has already left the studio for their break."

    label day2choice:

    menu:
        e "Who will you go see?"

        "Amelia and Olive are outside.":

            #e "To be added."

            jump ao1

        "Ren and Yosef are in the lobby.":

            #e "To be added."

            jump ry1

        "Donovan and Noel are in the break area.":

            jump dn1

    label ao1:

    #Scene AO1 START

    e "You decide to go outside for a bit."

    stop music fadeout 1

    scene bg entrance4
    with Dissolve(1.0)

    e "As you exit the building, you spot Amelia and Olive standing in front of the window."

    play music "downtownwalk.mp3" fadein 1

    show amelia rd at midleft
    with Dissolve(.5)

    show olive ld at midright
    with Dissolve(.5)

    o "Hi there, [name]! Out here for some fresh air?"

    a "Hello, [name]. Are you taking your break?"

    a "Hmm...Since you're both here, I may as well show you this..."

    e "Amelia shows you her phone screen. It's showing what looks like a social media profile."

    a "This is the official Jitter account for The Lonely Star. It just went up today."

    o "Nice! We've officially gone public!"

    o "Woah, 101 followers already?! How'd we get that popular that fast?"

    a "...Bot accounts."

    o "BOTS? Booooooo!"

    show amelia rc
    with Dissolve(.2)

    a "Yeah, I'm not too thrilled about it either, but that's how we get our foot in the door of Jitter's algorithm."

    show amelia rd
    with Dissolve(.2)

    a "I don't know the science behind it, but these 100 bot accounts will like and comment on every post we make."

    o "They leave comments? In that case, it's only a matter of time before someone notices that they're bots."

    a "Eh, I don't think most people are that observant."

    show olive lc
    with Dissolve(.2)

    o "Wow. That's kinda cold..."

    scene bg black
    with Dissolve(1.0)

    jump day2choice

    #Scene AO1 END

    label ry1:

    #Scene RY1 START

    e "You decide to head downstairs to the lobby."

    stop music fadeout 1

    scene bg lobby2
    with Dissolve(1.0)

    e "As you enter the lobby, you notice Ren and Yosef chatting near the front desk."

    play music "childhood.mp3" fadein 1

    show ren rd at midleft
    with Dissolve(.5)

    show yosef ld at midright
    with Dissolve(.5)

    y "Hello, friend! Please, come join us!"

    r "Hey, [name]."

    y "Ren here was just telling me about his personal computer, or \"Pee-Cee\" as he calls it."

    show ren rc
    with Dissolve(.2)

    r "Dude, how can you have never heard the abbreviation \"PC\" before? Aren't you a financial advisor or something?"

    show yosef lc
    with Dissolve(.2)

    y "I am not from America! In my country, we do not have that kind of slang."

    r "\"Slang\" he calls it..."

    scene bg black
    with Dissolve(1.0)

    jump day2choice

    #Scene RY1 END

    label dn1:

    #Scene DN1 START

    e "You decide to head downstairs to the break area."

    stop music fadeout 1

    scene bg dining1
    with Dissolve(1.0)

    e "The so-called break area is lined with many tables and chairs, and more so resembles a cafeteria."

    e "In the corner, you see Donovan and Noel eating in silence. They are both looking at their phones as they eat."

    show noel rp at midleft
    with Dissolve(.5)

    show donovan lp at midright
    with Dissolve(.5)

    e "They look up at you as you approach."

    play music "neonscapes.mp3" fadein 1

    show noel rg
    with Dissolve(.2)

    show donovan ln
    with Dissolve(.2)

    n "Oh! Hi [name]."

    menu:
        n "Would you like to sit with us?"

        "*Sit next to Noel*":

            #show noel at slidecenter

            #show donovan at slidefarright

            e "You slide into the left side of the booth, next to Noel."

            show noel rhg
            with Dissolve(.2)

            $ np += 1
            e "She softly smiles at you. {color=#0064ff}+1{/color}"

            #show noel rd
            #with Dissolve(.2)

        "*Sit next to Donovan*":

            #show donovan at slidecenter

            #show noel at slidefarleft

            e "You slide into the right side of the booth, next to Donovan."

            show donovan lg
            with Dissolve(.2)

            d "..."

            $ dp += 1
            e "He gives you an awkward look, but doesn't seem to mind you sitting next to him. {color=#800080}+1{/color}"

            show donovan ln
            with Dissolve(.2)

    show noel rg
    with Dissolve(.2)

    n "What did you bring for lunch today? I've got apple slices."

    show noel rd
    with Dissolve(.2)

    n "Hmm..."

    e "She looks curiously at the apple slice in her hand."

    n "Another food in a vague crescent-moon shape..."

    n "Though I guess this would be more of a half-moon, actually."

    d "..."

    e "Donovan doesn't respond, and instead takes a sip of his drink."

    scene bg black
    with Dissolve(1.0)

    jump day2choice

    # Scene DN1 END

    label ceo_meeting:

    play music "lazyafternoon.mp3" fadeout 1

    scene bg lobby2
    with Dissolve(1.0)

    #e "You step into the office. It is quite spacious compared to many other rooms in the building..."

    #e "Mr. Adams walks in behind you and sits down at his desk."

    show gerald ld
    with Dissolve(.5)

    menu work:
        m "So, [name], how do you like your work so far?"

        "It's fun!":

            show gerald lh
            with Dissolve(.2)

            m "That's great to hear! And people said that playing video games couldn't be a job..."

            m "Well, I hope that you continue to find it as rewarding as you are."

            show gerald ld
            with Dissolve(.2)

        "Well, it is work...":

            m "It's just another job for you, huh? I completely understand."

            m "Being a video game tester is more demanding than it sounds."

        "Honestly, I don't know if this type of thing is for me...":

            show gerald lc
            with Dissolve(.2)

            m "You don't like it? That's not what I was hoping to hear..."

            m "I am sorry to hear you say that. Hopefully you start to appreciate it more as you get used to it."

            show gerald ld
            with Dissolve(.2)

    m "Do you mind if I ask you something else?"

    menu team:
        m "What are your thoughts on your development team so far?"

        "Ren seems like a nice guy.":

            label ren:

                m "Ren does seem to work well with others."

                m "I don't know if you'd know him, but he used to be a member of a moderately popular esports team."

                m "I thought that input from a competitive gamer would give our games a unique perspective."

                m "His experience working on a team makes him a valuable asset for any project."

                m "Not to mention he's a very talented programmer as well."

            jump other_thoughts

        "Amelia is pretty serious.":

            label amelia:

                m "Indeed she is."

                m "Amelia might be hard to get to know, but I think you will come to appreciate her no-nonsense attitude."

                m "Has she told you that she is the first member of her family in several generations to go to college?"

                m "I imagine that is what drives her to work so hard."

                m "She doesn't waste any opportunities and is eager to prove herself, which I greatly respect."

                m "I worry about her sometimes, but I'm sure she can take care of herself."

            jump other_thoughts

        "Yosef is quite friendly.":

            label yosef:

                m "thoughts to be added."

            jump other_thoughts

        "Donovan has barely said a word.":

            label donovan:

                m "thoughts to be added."

            jump other_thoughts

        "Olive is a lot of fun.":

            label olive:

                m "thoughts to be added."

            jump other_thoughts

        "Noel is very knowledgeable.":

            label noel:

                m "thoughts to be added."

            jump other_thoughts

        "No thoughts at the moment.":

            m "No? Nothing you'd like me to know about anyone?"

            jump no_thoughts

    menu other_thoughts:
        m "Any other thoughts?"

        "Ren seems like a nice guy.":

            jump ren

        "Amelia is pretty serious.":

            jump amelia

        "Yosef is quite friendly.":

            jump yosef

        "Donovan has barely said a word.":

            jump donovan

        "Olive is a lot of fun.":

            jump olive

        "Noel is very knowledgeable.":

            jump noel

        "No other thoughts at the moment.":

            label no_thoughts:

                m "I hope that you will get along well with all of them, for your own sake as well as that of The Lonely Star."

                m "The game that your team is working on is one that I am especially looking forward to."

                m "One that I have been eager to see come to fruition for a very long time..."

                show gerald lh
                with Dissolve(.2)

                m "Dare I say, it will be the game that saves the world!"

                show gerald ld
                with Dissolve(.2)

                m "Ahem... well, thank you for meeting with me. I'll let you return to your team and resume your work."

    play music "passingtime.mp3" fadeout 1

    scene bg studio1
    with Dissolve(1.0)

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show ren rd at farleft
    with Dissolve(.2)

    show olive rd at qleft
    with Dissolve(.2)

    show donovan ld at qright
    with Dissolve(.2)

    show amelia ld at farright
    with Dissolve(.2)

    # These display lines of dialogue.

    menu player:
        r "So [name], what do you play games on?"

        "PC.":
            $ player_flag = True
            $ notplayer1_flag = False
            $ notplayer2_flag = False
            $ notplayer3_flag = True

            $ rp += 1
            r "Nice! I play on PC, too. {color=#ff0000}+1{/color}"

            jump choice_player

        "Consoles.":
            $ player_flag = False
            $ notplayer1_flag = False
            $ notplayer2_flag = False
            $ notplayer3_flag = True

            r "Consoles, huh? I'm more of a PC guy myself."

            $ dp += 1
            d "I mostly play on consoles. {color=#800080}+1{/color}"

            jump choice_player

        "On my phone.":
            $ player_flag = False
            $ notplayer1_flag = False
            $ notplayer2_flag = False
            $ notplayer3_flag = True

            r "Oh, you're one of THOSE people, huh?"

            r "...Nah, just kidding. Nothing wrong with being a mobile gamer."

            $ op += 1
            #show olive rd at qleft
            #with Dissolve(.2)
            o "I play games on my phone! I'm really into those cozy games, y'know? {color=#fd5d10}+1{/color}"

            show olive rd at qleft
            with Dissolve(.2)

            jump choice_player

        "I don't play video games.":

            r "Oh, that's cool...wait, what?"

            e "Everyone looks at you in disbelief."

            menu notplayer:
                r "No offense, but what made you want this job if you're not even into video games?"

                "I needed work of SOME kind.":

                    $ ap += 1

                    a "That's a respectable reason. I'm glad that you found some work. {color=#008000}+1{/color}"

                    show amelia lh at farright
                    with Dissolve(.2)

                    a "Hopefully you enjoy it, and it's enough to keep you afloat."

                    show amelia ld at farright
                    with Dissolve(.2)

                    jump pastime

                "I wanted to know more about them.":

                    hide donovan
                    with Dissolve(.5)

                    show noel ld at qright
                    with Dissolve(.5)

                    $ np += 1
                    n "That's kind of why I'm here. It seems like a lot of digital artists do work for games. {color=#0000ff}+1{/color}"

                    n "Plus, I want to finally understand what Olive is saying when she talks with her online friends."

                    show olive rd at qleft
                    with Dissolve(.2)

                    o "Oh, come on! The games we play aren't THAT complicated..."

                    n "So you say..."

                    jump pastime

                "Games are a big deal now. I wanted to join the revolution.":

                    hide donovan
                    with Dissolve(.5)

                    show yosef ld at qright
                    with Dissolve(.5)

                    $ yp += 1
                    y "Ha! Spoken like a true go-getter! {color=#ffd700}+1{/color}"

                    y "The video game industry is bigger than the music and movie industries combined!"

                    y "I never expected something like that to happen, but if that's where the money's at now, then so be it!"

                    show ren rc at farleft
                    with Dissolve(.2)

                    r "So you're just a bunch of trend followers. I see how it is..."

                    jump pastime

    label choice_player:

        menu:
            r "Do you prefer single player or multiplayer games?"

            "I like multiplayer games.":

                $ rp += 1

                if player_flag:
                    r "Me too! It seems like we have a lot in common already! {color=#ff0000}+1{/color}"

                else:
                    r "Me too! I love playing games with other people. {color=#ff0000}+1{/color}"

                jump lost

            "I prefer single player.":

                r "You like singleplayer?"

                r "I'm more into multiplayer games, but I enjoy a good solo experience from time to time."

                $ dp += 1
                show donovan lh at qright
                with Dissolve(.2)
                e "Donovan nods, seemingly in agreement. {color=#800080}+1{/color}"

                jump lost

            "Depends on what mood I'm in.":

                $ op += 1
                o "I feel you. Playing a game with your friends is WAY different than playing by yourself. {color=#fd5d10}+1{/color}"

                jump lost

    label lost:

        hide donovan
        with Dissolve(.5)

        show yosef ld at qright
        with Dissolve(.5)

        y "This conversation is completely lost on me..."

        jump end

    label pastime:

        menu:
            o "So if you're not into video games, what do you like to do?"

            "Spend time with family.":

                $ notplayer1_flag = False
                $ notplayer2_flag = False
                $ notplayer3_flag = True

                $ ap += 1
                show amelia lh at farright
                with Dissolve(.2)
                a "I'm happy to hear you say that. I always enjoy time with my brother and sister, however we spend it. {color=#008000}+1{/color}"

                show amelia ld at farright
                with Dissolve(.2)

                a "It seems like people don't set aside enough time for family these days..."

                a "Anyways..."

            "Go to parties!":

                $ notplayer1_flag = False
                $ notplayer2_flag = True
                $ notplayer3_flag = False

                hide donovan
                with Dissolve(.5)

                hide noel
                with Dissolve(.5)

                show yosef ld at qright
                with Dissolve(.5)

                $ yp += 1
                y "So you're a people person like I am! Glad to hear it! {color=#ffd700}+1{/color}"

                y "I wouldn't call myself a party animal, but I'm always at my best when I'm with others!"

                show amelia lc at farright
                with Dissolve(.2)

                a "You're at your loudest, too..."

                e "Amelia holds her hand to her ear."

            "That's a secret...":

                $ notplayer1_flag = True
                $ notplayer2_flag = False
                $ notplayer3_flag = False

                show amelia lc at farright
                with Dissolve(.2)

                a "A secret? It must be something we'd be better off not knowing..."

                hide donovan
                with Dissolve(.5)

                hide yosef
                with Dissolve(.5)

                show noel ld at qright
                with Dissolve(.5)

                $ np += 1
                n "I understand if you don't want to tell us much yet. We haven't known each other that long. {color=#0000ff}+1{/color}"

                a "Anyways..."

        jump end

    label end:

        a "Could we maybe get back to the topic at hand?"

        if notplayer1_flag:

            n "T-that's a good idea, yes..."

        if notplayer2_flag:

            y "Oh right. Of course."

        if notplayer3_flag:

            r "Y-yeah, sorry..."

        scene bg gray
        with Dissolve(1.0)

        #if rp > 0:

            #show ren rd at left
            #with Dissolve(.5)

        #if dp > 0:

            #show donovan ld at right
            #with Dissolve(.5)

        #if op > 0:

            #show olive rd at center
            #with Dissolve(.5)

        #if ap > 0:

            #show amelia ld at right
            #with Dissolve(.5)

        #if np > 0:

            #show noel ld at left
            #with Dissolve(.5)

        #if yp > 0:

            #show yosef ld at center
            #with Dissolve(.5)

        e "Thank you for playing this early release of Everyday! Please look forward to the full game!"

    # This ends the game.

    return
