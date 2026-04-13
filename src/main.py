"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f"Loaded songs: {len(songs)}")

    # Specific taste profile for comparisons
    user_prefs = {
        "favorite_genre": "pop",
        "favorite_mood": "happy", 
        "target_energy": 0.8,
        "likes_acoustic": False
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "="*80)
    print("TOP RECOMMENDATIONS FOR YOU")
    print("="*80 + "\n")
    
    for i, rec in enumerate(recommendations, 1):
        song, score, explanation = rec
        print(f"{i}. {song['title']}")
        print(f"   Artist: {song['artist']} | Genre: {song['genre']}")
        print(f"   Score: {score:.2f}/3.5")
        print(f"   Why: {explanation}")
        print()


if __name__ == "__main__":
    main()
