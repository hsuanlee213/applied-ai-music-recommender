def validate_user_query(query: str) -> tuple[bool, str]:
    """
    Validate the user's natural-language music request.

    Returns:
        (is_valid, message)
    """
    if query is None or query.strip() == "":
        return False, "Please enter a music preference, mood, genre, or listening activity."

    music_keywords = [
        # General music terms
        "music", "song", "songs", "playlist", "recommend", "recommendation",
        "track", "tracks", "artist", "album", "genre",

        # Listening activities
        "study", "studying", "workout", "exercise", "run", "running",
        "focus", "relax", "relaxing", "sleep", "party", "drive", "driving",

        # Genres
        "pop", "rock", "lofi", "lo-fi", "jazz", "ambient", "classical",
        "acoustic", "metal", "hip hop", "rap", "electronic",

        # Moods / vibes
        "chill", "calm", "happy", "sad", "moody", "intense", "peaceful",
        "romantic", "dark", "bright", "energetic", "upbeat",

        # Energy / tempo descriptions
        "fast", "slow", "high energy", "low energy", "energetic",
        "soft", "loud", "quiet", "tempo", "beat", "bpm"
    ]

    lowered = query.lower()

    if not any(keyword in lowered for keyword in music_keywords):
        return False, "This app is designed for music recommendations. Please enter a music-related request."

    return True, "Input is valid."