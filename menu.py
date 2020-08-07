import time
import curses

class Menu():
    def __init__(self):
        self.menu = ["Home", "Play", "Scoreboard", "Exit"]

    def print_menu(self, stdscr, selected_row):
        stdscr.clear()
        sh, sw = stdscr.getmaxyx()
        for row, text in enumerate(self.menu):
            x = sw//2 - len(text)//2
            y = sh//2 + row - len(self.menu)//2
            if row == selected_row:
                # set color scheme
                stdscr.attron(curses.color_pair(1))
                # write text on screen
                stdscr.addstr(y, x, text)
                # unset color scheme
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, text)
        stdscr.refresh()

def main(stdscr):
    # turn off cursor blinking
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)
    # get height and width of screen
    sh, sw = stdscr.getmaxyx()
    # create a new color scheme
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    current_row = 0
    menu = Menu()
    while 1:
        key = stdscr.getch()
        if key == curses.KEY_DOWN and (current_row<len(menu.menu)-1):
            current_row += 1
        elif key == curses.KEY_UP and (current_row>0):
            current_row -= 1
        elif key == curses.KEY_ENTER or key == ord('\n'):
            text = "You have choosen: "+ menu.menu[current_row]
            x = sw//2 - len(text)//2
            y = sh//2
            stdscr.clear()
            stdscr.addstr(y, x, text)
            stdscr.refresh()
            break
        menu.print_menu(stdscr, current_row)
    time.sleep(3)
    stdscr.clear()
    return menu.menu[current_row]

if __name__ == "__main__":
    curses.wrapper(main)















# code end
