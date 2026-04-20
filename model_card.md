# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeFinder 1.0**

---

## 2. Goal / Task

The goal is simple: given a user's taste preferences, find the songs in the catalog that match best and explain why. It is not trying to predict the future or learn from feedback. It just looks at what you like and finds the closest matches in the list. Think of it like a friend who knows your music taste and flips through a playlist for you.

---

## 3. Data Used

The catalog has 18 songs stored in data/songs.csv. Each song has a genre label, a mood label, and several numeric features scored between 0 and 1, including energy (how intense it feels), valence (how happy or dark it sounds), danceability, and acousticness. The dataset started with 10 songs and was expanded to cover a wider range of genres like hip-hop, classical, metal, reggae, blues, and folk. That said, it is still a tiny catalog, and genres like K-pop, Afrobeats, or Latin music are not represented at all, which means the system basically cannot serve those listeners well.

---

## 4. Algorithm Summary

The recommender scores each song by comparing it to what the user wants. A genre match is worth the most points (+2.0) because genre is usually the strongest indicator of taste. A mood match adds +1.0. Then for energy and valence, instead of rewarding more or less, the system rewards closeness. The nearer the song's energy is to what the user wants, the higher it scores. All songs get a score, then they get sorted from highest to lowest, and the top 5 are shown with a short explanation of why they ranked where they did.

---

## 5. Observed Behavior / Biases

The biggest pattern I noticed is that genre almost always wins. Since it is worth +2.0 and nothing else comes close, two songs with the same genre will almost always beat a song that perfectly matches everything else except genre. This creates a kind of filter bubble. If you like pop, you mostly get pop, even if an indie folk song would have made you feel exactly the same way.

The adversarial profile (high energy + sad mood) really showed this flaw. It asked for blues/sad but with high energy. The system returned a low-energy blues song at the top because it matched the genre, completely ignoring that the energy was way off. When preferences conflict, the system does not know how to balance them. It just picks the heaviest weight and goes with it.

---

## 6. Evaluation Process

Four user profiles were tested:

**High-Energy Pop** got Sunrise City at the top with a score of 4.46 out of 4.50. That felt right.

**Chill Lofi** surfaced both lofi/chill songs in the catalog near the top. Also made sense.

**Deep Intense Rock** only had one rock/intense song to find (Storm Runner), so it won easily. A bit too predictable.

**Adversarial (blues/sad + high energy)** returned a low-energy blues song. That felt wrong because the energy did not match at all, but the genre did.

A weight shift experiment was also set up. By halving the genre weight and doubling the energy weight, cross-genre songs with matching energy would bubble up higher. This makes the results feel more musically diverse.

---

## 7. Intended Use and Non-Intended Use

**Designed for:** Learning how content-based filtering works. This is a classroom simulation and it is great for understanding the mechanics of scoring and ranking.

**Not designed for:** Real music discovery. The catalog is too small, there is no learning from user behavior, no popularity signals, and no way to pick up on context like whether you are at the gym or trying to sleep. Using this in a real app would lead to repetitive, narrow recommendations very quickly.

---

## 8. Ideas for Improvement

**Genre clusters instead of exact matching.** Right now pop and indie pop are treated as completely different. Grouping related genres would make the scoring feel more natural.

**Tempo proximity scoring.** Adding tempo_bpm to the score would help separate a slow sad song from a fast sad song, which currently score the same.

**Diversity penalty.** If the top 5 are all the same genre, penalize the lower-ranked duplicates slightly to encourage variety in the results.

---

## 9. Personal Reflection

The biggest learning moment for me was realizing how much a single weight can control the entire output. I assumed the system would balance all the features together, but genre at +2.0 dominated almost every result. It made me understand why real platforms spend so much time tuning weights. A small change really does change what people see.

AI tools helped a lot with generating the song data, structuring the scoring logic, and catching edge cases I had not thought about, like the adversarial profile. But I always had to double-check the logic myself, especially when the output looked reasonable but for the wrong reasons, like the adversarial result that matched genre but completely missed energy. The AI produced working code, but only I could tell whether the results actually made sense as music recommendations.

What surprised me most was how simple the algorithm is, yet the results genuinely feel like recommendations. Scoring by genre, mood, and energy proximity and then sorting the list, that is really it. No neural network, no listening history, no complex math. And yet for a pop/happy user, it returns exactly what you would expect. It made me realize that a lot of what feels smart in a real app might just be well-tuned simple rules under the hood.

If I kept developing this, I would want to add a second layer asking what the user is doing right now, so the same person gets different recommendations for working vs. relaxing. That context gap is the thing that feels most missing from this version.
