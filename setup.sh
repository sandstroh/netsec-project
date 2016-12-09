#!/bin/bash

# check that script is run as root
if [ "$EUID" -ne 0 ]
then
    echo "Please run as root"
    exit
fi


echo "Apache configuration..."
cp apache/netsec /etc/apache2/sites-enabled/netsec
/etc/init.d/apache2 reload


echo "Static web page..."
WEBSITE_DIRECTORY=/var/www/netsec

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


echo "Snort configuration..."
cp snort/local.rules /etc/snort/rules/
cp snort/snort.conf /etc/snort/
chown root:root /etc/snort/snort.conf
/etc/init.d/snort restart


echo "Copying network security exam..."
COURSE_DIRECTORY=/home/netsec/course

if [ -d "$COURSE_DIRECTORY" ]
then
    rm -rf $COURSE_DIRECTORY
fi

mkdir -p $COURSE_DIRECTORY
chmod 770 $COURSE_DIRECTORY

cp exam.pdf $COURSE_DIRECTORY/exam.pdf
chmod 660 $COURSE_DIRECTORY/exam.pdf


#echo "Restore passwd script..."
#gcc -o restore-passwd restore-passwd.c
#mv restore-passwd /opt/
#chmod +s /opt/restore-passwd

echo "Finished!"

