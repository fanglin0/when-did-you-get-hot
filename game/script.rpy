define t = Character("Tina")
default y = Character("[p_name]")
default pronoun = Character("[p_sex]")
define d = Character("Dad")
define m = Character("Mom")
define ml = Character("Leo")
define fl = Character("Lina")
default p_confidence =0
default ml_score = 0
default fl_score=0
default school_area ="s"
default love_interest = "s" #placeholder
default memory = "s"
default love_interst_pronoun ="s"
default love_interest_prounoun2 ="s"
default li_check = False
default clingy_point = 0
init python:
   def li_checker(love_interest):
      return love_interest == "Leo"
# image mom happy  = im.Scale('mom happy', 1080, 1600)
transform half_size:
   zoom 0.7
transform dad_size:
   zoom .7
transform tina_size:
   zoom .9
transform leo_size:
   zoom .8

# li = leo = true; li=lina = false
# fixed location 
transform left_pos:
   xpos 0.0
   ypos 1.0
   xanchor 0.0
   yanchor 1.0
transform mid_left_pos:
   xpos 0.25
   ypos 1.0
   xanchor 0.5
   yanchor 1.0
transform mid_right_pos:
   xpos 0.75
   ypos 1.0
   xanchor 0.5
   yanchor 1.0
transform right_pos:
   xpos 1.0
   ypos 1.0
   xanchor 0
   yanchor 1.0


play music "audio/wdygh-main.opus" loop
# The game starts here.

