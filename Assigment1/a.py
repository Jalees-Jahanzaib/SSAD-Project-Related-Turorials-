# Curses uses cursor in terminal;
import curses
import time

def main(stdscr):
    curses.curs_set(0)
    stdscr.addstr(15,5,"Hello")
    stdscr.refresh()
    time.sleep(3)
curses.wrapper(main) # runs main function in try and error block and returns the terminal to initial state after code is completd
