"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

# Constant
VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# Global
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
drop_count = 0
trigger = True  # 滑鼠開關


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(drop)
    ball.filled = True

    window.add(ball, START_X, START_Y)


def drop(position):
    global GRAVITY, drop_count, trigger

    if trigger:
        trigger = False
        drop_speed = 0
        drop_count += 1

        while drop_count <= 3:
            drop_speed += GRAVITY
            ball.move(VX, drop_speed)
            if ball.y+drop_speed >= window.height-SIZE:
                """
                不能用ball.y+SIZE,因為有可能ball move的drop speed會掉到地板下，
                所以要改+drop speed，當最後一下+dp大於螢幕（地板）時，就要直接回彈，
                避免掉到地板下的情況
                """
                drop_speed = -drop_speed
                drop_speed *= REDUCE

            if ball.x >= window.width:
                trigger = True
                break

            pause(DELAY)
        window.add(ball, START_X, START_Y)


if __name__ == "__main__":
    main()
