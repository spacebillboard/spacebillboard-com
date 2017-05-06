// $Id$

(function ($) {

// soldCanvas

Drupal.behaviors.soldCanvas = {
  attach: function (context, settings) {
    
       
      function deg(deg) {
        return (Math.PI/180)*deg - (Math.PI/180)*90
      } 
 
      function drawCircle(){
          var cHr = $("#canvas_sold").get(0);
          if(cHr && typeof cHr.getContext === 'function') { // MDC: added the second operand because of IE 8
            var perSold = $(".sold-graph .val span").text();
            var ctx = cHr.getContext("2d");
            var grad= ctx.createLinearGradient(25, 25, 100, 100);
            ctx.clearRect(0, 0, cHr.width, cHr.height);
            ctx.beginPath();
            grad.addColorStop(0, "#6daded");
            grad.addColorStop(1, "#3587d0");
            ctx.strokeStyle = grad;
            ctx.lineCap = 'round';
            ctx.shadowOffsetX = 0;
            ctx.shadowOffsetY = 0;
            ctx.arc(50,50,43, (-90 * Math.PI/180),  (((perSold/100 * 360)-90) * Math.PI/180));
            ctx.lineWidth = 7;
            ctx.stroke();
        }
      } 
    
      drawCircle();
 
  }
}


// sidebar

Drupal.behaviors.sidebarHeight = {
  attach: function (context, settings) {
    
      
      $(window).bind("load", function() {

          if($('body').hasClass('page-node-4')) {
            
            var sidebarHeight = $("article#node-4").height();
//            $(".container .span3").height(sidebarHeight);
            
          }

      });      

 
  }
}

// EDITOR MENU


Drupal.behaviors.editormenu = {
attach: function(context, settings) {
	$(window).load(function(){
			$('.region-editor-menu #block-menu-menu-editor h2').click( function () {
			
				if($('#block-menu-menu-editor').hasClass('editor-open')){
					$('#block-menu-menu-editor').animate({marginRight: "-220px"}, 200 ).removeClass('editor-open');
				}
				else{
					$('#block-menu-menu-editor').animate({marginRight: "0"}, 200 ).addClass('editor-open');
				}
			});
	});
}
} 



})(jQuery);




