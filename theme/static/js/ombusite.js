$.fx.speeds._default = 400;

function closestToTop() {
    var currDelta = Number.POSITIVE_INFINITY, currElem;
    $('.pane').each(function() {
        $th = $(this);
        var delta = $th.position().top - window.scrollY;
        if(Math.abs(delta) < Math.abs(currDelta)) {
            currDelta =  delta;
            currElem =  $th;
        }
    });
    return currElem;
}

jQuery(document).ready(function($) {

    // Center closest pane after ms of no resizing
    var id, ms = 500;
    $(window).resize(function() {
        clearTimeout(id);
        id = setTimeout(function() {
            var el = closestToTop(),
           i = $('.pane').index(el);
        $('.nav > li > a').eq(i).trigger('click');
        }, ms);
    });

    // Scroll panes when clicking on nav items
    $('#main-nav a').click(function(event) {
        event.preventDefault();
        $('html,body').animate({scrollTop: $(this.hash).offset().top});
        window.location.hash = this.hash;
    });

    // Start carousels
    $('.carousel').carousel({interval: false});
    $('.project .nav-stacked').on('click', 'li', function(e) {
        var $th, c;
        e.preventDefault();
        $th = $(this);
        $th.siblings().removeClass('active');
        $th.addClass('active');
        c = $th.parents('.project').find('.carousel');
        c.data('carousel').to($th.index());
    });
});

