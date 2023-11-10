import random

def montyhallproblem(N):    #N is number of runs we wish to simulate
    runs = 0 
    win = 0
    loss = 0
    stay = 0 
    switch = 0
    staywin = 0
    switchwin = 0
    stayloss = 0
    switchloss = 0 

    while runs < N:

        car = random.randint(1, 3)
        goat1 = random.randint(1, 3)
        goat2 = random.randint(1, 3)

        choice1 = random.randint(1, 3)    #Pick one of 3 doors
        choice2 = random.randint(1, 2)    #Binary choice of switch or stay. 1 is stay, 2 is switch.       

        while goat1 == car or goat1 == goat2:   #Checks that assure car and goat door choices are random and not equal to one another
                goat1 = random.randint(1, 3)

        while goat2 == car or goat2 == goat1:
            goat2 = random.randint(1, 3)        
            
        if choice1 == car:                          #"reveals" one of the goats and sets the players first choice as 1
            car = 1
            goat1 = 2
            goat2 = 0
        elif choice1 == goat1:
            goat1 = 1
            car = 2
            goat2 = 0
        else:
            goat2 = 1
            car = 2
            goat1 =0 

        if choice2 == 1 and choice2 == car:
            stay += 1
            win += 1
            staywin += 1
        elif choice2 == 2 and choice2 == car:
            win += 1
            switch +=1
            switchwin += 1
        elif choice2 == 1 and choice2 != car:
            loss += 1
            stay += 1
            stayloss += 1 
        else:
            loss += 1
            switch += 1
            switchloss +=1 


        runs +=1


    lossperc = loss/N
    winperc = win/N

    switchperc = switch/N
    switchwinperc = switchwin/switch
    switchlossperc = switchloss/switch

    stayperc = stay/N
    staywinperc = staywin/stay
    staylossperc = stayloss/stay


    print("Number of runs: {}".format(N))
    print("Number of losers: {}".format(loss))
    print("Percent of losers: {}".format(lossperc))
    print("Number of winners: {}".format(win))
    print("Percentage overall that won: {}".format(winperc))

    print("\n")

    print("Number of switchers: {}".format(switch))
    print("Percentage of switchers: {}".format(switchperc))
    print("Percentage of those who switched and won: {}".format(switchwinperc))
    print("Percentage of those who switched and lost: {}".format(switchlossperc))

    print("\n")

    print("Number of stayers: {}".format(stay))
    print("Percentage of stayers: {}".format(stayperc))
    print("Percentage of those who stayed and won: {}".format(staywinperc))
    print("Percentage of those who stayed and lost: {}".format(staylossperc))


montyhallproblem(1000000)