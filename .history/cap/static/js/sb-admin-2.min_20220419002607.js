/*!
 * Start Bootstrap - SB Admin 2 v4.1.3 (https://startbootstrap.com/theme/sb-admin-2)
 * Copyright 2013-2021 Start Bootstrap
 * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-sb-admin-2/blob/master/LICENSE)
 */

// !function(l){"use strict";l("#sidebarToggle, #sidebarToggleTop").on("click",function(e){l("body").toggleClass("sidebar-toggled"),l(".sidebar").toggleClass("toggled"),l(".sidebar").hasClass("toggled")&&l(".sidebar .collapse").collapse("hide")}),l(window).resize(function(){l(window).width()<768&&l(".sidebar .collapse").collapse("hide"),l(window).width()<480&&!l(".sidebar").hasClass("toggled")&&(l("body").addClass("sidebar-toggled"),l(".sidebar").addClass("toggled"),l(".sidebar .collapse").collapse("hide"))}),l("body.fixed-nav .sidebar").on("mousewheel DOMMouseScroll wheel",function(e){var o;768<l(window).width()&&(o=(o=e.originalEvent).wheelDelta||-o.detail,this.scrollTop+=30*(o<0?1:-1),e.preventDefault())}),l(document).on("scroll",function(){100<l(this).scrollTop()?l(".scroll-to-top").fadeIn():l(".scroll-to-top").fadeOut()}),l(document).on("click","a.scroll-to-top",function(e){var o=l(this);l("html, body").stop().animate({scrollTop:l(o.attr("href")).offset().top},1e3,"easeInOutExpo"),e.preventDefault()})}(jQuery);
!function(o){"use strict";o("#sidebarToggle, #sidebarToggleTop").on("click",function(e){o("body").toggleClass("sidebar-toggled"),o(".sidebar").toggleClass("toggled"),o(".sidebar").hasClass("toggled")&&o(".sidebar .collapse").collapse("hide")}),o(window).resize(function(){o(window).width()<768&&o(".sidebar .collapse").collapse("hide"),o(window).width()<480&&!o(".sidebar").hasClass("toggled")&&(o("body").addClass("sidebar-toggled"),o(".sidebar").addClass("toggled"),o(".sidebar .collapse").collapse("hide"))}),o("body.fixed-nav .sidebar").on("mousewheel DOMMouseScroll wheel",function(e){if(o(window).width()>768){var s=e.originalEvent,l=s.wheelDelta||-s.detail;this.scrollTop+=30*(l<0?1:-1),e.preventDefault()}}),o(document).on("scroll",function(){o(this).scrollTop()>100?o(".scroll-to-top").fadeIn():o(".scroll-to-top").fadeOut()}),o(document).on("click","a.scroll-to-top",function(e){var s=o(this);o("html, body").stop().animate({scrollTop:o(s.attr("href")).offset().top},1e3,"easeInOutExpo"),e.preventDefault()}),o(".dropdown-menu a.dropdown-toggle").on("click",function(e){return o(this).next().hasClass("show")||o(this).parents(".dropdown-menu").first().find(".show").removeClass("show"),o(this).next(".dropdown-menu").toggleClass("show"),o(this).parents("li.nav-item.dropdown.show").on("hidden.bs.dropdown",function(e){o(".dropdown-submenu .show").removeClass("show")}),!1})}(jQuery);