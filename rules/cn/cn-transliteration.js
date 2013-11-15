/**
 * An input method for the Cyrillic alphabet with palochka, which is used by many languages in the
 * North Caucasus region. Most keyboard layouts don't support this letter, so people frequently type
 * other similarly looking characters instead, but this causes various problems, for example when
 * automatically converting from uppercase to lowercase and vice-versa.
 *
 * This layout assumes that the standard Russian keyboard layout is used. All the rules produce the
 * same character palochka, and the characters used are the same that are often used by the speakers
 * of these languages online: 1. Latin small 'l'. 2. Latin capital 'I'. 3. Ukrainian capital 'І'. 4.
 * Alt-1 (the digit one). 5. Alt-д (Cyrillic small 'de', on the same key as Latin 'l'). 6. Alt-ш
 * (Cyrillic small 'sha', on the same key as Latin 'i'). 7. Alt-Ш (Cyrillic capital 'sha', on the
 * same key as Latin 'I').
 */

( function ( $ ) {
	'use strict';
	// All the characters are very similar in appearance,
	// so it's better to give them names to avoid confusion.
	var cnTransliteration;

	cnTransliteration = {
		id: 'cn-transliteration',
		name: '中文',
		description: 'input method for Chinese',
		date: '2013-11-15',
		URL: 'http://github.com/Cybernetic1/jquery.ime',
		author: 'YKY',
		license: 'GPLv3',
		version: '1.0',
		patterns: [
			[ 'hh', '嘿' ],
			[ 'І', 'J' ] ]
	};

	$.ime.register( cnTransliteration );

}( jQuery ) );
