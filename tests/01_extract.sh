#!/usr/bin/env sh

set -e

. ./config.bashrc

for url in $urls ; do
  filename=$(basename $url)
  tar xzvf $filename
done



