$( document ).ready(function() {
  $("#join_btn").on('click', function(e) {
    var name = document.getElementById('name').value;
    var ssn = document.getElementById('ssn').value;
    var select = document.getElementById('select').value;
    var phone = document.getElementById('phone').value;
  });
});

$('.terms_of_use_btn').on('click', funsction(e) {
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
