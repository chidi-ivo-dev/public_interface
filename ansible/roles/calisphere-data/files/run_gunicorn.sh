#!/bin/sh
set -x

source /home/ec2-user/env.local

env | logger

env >&2

pushd /home/ec2-user/code/public_interface

/usr/local/bin/gunicorn -b 0.0.0.0:80 --pid /var/log/gunicorn/gunicorn.pid --error-logfile /var/log/gunicorn/error.log --access-logfile /var/log/gunicorn/access.log public_interface.wsgi &
