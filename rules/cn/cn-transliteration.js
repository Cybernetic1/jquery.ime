( function ( $ ) {
	'use strict';

	var cn = {
		id: 'cn',
		name: 'YKY Chinese',
		description: 'YKY`s testing.',
		date: '2013-11-15',
		URL: 'http://github.com/wikimedia/jquery.ime',
		author: 'YKY',
		license: 'GPLv3',
		version: '1.0',
		patterns: [
			['cx', ':)'],
			['cyb', '半機器人一號'],
			['gx', '嘿嘿嘿'],
			['hx', '嘿']
		]
	};

	$.ime.register( cn );
}( jQuery ) );
