$(function() {
  $('[data-toggle="tooltip"]').tooltip({
    'container': 'body'
  });
  $("html").niceScroll({horizrailenabled:false});
  $('a[data-confirm]').click(function(e) {
    /*bootbox.confirm($(this).attr('data-confirm'), function() {
      window.location = $(e.target).attr('href');
    });*/
    bootbox.dialog({
      message: $(this).attr('data-confirm'),
      title: "Confirmation",
      buttons: {
        success: {
          label: "Annuler",
          className: "btn-default",
          callback: function() {}
        },
        danger: {
          label: "Supprimer",
          className: "btn-danger",
          callback: function() {
            window.location = $(e.target).attr('href');
          }
        }
      }
    });
    return false;
  });

  setInterval(function(){ 
    $(".alert-box .alert").each(function() {
      if (!$(this).hasClass("timeout-on")) {
        $alert = $(this);
        setTimeout(function(){ 
         $alert.alert('close');
        }, 10000);
        $(this).addClass("timeout-on");
      }
    });
  }, 2000);

});