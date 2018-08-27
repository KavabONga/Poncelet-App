import sys, pygame, math, numpy
from pygame import gfxdraw


class XY:
    def __init__(self, xcoor, ycoor):
        self.x = xcoor
        self.y = ycoor

    def tup(self):
        return (self.x, self.y)


size = XY(1400, 800)
speed = 4


class Btn:
    def __init__(self, size, filename):
        self.x = size.x
        self.y = size.y
        self.img = pygame.image.load(filename)
        self.img.set_colorkey((0, 0, 0))


def dist(a, b):
    return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)


def draw_tch(cpnt, circ, pnt, color):
    x1 = circ.x + r * (r * (cpnt.x - circ.x) + (cpnt.y - circ.y) * math.sqrt(
        (cpnt.y - circ.y) ** 2 + (cpnt.x - circ.x) ** 2 - r ** 2)) / ((cpnt.y - circ.y) ** 2 + (cpnt.x - circ.x) ** 2)
    y1 = circ.y + r * (r * (cpnt.y - circ.y) - (cpnt.x - circ.x) * math.sqrt(
        (cpnt.y - circ.y) ** 2 + (cpnt.x - circ.x) ** 2 - r ** 2)) / ((cpnt.y - circ.y) ** 2 + (cpnt.x - circ.x) ** 2)
    if (cpnt.x == x1):
        xs = cpnt.x
        ys = pnt.y
    else:
        if (cpnt.y == y1):
            ys = cpnt.y
            xs = pnt.x
        else:
            xs = int(((pnt.y - pnt.x * (-1 / ((cpnt.y - y1) / (cpnt.x - x1)))) - (
                    (x1 * cpnt.y - cpnt.x * y1) / (x1 - cpnt.x))) / (
                             ((cpnt.y - y1) / (cpnt.x - x1)) - (-1 / ((cpnt.y - y1) / (cpnt.x - x1)))))
            ys = int((((x1 * cpnt.y - cpnt.x * y1) / (x1 - cpnt.x)) * (-1 / ((cpnt.y - y1) / (cpnt.x - x1))) - (
                    pnt.y - pnt.x * (-1 / ((cpnt.y - y1) / (cpnt.x - x1)))) * ((cpnt.y - y1) / (cpnt.x - x1))) / (
                             (-1 / ((cpnt.y - y1) / (cpnt.x - x1))) - ((cpnt.y - y1) / (cpnt.x - x1))))
    pygame.draw.line(screen, color, (x1, y1), (cpnt.x, cpnt.y))
    pygame.draw.line(screen, color, (x1, y1), (2 * xs - cpnt.x, 2 * ys - cpnt.y))
    return XY(2 * xs - cpnt.x, 2 * ys - cpnt.y)


def get_tch(cpnt, circ, pnt):
    x1 = circ.x + r * (r * (cpnt.x - circ.x) + (cpnt.y - circ.y) * math.sqrt(
        (cpnt.y - circ.y) ** 2 + (cpnt.x - circ.x) ** 2 - r ** 2)) / ((cpnt.y - circ.y) ** 2 + (cpnt.x - circ.x) ** 2)
    y1 = circ.y + r * (r * (cpnt.y - circ.y) - (cpnt.x - circ.x) * math.sqrt(
        (cpnt.y - circ.y) ** 2 + (cpnt.x - circ.x) ** 2 - r ** 2)) / ((cpnt.y - circ.y) ** 2 + (cpnt.x - circ.x) ** 2)
    if (cpnt.x == x1):
        xs = cpnt.x
        ys = pnt.y
    else:
        if (cpnt.y == y1):
            ys = cpnt.y
            xs = pnt.x
        else:
            xs = int(((pnt.y - pnt.x * (-1 / ((cpnt.y - y1) / (cpnt.x - x1)))) - (
                    (x1 * cpnt.y - cpnt.x * y1) / (x1 - cpnt.x))) / (
                             ((cpnt.y - y1) / (cpnt.x - x1)) - (-1 / ((cpnt.y - y1) / (cpnt.x - x1)))))
            ys = int((((x1 * cpnt.y - cpnt.x * y1) / (x1 - cpnt.x)) * (-1 / ((cpnt.y - y1) / (cpnt.x - x1))) - (
                    pnt.y - pnt.x * (-1 / ((cpnt.y - y1) / (cpnt.x - x1)))) * ((cpnt.y - y1) / (cpnt.x - x1))) / (
                             (-1 / ((cpnt.y - y1) / (cpnt.x - x1))) - ((cpnt.y - y1) / (cpnt.x - x1))))
    return XY(2 * xs - cpnt.x, 2 * ys - cpnt.y)


