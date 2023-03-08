#moduler

from os import system
from random import randint
from time import sleep

# liste for å holde items
items = []
# bool for å sjekke om flashlight-en er på 
flashlightOn = False

#----------------------------------- "Gameplay" funksjoner

# read funksjon tar stringen som er i argumentet, og printer hver bokstav etter en 0.06 sekunder delay. 
def read(arg):
    # lager variabel i, som holder 1
    i = 1
    for x in arg:
        # printer argumentet fra første til siste bokstav, og \r gjør at printen blir returnert til på neste print
        print(arg[0:i], end="\r")
        # 0.06 sekunder delay
        sleep(0.06)
        # plusser i med 1 for hver loop
        i += 1
        # hvis i er lik lengden av argumentet..
        if i == len(arg):
            # print ut argumentet som en input, fordi printen over fjerner denne
            input(arg)
            # gjør variabel i tilbake til 1
            i = 1

def end1():
    # fjerner alt fra terminalen
    system('cls')
    # gir terminalen en ny farge
    system('color 40')
    # bruker read funksjonen til å lese tekst
    read('You got the bad ending.')
    read('There is another ending though. Will you try to find it?')
    # color 7 er som regel den vanlige fargen i terminalen
    system('color 7')
    
def end2():
    system('cls')
    system('color 2e')
    read('Good job!')
    read('You got the good ending!')
    system('color 7')
    
def end3():
    system('cls')
    read('huh?')
    read('you got the lost ending.')
    system('color 7')

def death():
    system('cls')
    system('color 4c')
    print('The boy has died.')
    read('Press enter to restart...')
    system('color 7')
    system('cls')
    # restarter spillet ved å kjøre start funk
    start()

#----------------------------------- Funksjoner for spillets main valg

#-------- 1

def start():
    read('A little boy needs to take a trip down to his basement, since his mother asked him to go grab some flour for her.')
    read('However, the basement is very dark, and the boy is afraid of the dark.')
    read('He could try to find a source of light, like a flashlight.')
    read('But, he could also ignore the darkness, and think positive thoughts.')
    # uendelig while loop
    while True:
        # tar inn en input
        x = input('[1] Try to find a flashlight.\n[2] Think positive thoughts.\n +  ')
        # hvis inputten er 1, blir funksjonen opt1a kjørt, og loopen blir ødelagt
        if x == '1':
            opt1a()
            break
        elif x == '2':
            opt1b()
            break
        # hvis inputten er ikke lik 1 eller 2, kommer teksten under opp
        else:
            print('Feil input, vennligst prøv igjen!')
            # looper tilbake til inputen
    
def opt1a():
    read('The boy decides to try to find a flashlight.')
    read('He asks his mom, and she gives him a flashlight.')
    read('The boy is now ready to walk down.')
    items.append('Flashlight') #setter flashlight i items lista
    opt2()
    
def opt1b():
    read('The boy starts to think positive thoughts, to try to ignore the overwhelming darkness.')
    read('Unicorns, sunshine, and rainbows are what he is thinking about.')
    system('color 5e')
    while True:
        x = input('s#0uld YOU cl0se YOUR ey4s?\n-1- Yes.\n-2- No.\n +  ')
        if x == '1':
            opt1c()
            break
        elif x == '2':
            # nullstiller fargen
            system('color 7')
            # fjerner alt fra terminalen
            system('cls')
            # kjører funksjon opt2, og ødelegger loopen
            opt2()
            break
        else:
            print('Feil input, vennligst prøv igjen!')
    
#-------- 2
    
def opt2():
    read('He starts walking down the stairs.')
    read('The stairs start to creak loudly, and sound like they are about to break.')
    read('The boy could run quickly down the stairs.')
    read('He could also walk down slowly and steadily.')
    read('Or, he could close his eyes and ignore the noise.')
    while True:
        x = input('[1] Run down the stairs.\n[2] Walk slowly down the stairs.\n[3] Close your eyes, and walk blindly down.\n +  ')
        if x == '1':
            opt2a()
            break
        elif x == '2':
            opt2b()
            break
        elif x == '3':
            opt2c()
            break
        else:
            print('Feil input, vennligst prøv igjen!')
    
def opt2a():
    read('The boy runs as fast as he can down the stairs.')
    read('However, he manages to trip on the final step.')
    read('There is a sharp nail laying face up on the floor in front of him. It is pointing directly at his eye.')
    read('It goes through his eye, and reaches his brain instantly killing the boy.')
    death()
    
def opt2b():
    # deklarerer flashlightOn som en global variabel
    global flashlightOn
    
    read('The boy walks down the stairs.')
    read('Slowly..')
    read('..And steadily')
    read('He ends up in the basement, completely unharmed and safe.')
    read('It is very dark.')
    # hvis flashlight er i items
    if 'Flashlight' in items:
        while True:
            x = input('Turn on the flashlight?\n[1] Yes\n[2] No\n -  ')
            if x == '1':
                # gjør terminalen lys
                system('color 70')
                # gjør bool flashlightOn sann
                flashlightOn = True
                read('The flashlight illuminates the entire basement.')
                break
            elif x == '2':
                read('The boy doesnt turn the flashlight on.')
                break
            else:
                print('Feil input, vennligst prøv igjen!')
            
    opt3()

