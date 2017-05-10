(function () {
    $('button[type=submit').click(function (e) {

        var input = {
            value: $('input[name=keywork]').val(),
            message: '',
            helpElement: $('#searchHelp'),
            regex: /^[A-Za-z0-9 ]+$/
        };

        var error = false;

        if (input.value === '') {
            console.log("input empty");
            input.message = "Vui lòng nhập lại Mã đề tài";
            error = true;
        } else if (!input.regex.test(input.value)) {
            input.message = 'Không tìm thấy đề tài. Vui lòng nhập lại Mã đề tài';
            error = true;
        } else if (input.value.length > 10)
        {
            input.message = 'Chỉ được nhập tối đa 10 kí tự';
            error = true;
        }

        input.helpElement.text(input.message);

        if (error) {
            e.preventDefault();
        }
    });
})()