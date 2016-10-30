function update_front() {
    var image = $("#target-front");
    var img_w = image.width() / 2;
    var img_h = image.height() / 2;

    var bumper = $("#front");
    bumper.css({
        top: img_h - (bumper.height() / 2) + (img_h * 0.4),
        left: img_w - (bumper.width() / 2) - (img_w * 0.65)
    });

    var bumper = $("#passenger_side");
    bumper.css({
        top: img_h - (bumper.height() / 2) + (img_h * 0),
        left: img_w - (bumper.width() / 2) + (img_w * 0.6)
    });

    var fl_light = $("#fl_light");
    fl_light.css({
        top: img_h - (bumper.height() / 2) + (img_h * 0.1),
        left: img_w - (bumper.width() / 2) - (img_w * 0.1)
    });

    var fl_light = $("#fr_light");
    fl_light.css({
        top: img_h - (bumper.height() / 2) + (img_h * 0.0),
        left: img_w - (bumper.width() / 2) - (img_w * 0.85)
    });

    var fl_light = $("#roof");
    fl_light.css({
        top: img_h - (bumper.height() / 2) - (img_h * 0.9),
        left: img_w - (bumper.width() / 2) + (img_w * 0.3)
    });

    var fl_light = $("#front_windscreen");
    fl_light.css({
        top: img_h - (bumper.height() / 2) - (img_h * 0.6),
        left: img_w - (bumper.width() / 2) + (img_w * 0)
    });
}

function update_back() {
    var image = $("#target-back");
    var img_w = image.width() / 2;
    var img_h = image.height() / 2;

    var bumper = $("#back");
    bumper.css({
        top: img_h - (bumper.height() / 2) + (img_h * 0.2),
        left: img_w - (bumper.width() / 2) - (img_w * 0.65)
    });

    var bumper = $("#driver_side");
    bumper.css({
        top: img_h - (bumper.height() / 2) + (img_h * 0),
        left: img_w - (bumper.width() / 2) + (img_w * 0.6)
    });

    var fl_light = $("#bl_light");
    fl_light.css({
        top: img_h - (bumper.height() / 2) - (img_h * 0.2),
        left: img_w - (bumper.width() / 2) - (img_w * 0.2)
    });

    var fl_light = $("#br_light");
    fl_light.css({
        top: img_h - (bumper.height() / 2) - (img_h * 0.2),
        left: img_w - (bumper.width() / 2) - (img_w * 0.85)
    });

    // var fl_light = $("#roof");
    // fl_light.css({
    //     top: img_h - (bumper.height() / 2) - (img_h * 0.9),
    //     left: img_w - (bumper.width() / 2) + (img_w * 0.3)
    // });

    var fl_light = $("#back_windscreen");
    fl_light.css({
        top: img_h - (bumper.height() / 2) - (img_h * 0.7),
        left: img_w - (bumper.width() / 2) - (img_w * 0.3)
    });
}

$(document).ready(function () {
    update_front();
    update_back();

    $('.floating-button-front').on('click', function () {
        var btn = $(this);
        var id = btn.attr('id');
        var title = btn.attr('title');

        $('#damage_header-front').text(title);
        $('#btn-low-front').attr('href', '#claim_' + id);
        $('#btn-medium-front').attr('href', '#claim_' + id);
        $('#btn-high-front').attr('href', '#claim_' + id);
    });

    $('#btn-low-front').on('click', function () {
        var btn = $(this);
        $(btn.attr('href')).attr('value', 1);
    });

    $('#btn-medium-front').on('click', function () {
        var btn = $(this);
        $(btn.attr('href')).attr('value', 2);
    });

    $('#btn-high-front').on('click', function () {
        var btn = $(this);
        $(btn.attr('href')).attr('value', 2);
    });

    $('.floating-button-back').on('click', function () {
        var btn = $(this);
        var id = btn.attr('id');
        var title = btn.attr('title');

        $('#damage_header-back').text(title);
        $('#btn-low-back').attr('href', '#claim_' + id);
        $('#btn-medium-back').attr('href', '#claim_' + id);
        $('#btn-high-back').attr('href', '#claim_' + id);
    });

    $('#btn-low-back').on('click', function () {
        var btn = $(this);
        $(btn.attr('href')).attr('value', 1);
    });

    $('#btn-medium-back').on('click', function () {
        var btn = $(this);
        $(btn.attr('href')).attr('value', 2);
    });

    $('#btn-high-back').on('click', function () {
        var btn = $(this);
        $(btn.attr('href')).attr('value', 2);
    });

    setInterval(function () {
        update_back();
        update_front();
    }, 50);
});

$(window).resize(function () {
    update_front();
    update_back();
});
