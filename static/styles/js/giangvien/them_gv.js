(function () {
    $('button[type=submit').click(function (e) {
        console.log("Clicked");

        var name = {
                value: $('input[name=name]').val(),
                helpElement: $('#nameHelp'),
                message: '',
                regex: /^[A-Za-z ]+$/
            },
            msgv = {
                value: $('input[name=msgv]').val(),
                helpElement: $('#msgvHelp'),
                message: '',
                regex: /^GV\d+$/
            },
            diachi = {
                value: $('input[name=diachi]').val(),
                helpElement: $('#diachiHelp'),
                message: '',
                regex: /^.*$/
            },
            email = {
                value: $('input[name=email]').val(),
                helpElement: $('#emailHelp'),
                message: '',
                regex: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/
            },
            sdt = {
                value: $('input[name=sdt]').val(),
                helpElement: $('#sdtHelp'),
                message: '',
                regex: /^\+{0,1}\d+$/
            },
            hocvi = {
                value: $('input[name=hocvi]').val(),
                helpElement: $('#hocviHelp'),
                message: '',
                regex: /^[A-Za-z0-9 ]+$/
            },
            chuyennganh = {
                value: $('input[name=chuyennganh]').val(),
                helpElement: $('#chuyennganhHelp'),
                message: '',
                regex: /^[A-Za-z0-9 ]+$/
            };

        var error = false;
        var fieldInputed = 0;

        if (name.value === '') {
            name.message = "Vui lòng nhập lại tên giảng viên";
            error = true;
        } else if (!name.regex.test(name.value)) {
            name.message = 'Tên giảng viên sai định dạng. Vui lòng nhập lại Tên giảng viên';
            error = true;
            fieldInputed++;
        } else if (name.value.length > 100)
        {
            name.message = 'Chỉ được nhập tối đa 100 kí tự';
            error = true;
            fieldInputed++;
        }

        if (msgv.value === '') {
            msgv.message = "Vui lòng nhập lại MSGV";
            error = true;
        } else if (!msgv.regex.test(msgv.value)) {
            msgv.message = 'MSGV sai định dạng. Vui lòng nhập lại MSGV';
            error = true;
            fieldInputed++;
        } else if (msgv.value.length > 10)
        {
            msgv.message = 'Chỉ được nhập tối đa 10 kí tự';
            error = true;
            fieldInputed++;
        }

        /*Dia chi */
        if (diachi.value === '') {
            diachi.message = "Vui lòng nhập lại Địa chỉ";
            error = true;
        } else if (diachi.value.length > 100)
        {
            diachi.message = 'Chỉ được nhập tối đa 100 kí tự';
            error = true;
            fieldInputed++;
        }

        // Email
        if (email.value === '') {
            email.message = "Vui lòng nhập lại Email";
            error = true;
        } else if (!email.regex.test(email.value)) {
            email.message = 'Email sai định dạng. Vui lòng nhập lại Email';
            error = true;
            fieldInputed++;
        } else if (email.value.length > 100)
        {
            email.message = 'Chỉ được nhập tối đa 100 kí tự';
            error = true;
            fieldInputed++;
        }

        // SDT
        if (sdt.value === '') {
            sdt.message = "Vui lòng nhập lại SĐT";
            error = true;
        } else if (!sdt.regex.test(sdt.value)) {
            sdt.message = 'SĐT sai định dạng. Vui lòng nhập lại SĐT';
            error = true;
            fieldInputed++;
        } else if (sdt.value.length > 11)
        {
            sdt.message = ' SĐT chỉ được nhập tối đa 11 số';
            error = true;
            fieldInputed++;
        }

         /* Hoc vi */
        if (hocvi.value === '') {
            hocvi.message = "Vui lòng nhập lại Học vị";
            error = true;
        } else if (hocvi.value.length > 50)
        {
            hocvi.message = 'Chỉ được nhập tối đa 50 kí tự';
            error = true;
            fieldInputed++;
        }

        /* Chuyen nganh */
        if (chuyennganh.value === '') {
            chuyennganh.message = "Vui lòng nhập lại Chuyên ngành";
            error = true;
        } else if (chuyennganh.value.length > 50)
        {
            chuyennganh.message = 'Chỉ được nhập tối đa 50 kí tự';
            error = true;
            fieldInputed++;
        }


        name.helpElement.text(name.message);
        msgv.helpElement.text(msgv.message);
        diachi.helpElement.text(diachi.message);
        email.helpElement.text(email.message);
        sdt.helpElement.text(sdt.message);
        hocvi.helpElement.text(hocvi.message);
        chuyennganh.helpElement.text(chuyennganh.message);


        if (error) {
            e.preventDefault();
        }
    });
})()