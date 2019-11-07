import os
import sys
import re
from pathlib import Path
from tqdm import tqdm

import numpy as np
import matplotlib.pyplot as plt

data_max = 500
fs = 1
bed_x = 32
bed_y = 64

def main():

    print("Generating heatmaps...\n")

    dataset_path = "a-pressure-map-dataset-for-in-bed-posture-classification-1.0.0"
    exp1_path = Path(f"data/{dataset_path}/experiment-i/")
    subject_paths, subject_names  = fetch_subjects(exp1_path)

    supine_positions = {
        "side": "supine",
        "positions": [1, 8, 9, 10, 11, 12, 15, 16, 17],
        "total": 0
    }
    right_positions  = {
        "side": "right",
        "positions": [2, 4, 5, 13],
        "total": 0
    }
    left_positions   = {
        "side": "left",
        "positions": [3, 6, 7, 14],
        "total": 0
    }

    print("Building supine heatmaps")
    iterate_subjects(subject_paths, subject_names, supine_positions)

    print("\nBuilding right heatmaps")
    iterate_subjects(subject_paths, subject_names, right_positions)

    print("\nBuilding left heatmaps")
    iterate_subjects(subject_paths, subject_names, left_positions)

def iterate_subjects(subject_paths, subject_names, position_dict):

    for subject_path, subject_name in zip(subject_paths, subject_names):
        for position in position_dict["positions"]:

            print(f"Getting heatmaps from subject {subject_name}, position {position}")

            input_path = subject_path/(str(position)+".txt")
            output_path = f"results/{position_dict['side']}/"

            if not os.path.exists(output_path):
                os.mkdir(output_path)

            build_heatmaps(input_path, output_path, position_dict)

            if position_dict["total"] > data_max:
                return

def build_heatmaps(input_path, output_path, position_dict):

    data_matrix = np.loadtxt(input_path)
    num_frames = data_matrix.shape[0]

    for f_ix in tqdm(range(num_frames)):
        target_frame = data_matrix[f_ix]
        heatmap = build_heatmap(target_frame)
        fname = f"{output_path}{position_dict['total']}.png"
        save_heatmap(heatmap, fname)
        position_dict["total"] += 1

def save_heatmap(heatmap, fname):

    #print(f"Saving {fname}")

    fig, ax = plt.subplots(figsize=(10,10))
    im = ax.imshow(heatmap, cmap='hot')
    ax.axis('off')
    plt.savefig(fname, bbox_inches = 'tight', pad_inches = 0)
    plt.close()

def build_heatmap(frame):

    frame_image = np.zeros((bed_y, bed_x))

    sensor_ix = 0
    for y in range(bed_y):
        for x in range(bed_x):
            frame_image[y,x] = frame[sensor_ix]
            sensor_ix += 1

    return frame_image

def fetch_subjects(exp1_path):

    subject_pattern = "S[0-9]+"
    subject_dirs  = [session_dir for session_dir in os.listdir(exp1_path)]

    subject_paths = []
    subject_names = []
    for subject in subject_dirs:
        match = re.findall(r"S\d+", subject)
        if match:
            subject_paths.append(exp1_path/match[0])
            subject_names.append(match[0])

    return subject_paths, subject_names

if __name__ == "__main__":
    main()
