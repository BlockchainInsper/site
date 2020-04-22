/* =================================
------------------------------------
	Labs - Design Studio
	Version: 1.0
 ------------------------------------ 
 ====================================*/

'use strict';

/*------------------
	Preloder
--------------------*/
function loader() {
	$(window).on('load', function () {
		$(".loader").fadeOut();
		$("#preloder").delay(400).fadeOut("slow");
	});
}

fetch('https://api.rss2json.com/v1/api.json?rss_url=https://medium.com/feed/@binsper')
   .then((res) => res.json())
   .then((data) => {
      // Filter for acctual posts. Comments don't have categories, therefore can filter for items with categories bigger than 0
      const res = data.items //This is an array with the content. No feed, no info about author etc..
      const posts = res.filter(item => item.categories.length > 0) // That's the main trick* !

      // Functions to create a short text out of whole blog's content
      function toText(node) {
         let tag = document.createElement('div')
         tag.innerHTML = node
         node = tag.innerText
         return node
      }
      function shortenText(text,startingPoint ,maxLength) {
         return text.length > maxLength?
         text.slice(startingPoint, maxLength):
         text
      }

      // Put things in right spots of markup
	  let output = '';
	  var i = 0;
	  posts.every(function(element, index) {
		i++;
		output += `
		<li class="blog__post">
		<a href="${element.link}">
			<img src="${element.thumbnail}" class="blog__topImg"></img>
			<div class="blog__content">
				<div class="blog_preview">
					<h2 class="blog__title">${shortenText(element.title, 0, 30)+ '...'}</h2>
					<p class="blog__intro">${'...' + shortenText(toText(element.content),60, 300)+ '...'}</p>
				</div>
				<hr>
				<div class="blog__info">
					<span class="blog__author">${element.author}</span>
					<span class="blog__date">${shortenText(element.pubDate,0 ,10)}</span>
				</div>
			</div>
		<a/>
		</li>`
		if (i > 3) return false
		else return true
	  })
	//   for(item in posts) {
	// 	i++;

	// 	if (i > 3) {
	// 		break
	// 	}
	//   }

    //   posts.forEach((item) => {
	// 	i++;

	// 	if (i > 3) {
	// 		return;
	// 	}
    //   })
      document.querySelector('.blog__slider').innerHTML = output
})




/*------------------
	Navigation
--------------------*/
function responsive() {
	// Responsive 
	$('.responsive').on('click', function (event) {
		$('.menu-list').slideToggle(400);
		event.preventDefault();
	});
}



/*------------------
	Hero Section
--------------------*/
function heroSection() {
	//Slide item bg image.
	$('.hero-item').each(function () {
		var image = $(this).data('bg');
		$(this).css({
			'background-image': 'url(' + image + ')',
			'background-size': 'cover',
			'background-repeat': 'no-repeat',
			'background-position': 'center bottom'
		});
	});
	//slider auto height 
	var iit = setInterval(slide_item, 1);

	function slide_item() {
		var bh = $('body').height();
		$('.hero-item').height(bh);
	}
	slide_item();

	var time = 7;
	var $progressBar,
		$bar,
		$elem,
		isPause,
		tick,
		percentTime;

	// Init the carousel
	$('#hero-slider').owlCarousel({
		loop: true,
		nav: true,
		items: 1,
		autoHeight: true,
		animateOut: 'fadeOut',
		animateIn: 'fadeIn',
		navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
		onInitialized: progressBar,
		onTranslated: moved,
		onDrag: pauseOnDragging
	});

	// Init progressBar where elem is $("#owl-demo")
	function progressBar() {
		// build progress bar elements
		buildProgressBar();

		// start counting
		start();
	}

	// create div#progressBar and div#bar then prepend to $("#owl-demo")
	function buildProgressBar() {
		$progressBar = $("<div>", {
			id: "progressBar"
		});
		$bar = $("<div>", {
			id: "bar"
		});
		$progressBar.append($bar).prependTo($("#hero-slider"));
	}

	function start() {
		// reset timer
		percentTime = 0;
		isPause = false;
		// run interval every 0.01 second
		tick = setInterval(interval, 10);
	};

	function interval() {
		if (isPause === false) {
			percentTime += 1 / time;

			$bar.css({
				width: percentTime + "%"
			});

			// if percentTime is equal or greater than 100
			if (percentTime >= 100) {
				// slide to next item 
				$("#hero-slider").trigger("next.owl.carousel");
				percentTime = 0; // give the carousel at least the animation time ;)
			}
		}
	}

	// pause while dragging 
	function pauseOnDragging() {
		isPause = true;
	}

	// moved callback
	function moved() {
		// clear interval
		clearTimeout(tick);
		// start again
		start();
	}

}



