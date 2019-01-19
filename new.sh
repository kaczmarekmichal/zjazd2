#! /bin/bash


ip address |grep  inet | grep 10 |awk '{print  $2}'|cut -d/ -f1
