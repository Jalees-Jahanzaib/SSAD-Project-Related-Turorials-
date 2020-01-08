# Curses uses cursor in terminal;
import curses
import time

def main(stdscr):
    curses.curs_set(0)
    while 1:
        key=stdscr.getch()
        stdscr.clear()
        if key==curses.KEY_UP:
            stdscr.addstr(0,0,"You Pressed UP Key!!")
        elif key==curses.KEY_DOWN:
            stdscr.addstr(0,0,"You Pressed DOWN Key!!")
        elif key==curses.KEY_ENTER or key in [10,13]:
            stdscr.addstr(0,0,"You Pressed ENTER Key!!")    
        stdscr.refresh()

curses.wrapper(main) # runs main function in try and error block and returns the terminal to initial state after code is completd
