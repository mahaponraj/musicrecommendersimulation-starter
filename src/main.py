"""
Command line runner for the Music Recommender Simulation.

Runs the recommender across multiple user profiles — three standard taste
profiles and four adversarial/edge-case profiles designed to stress-test
the scoring logic.
"""

from recommender import load_songs, recommend_songs


# ─────────────────────────────────────────────────────────────────────────────
# STANDARD USER PROFILES
# Each profile represents a coherent listener archetype.
# ─────────────────────────────────────────────────────────────────────────────

HIGH_ENERGY_POP = {
    "name": "High-Energy Pop",
    "favorite_genre": "pop",
    "favorite_mood": "happy",
    "target_energy": 0.9,
    "likes_acoustic": False,
}

CHILL_LOFI = {
    "name": "Chill Lofi",
    "favorite_genre": "lofi",
    "favorite_mood": "chill",
    "target_energy": 0.35,
    "likes_acoustic": True,
}

DEEP_INTENSE_ROCK = {
    "name": "Deep Intense Rock",
    "favorite_genre": "rock",
    "favorite_mood": "intense",
    "target_energy": 0.9,
    "likes_acoustic": False,
}


# ─────────────────────────────────────────────────────────────────────────────
# ADVERSARIAL / EDGE-CASE USER PROFILES
# These profiles contain internal contradictions or extreme values meant to
# reveal whether the scoring logic handles tension gracefully or breaks down.
# ─────────────────────────────────────────────────────────────────────────────

# Conflict: high energy (0.9) paired with melancholic mood.
# High-energy songs are rarely melancholic; the scorer will reward energy but
# never award the mood bonus, so results will be energetic-but-wrong-vibe songs.
HIGH_ENERGY_MELANCHOLIC = {
    "name": "Adversarial – High Energy + Melancholic Mood",
    "favorite_genre": "blues",
    "favorite_mood": "melancholic",
    "target_energy": 0.9,
    "likes_acoustic": False,
}

# Conflict: genre=classical but target_energy=0.98.
# Classical songs in the dataset have energy ~0.25, so the energy component
# will always penalise the only genre-match song. Can genre alone beat
# better-energy songs from other genres?
CLASSICAL_RAGER = {
    "name": "Adversarial – Classical Rager (genre vs energy war)",
    "favorite_genre": "classical",
    "favorite_mood": "calm",
    "target_energy": 0.98,
    "likes_acoustic": False,
}

# Conflict: lofi fan who dislikes acoustic.
# Lofi tracks in the dataset are highly acoustic (0.71–0.86). The genre/mood
# bonus competes directly with the acoustic penalty for the very same songs.
NON_ACOUSTIC_LOFI = {
    "name": "Adversarial – Non-Acoustic Lofi Fan",
    "favorite_genre": "lofi",
    "favorite_mood": "chill",
    "target_energy": 0.35,
    "likes_acoustic": False,
}

# Conflict: every dimension points in a different direction.
# folk / energetic mood / near-zero energy / non-acoustic.
# Folk songs are slow and acoustic; "energetic" mood doesn't exist for folk in
# the dataset. This profile should produce a chaotic mix of top results.
THE_CONTRADICTION = {
    "name": "Adversarial – The Contradiction (folk + energetic + low energy)",
    "favorite_genre": "folk",
    "favorite_mood": "energetic",
    "target_energy": 0.05,
    "likes_acoustic": False,
}


# ─────────────────────────────────────────────────────────────────────────────
# RUNNER
# ─────────────────────────────────────────────────────────────────────────────

ALL_PROFILES = [
    HIGH_ENERGY_POP,
    CHILL_LOFI,
    DEEP_INTENSE_ROCK,
    HIGH_ENERGY_MELANCHOLIC,
    CLASSICAL_RAGER,
    NON_ACOUSTIC_LOFI,
    THE_CONTRADICTION,
]


def run_profile(user_prefs: dict, songs: list) -> None:
    """Print top-5 recommendations for a single user profile."""
    name = user_prefs.pop("name")          # pull display name out before scoring
    print("\n" + "=" * 80)
    print(f"PROFILE: {name}")
    print(
        f"  genre={user_prefs['favorite_genre']} | "
        f"mood={user_prefs['favorite_mood']} | "
        f"energy={user_prefs['target_energy']} | "
        f"acoustic={user_prefs['likes_acoustic']}"
    )
    print("=" * 80)

    recommendations = recommend_songs(user_prefs, songs, k=5)

    for i, rec in enumerate(recommendations, 1):
        song, score, explanation = rec
        print(f"\n  {i}. {song['title']}  —  {song['artist']}")
        print(f"     Genre: {song['genre']} | Mood: {song['mood']} | Energy: {song['energy']}")
        print(f"     Score: {score:.2f}  |  {explanation}")

    user_prefs["name"] = name              # restore so profile dict stays intact


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded {len(songs)} songs.\n")

    for profile in ALL_PROFILES:
        run_profile(profile, songs)

    print("\n" + "=" * 80)
    print("All profiles evaluated.")


if __name__ == "__main__":
    main()
