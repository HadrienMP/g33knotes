$(function() {
    $('.timeline-icon').click(function() {
        $(this).parents('.timeline-row').toggleClass('selected');
        toggleDisabledMoveButton();
    });

    $('#check-all').click(function(e) {
        var $i = $(this).find('i');

        if ($i.hasClass('fa-check')) {
            $('.timeline-row').addClass('selected');
        }
        else {
            $('.timeline-row').removeClass('selected');
        }
        $i.toggleClass('fa-check').toggleClass('fa-ban');

        toggleDisabledMoveButton();

        $(this).blur();
    });

    // Displays the modal form
    $('#move-notes').click(function() {
        if (!$(this).hasClass('disabled')) {
            // Clean up
            $('#notes-move-modal input[type="checkbox"]').prop('checked', '');

            // Automatic checkbox checking
            var $selected_notes = $('.timeline-row.selected')
            $selected_notes.each(function() {
                var slug = $(this).find('a').attr('href').split('/')[2];
                $('#notes-move-modal input[type="checkbox"][value="' + slug + '"]').prop('checked', 'true');
            });
            
            // Displays the number of checked notes
            $('#selected-notes-displayer .badge').text($selected_notes.length);

            // Display the modal
            $('#notes-move-modal').modal();
        }
    });

    $('#selected-notes-displayer a').click(function() {
        $('#notes-move-modal .notes').toggle();
        $(this).find('.fa').toggleClass('fa-caret-right').toggleClass('fa-caret-down');
        var text = "Afficher";
        var $display_type = $('#notes-display-type');
        if ($display_type.text() === text) {
            $display_type.text("Cacher");
        } else {
            $display_type.text(text);
        }
        return false;
    });
});

function toggleDisabledMoveButton() {
    if ($('.timeline-row.selected').length > 0) {
        $('#move-notes').removeClass('disabled');
    }
    else {
        $('#move-notes').addClass('disabled');
    }
}