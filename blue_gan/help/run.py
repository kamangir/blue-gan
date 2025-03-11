from typing import List

from blue_options.terminal import show_usage, xtra
from abcli.help.generic import help_functions as generic_help_functions

from blue_gan import ALIAS

list_of_examples = [
    "bicyclegan",
]


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
            "<implementation>",
        ],
        "run <implementation>.",
        {
            "implementation(s): {}".format(", ".join(list_of_examples)): [],
        },
        mono=mono,
    )