label start:
   $ p_name = renpy.input("Put your name.")
   t "—would think you're moving houses. Do you really have to take everything you own?"
   scene car 
   show tina annoyed at left_pos, tina_size
   "Coming home from college—it was the one time a year you got to see your family and friends."
   "This is your sister, Tina. Not yet in college. But with the way she's talking, you'd think she was."
   t "Seriously. Your darling vanity is using my lap as a seatrest. At this point, {i}she{/i} might as well be your sister. Not me."
   t "Everything."
   show dad awkward at half_size, mid_right_pos
   d "Give her a break, Tina."
   show dad neutral at dad_size, mid_right_pos
   d "You tell she's tired by the way she's not arguing with you. You'd typically be at each other's throat by now."
   show tina smug at left_pos, tina_size
   t "Yeah, and she's just sitting there with that dark look and even darker eyebags. you're not intimidating me, y'know. i'm practically an adult, now."
   show dad neutral at dad_size, mid_right_pos
   d "Want a pick-me-up, [p_name]? We're still half an hour from home."
   menu:
      "I could use some Coffee.":
         d "Hah, you're just like your mother."
         d "She left a cup just for you. Her world famous, darker-than-the-void coffee."
         y "…appreciate it."
      "Tea, please.":
         d "You got it, champ."
         t "We just got new tea in, y'know. You're in luck."
         y "….would involve waiting till we're home, though."
         d "Open to settling for gas station tea?"
         t "Eugh. Don't. You remember what happened last time."
      "Something sugary":
         t "Oh, I want Dunkin's!"
         d "Let's see if they have 'em."
         t "Way ahead of you. Checked google maps and… yeah, no. Nothing. They only have… McDonalds and Subways."
         y "NototheMcDonaldsCoffee."
      "It's okay. I just wanna sleep….":
         show dad neutral at dad_size, mid_right_pos
         d "You got it."
   "Even Tina lowers the generic pop trash you both loved down for you to nap. Guess she finally grew a conscience."
   "Only took a year's absence for her to grow nicer. Who knew?"
   show dad neutral at dad_size, mid_right_pos
   d "Well, before you fall asleep…"
   "You already knew where this was going."
   d "What are you looking forward to this summer?"
   y "Uh…"
   menu:
      "Rotting in bed.":
         "You've been working hard enough. All you wanted, now, was a break."
      "Advancing my career, obviously.":
         $ p_confidence+=1
         "Ambition is hot."
         "And you're a hot girl. It's only natural."
      "Hanging with friends.":
         pass
      "Vacation":
         pass
   "There was someone in particular you looked forwrad to seeing again."
   "You always had a soft spot for---"
   menu:
      "Golden retriver boys.":
         $ love_interest = "Leo"
         $love_interst_pronoun = "his"
         $love_interest_prounoun2 = "he"
         $memory = "goaded by your himbo, golden retriver adrenaline-junkie"
      "Black cat girls.":
         $memory = "wanting to impress your sweet, black cat"
         $ love_interest = "Lina"
         $love_interst_pronoun = "her"
         $love_interest_prounoun2 = "she"
   "The memory of sneaking into the liquor cabinate a summer ago [memory] of a best friend has you going hot at the collar."
   "Your parents never found out. Neither did [love_interst_pronoun]'s."
   "Sharing drunken kisses in your bedroom---"
   show tina smug
   t "[y] is blushing!"
   y "I'm not!"
   "Your voice comes out squeaky."
   "They're both laughing at you."
   "God damn it."
   "Your family has always wanted you to get together."
   "And you suspect, that they suspect something had happened that summer when you grew clingy and emebarssed around each other."
   "You haven't talked about it."
   "Actually, screatch that. You haven't talked at all, since."
   "And it's been a year."
   "You'll find out what [love_interest] has been up to soon enough."
   "{cps=*.5}..."
   menu:
      "Ask, now.":
         "Your curiosity is killing you."
         y "What's [love_interest] been up to?"
         show tina annoyed
         t "Are you {i}really{/i} interested in what [love_interest] has been up to?"
         show tina smug
         t "Or are you asking if [love_interest_prounoun2]'s got a girlfriend, hm?"
         menu:
            "I'm actually interested.":
               y "I'm actually interested. Obviously."
               t "Fine."
               t "Quite a lot happened while you were gone."
               t "And while I would love to retell the whole tale, I'm sure [love_interest] would love to tell you [love_interest_prounoun]self."
            "You got me.":
               t "Pfft."
               t "And you say you're just friends?"
               y "We are---"
               d "[y], [love_interest_prounoun2] doesn't."
               d "Maybe this is the summer, hm?"
               y "The summer for what?"
               d "You'll both find someone."
               t "Or they'll find each other, again."
               "You feel like the butt of their joke, and very wisely shut up."
      "Avoid further humiliation.":
         "You'll find out {i}soon enough {/i}."
   "You yawn and fight sleep trying to weigh down your eyelids."
   show dad neutral at dad_size, mid_right_pos
   d "Liv wants to see you. So does Leo."
   d "They've both been asking after you for so long."
   d "I have a position for you as a manager for our small new team."
   show tina annoyed
   t "Dad! {i}Wetalkedaboutthis{/i}. She just came home! She doesn't need all this stress."
   d "Well, what better time to talk about this than the present?"
   d "You can connect with the youth! Do what you do best, with that little… engineering major of yours."
   menu:
      "It's advertising.":
         $ p_confidence +=2
      "Yeah...":
         pass
   #confidence level impacts dialogue options and how user interacts with the story and world in general. Similar to Our Live
   show dad neutral at dad_size, mid_right_pos
   d "I know, I know! Just doing my dad things. Reminding you that you have that safety net, champ."
   "Safety net."
   "You..."
   menu:
      "Resent it.":
         "You hate talking about your family."
         "At every turn, you're dubbed a nepo baby."
         "It discredits everything you've worked hard far as just that satus."
         "Being born into wealth."
         $ fl_score+=1
      "Are grateful.":
         "Your father worries too much."
         "But you know it's out of love."
         "He just wants to shield you from the worst of the world."
         "Whether that's turned out better or worse for you, you know his intentions are pure."
         $ ml_score+=1
   # show dad neutral at dad_size, mid_right_pos
   d "You're still my baby girl at the end of day."
   d "I'd hate to have to watch you work so hard."
   d "But you can always feel free to do anything else. Enjoy your summer, you deserve this break."
   y "Yeah. I'll… think about it."
   jump home

