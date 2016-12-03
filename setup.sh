#!/bin/bash

# check that script is run as root
if [ "$EUID" -ne 0 ]
then
    echo "Please run as root"
    exit
fi


cp nginx/static.page /etc/nginx/site-enabled/
nginx -s reload

WEBSITE_DIRECTORY=/var/www/netsec/

if [ -d "$WEBSITE_DIRECTORY" ]
then
    rm -rf $WEBSITE_DIRECTORY
fi

cp -r www/css/ $WEBSITE_DIRECTORY/css
cp -r www/fonts/ $WEBSITE_DIRECTORY/fonts
cp -r www/images/ $WEBSITE_DIRECTORY/images
cp -r www/js $WEBSITE_DIRECTORY/js
cp www/netsec.html $WEBSITE_DIRECTORY/netsec.html
chown -R www-data:www-data /var/www

cp www/index.cgi /usr/lib/cgi-bin/index.cgi
chmod +x /usr/lib/cgi-bin/index.cgi

