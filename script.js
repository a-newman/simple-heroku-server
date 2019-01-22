$(document).ready(function() {
    console.log("Document is loaded!");

    $("#name-button").click(function() {
        $("#welcome").text("Welcome, " + $("input").val());
    });

    $("#save-button").click(function() {
        payload = {name: $("input").val()};
        $.ajax({
            url: "data",
            type: "POST",
            data: JSON.stringify(payload),
            dataType: "json"
        }).then(function(response) {
            console.log("SUCCESS:", response);
        }).catch(function(error) {
            console.log("ERROR SAVING CODE", error);
        })
    });
});
