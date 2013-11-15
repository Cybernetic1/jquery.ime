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
			['ĉx', 'cx'],
			['ĝx', 'gx'],
			['ĥx', 'hx'],
			['ĵx', 'jx'],
			['ŝx', 'sx'],
			['ŭx', 'ux'],
			['Ĉx', 'Cx'],
			['Ĝx', 'Gx'],
			['Ĥx', 'Hx'],
			['Ĵx', 'Jx'],
			['Ŝx', 'Sx'],
			['Ŭx', 'Ux'],
			['ĈX', 'CX'],
			['ĜX', 'GX'],
			['ĤX', 'HX'],
			['ĴX', 'JX'],
			['ŜX', 'SX'],
			['ŬX', 'UX'],
			['cx', ':)'],
			['gx', '嘿嘿嘿'],
			['hx', '嘿'],
			['jx', 'ĵ'],
			['sx', 'ŝ'],
			['ux', 'ŭ'],
			['Cx', 'Ĉ'],
			['Gx', 'Ĝ'],
			['Hx', 'Ĥ'],
			['Jx', 'Ĵ'],
			['Sx', 'Ŝ'],
			['Ux', 'Ŭ'],
			['CX', 'Ĉ'],
			['GX', 'Ĝ'],
			['HX', 'Ĥ'],
			['JX', 'Ĵ'],
			['SX', 'Ŝ'],
			['UX', 'Ŭ']]
	};

	$.ime.register( cn );
}( jQuery ) );
