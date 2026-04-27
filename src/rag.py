from typing import List, Tuple, Dict


def build_rag_context(
    user_query: str,
    recommendations: List[Tuple[Dict, float, str]]
) -> str:
    """
    Build a RAG context string using the user's query and retrieved songs.

    The AI generator should use this context to create grounded recommendations.
    """
    lines = []

    lines.append("User request:")
    lines.append(user_query)
    lines.append("")
    lines.append("Retrieved songs from the local catalog:")

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        lines.append(
            f"{rank}. Title: {song['title']}\n"
            f"   Artist: {song['artist']}\n"
            f"   Genre: {song['genre']}\n"
            f"   Mood: {song['mood']}\n"
            f"   Energy: {song['energy']}\n"
            f"   Tempo BPM: {song['tempo_bpm']}\n"
            f"   Acousticness: {song['acousticness']}\n"
            f"   Retrieval Score: {score:.2f}\n"
            f"   Retrieval Reasons: {explanation}"
        )

    lines.append("")
    lines.append(
        "Task: Recommend the best songs from the retrieved list. "
        "Only use songs listed in the retrieved context. "
        "Explain why each song fits the user's request."
    )

    return "\n".join(lines)