label home:
   "You drift off. And before you know it, you're back home."
   "Your school isn't like this."
   "Your school is—--"
   menu:
      "In a big city.":
         $ school_area = "urban"
      "In the suburbs.":
         $ school_area = "suburban"
      "In the middle of nowhere.":
         $ school_area = "rural"
   "---[school_area]."
   "Surrounded by strangers, you've made quite a few close friends."
   "You always preferred being"
   menu:
      "The life of the party.":
         $ p_confidence+=1
         "You were alwyas popular, and college was no different."
         "It's nice to keep to yourself."
      "A wallflower.":
         $p_confidence-=1
         "It's nice to keep to yourself."
   "Still. You've missed home."
   scene house door with fade
   menu:
      "Walk through the door.":
         pass
   scene house with fade
   "The smell of your mother's cooking, garlic bread and spaghetti, your favorite comfort meal fills your nose."
   "That, and the fainter underscent of lilacs."
   show lilac
   "It's your mother's favorite flowers."
   "Earthy, comforting, and always reminds you of her hugs."
   hide lilac
   show mom happy at mid_right_pos, half_size
   m "Look whose home!"
   m "Oh, my love."
   "She hugs you. She smells like lilacs."
   m "I'm so happy you're home!"
   y "Me too."
   "Your dad and sister walks slips through the door."
   show tina smug
   show dad neutral at dad_size, left_pos
   jump ml_meeting
