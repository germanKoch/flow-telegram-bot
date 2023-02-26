from fastai.vision.all import *
from fastai.vision.widgets import *
from fastcore.all import *


class FlowerClassifier:

    def __init__(self, pkl_path) -> None:
        super().__init__()
        self.learner = load_learner(pkl_path)

    def predict(self, image_path):
        (res, _, _) = self.learner.predict(image_path)
        return res


classifier = FlowerClassifier('./../../resource/export.pkl')
print(classifier.predict('D:\\projectsHome\\flow-bot\\resource\\files\\IMG-20191209-WA0001.jpg'))
