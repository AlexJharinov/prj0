import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "n, expected_result",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(n: str, expected_result: str) -> None:
    assert mask_account_card(n) == expected_result


def test_get_date() -> None:
    assert get_date("2018-07-11T02:26:18.671407") == "11.07.2018"