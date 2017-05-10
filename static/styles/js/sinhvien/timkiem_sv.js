(function () {
    $('button[type=submit').click(function (e) {

        var input = {
            value: $('input[name=keywork]').val(),
            message: '',
            helpElement: $('#searchHelp'),
            regex: /^SV3\d+$/
        };

        var error = false;

        if (input.value === '') {
            console.log("input empty");
            input.message = "Vui lòng nhập lại MSSV";
            error = true;
        } else if (!input.regex.test(input.value)) {
            input.message = 'Không tìm thấy MSSV. Vui lòng nhập lại MSSV';
            error = true;
        }

        input.helpElement.text(input.message);

        if (error) {
            e.preventDefault();
        }
    });
})()