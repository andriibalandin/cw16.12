jQuery(document).ready(function ($) {
    var autoplay = false;
    $('#checkbox').change(function(){
        autoplay = $(this).is(':checked');
    });

    var slideCount = $('#slider ul li').length;
    var slideWidth = 340;
    var sliderUlWidth = slideCount * slideWidth;

    $('#slider').css({ width: slideWidth });
    $('#slider ul').css({ width: sliderUlWidth, left: -slideWidth });
    $('#slider ul li:last-child').prependTo('#slider ul');

    function updateSliderHeight() {
        var newHeight = $('#slider ul li').eq(1).outerHeight();
        $('#slider').animate({ height: newHeight }, 200);
    }
    updateSliderHeight();

    function moveLeft() {
        $('#slider ul').animate({
            left: + slideWidth
        }, 200, function () {
            $('#slider ul li:last-child').prependTo('#slider ul');
            $('#slider ul').css('left', -slideWidth);
            updateSliderHeight();
        });
    };

    function moveRight() {
        $('#slider ul').animate({
            left: - slideWidth * 2
        }, 200, function () {
            $('#slider ul li:first-child').appendTo('#slider ul');
            $('#slider ul').css('left', -slideWidth);
            updateSliderHeight();
        });
    };

    $('a.control_prev').click(function (e) {
        e.preventDefault();
        moveLeft();
    });

    $('a.control_next').click(function (e) {
        e.preventDefault();
        moveRight();
    });

    setInterval(function() {
        if (autoplay) {
            moveRight();
        }
    }, 3000);
});
