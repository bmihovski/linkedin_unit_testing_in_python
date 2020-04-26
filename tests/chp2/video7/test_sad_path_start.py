import pytest
from scripts import data_processor

# from scripts import data_processor


@pytest.fixture(scope="function")
def city_list_location_malformed():
    return 'tests/resources/cities/malformed_map.csv'


def test_csv_reader_malformed_data_contents(city_list_location_malformed):
    """
    Sad Path Test

    We will need to wrap the following line
    in the exceptions context manager:
    """
    with pytest.raises(ValueError) as exp:
        data_processor.csv_reader(city_list_location_malformed)
    assert str(exp.value) == "could not convert string to float: 'not_an_altitude'"
