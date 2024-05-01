import pytest

from dagster_mathias.assets import check_num_bibs_available


@pytest.mark.parametrize(
    "input,expected",
    [
        (
            {
                "data": {
                    "event": {
                        "registrations_for_sale_count": 0,
                    }
                }
            },
            0,
        ),
        (
            {
                "data": {
                    "event": {
                        "registrations_for_sale_count": 5,
                    }
                }
            },
            5,
        ),
        (
            {
                "not_data": {
                    "not_event": {
                        "registrations_for_sale_count": 5,
                    }
                }
            },
            pytest.raises(KeyError),
        ),
    ],
)
def test_amsterdam_bibs_available(input, expected):
    if isinstance(expected, int):
        # Use the expected context manager to check for exceptions
        assert check_num_bibs_available(input) == expected
    else:
        # Use the expected context manager to check for exceptions
        with expected:
            check_num_bibs_available(input)
