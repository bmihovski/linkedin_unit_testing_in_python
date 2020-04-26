import pytest
import os
from scripts import data_processor


@pytest.fixture(scope="module")
def city_list_location():
    return "tests/resources/cities/"


@pytest.fixture(scope="module")
def process_data(city_list_location):
    files = os.listdir(city_list_location)

    def _specify_type(file_name_or_type):
        for f in files:
            if file_name_or_type == f:
                if file_name_or_type.split('.')[1] != "json":
                    data = data_processor.csv_reader(city_list_location + f)
                else:
                    data = data_processor.json_reader(city_list_location + f)
        return data
    yield _specify_type


def test_csv_reader_header_fields(process_data):
    """
    Happy Path test to make sure the processed data
    contains the right header fields
    """
    data = process_data(file_name_or_type='clean_map.csv')
    header_fields = list(data[0].keys())
    assert header_fields == [
            'Country',
            'City',
            'State_Or_Province',
            'Lat',
            'Long',
            'Altitude'
            ]


def test_json_reader_file_keys(process_data):
    """
    Happy path test to make sure the processed data
    contains the right name keys

    Arguments:
        process_data {[function]} -- [Add file to be processed and return it's content]
    """
    data = process_data(file_name_or_type='scooter_data.json')
    for scooter in data:
        names_keys = list(scooter.keys())
        assert names_keys == ['id', 'name', 'vin_number',
                              'electric_scooter', 'color',
                              'city', 'usage', 'cost_usd',
                              'total_years_of_use']


def test_csv_reader_data_contents(process_data):
    """
    Happy Path Test to examine that each row
    had the appropriate data type per field
    """
    data = process_data(file_name_or_type='clean_map.csv')

    # Check row types
    for row in data:
        assert(isinstance(row['Country'], str))
        assert(isinstance(row['City'], str))
        assert(isinstance(row['State_Or_Province'], str))
        assert(isinstance(row['Lat'], float))
        assert(isinstance(row['Long'], float))
        assert(isinstance(row['Altitude'], float))

    # Basic data checks
    assert len(data) == 180  # We have collected 180 rows
    assert data[0]['Country'] == 'Andorra'
    assert data[106]['Country'] == 'Japan'


def test_json_reader_data_contents(process_data):
    """[Happy Path test to examine that each key
        had the appropriate data type per child]

    Arguments:
        process_data {[functions]} -- [Factory function
        which returns json file content]
    """
    json_data = process_data(file_name_or_type='scooter_data.json')
    for val in json_data:
        assert(isinstance(val['id'], int))
        assert(isinstance(val['name'], str))
        assert(isinstance(val['vin_number'], str))
        assert(isinstance(val['electric_scooter'], bool))
        assert(isinstance(val['city'], str))
        assert(isinstance(val['usage'], str))
        assert(isinstance(val['cost_usd'], float))
        assert(isinstance(val['total_years_of_use'], int))


def test_csv_reader_malformed_data_contents(process_data):
    """
    Sad Path Test
    """
    with pytest.raises(ValueError) as exp:
        process_data(file_name_or_type='malformed_map.csv')
    assert str(exp.value) == "could not convert string to float: 'not_an_altitude'"


def test_json_reader_malformed_data_contents(process_data):
    """
    [Sad Path Test]

    Arguments:
        process_data {[function]} -- [Factory function
        which returns json file content]
    """
    with pytest.raises(ValueError) as exp:
        process_data(file_name_or_type='malformed_scooter_data.json')
    assert str(exp.value) == "invalid literal for int() with base 10: 'tree'"
