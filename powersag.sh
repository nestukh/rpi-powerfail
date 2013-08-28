#!/bin/sh

#send myself a text that power sag has occurred
pypy /root/sendpsag.py &

#log power sag
echo Raspberry Pi: Sag occured on `date` >> /var/log/powerfail.log
