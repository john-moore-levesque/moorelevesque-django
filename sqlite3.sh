#!/bin/bash

PROJ=`pwd`
MANAGE=`find . -name "manage.py"`
cd /tmp/
wget https://www.sqlite.org/2022/sqlite-autoconf-3380200.tar.gz
tar -xzf sqlite-autoconf-3380200.tar.gz
cd sqlite-autoconf-3380200
./configure
make
sudo make install
export LD_LIBRARY_PATH="/usr/local/lib"
cd $PROJ
python $MANAGE migrate
