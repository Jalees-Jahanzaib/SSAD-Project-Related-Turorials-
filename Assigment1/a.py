# Curses uses cursor in terminal;
import curses
import time

stdscr= curses.initscr() #Initizes terminal session
curses.noecho() #no print on terminal
curses.cbreak() # write something and it is collected and enter is not required
stdscr.keypad(True) #activates the Keyboard for input

stdscr.addstr(15,5,"Hello")
stdscr.refresh()
time.sleep(3)
curses.echo() 
curses.nocbreak() # Reseting
stdscr.keypad(False)
curses.endwin() # Ends terminal Session