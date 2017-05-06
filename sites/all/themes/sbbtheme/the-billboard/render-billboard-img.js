var page = require('webpage').create();
page.open('http://local.spacebillboard.com/?k=eenstompaswoord', function() {
  var clipRect = page.evaluate(function() {
    var billboard = document.querySelector("table.billboard");
    return billboard.getBoundingClientRect();
  });
  page.clipRect = {
      top:    clipRect.top,
      left:   clipRect.left,
      width:  clipRect.width,
      height: clipRect.height
  };
  page.render('generated/the-billboard.png');
  phantom.exit();
});
