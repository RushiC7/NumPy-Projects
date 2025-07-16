# 🧠 1. Student Score Analyzer
# Skills: Array slicing, stats, conditions
# What to build:
# Input names and scores of students (use NumPy arrays).
# Calculate highest, lowest, average scores.
# Find students who scored above average.
# Sort by scores.

import numpy as np
dic={
    "Rushi": 100, 
    "Rex": 99,
    "Tony": 72,
    "Fiza": 89
}
score=np.array(list(dic.values()))
names=np.array(list(dic.keys()))
HighScore=score.max()
print(f"Highest Score: {HighScore}")

LowScore=score.min()
print(f"Lowest Score: {LowScore}")

MeanScore=score.mean()
print(f"Mean Score: {MeanScore}")

above_avg=score>=MeanScore
print(above_avg)
print("Toppers: ")
for name, score in zip(names[above_avg], score[above_avg]):
    print(f"{name}: {score}")


