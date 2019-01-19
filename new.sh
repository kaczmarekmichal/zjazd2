#! /bin/bash


ip address |grep dynamic |awk {'print $2'} |cut -d/ -f1
