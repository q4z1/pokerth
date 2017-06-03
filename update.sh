#!/bin/sh

echo "Starting rsync"
rsync --delete -avze ssh bbcbot@pth:/home/www/bbc/exp3/bbcbot/*.txt ./botfiles/
echo "Done."