arw_right = Btn(XY(60, 60), 'btn_right.png')
arw_left = Btn(XY(60, 60), 'btn_left.png')
arw_up = Btn(XY(60, 60), 'btn_up.png')
arw_down = Btn(XY(60, 60), 'btn_down.png')
arws_up = Btn(XY(64, 64), 'arrows_up.png')
arws_down = Btn(XY(64, 64), 'arrows_down.png')
window = pygame.display.set_mode(size.tup())
pygame.display.set_caption('This is going to be something new')
screen = pygame.Surface(size.tup())
pygame.key.set_repeat(1, 200)
circle_coor = XY(400, 400)
point = XY(int(size.x / 2) - 100, int(size.y / 2))
color = (255, 255, 255)
r = 100
bigr = int(size.y / 2) - 10
cirpnt = XY(point.x, point.y - bigr)
draw_line = False
mig = 0
do_mig = False
pi = 3.141592653
close = False
wid = 3
pre_succ = False
while True:
    moved = False
    for e in pygame.event.get():
        if (e.type == pygame.QUIT):
            sys.exit()
    if (True in pygame.mouse.get_pressed()):
        m = pygame.mouse.get_pos()
        if ((m[0] < size.x) and (m[0] > size.x - arw_right.x)) and (
                (m[1] < size.y - arw_down.y) and (m[1] > size.y - arw_down.y - arw_right.y)):
            if (dist(XY(circle_coor.x + 1, circle_coor.y), point) + r < bigr - 40):
                circle_coor.x += 1
                moved = True
        if ((m[0] < size.x - arw_right.x) and (m[0] > size.x - arw_right.x - arw_down.x)) and (
                (m[1] < size.y) and (m[1] > size.y - arw_down.y)):
            if (dist(XY(circle_coor.x, circle_coor.y + 1), point) + r < bigr - 40):
                circle_coor.y += 1
                moved = True
        if ((m[0] < size.x - arw_right.x - arw_down.x) and (
                m[0] > size.x - arw_right.x - arw_down.x - arw_left.x)) and (
                (m[1] < size.y - arw_down.y) and (m[1] > size.y - arw_down.y - arw_right.y)):
            if (dist(XY(circle_coor.x - 1, circle_coor.y), point) + r < bigr - 40):
                circle_coor.x -= 1
                moved = True
        if ((m[0] < size.x - arw_right.x) and (m[0] > size.x - arw_right.x - arw_up.x)) and (
                (m[1] < size.y - arw_down.y - arw_right.y) and (m[1] > size.y - arw_down.y - arw_right.y - arw_up.y)):
            if (dist(XY(circle_coor.x, circle_coor.y - 1), point) + r < bigr - 40):
                circle_coor.y -= 1
                moved = True
        if ((m[0] < size.x - arw_right.x * 3) and (m[0] > size.x - arw_up.x * 3 - 150)) and (
                (m[1] < size.y - arw_right.y * 1.5) and (m[1] > size.y - arw_up.y * 1.5 - 100)) and (
        (dist(XY(circle_coor.x, circle_coor.y - 2), point) + r + 0.5 < bigr - 40)):
            r += 1
            moved = True
        if ((m[0] < size.x - arw_right.x * 3) and (m[0] > size.x - arw_up.x * 3 - 150)) and (
                (m[1] < size.y) and (m[1] > size.y - arw_up.y * 1.5)):
            if (r > 50):
                r -= 1
                moved = True
        if (dist(XY(m[0], m[1]), point) > bigr - 80) and (dist(XY(m[0], m[1]), point) < bigr + 80):
            cirpnt.x = int(point.x + (m[0] - point.x) * bigr / dist(point, XY(m[0], m[1])))
            cirpnt.y = int(point.y - (point.y - m[1]) * bigr / dist(point, XY(m[0], m[1])))
    screen.fill((0, 0, 0))
    '''gfxdraw.pixel(screen,point.x,point.y, color)
    x1=circle_coor.x+r*(r*(point.x-circle_coor.x)+(point.y-circle_coor.y)*math.sqrt((point.y-circle_coor.y)**2 + (point.x-circle_coor.x)**2-r**2))/((point.y-circle_coor.y)**2 + (point.x-circle_coor.x)**2)
    x2=circle_coor.x+r*(r*(point.x-circle_coor.x)-(point.y-circle_coor.y)*math.sqrt((point.y-circle_coor.y)**2 + (point.x-circle_coor.x)**2-r**2))/((point.y-circle_coor.y)**2 + (point.x-circle_coor.x)**2)
    y1=circle_coor.y+r*(r*(point.y-circle_coor.y)-(point.x-circle_coor.x)*math.sqrt((point.y-circle_coor.y)**2 + (point.x-circle_coor.x)**2-r**2))/((point.y-circle_coor.y)**2 + (point.x-circle_coor.x)**2)
    y2=circle_coor.y+r*(r*(point.y-circle_coor.y)+(point.x-circle_coor.x)*math.sqrt((point.y-circle_coor.y)**2 + (point.x-circle_coor.x)**2-r**2))/((point.y-circle_coor.y)**2 + (point.x-circle_coor.x)**2)
    tch1=XY(x1,y1)
    tch2=XY(x2,y2)
    pygame.draw.line(screen, color, point.tup(), tch1.tup())
    pygame.draw.line(screen, color, point.tup(), tch2.tup())'''
    pygame.draw.circle(screen, color, point.tup(), bigr, 3)
    circolor = (255, 255, 0)
    if (True):
        colorit = (0, 255, 0)
        newpnt = get_tch(cirpnt, circle_coor, point)
        newnewpnt = get_tch(newpnt, circle_coor, point)
        lastpnt = get_tch(newnewpnt, circle_coor, point)
        if (dist(lastpnt, cirpnt) < 20 or (pre_succ and not moved)):
            colorit = (64, 230, 255)
            close = True
            wid = 0
            circolor = (255, 0, 0)
            pre_succ = True
        else:
            close = False
            pre_succ = False
            wid = 3
        pygame.draw.line(screen, colorit, cirpnt.tup(), newpnt.tup())
        pygame.draw.line(screen, colorit, newnewpnt.tup(), newpnt.tup())
        if close:
            pygame.draw.line(screen, colorit, newnewpnt.tup(), cirpnt.tup())
        else:
            pygame.draw.line(screen, colorit, newnewpnt.tup(), lastpnt.tup())
        if lastpnt.y == point.y:
            if (lastpnt.x < point.x):
                arc1 = pi
            else:
                arc1 = 0
        else:
            arc1 = numpy.arccos(-(point.x - lastpnt.x) / bigr)
            if (lastpnt.y > point.y):
                arc1 = 2 * pi - arc1
        if cirpnt.y == point.y:
            if (cirpnt.x < point.x):
                arc2 = pi
            else:
                arc2 = 0
        else:
            arc2 = numpy.arccos(-(point.x - cirpnt.x) / bigr)
            if (cirpnt.y > point.y):
                arc2 = 2 * pi - arc2
        if (arc1 > arc2):
            arc1, arc2 = arc2, arc1
        if (arc2 - arc1 > pi):
            arc1, arc2 = arc2, arc1
        pygame.draw.arc(screen, (255, 0, 0), [point.x - bigr, point.y - bigr, 2 * bigr, 2 * bigr], arc1, arc2, 5)

    pygame.draw.circle(screen, circolor, circle_coor.tup(), r, wid)
    pygame.draw.circle(screen, (0, 0, 255), cirpnt.tup(), 8, 0)
    screen.blit(arws_up.img, (size.x - 300, size.y - 154))
    screen.blit(arws_down.img, (size.x - 300, size.y - 90))
    screen.blit(arw_right.img, (size.x - arw_right.x, size.y - arw_right.y * 2))
    screen.blit(arw_down.img, (size.x - arw_down.x * 2, size.y - arw_down.y))
    screen.blit(arw_left.img, (size.x - arw_left.x * 3, size.y - arw_left.y * 2))
    screen.blit(arw_up.img, (size.x - arw_down.x * 2, size.y - arw_down.y * 3))
    window.blit(screen, (0, 0))
    pygame.display.flip()
    pygame.time.delay(5)