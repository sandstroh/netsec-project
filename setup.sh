#!/bin/bash

# check that script is run as root
if [ "$EUID" -ne 0 ]
then
    echo "Please run as root"
    exit
fi
