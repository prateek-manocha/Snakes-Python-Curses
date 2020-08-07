from menu import main as menu
from menu import Menu
from snakes import main as game
import curses
import time


def main(stdscr):
    while True:
        menu_list = Menu().menu
        sh, sw = stdscr.getmaxyx()
        choice = menu(stdscr)
        if choice == "Play":
            game(stdscr)
        elif choice == "Exit":
            break

if __name__ == "__main__":
    curses.wrapper(main)
