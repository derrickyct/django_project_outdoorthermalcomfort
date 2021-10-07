$(document).ready(function(){
    // keep focus on the table
    if ($("#tableAnchor").attr("title") == 'True') {
//        var pos = $("#tableAnchor").attr("href");
//        $('html,body').animate({scrollTop: $(pos).offset().top},'slow');
        $(document).scrollTop($("#tableAnchor").offset().top);
    };

    // form expansion
    $('#filterTitle').click(function() {
        if($("#subjectiveForm").is(":visible") || $("#demographyForm").is(":visible") || $("#individualForm").is(":visible") ||
        $("#measurementForm").is(":visible") || $("#surveyForm").is(":visible")){
            $('#subjectiveForm').hide(600);
            $('#demographyForm').hide(600);
            $('#individualForm').hide(600);
            $('#measurementForm').hide(600);
            $('#surveyForm').hide(600);
        }else{
            $('#subjectiveForm').show(600);
            $('#demographyForm').show(600);
            $('#individualForm').show(600);
            $('#measurementForm').show(600);
            $('#surveyForm').show(600);
        }
    });
    $('#subjectiveTitle').click(function() {
        $('#subjectiveForm').toggle(600);
    });
    $('#demographyTitle').click(function() {
        $('#demographyForm').toggle(600);
    });
    $('#individualTitle').click(function() {
        $('#individualForm').toggle(600);
    });
    $('#measurementTitle').click(function() {
        $('#measurementForm').toggle(600);
    });
    $('#surveyTitle').click(function() {
        $('#surveyForm').toggle(600);
    });

    // demography
    $("#age-slider").slider({});
    $("#age-slider").on("slide", function(slideEvt){
        $("#age_value").text(slideEvt.value);
    });
    $("#height-slider").slider({});
    $("#height-slider").on("slide", function(slideEvt){
        $("#height_value").text(slideEvt.value);
    });
    $("#weight-slider").slider({precision: 2,});
    $("#weight-slider").on("slide", function(slideEvt){
        $("#weight_value").text(slideEvt.value);
    });
    // individual activity background
    $("#metabolic_rate-slider").slider({precision: 2,});
    $("#metabolic_rate-slider").on("slide", function(slideEvt){
        $("#metabolic_rate_value").text(slideEvt.value);
    });
    $("#clothing_index-slider").slider({precision: 2,});
    $("#clothing_index-slider").on("slide", function(slideEvt){
        $("#clothing_index_value").text(slideEvt.value);
    });
    $("#thermal_history-slider").slider({precision: 2,});
    $("#thermal_history-slider").on("slide", function(slideEvt){
        $("#thermal_history_value").text(slideEvt.value);
    });
    // measurement
    $("#air_temp-slider").slider({precision: 2,});
    $("#air_temp-slider").on("slide", function(slideEvt){
        $("#air_temp_value").text(slideEvt.value);
    });
    $("#relative_humidity-slider").slider({precision: 2,});
    $("#relative_humidity-slider").on("slide", function(slideEvt){
        $("#relative_humidity_value").text(slideEvt.value);
    });
    $("#wind_speed-slider").slider({precision: 2,});
    $("#wind_speed-slider").on("slide", function(slideEvt){
        $("#wind_speed_value").text(slideEvt.value);
    });
    $("#global_temp-slider").slider({precision: 2,});
    $("#global_temp-slider").on("slide", function(slideEvt){
        $("#global_temp_value").text(slideEvt.value);
    });
    $("#mean_radiant_temp-slider").slider({precision: 2,});
    $("#mean_radiant_temp-slider").on("slide", function(slideEvt){
        $("#mean_radiant_temp_value").text(slideEvt.value);
    });
    $("#radiation-slider").slider({precision: 2,});
    $("#radiation-slider").on("slide", function(slideEvt){
        $("#radiation_value").text(slideEvt.value);
    });
    $("#pet-slider").slider({precision: 3,});
    $("#pet-slider").on("slide", function(slideEvt){
        $("#pet_value").text(slideEvt.value);
    });
    $("#utci-slider").slider({precision: 3,});
    $("#utci-slider").on("slide", function(slideEvt){
        $("#utci_value").text(slideEvt.value);
    });
});
