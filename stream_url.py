#!/bin/python2
"""
Copyright (C) 2014 Mike Tzou
This script is licensed under GPLv3 (http://www.gnu.org/licenses/gpl-3.0.html)
"""

import re , urllib , numbers

def hinet_radio_stream_url( id ):
	"""
	return radio stream url for `id`
	return empty string when error occurs

	arguments:
	id (integer) -- should be a valid radio ID
	"""

	# naive input checking
	if not isinstance( id , numbers.Integral ):
		return ""

	base_url = "http://hichannel.hinet.net/radio/mobile/index.do?id=" + str( id )
	base_url_data = urllib.urlopen( base_url ).read()

	url1 = re.search( "(?<=').+token1.+token2.+?(?=')" , base_url_data )
	if url1 == None:
		return ""
	url1 = url1.group()
	url1 = url1.replace( "\\" , "" )

	url2 = urllib.urlopen( url1 ).read()
	url2 = re.search( "^.+token1.+token2.+" , url2 , re.MULTILINE ).group()
	url2 = url2.replace( "-video=0" , "" )

	url3 = re.sub( "index.m3u8.*$" , "" , url1 ) + url2
	return url3


import sys
if __name__ == "__main__":
	id = sys.argv[1:]
	if not id:
		id = [228]

	for i in id:
		j = int( i )
		print ( "\nStation ID: %d\n\nStream URL: %s\n" ) % ( j , hinet_radio_stream_url( j ) )
