// Flush footer to bottom of page if content does not fill page.
//https://stackoverflow.com/questions/10099422/flushing-footer-to-bottom-of-the-page-twitter-bootstrap/20971428#20971428
$(document).ready(function() {
    setInterval(function() {
        var docHeight = $(window).height();
        var footerHeight = $('#footer').height();
        var footerTop = $('#footer').position().top + footerHeight;
        var marginTop = (docHeight - footerTop + 10);

        if (footerTop < docHeight)
            $('#footer').css('margin-top', marginTop + 'px'); // padding of 30 on footer
        else
            $('#footer').css('margin-top', '0px');
    }, 250);
});