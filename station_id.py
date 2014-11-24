#!/bin/python2
"""
Copyright (C) 2014 Mike Tzou
This script is licensed under GPLv3 (http://www.gnu.org/licenses/gpl-3.0.html)
"""

import re , urllib , itertools

def hinet_radio_station_id():
	"""
	return a dictionary{ (int) station_id : (utf8 string) "station_name" }
	"""

	base_url = "http://hichannel.hinet.net/radio/mobile/index.do"
	base_url_data = urllib.urlopen( base_url ).read()

	id_tmp = re.findall( "(?<=\?id=).+?(?=')" , base_url_data )
	id = map( int , id_tmp )

	name = re.findall( '(?<=stationName">).+?(?=<)' , base_url_data )

	return dict( itertools.izip( id , name ) )


if __name__ == "__main__":
	id_list = hinet_radio_station_id()
	for i in sorted( id_list ):  # same as `sorted( id_list.keys() )`
		print "%d - %s" % ( i , id_list[ i ].decode( 'utf-8' ).encode( 'big5' ) )