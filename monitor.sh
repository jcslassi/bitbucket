#!/bin/bash

URL=$1

if [ $# -eq 0 ]
    then
        echo "usage: ./monitor.sh www.domain.tld"
        exit 1
fi

if [ ! -f /tmp/music.mp3 ]; then
    echo "getting sndfx..."
    curl -s http://www.trekcore.com/audio/background/voy_astrometrics.mp3 > /tmp/bg_snd.mp3
    curl -s http://www.trekcore.com/audio/computer/consolewarning.mp3 > /tmp/music.mp3
    echo "initiating scan..."
    afplay /tmp/bg_snd.mp3 &
fi

echo "scanning..."
for (( ; ; )); do
    mv /tmp/new.html /tmp/old.html 2> /dev/null
    curl $URL -L --compressed -s > /tmp/new.html
    DIFF_OUTPUT="$(diff -I '.*Running for.*' /tmp/new.html /tmp/old.html)"
    if [ "0" != "${#DIFF_OUTPUT}" ]; then
        sleep 3
        echo ${DIFF_OUTPUT}
        afplay /tmp/music.mp3
    fi
done
