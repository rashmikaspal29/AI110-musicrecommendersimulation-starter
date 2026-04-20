# Reflection: Profile Comparison Notes

## High-Energy Pop vs. Chill Lofi

These two profiles produce almost completely opposite top 5 lists. The pop/happy profile surfaces high-energy, bright songs like Sunrise City and Gym Hero, while the lofi/chill profile brings up slow, acoustic tracks like Library Rain and Midnight Coding. That makes total sense because genre and mood are the two strongest signals in the scoring, and here they point in completely different directions. What I found interesting is that a song like Rooftop Lights (indie pop, happy) shows up for the pop user but not the lofi user, even though its energy level of 0.76 is actually closer to what a lofi listener would want. Genre just wins.

## Chill Lofi vs. Deep Intense Rock

Both profiles want a very specific mood, chill vs. intense, but their energy targets are on opposite ends of the scale (0.38 vs. 0.92). The rock profile finds its top result immediately because there is exactly one rock/intense song in the catalog, Storm Runner, and it wins by a mile. The lofi profile at least has two lofi/chill songs to pick from. What this exposed is a catalog imbalance. Some genres only have one song representing them, so those users get a result that feels obvious and a little forced, not like a real discovery.

## Deep Intense Rock vs. Adversarial (high energy + sad)

This comparison was the most eye-opening. The rock profile gets Storm Runner at the top with a score of 4.46 and it feels completely right. The adversarial profile asked for blues/sad but with high energy (0.90). The system returned Delta Blues Waltz at the top, which has a low energy of 0.44. The genre match gave it +2.0 points and that completely drowned out the fact that the energy was way off. To any real listener, that recommendation would feel wrong. It showed that when two preferences conflict, the system cannot find a middle ground. It just goes with whichever signal carries the most weight.

## Why Does Gym Hero Keep Showing Up for Pop Users?

Gym Hero is a pop/intense song and it scores well for pop users even when they want a happy mood. It picks up the full +2.0 for genre and scores high on energy proximity, so it only misses the +1.0 mood bonus. That is still enough to land it in the top 3 most of the time. For someone who wants happy pop, Gym Hero as a second choice is not terrible, but for someone in a relaxed or chill mood, it would feel completely out of place. A smarter system would factor in context, like what time of day it is or what activity the user is doing, to catch situations like this.
