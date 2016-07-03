function Slider( container, nav ) {
  this.container = container;
  this.nav = nav.show();

  this.imgs = this.container.find('li');
  //this.imgWidth = this.container.find('div:first-child').width();
  this.imgsLen = this.imgs.length;

  this.current = 0;
}

Slider.prototype.transition = function( coords ) {
  this.container.animate({
    //'margin-left' : coords || -( this.current * this.imgWidth )
    'margin-left' : coords || -( this.current * this.container.find('div:first-child').width() )
  });
};

Slider.prototype.resize_transition = function() {
  this.container.css({
    'margin-left' : -( this.current * this.container.find('div:first-child').width() )
  });
};

Slider.prototype.setCurrent = function( dir ) {
  var pos = this.current;
  pos += ( ~~( dir === 'next') || -1 ); //example: ~~(true) = 1

  this.current = ( pos < 0 ) ? this.imgsLen - 1 : pos % this.imgsLen;

  return pos;
};