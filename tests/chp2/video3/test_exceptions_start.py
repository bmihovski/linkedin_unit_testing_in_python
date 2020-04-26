from scripts.chp2.video3.mapmaker_exceptions_start import Point
from scripts.chp2.video3.mapmaker_exceptions_start import Map
import pytest


def test_make_one_point():
    p1 = Point("Dakar", 14.7167, 17.4677)
    assert p1.get_lat_long() == (14.7167, 17.4677)


def test_invalid_point_generation():
    with pytest.raises(ValueError) as exp:
        Point("Sofia", 12.11386, -555.08262)
    assert str(exp.value) == "Invalid latitude, longitude combination"


def test_invalid_point_city_name():
    with pytest.raises(ValueError) as exp:
        Point(4, 33.322, 23.332)
    assert str(exp.value) == "Invalid city name type"


def test_map_two_points():
    p1 = Point("res", 23.342, 25.235)
    p2 = Point("tes", 23.533, 12.533)
    map_obj = Map()
    map_obj.maps = p1
    map_obj.maps = p2
    assert map_obj.maps == [p1, p2]


def test_invalid_maps_point():
    p1 = Point("tess", 23.535, 34.233)
    p2 = Point("tere", 22.234, 12.445)
    map_obj = Map()
    map_obj.maps = p1
    assert map_obj.is_point_present(p1)
    with pytest.raises(Exception) as exp:
        map_obj.is_point_present(p2)
    assert str(exp.value) == "Point not found"