def opt2c():
    read('The boy closes his eyes, and walks down blindly.')
    read('He trips over, and cracks his skull open.')
    death()
    
#-------- 3

def opt3():
    read('He hears a squeak coming from one direction.')
    read('However, he should try to find the flour.')
    while True:
        x = input('[1] Find what made the noise.\n[2] Search for the flour.\n +  ')
        if x == '1':
            opt3a()
            break
        elif x == '2':
            opt3b()
            break
        else:
            print('Feil input, vennligst prøv igjen!')

def opt3a():
    read('He goes in a direction, to try to find what made the noise.')
    if flashlightOn:
        read('He looks around, navigating himself with the flashlight.')
        read('Out of nowhere, a medium sized rat jumps up on him!')
        read('The boy was able to punch the rat down to the ground, and beat it up before it could do any damage.')
        read('Inside of the rats mouth, there was a key!')
        items.append('Key') # setter Key i items lista
        read('The boy walks away, to try to find the flour.')
        read('After stumbling around..')
        opt4()
    
    else:
        read('A medium sized rat sneaks up, and tries to eat the boy.')
        if 'Sword' != items: # hvis sverd er ikke i lista, blir death funksjonen kjørt
            read('He digs his teeth into the boy, and slowly eats him.')
            death()
        else:
            read('Before the rat gets his teeth into the boy, he slices him into pieces.')
            opt4()
        
def opt3b():
    read('The boy ignores the noise, and goes searching for the flour.')
    if 'Flashlight' in items:
        read('Having a flashlight really helps.')
        opt4()
    else:
        read('It is nearly impossible to navigate around the basement, due to the boy not having a flashlight.')
        randint(1, 5) #20% sjangse å finne flour
        if randint == 1:
            opt4()
        else:
            read('The boy starves before he finds the flour.')
            death()
    
#-------- 4
    
def opt4():
    read('The boy finds the flour!')
    read('However, there is a giant rat in his way.')
    while True:
        print('[1] Fight the rat with his bare fists.')
        if 'Sword' in items: print('[2] use the SWORD.') # hvis sword er i lista, kommer det opp alternativ 2
        if 'Key' in items: print('[3] Throw the key on the ground')
        x = input(' +  ')
        if x == '1':
            opt4a()
            break
        elif x == '2' and 'Sword' in items: #hvis input er 2, og sword er i items lista, kj;res 4b funksjonen og loopen blir ødelagt
            opt4b()
            break
        elif x == '3' and 'Key' in items:
            opt4c()
            break
        else:
            print('Feil input, vennligst prøv igjen!')

def opt4a():
    read('The boy walks towards the big rat.')
    read('He punches forwards, but the rat dodges his attack.')
    read('The rat spins around, and uses his tail to knock the boy off his feet.')
    read('The boy tries to defend himself while on the ground, but the rat eventually overwhelms him.')
    end1()

def opt4b():
    read('The boy takes out the great sword of Akerbajik.')
    read('The big rat goes into attack, and throws himself at the boy.')
    read('The boy deflects the rat using his sword, and he proceeds to cut the rat.')
    read('The boy rushes over to the wounded rat, and slices the creatures head off, killing him.')
    read('The boy retrieves the flour, and makes his way back up the basement.')
    read('He gives the flour to his mom, and she makes incredible pancakes.')
    end2()
    
def opt4c():
    read('The boy throws the key onto the ground, and a portal opens up below him.')
    read('He falls through the portal before the rat gets to him.')
    system('cls')
    system('color 9f')
    read('...')
    read('The boy wakes up.')
    read('He finds himself on a soft cloud, up in the sky.')
    read('Looking around, there is nothing to see other than the bright blue sky.')
    read('Where am i? is what the boy wondered.')
    end3()
 
#----------------------------------- Alternativ Rute for å få Sverd

def opt1c():
    read('You close your eyes, and start walking down the stairs.')
    read('It feels like youve been walking for an eternity')
    system('cls')
    read('...')
    read('You open your eyes.')
    read('You get blinded by a bright orange light, coming down from above.')
    read('Your eyes eventually adapt, and you sees a world completely different from your own.')
    read('Purple grass surrounds him, and the sky is orange with pink clouds.')
    read('Its warm, but you feel a slight cold breeze of air on your skin.')
    while True:
        x = input('do you want to expl0re?\n-1- Yes.\n-2- No.\n -  ')
        if x == '1':
            opt2d()
            break
        else:
            opt2e()
            break
    
def opt2d():
    read('You start to explore the newfound world.')
    read('Walking around, on the sharp, purple grass you eventually stumble upon a great temple.')
    read('You enter it, and find a tomb in the center of it.')
    read('you open the tomb, and steal the SWORD that is inside.')
    read('You get shot out of the orange world, and back to the real world.')
    items.append('Sword')
    system('color 7')
    system('cls')
    opt4()

def opt2e():
    read('3scap1ng 1snt 4 0ption.')
    system('cls')
    opt2d()