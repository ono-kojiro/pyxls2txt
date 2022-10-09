#!/usr/bin/env python3

import os
import sys
import re

import getopt

import json
import xmltodict

from datetime import datetime
import dateutil.parser

from pprint import pprint

def usage():
	print("Usage : {0} [-o output.jsonl] [input.xml]".format(sys.argv[0]))

def xml2jsonl(fp, filepath) :
	count = 1
	fp_in = open(filepath, mode='r', encoding='utf-8')
	data = xmltodict.parse(fp_in.read())


	timestamp = data['testsuites']['testsuite']['@timestamp']
	dt = dateutil.parser.parse(timestamp)

	pprint(dt)
	
	index_str = 'mydata-{0:04d}.{1:02d}.{2:02d}'.format(dt.year, dt.month, dt.day)

	index = {
		"index" : {
			"_index" : index_str,
		}
	}

	for testcase in data['testsuites']['testsuite']['testcase'] :
		fp.write(
			json.dumps(
				index,
				ensure_ascii=False,
			)
		)
		fp.write('\n')
		
		fp.write(
			json.dumps(
				testcase,
				ensure_ascii=False,
			)
		)
		fp.write('\n')

		count += 1

	#fp.write(
	#	json.dumps(
	#		data,
	#		indent=4,
	#		ensure_ascii=False
	#	)
	#)

	fp_in.close()

def main():
	ret = 0

	try:
		opts, args = getopt.getopt(
			sys.argv[1:], "hvo:", ["help", "version", "output="])
	except getopt.GetoptError as err:
		print(str(err))
		sys.exit(2)
	
	output = None
	
	for o, a in opts:
		if o == "-v":
			usage()
			sys.exit(0)
		elif o in ("-h", "--help"):
			usage()
			sys.exit(0)
		elif o in ("-o", "--output"):
			output = a
		else:
			assert False, "unknown option"
	
	if ret != 0:
		sys.exit(1)

	if len(args) == 0 :
		usage()
		sys.exit(1)
	
	if output is not None :
		fp = open(output, mode='w', encoding='utf-8')
	else :
		fp = sys.stdout

	for filepath in args:
		xml2jsonl(fp, filepath)
	
	if output is not None :
		fp.close()
	
if __name__ == "__main__":
	main()
