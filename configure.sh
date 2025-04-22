#!/usr/bin/env bash

mkdir -p ~/tekbot_ws/src
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
ln -s -t ~/tekbot_ws/src $SCRIPTPATH

cd ~/tekbot_ws
source /opt/ros/humble/setup.bash
colcon build
source ~/tekbot_ws/install/setup.bash
