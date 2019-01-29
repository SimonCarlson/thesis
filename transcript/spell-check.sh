#!/bin/bash
for filename in *.tex; do
    [ -e "$filename" ] || continue
    aspell -t -c $filename
done
rm *.tex.bak