label ml_meeting:
   t "You're about to be a lot gladder. Look whose here!"
   # hide dad neutral
   # hide tina smug
   # hide mom happy
   show leo neutral at leo_size, right
   ml "Heyyyyyy."
   "It's your blonde, puppy-dog eyed golden retriver of a best friend."
   menu:
      "Blonde?":
         pass
   "Uh, well, not exactly blonde now."
   menu:
      "\"Did you dye your hair?\"":
         show leo shy
         ml "Yeah."
         ml "You like it?"
         y "Uh..."
         show leo sad
         ml "You don't like it?"
         menu:
            "You like it.":
               y "Nah, I do."
               "Just a big change"
               show leo shy
               ml "Thought you would."
            "You don't like it.":
               y "Don't fish for compliments."
               show leo sad 
      "Don't ask.":
         pass
   "Anyways."
   show leo neutral
   "And how you've missed him."
   "Sunkissed, atheletic, loud, he fits every stereotype of the outgoing intimidating womanizing jock."
   "But he's a sweetheart. And he always looks at you with such open awe and adoration in his eyes it makes you melt."
   "Like it was your first meeting again."
   menu:
      "Heyyyyyyyyyy!":
         y "Heyyyyyyyyyyyyyyyyy!"
         ml "Hiiiiiiiii."
         t "Can I join in too, or---"
         $ml_score+=1
      "Ask him why he's here.":
         y "Why are you here?"
         ml "Wow."
         ml "Way to show enthusiam. I came all this way!"
         menu: 
            "I am not enthusiastic.":
               y "From a block away?"
               show leo sad 
               ml "Yes!"
               ml "Quite a long block, might I add."
               t "That shit wasn't long at all."
               if (love_interest=="Leo"):
                  t "Freaking anchild."
                  t "Everyday I question why you like him."
                  y "Tina!"
                  "Leo doesn't seem to have heard. He's now talking to your dad."
                  show tina smug
            "I am enthusiatic.":
               y "Nah."
               "Uhh."
               y "I meant it in a enthusatisc way."
               y "Like, you're really here?"
               show leo sad
               y "Wow."
               ml "...wow."
               
               if (love_interest=="Leo"):
                  t "Pfft."
                  t "That's your girlfriend?"
                  ml "My what?"
               $ml_score+=1
      "Run into his arms.":
         $ml_score+=1
   
   "Physical affection is commonplace in your family."
   "So you shouldn't be surprised when he hugs you."
   "But you are, anyway."
   if (love_interest=="Leo"):
      "After last summer.."
   if p_confidence<2:
      "He wraps his arms around you."
   if p_confidence >=2:
      "You throw your hands back around him."
   "He feels muscular."
   "And sweaty."
   "Puberty."
   if ml_score==1:
      "You kind of like it..."
   "You grew up together."
   "Yet at the most, you usually playfight."
   "..."
   "When did he grow so tall?"
   "You ruffle his hair, and he laughs."
   "He would swat you away, but he just grabs your hand and holds you in place."
   "See? Gentle giant."
   y "When'd you grow so tall?"
   show leo sad
   ml "Haven't you been saying that since middle school?"
   y "I swear you got taller in the little time I haven't seen you."
   ml "One year."
   "He says too eagerly. And before you could question if he's been {i}keeping count{/i}, he says louder."
   "And maybe, y'know, your bad posture made you shrink---"
   "He grunts when you pull harder."
   y "I can still beat you."
   "He laughs, and the sound comes right by your ear as he presses his face onto the crown of your hair."
   menu:
      "Pull his hair.":
         ml "Ow!"
         show leo shy
         ml "I meant that in a complement-y way. You're all petite and cute."
         ml "Girls like being called petite, right? Ow ow ow."
         if (love_interest=="Leo"):
            "His voice sounds breathy, from maybe not just pain, and you ignore the twinge of heat it stokes in your gut."
            y "You're so annoying."
         else:
            "You roll your eyes and stifle a giggle."
            y "Just shut up, dude."
      "Pull away.":
         "You push him away. This guy's like a human furnace."
         if (love_interest == "Leo"):
            "That's the only rational explanation for why your face feels so warm, surely."
         else:
            "You don't want his sweat on you."
         $ p_confidence-=1
         show leo neutral
   ml "That's my girl."
   "He has no idea how to treat a girl. It's no wonder he doesn't have a girlfriend yet."
   "Wait."
   "A year ago, you would say this with confidnece."
   "But now, you're not so sure."
   menu:
      # "Ask.":
      #    y "Are you still single?"
         
      "Ask.":
         "You'll tread the waters carefully."
         y "You have no idea how to treat a girl."
         "You laugh, and to your great relief it comes out as nonchalant as you aimed for."
         y "Seriously, do you even have a girlfriend yet?"
         "Subtlely is your strong suit, you've been told."
         "Leo stares at ypu wide-eyed, as if caught off guard."
         "which is weird, because nothing you said would indicate anything past platonic."
         "Then he laughs, as strained as you feel, and lowers his voice conspiriotorially."
         ml "You hitting on me?"
         "Sublety is not his strong suit, you think."
         menu:
            "Yes.":
               y "So what if I am?"
               show leo shy
               "He laughs again. And fidgets with the cup in his hand."
            "No.":
               y "I'm not."
               show leo sad
               ml "That's too bad. I wouldn't mind if you were."
         ml "Anyway, I don't have a girlfriend."
         y "I'm surprised."
         ml "Why? Because I've been waiting for that special girl?"
         y "You act like a fuck boy. I expected you be treated like one."
         ml "Nah, I respect women [p_name]."
         y "Alright, dude."
         ml "No, dude. I've not even---"
         "He breaks off, emebarassedly, and shifts the topic abruptly."
         ml "Anyway..."
      "Don't.":
         pass
   ml "I missed you."
   if ml_score >=1:
      "Your face feels hot."
   ml "So much."
   "No matter how many times you heard it from him, it always feels like the first."
   "It speaks volumes how well the perfromative soft boy act works on you."
   "Not an act coming from him. But still."
   menu:
      "Tell him you didn't miss him.":
         "I didn't miss you."
         show leo sad
         t "She did! She totoally did."
      "Tell him to shut up.":
         y "Shut up."
         show leo shy
         ml "It's okay, babes."
         ml "I know how you truly feel."
         m "Our brains. It's connected."
         $ml_score+=1
      "Tell him you missed him too.":
         y "Missed you too."
         show leo shy
         $ml_score+=1
         show tina annoyed
         if (love_interest=="Leo"):
            t "Get a room, dudes."
            "Tina rolls her eyes, reminding you that there's still an audinece of very-much-smiling and failing-to-look-like-they're-minding-their-own-business people in the room with you."
   d "Ahem. Dinner's served!"
   "You turn away from him to help at the dinner table."
   "Your dad carries a large crockpot to the table, urging everyone to get out the way."
   "Your mom and sister are busy prepping dessert and wine."
   "Organized chaos. You can't help the giddiness bubbling in you at the nostalgic scene."
   "When you're dutifully kicked out of the kicthen on account of being 'the guest', you find Leo by the couch."
   show leo neutral
   "Leo leans against the couch, spreading his legs wider. He smiles."
   ml "Want some?"
   y "What is that?"
   "He moves his hand to the side, revealing a cup of something pink and bubbly."
   show champagne
   ml "Riesling."
   menu:
      "Drink it.":
         "You drink it."
         hide champagne
         show leo shy
         ml "Like it?"
         "It tastes like juice."
         "Like lemonade, fruity and sweet."
         "The bubbliness of it really hits your throat."
         if ml_score >=1:
            "And you like it."
            ml "See? I know you better than you know yourself."
            menu:
               "I do like it.":
                  "You tell the truth."
                  y "Reminds me of capri suns."
                  $ ml_score+=1
               "I don't like it.":
                  if (love_interest=="Leo"):
                     "You lie."
                  if not (love_interest=="Leo"):
                     pass
                  y "Not for me."
                  ml "Pft, liar."
                  y "I'm not lying!"
                  ml "Then I'll finish the cup."
                  menu:
                        "Give it to him.":
                           "You hand the cup to him."
                           "Leo grins. Your hands brush when you exchange the cup."
                           "See? Golden retriever."
                           "You scowl, because it's better than smiling back."
                           "Not like he did anything wrong. But his enthusiasm always knocks you off guard."
                           ml "I'll be nursing this baby the rest of the night."
                           y "Don't get drunk."
                           "He turns the cup slightly, whether on purpose or not you don't know, so that he's drinking from where your lips left an imprint of gloss on the rim."
                           "Flirt."
                           "But at the same time, he's so unaware sometimes that it's equally plausible he doesn't know what he's doing to you."
                           "You feel your face heat up, and look away."
                        "Keep it for yourself.":
                           y "You gave it to me."
                           ml "Yeah?"
                           "'So I'm keeping it', almost slips from your mouth. You bite it back just in time."
                           y "I'll spare you from this capri-sun knockoff."
                           ml "Dude..."
            "Leo rolls his eyes, but you know that he's secretly pleased."
         else:
               "And you don't like it."
               jump dislike
      "Don't drink it.":
         hide champagne
         jump dislike
   jump dinner
