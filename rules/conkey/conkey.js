( function ( $ ) {
	'use strict';

	var conkey = {
		id: 'conkey',
		name: 'Concept keyboard',
		description: 'Use conceptual menus and pictures to type',
		date: '2013-12-07',
		URL: 'http://github.com/Cybernetic1/jquery.ime',
		author: 'YKY, Joseph Cheng',
		license: 'GPLv3',
		version: '1.0',
		// Conceptually organized menu
		conceptMenu: [
			['d','e',0,'的',4.094325318]
		],

		// Hide or show context menu
		showMenu: function() {
			var $elem = $('<div style="display:none;" class="popup-box"><img src=""/></div>');
			$('img', $elem).attr('src', 'http://placehold.it/640x480');
			$elem.appendTo('body').fadeIn();

			var	moveLeft = $(this).outerWidth(),
					moveDown = ($elem.outerHeight() / 2);
		},

		// This function is specially for Concept keyboard
		patterns: function( input, context ) {

			// *************** Local Functions ****************

			// ************ Main function begins here **************

			var i, replacement, rule, timer,
				conceptMenu = this.inputmethod.conceptMenu,
				unsorted = [], selections = [],
				k_n, dk, dn, d, score, // beta = 30.0,
				$menu, $li, $ul,
				$element = this.$element,
				$selector = $element.data('imeselector'),
				liHeight = 32,
				moveLeft = 0,
				moveDown = 0;

			// Todo:
			// 0. How to store the context menu? (Joseph)
			// 1. need to display menu even before any key is struck
			//		- Ctrl key toggles menu
			//		- when to hide menu?
			// 2. after a key is struck, display a sub-menu
			//		- do we keep the higher-level menus on display?
			// 3. after a number key is struck, do replacement

			// Find fuzzy match
			for ( i = 0; i < pinyinList.length; i++ ) {
				rule = pinyinList[i];

				// 2. calculate distance between consonants
				dk = distance_k( k_n[1], rule[0] );

				// 3. calculate distance between nuclei
				dn = distance_n( k_n[2], rule[1] );

				// 4. calculate overall distance
				d = 0.5 * dk + 0.5 * dn;

				// 5. calculate score
				// The number '19' in denominator can be tweaked.
				score = (1.0 - d) * (Math.log( rule[4] ) + 16) / 19;

				unsorted.push( [rule[3], rule[0] + rule[1], dk, dn, score.toFixed(5)] );

				//if (selections.length > 100)
				//	{ break; }
			}

			//return input;
			// console.log("Selections = " + selections);

			// Sort selections by score
			unsorted.sort( function(a, b) {
				return (b[4] - a[4]);
			} );

			// Get only the top 100 suggestions
			selections = unsorted.slice( 0, 100 );

			// the top of selections
			replacement = selections[0][0];

			// Create selection menu
			$menu = $( '.ime-autocomplete', $selector.$imeSetting );

			// Initialize selection menu
			if ( !$menu.length ) {
				$menu = $( '<div class="ime-autocomplete"></div>' );
				$ul = $( '<ul></ul>' );
				$ul.appendTo( $menu );
				$selector.$imeSetting.append( $menu );

			// Reuse the menu
			} else {
				$ul = $( 'ul', $menu );
				// Reset menu
				$menu.unbind( 'scroll' );
				$ul.empty();
				$('li', $ul).navigate( 'destroy' );
			}

			// Fill data into selection menu
			for ( i = 0; i < selections.length; i++ ) {
				$li = $( '<li><div class="word"></div></li>' );
				$li.appendTo( $ul )
					.data( 'replacement', selections[i][0] );

				// Insert matched word to menu
				$('.word', $li).html( selections[i][0] + '<em>' + selections[i][1] + '</em>');

				// Insert image to menu
				// TODO: fetch proper image to menu
				$li.hover(function() {
					var $elem = $('<div style="display:none;" class="popup-box"><img src=""/></div>');
					$('img', $elem).attr('src', 'http://placehold.it/640x480');
					$elem.appendTo('body').fadeIn();

					moveLeft = $(this).outerWidth();
					moveDown = ($elem.outerHeight() / 2);
				}, function() {
					$('.popup-box').remove();
				});

				$li.mousemove(function(e) {
					var target = '.popup-box',
						leftD = e.pageX + parseInt(moveLeft),
						maxRight = leftD + $(target).outerWidth(),
						windowLeft = $(window).width() - 40,
						windowRight = 0,
						maxLeft = e.pageX - (parseInt(moveLeft) + $(target).outerWidth() + 20);

					if (maxRight > windowLeft && maxLeft > windowRight) {
						leftD = maxLeft;
					}

					var topD = e.pageY - parseInt(moveDown),
						maxBottom = parseInt(e.pageY + parseInt(moveDown) + 20),
						windowBottom = parseInt(parseInt($(document).scrollTop()) + parseInt($(window).height())),
						maxTop = topD,
						windowTop = parseInt($(document).scrollTop());

					if(maxBottom > windowBottom) {
							topD = windowBottom - $(target).outerHeight() - 20;
					} else if(maxTop < windowTop) {
							topD = windowTop + 20;
					}

					$(target).css('top', topD).css('left', leftD);
				});
			}

			// Bind scroll event
			$menu.scroll( function(e) {
				var $this, scrollTop, newPos, index, $li;

				$this = $( this );
				// Clear all timer
				clearTimeout( timer );

				// Restrict scroll position must be align to the top li
				timer = setTimeout( function() {
					scrollTop = $this.scrollTop();
					newPos = index * liHeight;

					// Scroll to new position
					if((scrollTop % liHeight) > 0) {
						$this.stop().animate( {scrollTop: newPos}, 'fast' );
					}
				}, 100 );
			} );

			// Stop ime.selector timer to prevent ime menu hiding
			$selector.stopTimer();

			// Initialize jquery.navigate to make menu items keyboard-navigable
			$('ul li', $menu).not('.nokeyboard').navigate( {
				wrap: true
			} ).click( function() {
				var $input = $element,
					val = $input.val(),
					newReplacement = $(this).data('replacement'),
					pos = val.lastIndexOf(replacement);

				// Reset
				$('.popup-box').remove();
				$( 'li', $ul ).navigate( 'destroy' );
				$menu.remove();
				$input.val( val.substr(0, pos) + newReplacement ).focus();
			} );

			// Replace input string and return
			return input.replace( k_n[0], replacement );
		}

	};
	$.ime.register( conkey );
}( jQuery ) );

