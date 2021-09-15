
$(document).ready(function(){
    $('#subjectiveTitle').click(function() {
        $('#subjectiveForm').toggle(1500);
    });
    $('#demographyTitle').click(function() {
        $('#demographyForm').toggle(1500);
    });
    $('#individualTitle').click(function() {
        $('#individualForm').toggle(1500);
    });
    $('#measurmentTitle').click(function() {
        $('#measurmentForm').toggle(1500);
    });
    $('#surveyTitle').click(function() {
        $('#surveyForm').toggle(1500);
    });
    // demography
    $("#age").slider({tooltip: 'always'});
    $("#age").on("slide", function(slideEvt){
        $("#age_value").text(slideEvt.value);
    });
    $("#height").slider({tooltip: 'always'});
    $("#height").on("slide", function(slideEvt){
        $("#height_value").text(slideEvt.value);
    });
    $("#weight").slider({tooltip: 'always',precision: 2,});
    $("#weight").on("slide", function(slideEvt){
        $("#weight_value").text(slideEvt.value);
    });
    // individual activity background
    $("#metabolic_rate").slider({tooltip: 'always',precision: 2,});
    $("#metabolic_rate").on("slide", function(slideEvt){
        $("#metabolic_rate_value").text(slideEvt.value);
    });
    $("#clothing_index").slider({tooltip: 'always',precision: 2,});
    $("#clothing_index").on("slide", function(slideEvt){
        $("#clothing_index_value").text(slideEvt.value);
    });
    $("#thermal_history").slider({tooltip: 'always',precision: 2,});
    $("#thermal_history").on("slide", function(slideEvt){
        $("#thermal_history_value").text(slideEvt.value);
    });
    // measurment
    $("#air_temp").slider({tooltip: 'always',precision: 2,});
    $("#air_temp").on("slide", function(slideEvt){
        $("#air_temp_value").text(slideEvt.value);
    });
    $("#relative_humidity").slider({tooltip: 'always',precision: 2,});
    $("#relative_humidity").on("slide", function(slideEvt){
        $("#relative_humidity_value").text(slideEvt.value);
    });
    $("#wind_speed").slider({tooltip: 'always',precision: 2,});
    $("#wind_speed").on("slide", function(slideEvt){
        $("#wind_speed_value").text(slideEvt.value);
    });
    $("#global_temp").slider({tooltip: 'always',precision: 2,});
    $("#global_temp").on("slide", function(slideEvt){
        $("#global_temp_value").text(slideEvt.value);
    });
    $("#mean_radiant_temp").slider({tooltip: 'always',precision: 2,});
    $("#mean_radiant_temp").on("slide", function(slideEvt){
        $("#mean_radiant_temp_value").text(slideEvt.value);
    });
    $("#radiation").slider({tooltip: 'always',precision: 2,});
    $("#radiation").on("slide", function(slideEvt){
        $("#radiation_value").text(slideEvt.value);
    });
    $("#pet").slider({tooltip: 'always',precision: 3,});
    $("#pet").on("slide", function(slideEvt){
        $("#pet_value").text(slideEvt.value);
    });
    $("#utci").slider({tooltip: 'always',precision: 3,});
    $("#utci").on("slide", function(slideEvt){
        $("#utci_value").text(slideEvt.value);
    });
});

// $( function() {
//    $( "#heightSlider" ).slider({
//        range: true,
//        min: {{ age_min }},
//        max: {{ age_max }},
//        values: [ 75, 300 ],
//        slide: function( event, ui ) {
//            $( "#height" ).val(ui.values[ 0 ] + " - " + ui.values[ 1 ] );
//        }
//    });
//    $( "#height" ).val($( "#heightSlider" ).slider( "values", 0 ) + " - " + $( "#heightSlider" ).slider( "values", 1 ) );
// });
// $( function() {
//    $( "#weightSlider" ).slider({
//        range: true,
//        min: {{ age_min }},
//        max: {{ age_max }},
//        values: [ 75, 300 ],
//        slide: function( event, ui ) {
//            $( "#weight" ).val(ui.values[ 0 ] + " - " + ui.values[ 1 ] );
//        }
//    });
//    $( "#weight" ).val($( "#weightSlider" ).slider( "values", 0 ) + " - " + $( "#weightSlider" ).slider( "values", 1 ) );
// });