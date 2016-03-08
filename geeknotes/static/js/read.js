$(function() {
    
    if ($(window).width() > 750) {
        $('.panel.toc').width($('.panel.toc').width());
        $('.panel.toc').affix({
            offset: 40
        });
    }

    /**
     * Creates the checkboxes 
     */
    var checkboxSelector = '#note li:contains("[ ]"), #note li:contains("[X]"), #note li:contains("[>]")';
    checkboxSelector += ', #note td:contains("[ ]"), #note td:contains("[X]"), #note td:contains("[>]")';
    $(checkboxSelector).each(function() {
        $(this).html($(this).html()
            .replace(/\[\s\]/g, '<i class="fa fa-square-o"></i>')
            .replace(/(.*)\[X\](.*)/g, '<span style="color: grey; font-size: 0.9em">$1<i class="fa fa-check-square-o"></i>$2</span>')
            .replace(/\[&gt;\]/g, '<i class="fa fa-caret-square-o-right"></i>')); 
    });
    /**
     * Creates the arrows
     */
    $("#note *:contains('->')").each(function() {
        $(this).html($(this).html()
            .replace(/-&gt;/g, '<i class="fa fa-long-arrow-right"></i>'));
    });
    /**
     * Creates the exclamation marks
     */
    $("#note *:contains('/!\')").each(function() {
        $(this).html($(this).html()
            .replace(/\/!\\/g, '<i class="fa fa-exclamation-triangle"></i>'));
    });
    /**
     * Creates the calendar events
     */
    $("#note *:contains('!E')").each(function() {
        $(this).html($(this).html()
            .replace(/!E/g, '<i class="fa fa-calendar"></i>'));
    });
    /**
     * Creates the actions ("@FJO:demain")
     */
    $("#note *").each(function() {
        $(this).html($(this).html()
            .replace(/(@\w+(:[\w\d]+)?)/g, "<strong>$1</strong>"));
    });
});