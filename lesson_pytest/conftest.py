import pytest
import random

@pytest.fixture
def age():
    r_age = random.randint(0, 100)
    print(f"Random age is {r_age}")
    return r_age
