#!/usr/bin/env sh

set -e

. ./config.bashrc


for url in $urls; do
  filename=$(basename $url)

  if [ ! -e "$filename" ]; then
    wget $url
  else
    exit 0
  fi
done

