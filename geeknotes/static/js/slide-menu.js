$('.easy-sidebar-toggle').click(function(e) {
  e.preventDefault();
  $('body').toggleClass('toggled');
  $('.navbar.easy-sidebar').removeClass('toggled');
});
$('html').on('swiperight', function(){
  $('body').addClass('toggled');
});
$('html').on('swipeleft', function(){
  $('body').removeClass('toggled');
});
