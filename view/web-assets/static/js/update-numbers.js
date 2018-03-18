(function() {
    $.getJSON( "/last-draw", function( d ) {
        console.log(d);
        var draw_data = d.draw;
        var draw_no = draw_data.drawNo;
        var draw_time = draw_data.drawTime;
        var draw_results = draw_data.results;
//        var draw_bonus = draw_results[-1]

        draw_results.each(function( val ) {
            console.log(val);
            $("#"+val).addClass("color-class");
        });
    });
});