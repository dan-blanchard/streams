#!/bin/bash
ssh cogtree@ue1a-web1a.cogtree.com mkdir -p /data/vhosts/www.parsely.com/misc/slides/pystorm2015
rsync -Pavz --exclude=.git ./_build/slides/ cogtree@ue1a-web1a.cogtree.com:/data/vhosts/www.parsely.com/misc/slides/pystorm2015
rsync -Pavz --exclude=.git ./_build/html/ cogtree@ue1a-web1a.cogtree.com:/data/vhosts/www.parsely.com/misc/slides/pystorm2015/notes/
