"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


PROFILES = {
    "High-Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.85, "valence": 0.80},
    "Chill Lofi":      {"genre": "lofi", "mood": "chill", "energy": 0.38, "valence": 0.58},
    "Deep Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.92, "valence": 0.45},
    "Adversarial (high energy + sad mood)": {"genre": "blues", "mood": "sad", "energy": 0.90, "valence": 0.30},
}

def print_recommendations(label: str, recommendations: list) -> None:
    print("\n" + "="*50)
    print(f"  Profile: {label}")
    print("="*50)
    for i, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n#{i}  {song['title']} by {song['artist']}")
        print(f"    Score : {score:.2f} / 4.50")
        print(f"    Why   : {explanation}")

def main() -> None:
    songs = load_songs("data/songs.csv")

    for label, user_prefs in PROFILES.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)
        print_recommendations(label, recommendations)


if __name__ == "__main__":
    main()
