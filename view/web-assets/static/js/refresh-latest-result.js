var updater = function () {
                           $('#latest-result').load('latest-result').fadeIn("slow");
                           $.getJSON( "/last-draw", function( d ) {
                              var draw_no = d.drawNo;
                              var draw_time = d.drawTime;
                              var draw_results = d.results;
                              var arrayLength = draw_results.length;
                              var draw_bonus = draw_results[arrayLength-1]

                              for (var i = 0; i < arrayLength; i++) {
                                  $("#"+draw_results[i]).removeClass();
                                  $("#"+draw_results[i]).addClass("selected");
                              }
                              $("#"+draw_bonus).removeClass();
                              $("#"+draw_bonus).addClass("bonus");

                              $("#draw-details").html("Αριθμός κλήρωσης: <b>"+draw_no+"</b><br>Ώρα κλήρωσης: <b>"+draw_time+"</b>");
                           });
                           };
updater();
var autoLoad = setInterval( updater, 60000*5); // refresh page every 60*5 seconds
