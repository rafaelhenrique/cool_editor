$(function(){
    var csrftoken = $('meta[name=csrf-token]').attr('content');

    $('#code-editor').on("keyup click", function(event){
        var code_editor = $(this)[0];
        // line where the cursor is
        var cursor = code_editor.selectionStart;
        // array of lines after cursor
        var lines_after_cursor = code_editor.value.substr(0, cursor).split("\n")
        // line must be start in 0
        var actual_line_number = lines_after_cursor.length - 1
        var actual_line = lines_after_cursor[actual_line_number]

        var endpoint = $(this).data("endpoint");
        var verb = $(this).data("verb");

        $.ajax({
            url: endpoint,
            type: verb,
            data: {'key': actual_line_number, 'value': actual_line},
        })
        .fail(function(jqXHR, textStatus) {
            var payload = jqXHR.responseJSON;
            console.log(payload);
        })        

        // Only debug purposes
        // console.log(actual_line_number);
        // console.log(actual_line);
        // console.log(csrftoken);
        return false;
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
                }
            });
            code_editor.val(lines.join("\n"));
        });
    }

    get_doc();
});
