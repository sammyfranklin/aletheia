import os
import sys
import glob
import json
import time
import scipy
import numpy
import pandas
import pickle
import shutil
import random
import imageio
import tempfile
import subprocess
import tensorflow.compat.v1 as tf


import numpy as np

from PIL import Image
from scipy import misc
from matplotlib import pyplot as plt
from imageio import imread

from aletheialib import jpeg
from aletheialib import attacks, utils
from aletheialib import stegosim, feaext
from aletheialib.octave_interface import _attack
from aletheialib import models

MODEL_FILE = 'models/effnetb0-A-alaska2-steghide.h5'
DEV_ID = "CPU"
# global graph
# graph = tf.get_default_graph()

os.environ["CUDA_VISIBLE_DEVICES"] = DEV_ID
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

class Effnetb0():
    def __init__(self):
        self.model = models.NN("effnetb0")
        self.model.load_model(MODEL_FILE)

    def classify(self, files):
        # with graph.as_default():
        pred = self.model.predict(files, min(10, len(files)))
        return pred