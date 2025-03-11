import os

from blue_objects import file, README

from blue_gan import NAME, VERSION, ICON, REPO_NAME


items = README.Items(
    [
        {
            "name": "PyTorch-GAN",
            "marquee": "https://github.com/eriklindernoren/PyTorch-GAN/raw/master/assets/logo.png",
            "description": "Code base.",
            "url": "https://github.com/eriklindernoren/PyTorch-GAN",
        }
    ]
)


def build():
    return README.build(
        items=items,
        path=os.path.join(file.path(__file__), ".."),
        ICON=ICON,
        NAME=NAME,
        VERSION=VERSION,
        REPO_NAME=REPO_NAME,
    )