label dislike:
   ml "No?"
   y "Sorry. Just not for me."
   show leo sad
   "He looks genuinely hurt, and you feel bad for him."
   "See? Golden retriver."
   ml "It's okay."
   "He takes the cup back, and downs the rest of it in one swig."
   ml "Just means I'll have to work harder to find something you will like."
   jump dinner


label dinner:
   t "When's Lina coming?"
   "Thankfully, Tina's loud voice breaks any tension there was, or the lack of it."
   y "Tina?"
   show tina annoyed
   t "Yeah. She's supposed to be coming."
   t "You don't know this, but she's turned into a total work-a-holic while you were gone."
   "Tina, the lovable, quiet, and sardonic girl you knew since childhood?"
   y "Yeah, I believe it."
   ml "Honestly! My dad's been comparing us so much lately. It's his new favorite hobby."
   "For the longest time that you've known the twins, you know they have a sort of sibling rivalry. And that extends to the business side, too, of course."
   "However, the twins, as much as they look alike, have completelyv opposite personalities."
   "While Leo is the happy-go-lucky, suave popular boy, Lina was always much more reserved and ambitious."
   "So while it's no surprise that she's busy working, the news still stings."
   "..."
   "Honestly, she's the type of pretty you see few times in your life."
   "You play back your old voice notes sometimes. She's not one for texting, but she's always had a soothing voice you begged to hear."
   "You're nonchalant and sauve. But, when you got her to oblige to your pleads, you always made sure to memoralize your achivements."
   "Like, you're not expecting this since-birth work-a-holic girl to drop everything for dinner."
   "But it's the first time you've been home in half a year."
   if not (love_interest=="Leo"):
      "Is it so much to ask to want to see your favorite person after the six hour long planeride?"
      "She's even been calling you less."
      "After last summer..."
   else:
      "You miss your best friend."
   menu:
      "You were looking forward to seeing her again.":
         y "Aw..."
         t "Aw is right."
         y "I hope she isn't overworking herself."
         y "You better have been taking care of her."
         ml "I would! But---"
         if not (love_interest=="Leo"):
            y "You know how she gets!"
         else:
            y "You're her brother!"
         show leo sad
         "---but, she's been super independent lately. She's always working on that startup of her's."
         y "Startup??"            
         show leo neutral
         ml "Some tech-o mumble jumbo."
         ml "Jeez. Don't look so interested."
         "Talk to her when she gets here. She said she'd tried to make it for dinner."
      "You don't mind spending more alone time with Leo.":
            "Even if it's dissapointing, you don't mind too terribly."
            "After all, it means more time spent with Leo."
            "Who is probbaly flirting with you but you can't quite tell."
            "If he treats other girls like this you'll kill him."
            #continue
   t "Maybe at the end of dinner, when we're cleaning up."
   ml "Assuming she makes it before curfew."
   "Tina sighs empathetically. It begs the question: "
   y "What's she doing out there so late anyway?"
   ml "No clue, dude."
   ml "Meeting investors, 'building her business', buzz word after buzz word."
   ml "All I know is that she goes out there with her morning smoothie bowl. Looking hella productive, going on runs and all."
   ml "And ends up coming home while I'm in the middle of my gaming sesh."
   ml "I mean, my... winding down."
   menu:
      "That's great.":
         $ml_score+=1
      "That's... great.":
         "Bum."
         show leo sad
         $ ml_score-=1
   t "You sound like a loser."
   ml "It's totally startegic! EVery man needs some winding down."
   ml "You know the saying: all work and no play, uh"
   y "Makes Jack a dull boy?"
   ml "Yeah, that. Whatever."
   "It's time to play your favorite game."
   "When is Lina going to be home?"
   "It makes you feel like a fornlorn housewife, waiting anxiously for her husband to get home."
   "Or a dog, waiting at her post, maybe."
   if not (love_interest=="Leo"):
      "Waiting for your productive, successful wife to come home while you're home tending the kids."
   y "Jeez..."
   "The family is happy to see you home, regardless."
   "You let yourself relax in the happy atomosphere."
   "Your mom had cooked all of your favorites."
   "Beef noodles. Delicious!" 
   pause 2.0
   "The clock hits 12."
   "Is she going to show up?"
   menu:
      "Yes!":
         $clingy_point+=1
         #change
      "Not yet.":
         pass
   "..."
   "Halfway through the diner, now."
   "She hasn't shown up."
   "Should you check your phone? Or leave it up to fate?"
   "Not like she told {i}you{/i} she's coming for dinner. You heard it through the very (tentative) grapvine."
   menu:
      "Text her.":
         "You would pull your phone out on the dinner tabel, but everyone is having a great time conversing."
         "Everyone but you."
         "You excuse yoruself to the bathroom."
         "It's not like... that shameful to use your phone under the tabnle quickly. But everyone else doesn't seem to care that Tina wasn't coming. So you might as well."
         menu:
            "Be cool about it.":
               "You type."
               y "Hey, I'm home for the holidays!"
               y "Dunno if you've heard."
               y "R u coming over later?"
               "'It'd be nice to see u', you type out, but hesitate."
               menu:
                  "Send it.":
                     y "It'd be nice to see u."
                     "You add a smiley emoji at the end to balance it out. So it sounds less"
                     if not(love_interest == "Leo"):
                        "like hurtling towards your death."
                     if (love_interest=="Leo"):
                        "passive aggresive."
                  "Don't.":
                     "You delete the message."
                     "That part's insinuated anyway."
            "Be not cool about it.":
               "You type."
               #phone ui
               y "It's just like you to miss my first dinner home..."
         "You wait in the meantime."
      "Stay nonchalant.":
         if (love_interest=="Leo"):
         
            "You don't need to chase a woman."  
         
         if not (love_interest=="Leo"):
         
            "You know she's probably busy."
         
   d "Clean up time!"
   "It's time to clean up after dinner."
   "Your mom and dad get busy chatting and putting the dishes away."
   jump fl_meeting

