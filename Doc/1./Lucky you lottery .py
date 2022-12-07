win = open('/Users/wahaha/Documents/GitHub/Code-pen/Python-learning-note/Doc/1./lotteryNumber.txt').read().split()
mine = open(
    '/Users/wahaha/Documents/GitHub/Code-pen/Python-learning-note/Doc/1./myNumber.txt').read().split()

for i, num in enumerate(mine):
    if num in win:
        print('Number', i+1, 'lottery ticket', num, 'is win !')
    else:
        print('Sorry try next time.')
