#!/bin/bash

# check that script is run as root
if [ "$EUID" -ne 0 ]
then
    echo "Please run as root"
    exit
fi


cp nginx/static.page /etc/nginx/site-enabled/
nginx -s reload

cp www/ var/www/static/
