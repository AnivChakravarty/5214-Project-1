import os
import tarfile

# Data:
# Download from kaggle: https://www.kaggle.com/dschettler8845/brats-2021-task1
# Extract into the parent directory of 5214-Project-1, leave name as "archive"

# Notes:
# participants can exclude the cases during training: [00109, 00123, 00709].

# Create Data Directory (will be created two parent folders up from this file's home)


def load_data():
    if not os.path.isdir("../../../project_data"):
        os.makedirs("../../../project_data", exist_ok=True)

    path = os.path.abspath("../../archive")
    for f in os.listdir(path):
        extract_file(os.path.join(path, f))


def extract_file(f):
    tar = tarfile.open(f)
    tar.extractall("../../project_data")
    tar.close()
