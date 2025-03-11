from typing import List

from blue_options.terminal import show_usage, xtra
from abcli.help.generic import help_functions as generic_help_functions

from blue_gan import env


def help_run(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "dryrun"

    return show_usage(
        [
            "@gan",
            "run",
            f"[{options}]",
            "<algo>",
        ],
        "run <algo>.",
        {
            "algo: {}".format(", ".join(env.BLUE_GAN_LIST_OF_ALGO)): [],
        },
        mono=mono,
    )
