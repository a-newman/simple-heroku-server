$(document).ready(function() {
    console.log("Document is loaded!");

    $("#name-button").click(function () {
        $("#welcome").text("Welcome, " + $("input").val());
    });
});
