from src.rag import build_rag_context


def test_build_rag_context_includes_user_query_and_retrieved_song():
    recommendations = [
        (
            {
                "title": "Quiet Morning",
                "artist": "Test Artist",
                "genre": "lofi",
                "mood": "chill",
                "energy": 0.3,
                "tempo_bpm": 80,
                "acousticness": 0.9,
            },
            4.2,
            "genre match, mood match, energy similarity",
        )
    ]

    context = build_rag_context(
        "I want calm music for studying",
        recommendations
    )

    assert "I want calm music for studying" in context
    assert "Quiet Morning" in context
    assert "Test Artist" in context
    assert "Retrieved songs from the local catalog" in context
    assert "Only use songs listed in the retrieved context" in context