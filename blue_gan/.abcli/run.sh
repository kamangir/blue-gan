#! /usr/bin/env bash

function blue_gan_run() {
    local options=$1
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)

    local algo=$2
    if [[ "+$BLUE_GAN_LIST_OF_ALGO+" != *"+$algo+"* ]]; then
        abcli_log_error "$algo: algo not found."
        return 1
    fi

    abcli_log "🪄"
}
