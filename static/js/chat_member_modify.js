$( document ).ready(function() {
  $("#modify_btn").on('click', function(e) {
    var name = document.getElementById('name').value;
    var ssn = document.getElementById('ssn').value;
    var select = document.getElementById('select').value;
    var phone = document.getElementById('phone').value;
    if (name == '' || ssn == '' || phone == '') {
        alert("회원수정정보를 입력해주세요!")

    }
    else if (ssn != '' && ssn.toString().length != 6) {
        alert("주민등록번호가 일치 하지 않습니다!")

    }
//    else if (select) {
//        alert("통신사가 일치 하지 않습니다!")
//    }

    else if (phone != '' && phone.toString().length != 11) {
        alert("전화번호가 일치 하지 않습니다!")

    }
//    alert(name);
    });

  $("#withdraw_btn").on('click', function(e) {
    var name = document.getElementById('name').value;
    var ssn = document.getElementById('ssn').value;
    var select = document.getElementById('select').value;
    var phone = document.getElementById('phone').value;
    if (name == '' || ssn == '' || phone == '') {
        alert("회원수정정보를 입력해주세요!")
    }
    else if (ssn != '' && ssn.toString().length != 6) {
        alert("주민등록번호가 일치 하지 않습니다!")
    }
//    else if (select) {
//        alert("통신사가 일치 하지 않습니다!")
//    }

    else if (phone != '' && phone.toString().length != 11) {
        alert("전화번호가 일치 하지 않습니다!")
    }
//    alert(name);
    });
});
