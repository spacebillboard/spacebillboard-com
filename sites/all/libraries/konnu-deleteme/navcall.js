(function ($) {


// onepage nav call

Drupal.behaviors.onepageNavCall = {
  attach: function (context, settings) {

    $('ul.sbb-sidenav').onePageNav({
      changeHash: false,
      scrollOffset: 60,
      scrollThreshold: 0.02
    });

  }
}



})(jQuery);
