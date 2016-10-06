#!/bin/sh

TARGET_DIR='/Applications/Ableton Live 9.7 Beta.app/Contents/App-Resources/MIDI Remote Scripts/Maschine_Jam_Evo'

cd `dirname $0`

if [ -d "$TARGET_DIR" ]; then
    rm -rf "$TARGET_DIR"
fi
mkdir "$TARGET_DIR"
cp ./src/*.py "$TARGET_DIR"
ls -al "$TARGET_DIR"
