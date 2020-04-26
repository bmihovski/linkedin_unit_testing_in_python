from datetime import datetime
import pytest
from scripts.fitness_log import FitnessLog


@pytest.fixture(scope='function')
def create_tracker():
    fitness_tracker = FitnessLog()

    start_time = datetime(year=2017, month=1, day=1, hour=5, minute=12)
    end_time = datetime(year=2017, month=1, day=1, hour=5, minute=55)
    # breakpoint()
    fitness_tracker.log_activity("run", start_time, end_time)

    yield fitness_tracker


def test_add_valid_activities(create_tracker):
    fitness_tracker = create_tracker
    # breakpoint()
    activities = fitness_tracker.get_activities()

    assert len(activities) == 1
    assert activities[0][0] == 'run'


@pytest.fixture(scope='session')
def create_overlapping_times():
    overlapping_start_time = datetime(year=2017, month=1, day=1, hour=5, minute=14)
    overlapping_end_time = datetime(year=2017, month=1, day=1, hour=5, minute=53)

    return overlapping_start_time, overlapping_end_time


@pytest.fixture(scope='session')
def create_non_overlapping_times():
    non_overlapping_start_time = datetime(year=2020, month=4, day=1, hour=6, minute=10)
    non_overlapping_stop_time = datetime(year=2020, month=4, day=1, hour=6, minute=14)
    return non_overlapping_start_time, non_overlapping_stop_time


def test_add_invalid_activity(create_tracker, create_overlapping_times):
    fitness_tracker = create_tracker
    overlapping_start_time, overlapping_end_time = create_overlapping_times

    with pytest.raises(Exception) as exp:
        fitness_tracker.log_activity("run", overlapping_start_time, overlapping_end_time)

    assert str(exp.value) == ('A new activity must not conflict with a logged activity. ' +
                              'Please delete the old activity before proceeding')
"""
 TO DO: Add a new test.
 You can run the following to expose which test functions
 and paths are covered:

 pytest --cov scripts
"""


def test_delete_activity(create_tracker):  # change function name here
    fitness_tracker = create_tracker
    activities = fitness_tracker.get_activities()
    fitness_tracker.delete_activity(*activities[0])
    assert len(activities) == 0


def test_validate_valid_entry(create_tracker):
    fitness_tracker = create_tracker
    _, start_time, end_time = fitness_tracker.get_activities()[0]
    assert fitness_tracker.validate_entry(start_time, end_time)


def test_validate_invalid_entry(create_tracker):
    fitness_tracker = create_tracker
    _, end_time, start_time = fitness_tracker.get_activities()[0]
    assert not fitness_tracker.validate_entry(start_time, end_time)


def test_when_no_activity_no_overlapping_entry(create_tracker):
    fitness_tracker = create_tracker
    activities = fitness_tracker.get_activities()
    _, start_time, end_time = activities[0]
    fitness_tracker.delete_activity(*activities[0])
    assert not fitness_tracker.overlapping_entry(start_time, end_time)


def test_when_new_activity_no_overlapping_then_true(create_tracker, create_non_overlapping_times):
    fitness_tracker = create_tracker
    assert not fitness_tracker.overlapping_entry(*create_non_overlapping_times)


def test_when_data_never_added_to_log_then_error(create_tracker, create_non_overlapping_times):
    fitness_tracker = create_tracker
    with pytest.raises(Exception) as exp:
        fitness_tracker.delete_activity("climb", *create_non_overlapping_times)
    assert str(exp.value) == "You can't delete non existing activity"
