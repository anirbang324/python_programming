from ctypes import POINTER, pointer
from ctypes.wintypes import POINT, POINTL
from curses.textpad import rectangle
from tkinter import Text
from tokenize import Pointfloat
from turtle import circle
from graphics import *


def create_board(win, size):
    board = []
    for row in range(size):
        board.append([])
        for col in range(size):
            square = rectangle(pointer(col, row), POINTER(col + 1, row + 1))
            square.draw(win)
            board[row].append(square)
    return board


def initialize_players(board, player1_pos, player2_pos):
    player1 = circle(Pointfloat(player1_pos[0] + 0.5, player1_pos[1] + 0.5), 0.4)
    player1.setFill("red")
    player1.draw(board[player1_pos[1]][player1_pos[0]].getCenter())

    player2 = Circle(POINT(player2_pos[0] + 0.5, player2_pos[1] + 0.5), 0.4)
    player2.setFill("green")
    player2.draw(board[player2_pos[1]][player2_pos[0]].getCenter())

    return player1, player2


def check_winner(board, player):
    x, y = int(player.getCenter().getX()), int(player.getCenter().getY())
    return all(board[yy][xx].getFill() == "blue" for xx, yy in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)])


def main():
    size = 8
    win = GraphWin("Icebreaker", 600, 600)
    win.setCoords(0, 0, size, size)

    board = create_board(win, size)

    player1_pos = (1, 1)
    player2_pos = (size - 2, size - 2)

    player1, player2 = initialize_players(board, player1_pos, player2_pos)

    turn_text = Text(POINTL(size / 2, size + 0.5), "Player 1's Turn")
    turn_text.draw(win)

    while True:
        if turn_text.getText() == "Player 1's Turn":
            current_player = player1
            opponent = player2
        else:
            current_player = player2
            opponent = player1

        click_point = win.getMouse()
        click_x = int(click_point.getX())
        click_y = int(click_point.getY())

        if (click_x, click_y) == (0, 0):
            break  # Quit the game if the user clicks at (0, 0)

        if board[click_y][click_x].getFill() == "white":
            current_player.move(click_x - current_player.getCenter().getX(),
                                click_y - current_player.getCenter().getY())
            turn_text.setText(f"Player {2 if current_player == player1 else 1}'s Turn")
        elif board[click_y][click_x].getFill() == "white":
            board[click_y][click_x].setFill("blue")

            # Check for a winner
            if check_winner(board, current_player):
                turn_text.setText(f"Player {1 if current_player == player1 else 2} Wins!")
                break


if __name__ == "__main__":
    main()