label fl_meeting:
   #placeholder
   ml "Your so short haha."
   "I'm gonna tap that, ahaha..."
   "Just as you think your evil, sinful thooughts, [fl] slams through the door like a wife catching infedelity in progress."
   show lina neutral
   "She's like a bloodsniffing hound, that one."
   fl "Sorry I'm late."
   "Spoken like your period after seeing this bad bitch."
   menu: 
      "Hold her accountable.":
         $temp="alpha"
         $temp1="Why were you late?"
      "Be a doormat.":
         $temp1="..."
         $temp="omega"
   "You're the [temp] here!"
   "Go ahead and show her what you're all about!"
   y "[temp1]"
   if temp=="alpha":
      "Her head whips to yours. She looks almost surprised."
      fl "What?"
      "The family looks to you, watching. They're lightly amused."
      fl "I mean, it's not my fault. They had me stay late. You're lucky I'm even here."
      "... {w=2.0}"
      ml "Wow."
      y "Woooowww."
      menu:
         "Hell no.":
            "Excuse me?"
            y "Excuse me? Just who do you think...?"
         "Bring [ml] into this.":
            "You hook an arm around [ml]'s shoulder. He has to stumble to match your height."
            y "Right, okay."
            y "Good to know you don't care."
            "Looking between you two, [ml]'s sister narrows her eyes."
            fl "..."
            fl "Look, I already—--"
            $ ml_score+=1
            $ fl_score+=1
         "I love being a submissive cuck.":
            "You channel your ancestry, all the submission and gentleness and meekness you've been taught, worthy of being a tradwife."
            y "Right. Sorry."
            $ fl_score-=1
            "She spares you a look that looks like 'that's what I thought'."
   else:
      "She looks exhausted, almost bored, with the scene in front of her."
   show leo neutral
   ml "I mean, me personally, I wouldn't take this."
   show lina distracted
   fl "Yeah, because you're fuckin'"
   fl "unemployed. {cps=*2}"
   show leo neutral
   ml "Excuse me?"
   "[t] really does have perfect timing. She chimes in, breaking the tension."
   t "So, who's hungry for desert?"
   fl "...You're real special, aren't you?"
   show tina smug
   t "I'll have you know---"
   d "Who's ready for your mom's world famous---"
   menu:
      "Chocolate cake.":
         $temp = "cheesecake"
      "Cheesecake.":
         $temp = "chocolate cake"
   d "---[temp]?"
   show tina annoyed
   "Tina shares a look with you."
   t "Uh, dad, you know---"
   if (love_interest=="Leo"):
      d "Just kidding! You didn't really think I'd forget my darling girl's favorite food, do you?"
      $temp="impactful"
   else:
      "Your dad shares a wide smile with the rest of the cast, as if he'd forgotten your existence."
      "...is this enough of a hint that you've chosen the wrong love interest?"
      $temp="wrong"
   "With that in mind, you pass the rest of the birthday as per usual. But you can't help but think that maybe, just maybe, you've made an [temp] choice."
   "It's not your birthday, but you sure want to ride out."
   "Your family spoils you. And they cooked all your favorite food as if this day was any more special than others."
   "So you're tempted to forget about the whole cake fiasco."
   "But you knew this would catch up with you sooner or later."
   "After cleaning up, your have some spare time. There's enough time to talk to one of the twins. Regardless of how you fight, they're still your favorite person in the entire world."
   "So you pick..."
   menu:
      "[fl]":
         $temp = "fl_choice"
      "[ml]":
         $temp = "ml_choice"
   "Let's go."
   "DEMO ENDED"
   "STAY TURNED FOR CHAPTER 1!"
   pause 2.0
   scene black
   jump chapter2
