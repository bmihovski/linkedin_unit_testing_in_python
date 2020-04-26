import pytest
from scripts.user import User


@pytest.mark.parametrize("height,color,candy_reward",
                         [
                             (135, "red", "candy bar"),
                             (156, "blue", "candy stick"),
                             (186, "green", "hard candy"),
                         ])
def test_user_got_candy(height, color, candy_reward):
    test_user = User(height, color)
    assert test_user.color == color
    assert test_user.reward() == candy_reward
