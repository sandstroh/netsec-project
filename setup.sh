#!/bin/bash

# check that script is run as root
if [ "$EUID" -ne 0 ]
then
    echo "Please run as root"
    exit
fi


cp apache/netsec /etc/apache2/sites-enabled/netsec
/etc/init.d/apache2 reload


WEBSITE_DIRECTORY=/var/www/netsec/

if [ -d "$WEBSITE_DIRECTORY" ]
then
    rm -rf $WEBSITE_DIRECTORY
fi

mkdir -p $WEBSITE_DIRECTORY


cp -r www/css/ $WEBSITE_DIRECTORY/css
cp -r www/fonts/ $WEBSITE_DIRECTORY/fonts
cp -r www/images/ $WEBSITE_DIRECTORY/images
cp -r www/js $WEBSITE_DIRECTORY/js
cp www/netsec.html $WEBSITE_DIRECTORY/
chown -R www-data:www-data /var/www

cp www/index.cgi /usr/lib/cgi-bin/
chmod +x /usr/lib/cgi-bin/index.cgi

