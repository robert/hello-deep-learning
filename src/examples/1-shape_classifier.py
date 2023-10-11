from fastai.vision.all import *
from PIL import Image
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

import paths

if __name__ == "__main__":
    block = DataBlock(
        blocks=(ImageBlock, CategoryBlock), 
        get_items=get_image_files, 
        splitter=RandomSplitter(valid_pct=0.2, seed=42),
        get_y=parent_label,
        item_tfms=Resize(128)
    )
    dls = block.dataloaders(paths.IMAGES)

    # Finetune the resnet vision learner
    learn = vision_learner(dls, resnet18, metrics=error_rate)
    learn.fine_tune(1)

    # Try some example predictions. These images are in the training set so this is
    # a terrible way of actually assessing anything, but good enough here.
    test_path1 = os.path.join(paths.IMAGES, "circles", "circle_0.png")
    preds1 = learn.predict(test_path1)
    print(preds1)

    test_path2 = os.path.join(paths.IMAGES, "rectangles", "rectangle_0.png")
    preds2 = learn.predict(test_path2)
    print(preds2)

    # Show confusion matrix to check performance, which should be perfect
    interp = ClassificationInterpretation.from_learner(learn)
    interp.plot_confusion_matrix()
    plt.show()
