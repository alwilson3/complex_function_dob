from datetime import date, datetime
import pytest

def age_checker(date_of_birth):
    if not isinstance(date_of_birth, str):
        raise Exception("Date must be a string value")
    dob = date.fromisoformat(date_of_birth)
    today = datetime.now().date()
    age = today.year - dob.year
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1

    if age < 16:
        return f"Access denied, you are {age} and you must be 16."
    return "Access granted!"
