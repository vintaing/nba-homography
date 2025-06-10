import numpy as np

court_points = np.array([
    [0, 0],
    [470, 0],
    [470, 500],
    [0, 500],
    [235, 250]
], dtype=np.float32)

np.save("nba_court_points.npy", court_points)
print("Saved court keypoints successfully.")