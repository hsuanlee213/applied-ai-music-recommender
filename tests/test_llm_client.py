from src.llm_client import generate_ai_recommendation


def test_generate_ai_recommendation_uses_retrieved_song():
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
            "genre match, mood match",
        )
    ]

    response = generate_ai_recommendation(
        user_query="I want calm music",
        recommendations=recommendations,
        rag_context="mock context"
    )

    assert "Quiet Morning" in response
    assert "Test Artist" in response
    assert "grounded" in response.lower()


def test_generate_ai_recommendation_handles_no_results():
    response = generate_ai_recommendation(
        user_query="I want something unusual",
        recommendations=[],
        rag_context=""
    )

    assert "could not find" in response.lower()