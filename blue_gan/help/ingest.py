from typing import List

from blue_options.terminal import show_usage, xtra

from blue_gan import env
from blue_gan.ingest.animals10 import translate


def help_ingest(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("~cache,", mono=mono),
            "dataset=<dataset>",
            xtra(",dryrun,", mono=mono),
            "upload",
        ]
    )

    return show_usage(
        [
            "@gan",
            "ingest",
            f"[{options}]",
            "[-|<object-name>]",
            "<ingest-options>",
        ],
        "browse blue_plugin.",
        {
            "dataset: {}".format(", ".join(env.BLUE_GAN_LIST_OF_DATASETS)): [],
            "ingest-options": [
                "animal={},count=<-1>".format(
                    " | ".join(sorted(translate.values())),
                ),
            ],
        },
        mono=mono,
    )
