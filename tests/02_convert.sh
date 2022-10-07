#!/bin/sh

set -e

. ./config.bashrc

for url in $urls ; do
  basename=$(basename $url .tar.gz)
  find $basename -name "*.xls" -o -name "*.xlsx" | \
	grep -v encrypted | \
	grep -v protected | \
    grep -v 2_____with_chart | \
	xargs ../xls2txt.py {} \;
done


