from fastai.vision.all import *
from fastai.vision.widgets import *
from fastcore.all import *
import pathlib

from app import config

temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath #TODO: replace for linux


class FlowerClassifier:

    def __init__(self, pkl_path) -> None:
        super().__init__()
        self.learner = load_learner(pkl_path)

    def predict(self, image_path):
        (res, _, _) = self.learner.predict(config.IMG_HOLDER_PATH / image_path)
        return res


classifier = FlowerClassifier(config.ML_MODEL_PATH)
print(classifier.predict('IMG-20191209-WA0001.jpg'))
