p1 = input('Player 1 [R:Rock P:Paper S:Scissors]: ')
p2 = input('Player 2 [R:Rock P:Paper S:Scissors]: ')

def winner(p1, p2):
    if p1 == p2:
        return 'It\'s a draw!'
    if p1 == 'R' and p2 == 'S' or p1 == 'S' and p2 == 'P' or p1 == 'P' and p2 == 'R':
        return 'Player 1 wins!'
    else:
        return 'Player 2 wins!'

print(winner(p1,p2))

