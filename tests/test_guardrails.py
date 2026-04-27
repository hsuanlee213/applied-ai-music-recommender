from src.guardrails import validate_user_query


def test_empty_query_is_invalid():
    is_valid, message = validate_user_query("")
    assert is_valid is False
    assert "Please enter" in message


def test_non_music_query_is_invalid():
    is_valid, message = validate_user_query("How do I cook pasta?")
    assert is_valid is False
    assert "music recommendations" in message


def test_music_query_is_valid():
    is_valid, message = validate_user_query("I want chill music for studying")
    assert is_valid is True
    assert message == "Input is valid."