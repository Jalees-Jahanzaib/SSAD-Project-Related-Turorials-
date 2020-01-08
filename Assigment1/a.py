# Curses uses cursor in terminal;
import curses
from curses import textpad
import time
def main(stdscr):
    curses.curs_set(0)
    sh,sw=stdscr.getmaxyx()
    box=[[3,3],[sh-3,sw-3]]
    textpad.rectangle(stdscr,box[0][0],box[0][1],box[1][0],box[1][1])
    stdscr.refresh()
    stdscr.getch()

curses.wrapper(main) # runs main function in try and error block and returns the terminal to initial state after code is completd
