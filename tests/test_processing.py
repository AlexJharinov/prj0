import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def data_():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512365'},
                                           {'id': 939719570, 'state': 'EXECUTED',
                                            'date': '2018-06-30T02:08:58.425572'}]


@pytest.mark.parametrize(
    "data_, result",
            [
                (
                    [
                        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                    ],
                    [
                        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                    ],
                )
            ],
        )


def test_filter_by_state(data_, result):
    assert filter_by_state(data_) == result




@pytest.mark.parametrize(
    "data_, result",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        )
    ],
)


def test_sort_by_date(data_, result):
    assert sort_by_date(data_) == result
