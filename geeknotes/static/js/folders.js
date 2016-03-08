$(function() {
    $('#create').click(function() {
        $.get($(this).attr('href'), function(data) {
            $("#folder_create_modal .modal-body").html(data);
        });
        $('#folder_create_modal').modal();
        return false;
    });
});