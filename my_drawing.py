"""
File:
Name:Kang
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: Chinese Rilakkuma
    This is Rilakkuma. He is famous for his cute face.
    However, as he got older, he went to China for cosmetic surgery,
    but unfortunately, the surgery was unsuccessful:(
    """
    window = GWindow(400, 400)
    background(window)
    left_ear(window)
    right_ear(window)
    head(window)
    eye(window)
    mouth(window)
    text(window)


def mouth(window):
    m = GOval(45, 40, x=185, y=150)
    m.filled = True
    m.fill_color = 'white'
    m.color = 'white'
    window.add(m)

    y1p = 170
    y2p = 178
    lbx = 209

    lb0 = GLine(lbx, y1p, lbx-13, y2p)
    window.add(lb0)
    lb = GLine(lbx+1, y1p, lbx-12, y2p)
    window.add(lb)
    lb2 = GLine(lbx+2, y1p, lbx-11, y2p)
    window.add(lb2)

    rb0 = GLine(lbx, y1p, lbx+13, y2p)
    window.add(rb0)
    rb = GLine(lbx+1, y1p, lbx+14, y2p)
    window.add(rb)
    rb2 = GLine(lbx+1, y1p, lbx+15, y2p)
    window.add(rb2)

    b1 = GOval(10, 10, x=lbx-5, y=160)
    b1.filled = True
    window.add(b1)


def eye(window):
    le = GOval(15, 15, x=155, y=135)
    le.filled = True
    le.fill_color = 'darkgrey'
    window.add(le)

    re = GOval(15, 15, x=le.x+88, y=le.y)
    re.filled = True
    re.fill_color = 'darkgrey'
    window.add(re)


def right_ear(window):
    re = GOval(50, 50, x=255, y=55)
    re.filled = True
    re.fill_color = 'darkgoldenrod'
    re.color = 'darkgrey'
    window.add(re)

    re1 = GOval(25, 25, x=270, y=80)
    re1.filled = True
    re1.fill_color = 'goldenrod'
    re1.color = 'darkgrey'
    window.add(re1)


def left_ear(window):
    le = GOval(50, 50, x=105, y=55)
    le.filled = True
    le.fill_color = 'darkgoldenrod'
    le.color = 'darkgrey'
    window.add(le)

    le1 = GOval(25, 25, x=115, y=80)
    le1.filled = True
    le1.fill_color = 'goldenrod'
    le1.color = 'darkgrey'
    window.add(le1)


def head(window):
    h = GOval(170, 140, x=120, y=60)  # head
    h.filled = True
    h.fill_color = 'darkgoldenrod'
    h.color = 'darkgrey'
    window.add(h)


def background(window):
    back = GRect(window.width, window.height)
    back.filled = True
    back.fill_color = 'goldenrod'
    window.add(back)


def text(window):
    text1 = GLabel('Made in China', x=50, y=300)
    text1.font = '-50'
    window.add(text)


if __name__ == '__main__':
    main()
