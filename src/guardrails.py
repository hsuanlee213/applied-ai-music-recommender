def validate_user_query(query: str) -> tuple[bool, str]:
    """
    Validate the user's natural-language music request.

    Returns:
        (is_valid, message)
    """
    if query is None or query.strip() == "":
        return False, "Please enter a music preference, mood, genre, or listening activity."

    music_keywords = [
        "music", "song", "songs", "playlist", "recommend", "genre",
        "mood", "energy", "study", "workout", "chill", "focus",
        "relax", "happy", "sad", "pop", "rock", "lofi", "jazz",
        "ambient", "acoustic", "intense"
    ]

    lowered = query.lower()

    if not any(keyword in lowered for keyword in music_keywords):
        return False, "This app is designed for music recommendations. Please enter a music-related request."

    return True, "Input is valid."