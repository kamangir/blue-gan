from abcli.tests.test_env import test_abcli_env
from blue_objects.tests.test_env import test_blue_objects_env


from blue_gan import env


def test_required_env():
    test_abcli_env()
    test_blue_objects_env()


def test_blue_gan_env():
    assert env.PYTORCH_GAN_LIST_OF_ALGO
    assert env.BLUE_GAN_LIST_OF_DATASETS
