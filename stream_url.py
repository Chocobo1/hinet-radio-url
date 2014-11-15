#!/usr/bin/python2

import re
import sys
import urllib


def hinet_radio_stream_url( id ):
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
	if ( len( sys.argv ) < 2 ):
		print hinet_radio_stream_url( 228 )
	else:
		for i in sys.argv[1:]:
			print hinet_radio_stream_url( int( i ) )