/*------------------
	Video Popup
--------------------*/
function videoPopup() {
	$('.video-popup').magnificPopup({
		type: 'iframe',
		autoplay: true
	});
}



/*------------------
	Testimonial
--------------------*/
function testimonial() {
	// testimonial Carousel 
	$('#testimonial-slide').owlCarousel({
		loop: true,
		autoplay: true,
		margin: 30,
		nav: false,
		dots: true,
		responsive: {
			0: {
				items: 1
			},
			600: {
				items: 2
			},
			800: {
				items: 2
			},
			1000: {
				items: 2
			}
		}
	});
}



/*------------------
	Progress bar
--------------------*/
function progressbar() {

	$('.progress-bar-style').each(function () {
		var progress = $(this).data("progress");
		var prog_width = progress + '%';
		if (progress <= 100) {
			$(this).append('<div class="bar-inner" style="width:' + prog_width + '"><span>' + prog_width + '</span></div>');
		}
		else {
			$(this).append('<div class="bar-inner" style="width:100%"><span>' + prog_width + '</span></div>');
		}
	});
}



/*------------------
	Accordions
--------------------*/
function accordions() {
	$('.panel').on('click', function (e) {
		$('.panel').removeClass('active');
		var $this = $(this);
		if (!$this.hasClass('active')) {
			$this.addClass('active');
		}
		e.preventDefault();
	});
}



/*------------------
	Progress Circle
--------------------*/
function progressCircle() {
	//Set progress circle 1
	$("#progress1").circleProgress({
		value: 0.75,
		size: 175,
		thickness: 5,
		fill: "#2be6ab",
		emptyFill: "rgba(0, 0, 0, 0)"
	});
	//Set progress circle 2
	$("#progress2").circleProgress({
		value: 0.83,
		size: 175,
		thickness: 5,
		fill: "#2be6ab",
		emptyFill: "rgba(0, 0, 0, 0)"
	});
	//Set progress circle 3
	$("#progress3").circleProgress({
		value: 0.25,
		size: 175,
		thickness: 5,
		fill: "#2be6ab",
		emptyFill: "rgba(0, 0, 0, 0)"
	});
	//Set progress circle 4
	$("#progress4").circleProgress({
		value: 0.95,
		size: 175,
		thickness: 5,
		fill: "#2be6ab",
		emptyFill: "rgba(0, 0, 0, 0)"
	});

}

$(document).ready(function () {
	$('.customer-logos').slick({
		slidesToShow: 4,
		slidesToScroll: 1,
		autoplay: true,
		autoplaySpeed: 1500,
		arrows: false,
		dots: false,
		pauseOnHover: false,
		responsive: [{
			breakpoint: 768,
			settings: {
				slidesToShow: 4
			}
		}, {
			breakpoint: 520,
			settings: {
				slidesToShow: 3
			}
		}]
	});
});

(function ($) {
	// Call all functions
	loader();
	responsive();
	heroSection();
	testimonial();
	progressbar();
	videoPopup();
	accordions();
	progressCircle();

})(jQuery);