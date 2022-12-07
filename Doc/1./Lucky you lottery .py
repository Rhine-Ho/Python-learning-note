win = open('lotteryNumber.txt').read().split()
mine = open('myNumber.txt').read().split()

for i, num in enumerate(mine):
    if num in win:
        print('Number', i+1, 'lottery ticket', num, 'is win !')
    else:
        print('Sorry try next time.')
