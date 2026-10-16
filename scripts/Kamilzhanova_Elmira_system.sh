#!/bin/bash

echo "=============================="
echo "Student Information"
echo "=============================="
echo "Name: Elmira"
echo "Surname: Kamilzhanova"
echo "Group: IT2-2304"
echo "Student ID: 37713"
echo "Course: DevOps"

echo "=============================="
echo "System Information"
echo "=============================="
echo "Username:"
whoami
echo "Hostname:"
hostname
echo "Current Date:"
date
echo "Operating System:"
uname -a
echo "Disk Usage:"
df -h /
echo "Memory Usage:"
free -h

if [ -f Kamilzhanova_Elmira_info.txt ]; then
    echo "Student information file exists."
else
    echo "Student information file does not exist."
fi
