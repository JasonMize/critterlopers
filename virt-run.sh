#!/bin/sh

. ./critterenv/bin/activate

export SECRET_KEY="crittersaretehbestest"

pip install -r ./requirements/local.txt

./manage.py migrate
./manage.py runserver 8087