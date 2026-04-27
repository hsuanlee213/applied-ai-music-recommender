"""
Command line runner for the Applied AI Music Recommender.

This version extends the original rule-based recommender into a simple
RAG-based flow:

User query
→ guardrails
→ retrieve songs from local catalog
→ build RAG context
→ generate AI-style recommendation response
"""

from src.recommender import load_songs, recommend_songs
from src.guardrails import validate_user_query
from src.rag import build_rag_context
from src.llm_client import generate_ai_recommendation
from src.logger_config import setup_logger


def query_to_user_prefs(query: str) -> dict:
    """
    Convert a natural-language user query into simple user preferences.

    This is a lightweight parser for the project demo.
    A more advanced version could use an LLM or NLP model to extract preferences.
    """
    lowered = query.lower()

    genre = "pop"
    mood = "happy"
    energy = 0.5
    likes_acoustic = False

    if "lofi" in lowered:
        genre = "lofi"
    elif "rock" in lowered:
        genre = "rock"
    elif "jazz" in lowered:
        genre = "jazz"
    elif "ambient" in lowered:
        genre = "ambient"
    elif "pop" in lowered:
        genre = "pop"

    if "chill" in lowered or "relax" in lowered or "calm" in lowered:
        mood = "chill"
        energy = 0.3
    elif "focus" in lowered or "study" in lowered:
        mood = "focused"
        energy = 0.4
    elif "happy" in lowered or "upbeat" in lowered:
        mood = "happy"
        energy = 0.8
    elif "intense" in lowered or "workout" in lowered:
        mood = "intense"
        energy = 0.9
    elif "moody" in lowered:
        mood = "moody"
        energy = 0.7

    if "acoustic" in lowered:
        likes_acoustic = True

    return {
        "genre": genre,
        "mood": mood,
        "energy": energy,
        "likes_acoustic": likes_acoustic
    }


def run_rag_demo() -> None:
    logger = setup_logger()
    songs = load_songs("data/songs.csv")

    print("\n🎵 Applied AI Music Recommender")
    print("=" * 70)
    print("Describe what kind of music you want.")
    print("Example: I want calm acoustic music for studying.")
    print("Type 'q', 'quit', or 'exit' to stop.")
    print("=" * 70)

    while True:
        user_query = input("\nYour request: ").strip()

        if user_query.lower() in ["q", "quit", "exit"]:
            logger.info("User exited the application.")
            print("\nThanks for using Applied AI Music Recommender. Goodbye! 🎵")
            break

        logger.info("User query received: %s", user_query)

        is_valid, validation_message = validate_user_query(user_query)

        if not is_valid:
            logger.warning("Invalid user query: %s", validation_message)
            print(f"\n{validation_message}")
            continue

        user_prefs = query_to_user_prefs(user_query)
        logger.info("Parsed user preferences: %s", user_prefs)

        recommendations = recommend_songs(user_prefs, songs, k=5)
        logger.info("Retrieved %d songs", len(recommendations))

        rag_context = build_rag_context(user_query, recommendations)
        logger.info("Built RAG context")

        ai_response = generate_ai_recommendation(
            user_query=user_query,
            recommendations=recommendations,
            rag_context=rag_context
        )
        logger.info("Generated AI recommendation response")

        print("\n" + "=" * 70)
        print("🤖 AI-GENERATED RECOMMENDATIONS")
        print("=" * 70)
        print(ai_response)
        print("=" * 70)


if __name__ == "__main__":
    run_rag_demo()