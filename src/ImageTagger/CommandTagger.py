import os
import sys

import ImageTagger.Predict as Predictor


def createTagFiles(path, threshold=0.35):
    if not os.path.isdir(path):
        print(f"The specified path is not a directory: {path}")
        sys.exit(1)

    predictor = Predictor.Predictor()
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
                file_path = os.path.join(root, file)
                tags = predictor.tag_image(file_path, threshold=threshold)
                # create tag file
                base = os.path.splitext(file_path)[0]
                with open(f"{base}.txt", "w", encoding="utf-8") as f:
                    f.write(tags)
    print("Done.")
