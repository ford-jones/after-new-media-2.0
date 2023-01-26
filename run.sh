#!/usr/bin/env bash

set -a
source config.env
set +a


    echo "Press [CTRL+C] to stop.."
while :
do
    python3 youtubeApiConsume.py
done