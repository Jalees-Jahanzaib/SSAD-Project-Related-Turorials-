# Curses uses cursor in terminal;
import curses
import time

def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1,curses.COLOR_RED,curses.COLOR_YELLOW)
    h,w=stdscr.getmaxyx()
    text= "Main Menu"
    x=int(w/2-len(text)/2)
    y=int(h/2)
    stdscr.attron(curses.color_pair(1))

    stdscr.addstr(y,x,text)
    stdscr.attroff(curses.color_pair(1))

    stdscr.refresh()
    time.sleep(3)

curses.wrapper(main) # runs main function in try and error block and returns the terminal to initial state after code is completd
