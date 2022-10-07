#!/usr/bin/env python3

import os
import urllib.request
from urllib.parse import urlparse

import pytest
import subprocess

from pprint import pprint

url="https://cpan.metacpan.org/authors/id/D/DO/DOUGW/Spreadsheet-ParseExcel-0.65.tar.gz"

res = urlparse(url)
path = res.path
filename = os.path.basename(path)

#if os.path.exists(filename) :
#  pass
#else :
#  urllib.request.urlretrieve(url, filename)

def test_run_shell():
	res = subprocess.call(['sh', '00_fetch.sh'])
	assert res == 0

def test_extract():
	res = subprocess.call(['sh', '01_extract.sh'])
	assert res == 0

def test_convert():
	res = subprocess.call(['sh', '02_convert.sh'])
	assert res == 0

#def test_clean():
#	res = subprocess.call(['sh', '09_clean.sh'])
#	assert res == 0


