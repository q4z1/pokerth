#!/bin/sh

echo "Starting rsync"
rsync --delete -avze ssh bbcbot@149.202.223.116:/home/www/bbc/exp3/bbcbot/*.txt ./botfiles/
echo "Done."
