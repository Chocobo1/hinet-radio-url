#!/bin/python2
"""
Chocobo1 (Mike Tzou), 2015
"""

import re , urllib , itertools

def hinet_radio_station_id():
	"""
	return a dictionary{ (int) station_id : (utf8 string) "station_name" }
	"""

	base_url = "http://hichannel.hinet.net/radio/index.do"
	base_url_data = urllib.urlopen( base_url ).read()

	id_tmp = re.findall( "(?<=onclick=\"indexUtil.setRadioDetail\(').+?(?=')" , base_url_data )
	id = map( int , id_tmp[1:] )

	name_tmp = re.findall( '(?<=\t\t\t\t\t\t\t\t\t\t<p>).+?(?=<)' , base_url_data )
	name = map( lambda x: x.decode( 'utf-8' ) , name_tmp )

	return dict( itertools.izip_longest( id , name ) )


if __name__ == "__main__":
	id_list = hinet_radio_station_id()
	for i in sorted( id_list ):  # same as `sorted( id_list.keys() )`
		print "%d - %s" % ( i , id_list[ i ].encode( 'big5' ) )