/*
 * jQuery.navigate - Allow any group of dom elements to be navigated with the keyboard arrows
 * Tom Moor, http://tommoor.com
 * Copyright (c) 2011 Tom Moor
 * MIT Licensed
 * @version 1.1
 */

(function($){
	'use strict';

	var handleKeyDown,
		handleMouseOver,
		navigate,
		options,
		$current,
		$collection,

	defaults = {
	mouse: true,
	activeClass: 'active',
	onSelect: function(){},
	onFocus: function(){},
	keys: {
		up: 38,
		down: 40,
		left: 37,
		right: 39,
		select: 13
		}
	},

	methods = {
		init : function(o){

		options = $.extend(defaults, o);
		$current = this.first().addClass(options.activeClass);
		$collection = this;

		handleKeyDown = function(e){

			if(!e){ var e = window.event; }

			switch(e.keyCode){
				case options.keys.up:
					navigate(0,-1);
					break;
				case options.keys.down:
					navigate(0,1);
					break;
				case options.keys.left:
					navigate(-1,0);
					break;
				case options.keys.right:
					navigate(1,0);
					break;
				case options.keys.select:
					$current.trigger('click');
					break;
			}

			e.preventDefault();

		};


		handleMouseOver = function() {
			$('.'+options.activeClass).removeClass(options.activeClass).trigger('blur');
			$current = $(this).addClass(options.activeClass).trigger('focus');
		};


		navigate = function(x, y) {

			var delta = x+y,
				$closest = $current,
				$difference = 0,
				a,b,d;

			$collection.each(function() {
				a = $(this);

			// ignore the current node
			if (a === $current) { return; }
			if (x !== 0) { d = parseInt(a.position().left - $current.position().left); }
			if (y !== 0) { d = parseInt(a.position().top - $current.position().top); }

			// node not in the right direction, drop out
			if (!(d > 0 && delta > 0) && !(d < 0 && delta < 0)) { return; }

			// distance calc would normally require sqrt but can be left out as we are only comparing.
			b = Math.pow($current.position().left-a.position().left,2)+Math.pow($current.position().top-a.position().top,2);

			// closest node so far?
			if(b < $difference || $difference === 0){
				$closest = a; $difference = b;
				}
			});

			// no more nodes in this direction
			if(options.wrap && $current === $closest) { return; }

			// trigger node as active
			$current.removeClass(options.activeClass);
			$current.trigger('blur');
			$closest.addClass(options.activeClass);
			$closest.trigger('focus');
			$current = $closest;
			options.onFocus.call($current);
		};


		// bind key and mouse events if required
		$(document).bind('keydown', handleKeyDown);
		$collection.bind('click', options.onSelect);
		if(options.mouse) { $collection.bind('mouseover', handleMouseOver); }

		return this;
	},
	destroy : function(){

		// if bound to a collection
		if($collection){

		// unbind all plugin event handlers
		$(document).unbind('keydown', handleKeyDown);
		$collection.unbind('mouseover', handleMouseOver);
		$collection.unbind('click', options.onSelect);
		$collection.removeClass(options.activeClass);

		// recover memory
		options = $current = $collection = null;
		}

		return this;
		}
	};


	$.fn.navigate = function( method ) {

	// Method calling logic
	if ( methods[method] ) {
		return methods[ method ].apply( this, Array.prototype.slice.call( arguments, 1 ));
		} else if ( typeof method === 'object' || ! method ) {
		return methods.init.apply( this, arguments );
		} else {
		$.error( 'Method ' +  method + ' does not exist on jQuery.navigate' );
		}

	};
} )( jQuery );
