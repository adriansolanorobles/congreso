// JavaScript Document



	$(window).on('load', function() {
	
		"use strict";
		
				
		/*----------------------------------------------------*/
		/*	Preloader
		/*----------------------------------------------------*/
		
		$(".loader").delay(100).fadeOut();
		$(".animationload").delay(100).fadeOut("fast");
				
		$(window).stellar({});
		
	});
	
	
	

	
	
		
	$(document).ready(function() {
		
		"use strict";

		
		/*----------------------------------------------------*/
		/*	Mobile Menu Toggle
		/*----------------------------------------------------*/
		
		$('.navbar-nav li a').on('click', function() {				
			$('#navigation-menu').css("height", "1px").removeClass("in").addClass("collapse");
			$('#navigation-menu').removeClass("open");				
		});	
		
		
		/*----------------------------------------------------*/
		/*	Countdown
		/*----------------------------------------------------*/
		
		$("#clock").countdown("2018/05/28 20:00:00", function(event) {
			$(this).html( event.strftime(''     
				+ '<div class="cbox-1 clearfix"><span class="cbox-1-digit">%D</span> <span class="cbox-1-txt">Días</span></div>'
				+ '<div class="cbox-1 clearfix"><span class="cbox-1-digit">%H</span> <span class="cbox-1-txt">Hrs</span></div>'
				+ '<div class="cbox-1 clearfix"><span class="cbox-1-digit">%M</span> <span class="cbox-1-txt">Min</span></div>'
				+ '<div class="cbox-1 clearfix"><span class="cbox-1-digit">%S</span> <span class="cbox-1-txt">Seg</span></div>'
			));
		});
		
		
		/*----------------------------------------------------*/
		/*	Animated Scroll To Anchor
		/*----------------------------------------------------*/
		
		$('.header a[href^="#"], .page-wrapper a.internal-link[href^="#"]').on('click', function (e) {
			
			e.preventDefault();

			var target = this.hash,
				$target = jQuery(target);

			$('html, body').stop().animate({
				'scrollTop': $target.offset().top - 60 // - 200px (nav-height)
			}, 'slow', 'easeInSine', function () {
				window.location.hash = '1' + target;
			});
			
		});
		
		
		/*----------------------------------------------------*/
		/*	ScrollUp
		/*----------------------------------------------------*/
		
		$.scrollUp = function (options) {

			// Defaults
			var defaults = {
				scrollName: 'scrollUp', // Element ID
				topDistance: 600, // Distance from top before showing element (px)
				topSpeed: 800, // Speed back to top (ms)
				animation: 'fade', // Fade, slide, none
				animationInSpeed: 200, // Animation in speed (ms)
				animationOutSpeed: 200, // Animation out speed (ms)
				scrollText: '', // Text for element
				scrollImg: false, // Set true to use image
				activeOverlay: false // Set CSS color to display scrollUp active point, e.g '#00FFFF'
			};

			var o = $.extend({}, defaults, options),
				scrollId = '#' + o.scrollName;

			// Create element
			$('<a/>', {
				id: o.scrollName,
				href: '#top',
				title: o.scrollText
			}).appendTo('body');
			
			// If not using an image display text
			if (!o.scrollImg) {
				$(scrollId).text(o.scrollText);
			}

			// Minium CSS to make the magic happen
			$(scrollId).css({'display':'none','position': 'fixed','z-index': '2147483647'});

			// Active point overlay
			if (o.activeOverlay) {
				$("body").append("<div id='"+ o.scrollName +"-active'></div>");
				$(scrollId+"-active").css({ 'position': 'absolute', 'top': o.topDistance+'px', 'width': '100%', 'border-top': '1px dotted '+o.activeOverlay, 'z-index': '2147483647' });
			}

			// Scroll function
			$(window).scroll(function(){	
				switch (o.animation) {
					case "fade":
						$( ($(window).scrollTop() > o.topDistance) ? $(scrollId).fadeIn(o.animationInSpeed) : $(scrollId).fadeOut(o.animationOutSpeed) );
						break;
					case "slide":
						$( ($(window).scrollTop() > o.topDistance) ? $(scrollId).slideDown(o.animationInSpeed) : $(scrollId).slideUp(o.animationOutSpeed) );
						break;
					default:
						$( ($(window).scrollTop() > o.topDistance) ? $(scrollId).show(0) : $(scrollId).hide(0) );
				}
			});

			// To the top
			$(scrollId).click( function(event) {
				$('html, body').animate({scrollTop:0}, o.topSpeed);
				event.preventDefault();
			});

		};
		
		$.scrollUp();
		
		
		/*----------------------------------------------------*/
		/*	Video Background
		/*----------------------------------------------------*/
		
		$('.video-play').vide("images/video/video", {
			posterType: "jpg"
		});
		
		
		/*----------------------------------------------------*/
		/*	Filterable Blog Posts
		/*----------------------------------------------------*/
	
		$("#blog-posts").mixitup({
			targetSelector: '.blog-article',
		});

				
		/*----------------------------------------------------*/
		/*	Single Image Lightbox
		/*----------------------------------------------------*/
				
		 $('.image-link').magnificPopup({
		  type: 'image'
		});
		
		
		/*----------------------------------------------------*/
		/*	Images Gallery Lightbox
		/*----------------------------------------------------*/
		
		$('.gallery-item').magnificPopup({
		  type: 'image',
		  gallery:{
			enabled:true
		  }
		});
		
		
		/*----------------------------------------------------*/
		/*	Video Link Lightbox
		/*----------------------------------------------------*/
		
		$('.video-popup').magnificPopup({
		    type: 'iframe',
		  	  
				iframe: {
					patterns: {
						youtube: {
			   
							index: 'youtube.com',
							src: 'https://www.youtube.com/embed/kuceVNBTJio'
				
								}
							}
						}		  		  
		});
		
		
		/*----------------------------------------------------*/
		/*	Testimonials Rotator
		/*----------------------------------------------------*/
		
		$('.flexslider').flexslider({
			animation: "fade",
			controlNav: true,
			directionNav: false,  
			slideshowSpeed: 6000,   
			animationSpeed: 2000,  
			start: function(slider){
				$('body').removeClass('loading');
			}
		});	
		
		
		/*----------------------------------------------------*/
		/*	Blog Articles Rotator
		/*----------------------------------------------------*/
	
		$("#blog-posts-holder").owlCarousel({
			
			autoPlay : true,
			slideSpeed : 800,
			items : 3,
			itemsDesktop : [1199,2],
			itemsDesktopSmall : [991,2],
			itemsTablet: [768,1],
			itemsMobile : [480,1],
			navigation: false,
			pagination: true,
			navigationText : false
					  
		});
		
		
		/*----------------------------------------------------*/
		/*	Register Form Validation
		/*----------------------------------------------------*/
		
		$("#register-form").validate({
			rules:{ 
					name:{
						required: true,
						minlength: 1,
						maxlength: 16,
					},
					email:{
						required: true,
						email: true,
					},
					ticket:{
						required: true,
						}
					},
					messages:{
							name:{
								required: "Please enter no more than (1) characters"
							}, 
							email:{
								required: "We need your email address to contact you",
								email: "Your email address must be in the format of name@domain.com"
							}, 
							ticket:{
								required: "This field is required"
							}, 
						}
		});	
		
		
		/*----------------------------------------------------*/
		/*	Comment Form Validation
		/*----------------------------------------------------*/
		
		$("#comment-form").validate({
			rules:{ 
					name:{
						required: true,
						minlength: 1,
						maxlength: 16,
					},
					email:{
						required: true,
						email: true,
					},
					subject:{
						required: true,
						minlength: 4,
						maxlength: 24,
					},		
					message:{
						required: true,
						minlength: 2,
						}
					},
					messages:{
							name:{
								required: "Please enter no more than (1) characters"
							}, 
							email:{
								required: "We need your email address to contact you",
								email: "Your email address must be in the format of name@domain.com"
							}, 
							message:{
								required: "Please enter no more than (2) characters"
							}, 
						}
		});	
		
				
		/*----------------------------------------------------*/
		/*	Newsletter Subscribe Form
		/*----------------------------------------------------*/
	
		$('.newsletter-form').ajaxChimp({
        language: 'cm',
        url: 'http://dsathemes.us3.list-manage.com/subscribe/post?u=af1a6c0b23340d7b339c085b4&id=344a494a6e'
            //http://xxx.xxx.list-manage.com/subscribe/post?u=xxx&id=xxx
		});


		$.ajaxChimp.translations.cm = {
			'submit': 'Submitting...',
			0: 'We have sent you a confirmation email',
			1: 'Please enter a value',
			2: 'An email address must contain a single @',
			3: 'The domain portion of the email address is invalid (the portion after the @: )',
			4: 'The username portion of the email address is invalid (the portion before the @: )',
			5: 'This email address looks fake or invalid. Please enter a real email address'
		};
		
				
	});	

	
	