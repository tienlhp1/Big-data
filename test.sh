#!/bin/sh
cd /home/tien/Big-data
git status
git add .
git commit -m "test add file"
git push
git config --global credential.helper store
