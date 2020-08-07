from menu import main as menu
from menu import Menu
from snakes import main as game
import curses
import time


def main(stdscr):
    diff_level = {"Easy": 100, "Medium": 75, "Hard":50}
    while True:
        menu_list = Menu().menu
        sh, sw = stdscr.getmaxyx()
        choice = menu(stdscr)
        if choice == "Exit_No":
            continue
        elif choice == "Exit_Yes":
            break
        elif choice in Menu().levels:
            game(stdscr, diff_level[choice])

if __name__ == "__main__":
    curses.wrapper(main)
