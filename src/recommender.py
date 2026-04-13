from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        """Initialize the recommender with a list of songs."""
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top k song recommendations for the given user profile."""
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Return a human-readable explanation of why a song was recommended."""
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    import csv
    
    songs = []
    print(f"Loading songs from {csv_path}...")
    
    with open(csv_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            song = {
                'id': int(row['id']),
                'title': row['title'],
                'artist': row['artist'],
                'genre': row['genre'],
                'mood': row['mood'],
                'energy': float(row['energy']),
                'tempo_bpm': int(row['tempo_bpm']),
                'valence': float(row['valence']),
                'danceability': float(row['danceability']),
                'acousticness': float(row['acousticness'])
            }
            songs.append(song)
    
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons = []
    
    # Genre match: +2.0 points
    if song['genre'] == user_prefs['favorite_genre']:
        score += 2.0
        reasons.append(f"Matches your favorite genre: {song['genre']}")
    
    # Mood match: +1.0 point
    if song['mood'] == user_prefs['favorite_mood']:
        score += 1.0
        reasons.append(f"Matches your favorite mood: {song['mood']}")
    
    # Energy similarity: +(1 - |song.energy - target|) × 1.0
    energy_similarity = 1 - abs(song['energy'] - user_prefs['target_energy'])
    score += energy_similarity
    reasons.append(f"Energy similarity: {energy_similarity:.2f} (target: {user_prefs['target_energy']}, song: {song['energy']})")
    
    # Acoustic preference: +0.5 × (acousticness or 1-acousticness)
    if user_prefs['likes_acoustic']:
        acoustic_score = song['acousticness'] * 0.5
        reasons.append(f"Acoustic preference: {acoustic_score:.2f} (song is {song['acousticness']:.2f} acoustic)")
    else:
        acoustic_score = (1 - song['acousticness']) * 0.5
        reasons.append(f"Non-acoustic preference: {acoustic_score:.2f} (song is {song['acousticness']:.2f} acoustic)")
    score += acoustic_score
    
    return (score, reasons)

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    # Score all songs
    scored_songs = [
        (song, *score_song(user_prefs, song))
        for song in songs
    ]
    
    # Sort by score (second element) in descending order
    ranked = sorted(scored_songs, key=lambda x: x[1], reverse=True)
    
    # Convert reasons list to string and return top k
    return [
        (song, score, " | ".join(reasons))
        for song, score, reasons in ranked[:k]
    ]
