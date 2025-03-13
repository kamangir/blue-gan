#! /usr/bin/env bash

function blue_gan_stylegan2_pytorch() {
    local options=$1
    local do_dryrun=$(abcli_option_int "$options" dryrun 0)
    local do_upload=$(abcli_option_int "$options" upload $(abcli_not $do_dryrun))

    local object_name=$(abcli_clarify_object $2 stylegan2_pytorch-$(abcli_string_timestamp_short))
    local object_path=$ABCLI_OBJECT_ROOT/$object_name

    abcli_eval dryrun=$do_dryrun \
        stylegan2_pytorch \
        --data $object_path/data \
        --name $object_name \
        --results_dir $object_path \
        --models_dir $object_path/models \
        "${@:3}"

    [[ $? -ne 0 ]] && return 1

    [[ "$do_upload" == 1 ]] &&
        abcli_upload - $object_name
}
