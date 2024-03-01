import os
import shutil
from sklearn.model_selection import train_test_split

# Path to your fashion datasetC:\\Use
dataset_path = 'path'#path to your dataset

# Create empty directories for the training and testing sets
train_dir = 'path'#path of train directory
test_dir = 'path'#path to your test directory

os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Iterate through your dataset and split it into training and testing sets
categories = os.listdir(dataset_path)

for category in categories:
    category_path = os.path.join(dataset_path, category)
    images = os.listdir(category_path)

    # Split the images into training and testing sets
    train_images, test_images = train_test_split(images, test_size=0.2, random_state=42)

    # Move training images to the training set directory
    for image in train_images:
        src_path = os.path.join(category_path, image)
        dest_path = os.path.join(train_dir, category, image)
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        shutil.copy(src_path, dest_path)

    # Move testing images to the testing set directory
    for image in test_images:
        src_path = os.path.join(category_path, image)
        dest_path = os.path.join(test_dir, category, image)
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        shutil.copy(src_path, dest_path)

print("Dataset split into training and testing sets.")
