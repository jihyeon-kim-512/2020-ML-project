$( document ).ready(function() {
  $("#join_btn").on('click', function(e) {
    var name = document.getElementById('name').value;
    var ERROR_NO_VALUE_NAME = "ERROR_NO_VALUE_NAME";
    var ssn = document.getElementById('ssn').value;
    var select = document.getElementById('select').value;
    var phone = document.getElementById('phone').value;
    if (name == '' || ssn == '' || phone == '') {
        alert("회원가입정보를 입력해주세요!")
    }
    else if (ssn != '' && ssn.toString().length != 6) {
        alert("주민등록번호 자리수를 확인해주세요!")
    }
    else if (phone != '' && phone.toString().length != 11) {
        alert("전화번호 자리수를 확인해주세요!")
    }

    else alert(name);
  });
});



$('.terms_of_use_btn').on('click', function(e) {
  e.preventDefault();
  var el = $($(this).attr('href'));
  if (!el.hasClass('open')) {
    el.addClass('open');
  } else {
    el.removeClass('open');
  }
});

$('.btn_popup_close').on('click', function(e) {
  $(this).closest('.Popup_page').removeClass('open');
});


$( document ).ready(function() {

});
