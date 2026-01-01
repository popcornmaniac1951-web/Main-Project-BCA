
// swiper for hero section


var swiper = new Swiper(".mySwiper", {
  loop: true,
  autoplay: {
    delay: 2500,
    disableOnInteraction: false,
  },
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  scrollbar: {
    el: ".swiper-scrollbar",
    hide: true,
  }
});



$(document).ready(function () {
  $('.img-owl').owlCarousel({
    loop: true,
    autoplay: true,
    margin: 15,
    nav: true,
    navText: [
      '<i class="fa fa-long-arrow-left" aria-hidden="true"></i>',
      '<i class="fa fa-long-arrow-right" aria-hidden="true"></i>'
    ],
    dots: false,
    responsive: {
      0: { items: 1 },
      576: { items: 2 },
      768: { items: 3 },
      1200: { items: 4 }
    }
  });
});


  $(document).ready(function(){
    $(".owl-carousel").owlCarousel({
      items: 1,              // number of items shown
      loop: true,            // loop the slides
      margin: 10,            // space between slides
      nav: true,             // show next/prev buttons
      dots: true,            // show dots below
      autoplay: true,        // enable auto play
      autoplayTimeout: 3000, // delay between slides
      autoplayHoverPause: true // pause on hover
    });
  });