label chapter2:
   "Welcome!"
   if (temp == "fl_choice"):
      $temp2 = "Lina"
   else:
      $temp2 = "Leo"
   "You're on the [temp2] route."
   "Let's get back to flirting with our favorite neighbors, shall we?"
   if (temp == "fl_choice"):
      jump fl_choice
   if not (temp == "fl_choice"):
      jump ml_choice

   label fl_choice:
      return

   label ml_choice:
      return



      



      

   
         # fvrwfvw
            



# ccccc



   
   # "What a bum."


         


   #       pass

   
   # show lina neutral
   # fl "Yeah, 'cause you're fucking unemployed."
   # ml "Excuse me????"

   



# twins lina and leo
# leo is a nepo baby manchild himbo— ego, bound to take over dads company. sauver. not that interested in the company but doesnt want to try too hard


# lina— the responsible one. workaholic, rough around the edges. odfte deosnt have time for u
# teach ehr to live int he present. overachiever
# dad wanted her to take oevt he company but shed rather making smth new for herself



# tehrye btohg inetrsed in u

# Both chidhood friends. Black cat Liv vs golden retrievr leo




   



# twins lina and leo
# leo is a nepo baby manchild himbo— ego, bound to take over dads company. sauver. not that interested in the company but doesnt want to try too hard


# lina— the responsible one. workaholic, rough around the edges. odfte deosnt have time for u
# teach ehr to live int he present. overachiever
# dad wanted her to take oevt he company but shed rather making smth new for herself



# tehrye btohg inetrsed in u

# Both chidhood friends. Black cat Liv vs golden retrievr leo



