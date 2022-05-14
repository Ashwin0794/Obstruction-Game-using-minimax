import solver
import sys

if len(sys.argv) != 3:
    print('Command line argument : [player] [algorithm]')
    sys.exit()

algo = sys.argv[2]
if algo != 'MM' and algo != 'AB':
    print('algorithm not be identified!! It can be only MM or AB')
    sys.exit()

# MAX player with symbol 'O'
if sys.argv[1] == '1':
    gameTurnOfAI = 1

#MIN player with symbol 'X'
else:
    gameTurnOfAI = 2

solver = solver.Solver()
solver.play(gameTurnOfAI)

print("End of Game")
