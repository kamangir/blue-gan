from typing import List

from blue_options.terminal import show_usage, xtra

from blue_gan import env


def help_ingest(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("~cache,", mono=mono),
            "dataset=<dataset>",
            xtra(",dryrun,~upload", mono=mono),
        ]
    )

    return show_usage(
        [
            "@gan",
            "ingest",
            f"[{options}]",
            "[-|<object-name>]",
        ],
        "browse blue_plugin.",
        {"dataset: {}".format(", ".join(env.BLUE_GAN_LIST_OF_DATASETS)): []},
        mono=mono,
    )
