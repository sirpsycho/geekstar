# geekstar

Tired of that painfully traditional star dominating the top of your office's religiously-neutral holiday tree? I'm right there with you. This holiday season, I opted for a geekier alternative, while learning some new tricks in Python.

![geekstar.gif](https://github.com/sirpsycho/geekstar/blob/master/geekstar.gif)

# Using Python's Curses module to dynamically update terminal output

For this project, I started out with a simple ASCII star that I cut out of some minified javascript code (geekstar.txt). Already, it was looking pretty good but I wanted to add a little animation. Specifically, I wanted to add a shimmer effect, making the star appear shiny.

To do this, I searched for some ideas on dynamically updating terminal output. I originally happened upon some articles which referenced using a return character ('\r') to go to the beginning of the line and overwrite it with new code (see a nice example of that [here](https://kyletk.com/post/9)). This happens to be a nice simple solution for single-line use cases, however, I wanted to dynamically update multiple lines simultaneously. This led me to python's [Curses module](https://docs.python.org/3/howto/curses.html). This allows you to have much more control over the terminal output, such as dynamically updating multiple lines, adding colors and being mindful of your terminal's window size.

# Want to spice up your own tree?

This code is ready to run in most terminal environments. Feel free to mess around with some of the settings under "Global Variables" to customize the output. My PoC ASCII star is attached, but the code should work with your own ASCII art as well.

Happy holidays!
