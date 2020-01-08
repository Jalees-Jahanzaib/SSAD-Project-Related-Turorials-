# Curses uses cursor in terminal;
import curses
import time

def main(stdscr):
    curses.curs_set(0)
    h,w=stdscr.getmaxyx()
    text= "Main Menu"
    x=int(w/2-len(text)/2)
    y=int(h/2)
    stdscr.addstr(y,x,text)
    stdscr.refresh()
    time.sleep(3)

curses.wrapper(main) # runs main function in try and error block and returns the terminal to initial state after code is completd
