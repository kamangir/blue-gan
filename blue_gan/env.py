import os
from blue_options.env import load_config, load_env, get_env

load_env(__name__)
load_config(__name__)


PYTORCH_GAN_LIST_OF_ALGO = str(get_env("PYTORCH_GAN_LIST_OF_ALGO")).split("+")

BLUE_GAN_LIST_OF_DATASETS = str(get_env("BLUE_GAN_LIST_OF_DATASETS")).split("+")
