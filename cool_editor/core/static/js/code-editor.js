$(function(){
    var csrftoken = $('meta[name=csrf-token]').attr('content');
    var file = {};

    $("#code-editor").on("keyup keydown", function(event){
        var lines = $(this).val().split('\n');
        var endpoint = $(this).data("endpoint");
        var verb = $(this).data("verb");

        $.each(lines, function(line_number, new_line){
            var old_line = file[line_number];

            // diff between versions of file line by line
            if (old_line != new_line){
                // Only debug porpouses
                // console.log("Diff: " + line_number + ". old: " + old_line + " new: " + new_line);
                $.ajax({
                    url: endpoint,
                    type: verb,
                    data: {'key': line_number, 'value': new_line},
                })
                .fail(function(jqXHR, textStatus) {
                    var payload = jqXHR.responseJSON;
                    console.log(payload);
                })
                file[line_number] = new_line;
            }
        });
    });

    var get_doc = function(){
        var code_editor = $('#code-editor');
        var endpoint = code_editor.data("endpoint");

        $.ajax({
            url: endpoint,
            type: "get",
        })
        .fail(function(jqXHR, textStatus) {
            var payload = jqXHR.responseJSON;
            console.log(payload);
        })
        .done(function(payload) {
            var lines = [];
            $.each(payload, function(line_number, line_value) {
                if ($.isNumeric(line_number) == true){
                    lines.push(line_value);
                    file[line_number] = line_value;
                }
            });
            code_editor.val(lines.join("\n"));
        });
    }

    get_doc();
});
