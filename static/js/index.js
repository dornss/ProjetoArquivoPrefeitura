$(document).ready(function() {
    var currentUrl = window.location.pathname;

    $(".sidebar ul li.active").removeClass('active');

    $(".sidebar ul li").each(function() {
        var linkUrl = $(this).find('a').attr('href');

        if (currentUrl === linkUrl) {
            $(this).addClass('active');
        }
    });
});