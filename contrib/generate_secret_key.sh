#!/bin/bash
which pwgen
if [ $? -ne 0 ]; then
    echo "Install pwgen! On Debian/Ubuntu: apt-get install pwgen"
else
    pwgen 51 -1 -s -y
fi
