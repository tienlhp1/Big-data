#!/bin/sh
git status
git add .
git commit -m "test add file $1"
git push
echo $1;


