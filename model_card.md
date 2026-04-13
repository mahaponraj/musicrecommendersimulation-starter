# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  
VibeMatcher 1.0  

---

## 2. Intended Use  

Suggests 5 songs from a small catalog based on user's favorite genre, mood, energy level, and acoustic preference. For classroom learning about recommenders. Not for real music apps or commercial use.  

---

## 3. How the Model Works  

Scores songs by matching genre (+1 point), mood (+1 point), energy closeness (×2 weight), and acoustic preference. Sorts by total score.

---

## 4. Data  

Uses 17 songs with features like genre, mood, energy, valence, danceability, acousticness. Limited to these songs only, no lyrics or artist history.  

---

## 5. Strengths  

Works well for users with clear preferences. Captures energy and acoustic taste patterns. Matches intuition for pop and lofi fans.  

---

## 6. Limitations and Bias 

Favors high-energy songs because energy is weighted heavily. May ignore mood if energy matches better. Dataset has more pop songs.

---

## 7. Evaluation  

Tested with 7 user profiles including standard types and edge cases. Ran experiments changing weights. Compared outputs between profiles.

---

## 8. Future Work  

Add more songs and genres. Include tempo and valence as user preferences. Show diverse recommendations instead of just top scores.  

---

## 9. Personal Reflection  

Building this showed me how simple rules can create smart recommendations. I was surprised that energy closeness often beat perfect genre matches. This makes me think real music apps must balance many factors carefully.  
