
pos1 = '1'
pos2 = '2'
pos3 = '3'
pos4 = '4'
pos5 = '5'
pos6 = '6'
pos7 = '7'
pos8 = '8'
pos9 = '9'

board = f'''
    {pos1} | {pos2} | {pos3}
   ---+---+---
    {pos4} | {pos5} | {pos6}
   ---+---+---
    {pos7} | {pos8} | {pos9}
'''
    
# print(board)


ply1 = 'X'
ply2 = 'O'
print(f'\n [[ PLAYER 1 YOUR ARE [{ply1}] AND PLAYER 2 YOU ARE [{ply2}] ]]] \n')




while True:
    all_pos = [pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8,pos9]
    if '1' not in all_pos and '2' not in all_pos  and '3' not in all_pos and '6' not in all_pos and '7' not in all_pos and '8' not in all_pos and '9':
        print('\n CLEANING BOARD RIGTH NOW \n')
        pos1 = '1'
        pos2 = '2'
        pos3 = '3'
        pos4 = '4'
        pos5 = '5'
        pos6 = '6'
        pos7 = '7'
        pos8 = '8'
        pos9 = '9'
        board = f'''
            {pos1} | {pos2} | {pos3}
            ---+---+---
            {pos4} | {pos5} | {pos6}
            ---+---+---
            {pos7} | {pos8} | {pos9}
        '''
        all_pos = [pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8,pos9]
        print(board)
        print('\n CLEANING BOARD SUCCESFULLY \n')


    while True:
        try:
            print(board)
            p_ply1 = int(input(' >>> PLAYER 1 YOUR TURN <<< \n CHOSE WERE YOU WANT TO PLAY BTW FROM [1 TO 9] ON THE BOARD IF AVALIABLE :'))
            if all_pos[p_ply1-1] not in ['X','O']:
                if p_ply1 == 1:
                    pos1 = ply1
                elif p_ply1 == 2:
                    pos2 = ply1
                elif p_ply1 == 3:
                    pos3 = ply1
                elif p_ply1 == 4:
                    pos4 = ply1
                elif p_ply1 == 5:
                    pos5 = ply1
                elif p_ply1 == 6:
                    pos6 = ply1
                elif p_ply1 == 7:
                    pos7 = ply1
                elif p_ply1 == 8:
                    pos8 = ply1
                elif p_ply1 == 9:
                    pos9 = ply1
                else:
                    print('\n ENTER THE PROPER NUMBER ON BOARD FROM [1 TO 9] ON THE BOARD IF AVALIABLE')
                if p_ply1 > 0 and p_ply1 < 10:
                    break
            else:
                print('\n PLEASE PLAY SOMEWHERE ELSE')
        except Exception as err :
            print(err)

    board = f'''
        {pos1} | {pos2} | {pos3}
        ---+---+---
        {pos4} | {pos5} | {pos6}
        ---+---+---
        {pos7} | {pos8} | {pos9}
    '''
    if pos1 =='X' and pos2=='X' and pos3 =='X':
        print(board)
        print('\n PLAYER 1 WON IN [[ ROW 1 ]] \n')
        break
    elif pos4 =='X' and pos5=='X' and pos6 =='X':
        print(board)
        print('\n PLAYER 1 WON IN [[ ROW 2 ]] \n')
        break
    elif pos7 =='X' and pos8=='X' and pos9 =='X':
        print(board)
        print('\n PLAYER 1 WON IN [[ ROW 3 ]] \n')
        break
    elif pos1 =='X' and pos4=='X' and pos7 =='X':
        print(board)
        print('\n PLAYER 1 WON IN [[ COLUMN 1 ]] \n')
        break
    elif pos2 =='X' and pos5=='X' and pos8 =='X':
        print(board)
        print('\n PLAYER 1 WON IN [[ COLUMN 2 ]] \n')
        break
    elif pos3 =='X' and pos6=='X' and pos9 =='X':
        print(board)
        print('\n PLAYER 1 WON IN [[ COLUMN 3 ]] \n')
        break
    elif pos1 =='X' and pos5=='X' and pos9 =='X':
        print(board)
        print('\n PLAYER 1 WON IN [[ DIAGONAL 1 ]] \n')
        break
    elif pos3 =='X' and pos5=='X' and pos7 =='X':
        print(board)
        print('\n PLAYER 1 WON IN [[ DIAGONAL 2 ]] \n')
        break
    else:
        pass

    all_pos = [pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8,pos9]
    if '1' not in all_pos and '2' not in all_pos  and '3' not in all_pos and '6' not in all_pos and '7' not in all_pos and '8' not in all_pos and '9':
        print('\n CLEANING BOARD RIGTH NOW \n')
        pos1 = '1'
        pos2 = '2'
        pos3 = '3'
        pos4 = '4'
        pos5 = '5'
        pos6 = '6'
        pos7 = '7'
        pos8 = '8'
        pos9 = '9'
        board = f'''
            {pos1} | {pos2} | {pos3}
            ---+---+---
            {pos4} | {pos5} | {pos6}
            ---+---+---
            {pos7} | {pos8} | {pos9}
        '''
        all_pos = [pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8,pos9]
        print(board)
        print('\n CLEANING BOARD SUCCESFULLY \n')


    while True:
        try:
            print(board)
            p_ply2 = int(input(' >>> PLAYER 2 YOUR TURN <<< \n CHOSE WERE YOU WANT TO PLAY BTW FROM [1 TO 9] ON THE BOARD IF AVALIABLE :'))
            if all_pos[p_ply2-1] not in ['X','O']:
                if p_ply2 == 1:
                    pos1 = ply2
                elif p_ply2 == 2:
                    pos2 = ply2
                elif p_ply2 == 3:
                    pos3 = ply2
                elif p_ply2 == 4:
                    pos4 = ply2
                elif p_ply2 == 5:
                    pos5 = ply2
                elif p_ply2 == 6:
                    pos6 = ply2
                elif p_ply2 == 7:
                    pos7 = ply2
                elif p_ply2 == 8:
                    pos8 = ply2
                elif p_ply2 == 9:
                    pos9 = ply2
                else:
                    print('\n ENTER THE PROPER NUMBER ON BOARD FROM [1 TO 9] ON THE BOARD IF AVALIABLE')
                if p_ply2 > 0 and p_ply2 < 10:
                    break
            else:
                print('\n PLEASE PLAY SOMEWHERE ELSE')
        except Exception as err :
            print(err)

    board = f'''
        {pos1} | {pos2} | {pos3}
        ---+---+---
        {pos4} | {pos5} | {pos6}
        ---+---+---
        {pos7} | {pos8} | {pos9}
    '''

    if pos1 =='O' and pos2=='O' and pos3 =='O':
        print(board)
        print('\n PLAYER 2 WON IN [[ ROW 1 ]] \n')
        break
    elif pos4 =='O' and pos5=='O' and pos6 =='O':
        print(board)
        print('\n PLAYER 2 WON IN [[ ROW 2 ]] \n')
        break
    elif pos7 =='O' and pos8=='O' and pos9 =='O':
        print(board)
        print('\n PLAYER 2 WON IN [[ ROW 3 ]] \n')
        break
    elif pos1 =='O' and pos4=='O' and pos7 =='O':
        print(board)
        print('\n PLAYER 2 WON IN [[ COLUMN 1 ]] \n')
        break
    elif pos2 =='O' and pos5=='O' and pos8 =='O':
        print(board)
        print('\n PLAYER 2 WON IN [[ COLUMN 2 ]] \n')
        break
    elif pos3 =='O' and pos6=='O' and pos9 =='O':
        print(board)
        print('\n PLAYER 2 WON IN [[ COLUMN 3 ]] \n')
        break
    elif pos1 =='O' and pos5=='O' and pos9 =='O':
        print(board)
        print('\n PLAYER 2 WON IN [[ DIAGONAL 1 ]] \n')
        break
    elif pos3 =='O' and pos5=='O' and pos7 =='O':
        print(board)
        print('\n PLAYER 2 WON IN [[ DIAGONAL 2 ]] \n')
        break
    else:
        pass