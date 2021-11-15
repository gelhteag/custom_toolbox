from custom_toolbox.toolbox import unix_to_datetime

def test_output_unix_to_datetime():
    assert unix_to_datetime(1622505700) == '2021-06-01 12:01am'
