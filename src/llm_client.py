from typing import List, Tuple, Dict


def generate_ai_recommendation(
    user_query: str,
    recommendations: List[Tuple[Dict, float, str]],
    rag_context: str
) -> str:
    """
    Generate an AI-style recommendation response.

    This mock version does not call an external API yet.
    It simulates the LLM response while staying grounded in retrieved songs.
    """
    if not recommendations:
        return (
            "I could not find strong matches in the local music catalog. "
            "Try using a different mood, genre, or activity."
        )

    response_lines = []
    response_lines.append(f"Based on your request: \"{user_query}\"")
    response_lines.append("")
    response_lines.append("Here are my grounded recommendations from the local catalog:")
    response_lines.append("")

    for rank, (song, score, explanation) in enumerate(recommendations[:3], start=1):
        response_lines.append(f"{rank}. {song['title']} by {song['artist']}")
        response_lines.append(
            f"   This song is a good match because it has a "
            f"{song['mood']} mood, belongs to the {song['genre']} genre, "
            f"and has an energy level of {song['energy']:.2f}. "
            f"The retriever selected it because: {explanation}."
        )
        response_lines.append("")

    response_lines.append(
        "These recommendations are grounded in the retrieved songs from the local dataset."
    )

    return "\n".join(response_lines)