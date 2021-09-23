import os
import tarfile

# Data:
# Download from kaggle: https://www.kaggle.com/dschettler8845/brats-2021-task1
# Extract into the parent directory of this file (as in one step out from this directory), leave name as "archive"

# References:
# Reading data: https://www.kaggle.com/dschettler8845/load-task-1-dataset-comparison-w-task-2-dataset/notebook

# Notes:
# participants can exclude the cases during training: [00109, 00123, 00709].

# Create Data Directory (will be created one parent file up from this file's home)

def load_data():
    if not os.path.isdir("../project_data"):
        os.makedirs("../project_data", exist_ok=True)

    # Extract Update
    print("\n... Extracting BraTSID=00495 Task1 Update Files ...")
    tar = tarfile.open("../archive/BraTS2021_00495.tar")
    tar.extractall("../project_data")
    tar.close()

    # Extract Update
    print("... Extracting BraTSID=00621 Task1 Update Files ...")
    tar = tarfile.open("../archive/BraTS2021_00621.tar")
    tar.extractall("../project_data")
    tar.close()

    # Extract Main Training Data
    print("... Extracting Main Task1 Training Files (3-5 Minutes) ...\n")
    tar = tarfile.open("../archive/BraTS2021_Training_Data.tar")
    tar.extractall("../project_data")
    tar.close()