from datetime import date, timedelta
from lib.age_checker import age_checker
import pytest

"""
check that access is granted for someone
over age of 16 
"""
def test_over_age_sixteen_access_granted():
    result = age_checker("2009-01-01") # => "Access granted!"
    assert result == "Access granted!"

# under 16 
def test_under_age_sixteen_access_denied():
    result = age_checker("2015-01-01") # => "Access denied, you are (age) and you must be 16."
    assert result == "Access denied, you are 11 and you must be 16."

# one day less 
def test_one_day_under_sixteen():
    today = date.today()
    birthdate = date(today.year - 16, today.month, today.day) + timedelta(days = 1)
    result = age_checker(birthdate.isoformat())
    assert result == "Access denied, you are 15 and you must be 16."

# 16 today 
def test_sixteen_today():
    today = date.today()
    birthdate = date(today.year - 16, today.month, today.day)
    result = age_checker(birthdate.isoformat())
    assert result == "Access granted!"

# 1 day after 16
def test_date_is_not_string_throw_error():
    with pytest.raises(Exception) as e:
        age_checker(123345)
    assert str(e.value) == "Date must be a string value"
