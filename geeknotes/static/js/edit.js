var editor = undefined;

$(function() {
    $('#editor, #note').css('height', $(window).height() - $('#editor').offset().top);
    activateAce();
    
    // Modification du tag généré par taggit autosuggest
    $('#id_tags__tagautosuggest').addClass('form-control');
    
    $('#edit-note-form').submit(function() {
        $('input[name="content"]').val(editor.getSession().getValue());
    });
    
    $(document).keydown(function(event) {
        // var currKey=0,e=e||event; 
        // currKey=e.keyCode||e.which||e.charCode;  //do this handle FF and IE
        if (!( String.fromCharCode(event.which).toLowerCase() == 's' && event.ctrlKey) && !(event.which == 19)) return true;
        event.preventDefault();
        $('#edit-note-form').submit();
        return false;
    });
    
    $("#save-note").click(function() {
        $('#edit-note-form').submit();
    });
    
    
    $(".ace_scrollbar, #note").niceScroll({horizrailenabled:false});
    
    // Adjust to the nicescroll width
    $(".ace_scroller").css('right', '0');
    $(".ace_scrollbar").width(4);
    
    $("#toggle-preview").click(function() {
       $("#note").toggleClass("col-md-6").toggleClass("col-md-0");
       $(".edit").toggleClass("col-md-6").toggleClass("col-md-12");
    });
});

function activateAce() {
    editor = ace.edit("editor");
    editor.getSession().setMode("ace/mode/markdown");
    editor.getSession().setUseWrapMode(true);
}