(function () {
    // console.log($("#nameHelp").removeClass('invisible').text("YoYo"));
    $('button[type=submit').click(function (e) {
        console.log("Clicked");

        var name = {
                value: $('input[name=name]').val(),
                helpElement: $('#nameHelp'),
                message: '',
                regex: /^[A-Za-z ]+$/
            },
            mssv = {
                value: $('input[name=mssv').val(),
                helpElement: $('#mssvHelp'),
                message: '',
                regex: /^SV3\d+$/
            },
            lop = {
                value: $('input[name=lop]').val(),
                helpElement: $('#lopHelp'),
                regex: /[a-zA-Z\d]+/,
                message: ''
            };

        var error = false;
        var fieldInputed = 0;

        if (name.value === '') {
            console.log("name empty");
            name.message = "Vui lòng nhập lại Tên sinh viên";
            error = true;
        } else if (!name.regex.test(name.value)) {
            console.log("Tên sinh viên sai định dạng. Vui lòng nhập lại Tên sinh viên");
            name.message = 'Tên sinh viên sai định dạng. Vui lòng nhập lại Tên sinh viên';
            error = true;
            fieldInputed++;
        } else if (name.value.length > 100)
        {
            name.message = 'Chỉ được nhập tối đa 100 kí tự';
            error = true;
            fieldInputed++;
        }

        if (mssv.value === '') {
            mssv.message = "Vui lòng nhập lại MSSV";
            error = true;
        } else if (!mssv.regex.test(mssv.value)) {
            mssv.message = 'MSSV sai định dạng. định dạng MSSV: SV3xxxxx';
            error = true;
            fieldInputed++;
        } else if (mssv.value.length > 10) {
            mssv.message = 'Chỉ được nhập tối đa 10 kí tự';
            error = true;
            fieldInputed++;
        }
        
        if (lop.value === '') {
            lop.message = "Vui lòng nhập lại Lớp";
            error = true;
        } else if (!lop.regex.test(lop.value)) {
            lop.message = 'Lớp sai định dạng. Vui lòng nhập lại Lớp';
            error = true;
            fieldInputed++;
        } else if (lop.value.length > 10)
        { 
            lop.message = 'Chỉ được nhập tối đa 10 kí tự';
            error = true;
            fieldInputed++;
        }

        name.helpElement.text(name.message);
        mssv.helpElement.text(mssv.message);
        lop.helpElement.text(lop.message);

        if (error) {
            e.preventDefault();
        }
    });
})();