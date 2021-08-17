import numpy as np


PI = np.pi


def calc_angle(ppl: int):
    return (ppl/100)*2*PI


def calc_tangent(ppl):
    return np.tan(0.5*PI-calc_angle(ppl))


def calc_coord(ppl, xrange=200, yrange=200):
    tgt = calc_tangent(ppl)
    if 12.5 <= ppl < 37.5:
        return [xrange, tgt*xrange]
    elif 37.5 <= ppl < 62.5:
        return [-yrange/tgt, -yrange]
    elif 62.5 <= ppl < 87.5:
        return [-xrange, -tgt*xrange]
    else:  # ppl >= 87.5 or <= 12.5
        return [yrange/tgt, yrange]


def calc_polygon(coord, xrange=200, yrange=200):
    coord = [int(i) for i in coord]
    x = coord[0]
    y = coord[1]
    assert (abs(x) == xrange or abs(y) == yrange)

    if x == 0 and y == yrange:
        polygon = [[-xrange, yrange], [xrange, yrange], [xrange, -yrange], [-xrange, -yrange]]  # all
    elif x > 0 and y == yrange:
        polygon = [[0, 0], [0, yrange], coord]
    elif x == xrange:
        # elif x == xrange and y > 0:
        polygon = [[0, 0], [0, yrange], [xrange, yrange], coord]
    # elif x == xrange and y < 0:
    #     polygon = [[0,0], [0,yrange], [xrange,yrange], coord]
    elif y == -yrange:
        # elif x > 0 and y == -yrange:
        polygon = [[0, 0], [0, yrange], [xrange, yrange], [xrange, -yrange], coord]
    # elif x < 0 and y == -yrange:
    #     polygon = [[0,0], [0,yrange], [xrange,yrange], [xrange,-yrange], coord]
    elif x == -xrange:
        polygon = [[0, 0], [0, yrange], [xrange, yrange], [xrange, -yrange], [-xrange, -yrange], coord]
    else:  # x < 0 and y == yrange
        polygon = [[0, 0], [0, yrange], [xrange, yrange], [xrange, -yrange], [-xrange, -yrange], [-xrange, yrange], coord]

    return polygon


def process_coord(coord, xrange=200, yrange=200):
    # convert from x-y to image coordinates
    return[coord[0]+xrange, abs(coord[1]-yrange)]


def process_polygon(polygon):
    return [process_coord(i) for i in polygon]
