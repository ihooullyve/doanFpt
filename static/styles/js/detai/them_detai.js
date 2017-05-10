(function () {
    $('button[type=submit').click(function (e) {
        console.log("Clicked");

        var name = {
                value: $('input[name=name]').val(),
                helpElement: $('#nameHelp'),
                message: '',
                regex: /^[A-Za-z0-9 ]+$/
            },
            madt = {
                value: $('input[name=madt]').val(),
                helpElement: $('#madtHelp'),
                message: '',
                regex: /^[A-Za-z0-9 ]+$/
            };

        var error = false;
        var fieldInputed = 0;

        if (name.value === '') {
            name.message = "Vui lòng nhập lại tên đề tài";
            error = true;
        } else if (!name.regex.test(name.value)) {
            console.log("Tên đề tài sai định dạng. Vui lòng nhập lại tên đề tài");
            name.message = 'Tên đề tài sai định dạng. Vui lòng nhập lại tên đề tài';
            error = true;
            fieldInputed++;
        } else if (name.value.length > 100)
        {
            name.message = 'Chỉ được nhập tối đa 100 kí tự';
            error = true;
            fieldInputed++;
        }

        if (madt.value === '') {
            madt.message = "Vui lòng nhập lại mã đề tài";
            error = true;
        } else if (!madt.regex.test(madt.value)) {
            madt.message = 'Mã đề tài sai định dạng. Vui lòng nhập lại mã đề tài';
            error = true;
            fieldInputed++;
        } else if (madt.value.length > 10)
        {
            madt.message = 'Chỉ được nhập tối đa 10 kí tự';
            error = true;
            fieldInputed++;
        }

        name.helpElement.text(name.message);
        madt.helpElement.text(madt.message);

        if (error) {
            e.preventDefault();
        }
    });
})()