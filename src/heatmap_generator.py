import os
import sys
import re
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

def main():

    print("Generating heatmaps...")

    exp1_path = Path("data/experiment-i/")
    subject_paths = build_subject_paths(exp1_path)

    position_num = 17

    for subject_path in subject_paths:
        for position in range(1,position_num+1):
            position_data_path = subject_path/(str(position)+".txt")

            build_heatmaps(position_data_path)

def build_heatmaps(data_path):



def build_subject_paths(exp1_path):

    subject_pattern = "S[0-9]+"
    subject_dirs  = [session_dir for session_dir in os.listdir(exp1_path)]

    subject_paths = []
    for subject in subject_dirs:
        match = re.findall(r"S\d+", subject)
        if match:
            subject_paths.append(exp1_path/match[0])

    return subject_paths

if __name__ == "__main__":
    main()
