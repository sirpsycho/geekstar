#!/usr/local/bin/python3

import sys
from time import sleep
import curses



### Global variables:

# Text file name / location of ASCII art
txtfile = 'geekstar.txt'

# How wide the shimmering band is
shimmerdepth = 4

# What character makes up the shimmering band
shimmerchar = '0'

# How fast the shimmer effect moves (in seconds, the lower the faster)
shimmerspeed = 0.02

# How long to wait before replaying the effect (in seconds)
shimmerwait = 8

# X and Y Coordinates to offset image on the screen
xoffset = 10
yoffset = 5

# Configure terminal colors (set 'configurecolors' to False to keep your terminal defaults, True to configure manually)
configurecolors = False
fontcolor = "green"
backgroundcolor = "black"


# Functions:

def replacechar(text, index=0, replace=shimmerchar):
  if index < 0 or index > len(text) - 2:
    # if the index is out of range, just return the original line
    return text
  else:
    # if the character is blank, leave it blank. Otherwise replace it with the shimmer character
    if text[index] == ' ':
      return '%s%s%s' % (text[:index], ' ', text[index+1:])
    else:
      return '%s%s%s' % (text[:index], replace, text[index+1:])

def printascii(text):
  # this function prints the ascii art to the screen using Curses to overlay the text in exact coordinates
  if configurecolors:
    stdscr.addstr(yoffset, 0, text, curses.color_pair(1))
    stdscr.refresh()
  else:
    stdscr.addstr(yoffset, 0, text)
    stdscr.refresh()



if __name__ == "__main__":

  # Initialize Curses (for dynamic screen/window updating)
  stdscr = curses.initscr()
  curses.noecho()
  curses.cbreak()
  if configurecolors:
    curses.start_color()
    if curses.has_colors():
      colors = {"black": curses.COLOR_BLACK,
        "red": curses.COLOR_RED,
        "green": curses.COLOR_GREEN,
        "yellow": curses.COLOR_YELLOW,
        "blue": curses.COLOR_BLUE,
        "magenta": curses.COLOR_MAGENTA,
        "cyan": curses.COLOR_CYAN,
        "white": curses.COLOR_WHITE}
      curses.init_pair(1, colors[fontcolor.lower()], colors[backgroundcolor.lower()])

  # Store ASCII art in a variable
  with open(txtfile, 'r') as f:
    asciilines = f.readlines()

  # Determine how far the shimmer line can travel based on the dimensions of the ASCII art
  shimmerdistance = len(max(asciilines, key=len)) + len(asciilines)

  # If the ASCII art is not wide enough, quit
  if shimmerdistance < 1:
    print("Error: ASCII art is not wide enough for shimmer effect")
    sys.exit()

  try:
    while True:
      for offset in range(shimmerdistance):
        newlines = []
        for index, line in enumerate(asciilines):
          newline = replacechar(line, index + offset - len(asciilines))
          for i in range(shimmerdepth):
            newline = replacechar(newline, index + offset - len(asciilines) + i)
          newlines.append(' ' * xoffset + newline)
        newascii = ''.join(newlines)
        printascii(newascii)
        sleep(shimmerspeed)
      sleep(shimmerwait)

  except:
    # When someone stops the program, return the window to normal settings before quitting
    curses.endwin()
    sys.exit()

  # return window to normal
  curses.endwin()
