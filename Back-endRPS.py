def rps_round(comp_move):
    '''
    Purpose:
    A single round game of rock paper scissors vs a cpu
    Parameter(s):
    The CPU's move which is "R", "P", "S", which repersents rock, paper, or scissors
    Return value:
    A win repersented by P, a tie repersented with T and a loss repersented with c
    '''
    move = input("Type your choice, R for Rock, S for scissors, P for paper: " )
    while move != "R" and move!= "P" and move!= "S":
        print("Invalid move")
        move = input("Type your choice, R for Rock, S for scissors, P for paper: " )
    if comp_move == "R":
        if move == "R":
            print("Tie!")
            return "T"
        if move == "P":
            print("Player wins!")
            return "P"
        if move == "S":
            print("Computer wins!")
            return "C"
    if comp_move == "P":
        if move == "P":
            print("Tie!")
            return "T"
        if move == "S":
            print("Player wins!")
            return "P"
        if move == "R":
            print("Computer wins!")
            return "C"
    if comp_move == "S":
        if move == "S":
            print("Tie!")
            return "T"
        if move == "R":
            print("Player wins!")
            return "P"
        if move == "P":
            print("Computer wins!")
            return "C"

def rps_game():
    '''
    Purpose:
    a 3 round game of rock paper scissors vs a CPU
    Parameter(s):
    None
    Return value: A victory against the CPU, the current amount of consecutive wins, and the amount of rounds played
    '''
    playerwins = 0
    rounds = 0
    while playerwins < 3:
        if playerwins < 3:
            firstround = rps_round("R")
            if firstround == "P":
                rounds = rounds + 1
                playerwins = playerwins + 1
                print('Rounds: ' , rounds , 'Consectutive wins: ', playerwins)
            if firstround == "T":
                rounds = rounds + 1
                playerwins =  0
                print('Rounds: ' , rounds , 'Consectutive wins: ', playerwins)
            if firstround == "C":
                rounds = rounds + 1
                playerwins = 0
                print('Rounds: ' , rounds , 'Consectutive wins: ', playerwins)
        if playerwins < 3:
            secondround = rps_round("P")
            if secondround == "P":
                rounds = rounds + 1
                playerwins = playerwins + 1
                print('Rounds: ' , rounds , 'Consectutive wins: ', playerwins)
            if secondround == "T":
                rounds = rounds + 1
                playerwins =  0
                print('Rounds: ' , rounds , 'Consectutive wins: ', playerwins)
            if secondround == "C":
                rounds = rounds + 1
                playerwins = 0
                print('Rounds: ' , rounds , 'Consectutive wins: ', playerwins)
        if playerwins < 3:
            thirdround = rps_round("S")
            if thirdround == "P":
                rounds = rounds + 1
                playerwins = playerwins + 1
                print('Rounds: ' , rounds , 'Consectutive wins: ', playerwins)
            if thirdround == "T":
                rounds = rounds + 1
                playerwins =  0
                print('Rounds: ' , rounds , 'Consectutive wins: ', playerwins)
            if thirdround == "C":
                rounds = rounds + 1
                playerwins = 0
                print('Rounds:' , rounds , 'Consectutive wins:', playerwins)


    print("Player wins!")
    return rounds
