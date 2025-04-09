name=input("enter your name ")
play=input(f"hey {name}. welcome to the 'The Lost Temple of Zantara'.type yes if youre worthy of claiming the lost treasure of temple ").lower()
if (play!="yes"):
    print(" leaving the jungle")
    quit()

q1=input('''
You're standing at the jungle entrance.
    A) Take the worn path through the thick vines.
    B) Cross the river on a shaky rope bridge ''').lower()
if(q1=='a'):
    print("You entered thick vines path.")
    q1_1=input('''          
You hear growling in the bushes.
    A) Hide behind a tree.
    B) Try to run
          ''').lower()
    if(q1_1=='a'):
        print("you founded the temple")

    elif(q1_1=='b'):
        print("there is a jaguagur which got your attention ")
        print("you died")
        quit()
    else:
        print("you choosed the wrong option. ")
        quit()

    
elif(q1=="b"):
    print("your crossing the bridge")
    q2_1=input('''
Halfway across, the bridge starts snapping!
    A) Turn back quickly.
    B) Jump to a vine nearby.''').lower()
    if(q2_1=='a'):
        print("you founded the temple")
        
    elif(q2_1=='b'):
        print("you got trapped in a quick sand")
        quit()
    else:
        print("you choosed the wrong option. ")
        quit()
else:  
    print("you choosed the wrong option. ")
    quit()
q3=input('''
You arrive at a giant stone door with three symbols: Sun, Moon, Snake.
    A) Press the Sun
    B) Press the Moon
    C) Press the Snake''').lower()
if(q3=='a'):
    print('you activated the weapon system.')
    quit()
elif(q3=='b'):
    print("the door opened")
    q3_1=input('''
Inside the temple, there are two rooms:
    A) Enter the room with golden statues
    B) Enter the room with stone carvings''').lower()
    if(q3_1=='a'):
        print('the gates closed and now your trap for eternity')
        quit()
    elif(q3_1=='b'):
        print("you got the treasure")
    else:
        print("you choosed the wrong option. ")
        quit()

else:
    print("you choosed the wrong option. ")
    quit()
