$(document).ready(function() {
	//little trick for slider
	cur_item_width = $(".baner").width();
	$(".resp-w-item").css('width', cur_item_width);

	//fitler in small resolutions
	$(".filter-btn").click(function() {
		$(this).toggleClass("off");
		$(".filter").slideToggle();
	});

	//forward call
	$(".callback").click(function(e) {
		e.preventDefault();
		$(".forward-call").fadeIn(300, function() {
			$(this).focus();
		});
	});

	$(".close").click(function() {
		$(".forward-call").fadeOut(300);
	});

	//toggle order details in My cabinet
	$(".more-cl").click(function() {
		$(this).html( $(this).text() == "▸" ? "▾" : "▸" );
		$(this).siblings(".more-info").slideToggle();
	});

	//menu clicking
	$('.toggle-mnu,.exit').click(function() {
		$('.sidebar').toggleClass('visible-sb');
	});

	//search in small resolutions
	$('.m-search, .closes').click(function() {
		$('.searchmob').toggleClass('visible-smob');
	});

	//Цели для Яндекс.Метрики и Google Analytics
	$(".count_element").on("click", (function() {
		ga("send", "event", "goal", "goal");
		yaCounterXXXXXXXX.reachGoal("goal");
		return true;
	}));

	//SVG Fallback
	if(!Modernizr.svg) {
		$("img[src*='svg']").attr("src", function() {
			return $(this).attr("src").replace(".svg", ".png");
		});
	};

	//Аякс отправка форм
	//Документация: http://api.jquery.com/jquery.ajax/
	$("#form").submit(function() {
		$.ajax({
			type: "POST",
			url: "mail.php",
			data: $(this).serialize()
		}).done(function() {
			alert("Спасибо за заявку!");
			setTimeout(function() {
				
				$("#form").trigger("reset");
			}, 1000);
		});
		return false;
	});

	//Chrome Smooth Scroll
	try {
		$.browserSelector();
		if($("html").hasClass("chrome")) {
			$.smoothScroll();
		}
	} catch(err) {

	};

	$("img, a").on("dragstart", function(event) { event.preventDefault(); });
});