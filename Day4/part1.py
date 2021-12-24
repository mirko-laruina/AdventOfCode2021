#!/bin/env python3

def mark_entry(board, number):
    for i, row in enumerate(board):
        for j, board_num in enumerate(row):
            if board_num[0] == number:
                board_num[1] = True
                return i, j
    return None        

def check_win(board, marked_pos):
    winning_row = True
    for board_num in board[marked_pos[0]]:
        if board_num[1] == False:
            winning_row = False
            break
        
    winning_col = True
    for i in range(len(board)):
        board_num = board[i][marked_pos[1]]
        if board_num[1] == False:
            winning_col = False
            break

    return winning_col or winning_row

def calc_sum(board):
    sum = 0
    for board_row in board:
        for board_num in board_row:
            if(board_num[1] == False):
                sum += board_num[0]

    return sum


with open("input.txt") as f:
    lines = f.readlines()

numbers_line = lines[0]
numbers = [int(n.strip()) for n in numbers_line.split(",")]

boards = []
current_board = []
for line in lines[1:]:
    splits = line.split()
    if(len(splits) == 0):
        current_board = []
        boards.append(current_board)
        continue

    row_numbers = [ [int(s), False] for s in splits ]
    current_board.append(row_numbers)


for number in numbers:
    for board in boards:
        marked_pos = mark_entry(board, number)
        if marked_pos is None:
            continue

        won = check_win(board, marked_pos)
        if won:
            sum = calc_sum(board)
            print("Sum:", sum)
            print("Called num:", number)
            print("Product:", sum*number)
            break

    if won:
        break