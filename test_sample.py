from collections import deque

import pytest

from core import distance, is_inside_the_reigon, direction, central, iou, is_walking
from core import does_trackers_olap
from core import count_people_in_reigon
test_deque= [(132, 198), (132, 198), (132, 198), (132, 198), (133, 199), (132, 196), (135, 199), (130, 197), (135, 199), (131, 200), (133, 200), (131, 198), (134, 198), (133, 195), (136, 198), (132, 197), (134, 197), (134, 197), (132, 197), (135, 197), (133, 197), (136, 197), (136, 200), (134, 198), (137, 198), (135, 197), (133, 197), (136, 197), (134, 196), (136, 196), (136, 196), (134, 191), (137, 194), (133, 193), (135, 193), (134, 192), (136, 192)]
trackers_list=[[12,47,111,87],[744,12,887,22]]
coordinates =[[369, 104, 430, 331], [94, 90, 171, 302]]


def test1_distance_function():
    assert distance([2,3],[1,6]) == 3.1622776601683795


def test3_tracker_overlaping():
    assert does_trackers_olap([122,32,11,46], trackers_list)== [False]

def test4_people_count():
    assert count_people_in_reigon([0,10,600,346], coordinates)== 2

def test5_is_inside_region():
    assert is_inside_the_reigon([0, 10, 600, 346], [122,32,12,75]) == True

def test6_direction():
    assert direction([123,53], [455,332]) == 'right'

def test7_central():
    assert central([369, 104, 430, 331]) == [399, 217]

def test8_iou():
    assert iou([369, 104, 430, 331], [300, 20, 449, 336]) == 29.409141109506415

def test9_is_walking():
    assert is_walking(test_deque) == True










