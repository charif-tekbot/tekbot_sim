#!/usr/bin/env bash

SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
mkdir -p ~/tekbot_ws/src
ln -s -t ~/tekbot_ws/src $SCRIPTPATH
cd ~/tekbot_ws

BIN_FOLDER=~/tekbot_ws/src/bin
if [ -d "$BIN_FOLDER" ]; then
    echo "Removing unnecessary bin folder: $BIN_FOLDER"
    rm -rf "$BIN_FOLDER"
fi

source /opt/ros/humble/setup.bash
colcon build
source ~/tekbot_ws/install/setup.bash
