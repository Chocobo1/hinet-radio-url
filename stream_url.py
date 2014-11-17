#!/bin/python2
# Copyright (C) 2014 Mike Tzou
# This script is licensed under GPLv3 (http://www.gnu.org/licenses/gpl-3.0.html)

import re
import sys
import urllib
import numbers

# input `id` is an integer
# return empty string when error occurs
def hinet_radio_stream_url( id ):

	# naive input checking
	if not isinstance( id , numbers.Integral ):
		return ""

	base_url= "http://hichannel.hinet.net/radio/mobile/index.do?id=" + str( id )
	base_url_data = urllib.urlopen( base_url ).read()

	url1 = re.search( "http.+token1.+token2.+?(?=')" , base_url_data )
	if url1 == None:
		return ""
	url1 = url1.group()
	url1 = re.sub( r"\\" , "" , url1 )

	url2 = urllib.urlopen( url1 ).read()
	url2 = re.search( ".+token1.+token2.+" , url2 ).group()
	url2 = re.sub( "-video=0" , "" , url2 )

	return re.sub( "index.m3u8.*$" , "" , url1 ) + url2


if __name__ == "__main__":
	id = sys.argv[1:]
	if not id:
		id = [228]

	for i in id:
		j = int( i )
		print ( "\nStation ID: %d\n\nStream URL: %s\n" ) % ( j , hinet_radio_stream_url( j ) )
