"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# Constant
SIZE = 30

# Global Variables
window = GWindow(title='draw line')
circle1 = GOval(SIZE, SIZE)
trigger = True
"""
The trigger can make the circle be deleted. If True it will be able to draw a circle,
or the circle be drawn will be deleted.(讓click會消除的機制，如果是True就可以畫圈，False就會消除圈)
"""


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """

    onmouseclicked(make_circle)


def make_circle(position):
    """
    param: mouse x, y
    """
    global trigger  # 宣吿global variable 變 local variable?

    if trigger:
        """
        If True, we can make a circle, it will be our star point of line
        """
        window.add(circle1, x=position.x-SIZE//2, y=position.y-SIZE//2)
        trigger = False
    else:
        """
        If False, it mean we had a circle, and don't need second circle. It will remove the circle_1,
        use the position of circle_1 and the position of mouse to draw a line.
        """

        line = GLine(circle1.x, circle1.y, position.x, position.y)
        window.add(line)
        window.remove(circle1)
        trigger = True


if __name__ == "__main__":
    main()
