(function () {
    $('button[type=submit').click(function (e) {

        var input = {
            value: $('input[name=keywork]').val(),
            message: '',
            helpElement: $('#searchHelp'),
            regex: /^GV\d+$/
        };

        var error = false;

        if (input.value === '') {
            console.log("input empty");
            input.message = "Vui lòng nhập lại MSGV";
            error = true;
        } else if (!input.regex.test(input.value)) {
            input.message = 'MSGV sai định dạng.Vui lòng nhập lại MSGV';
            error = true;
        } else if (input.value.length > 10)
        {
            input.message = 'Chỉ được nhập tối đa 10 kí tự';
            error = true;
        } else if (input.value === "GV0101") {
            input.message = 'Không tìm thấy MSGV. Vui lòng nhập lại MSGV';
            error = true;
        }

        input.helpElement.text(input.message);

        if (error) {
            e.preventDefault();
        }
    });
})()