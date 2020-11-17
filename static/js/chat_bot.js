//웹 소켓 연결
var socket = io.connect('http://' + document.domain + ':' + location.port);

//사용자명 임시 설정 (나중에 사용자명 받아와서 저장)
const user_name = "김미미";

//웹페이지에 소켓이 연결되면 실행
socket.on( 'connect', function() {
    //콘솔창에서 제대로 연결 되었는지 확인
    console.log("connect");

    //전송 버튼 클릭
    var form = $( '#push_btn' ).click(function( e ) {
        e.preventDefault()
        //message_form 함수 호출
        message_form();
    } )

    //텍스트입력 이후 enter키 push
    var enter = $(document).on('keydown', '#user_say', function(e){
        if(e.keyCode == 13 && !e.shiftKey) {
            e.preventDefault();
            //message_form 함수 호출
            message_form();
        }

    });

} )



function message_form() {
    //textarea에 있는 값 받아와서 저장
    let user_input = $( '#user_say' ).val()

        if (user_input.replace(/\s|　/gi, "").length == 0) {
            //공백일때 함수 없음
        } else {
            //공백이 아니면 소켓으로 다음의 데이터 전송

            socket.emit( 'my event', {
                user_name  : user_name,
                message    : user_input
            } )

        //데이터를 전송하면 textarea의 문자열을 지움
        $( '#user_say' ).val( '' ).focus()

    }
}

socket.on( 'start_chat' ,function(ans) {
  setTimeout(function() {
    console.log(ans);
    appendMessageTag("left", "체이스", ans);
  }, 500);

})

//웹소켓으로 전송된 데이터 수신부
socket.on( 'my response', function( msg ) {
    //콘솔창에서 수신된 json 확인
    console.log( msg );
    appendMessageTag("right", msg.user_name, msg.message);

})



// 메세지 태그 append
function appendMessageTag(LR_className, senderName, message) {
    const chatLi = createMessageTag(LR_className, senderName, message);
    // 스크롤바 아래 고정
    $("div.contents").scrollTop($("div.contents")[0].scrollHeight);
    $('div.chat:not(.format) ul').append(chatLi);

}



// 메세지 태그 생성
function createMessageTag(LR_className, senderName, message) {
    // 형식 가져오기
    let chatLi = $('div.chat.format ul li').clone();

    // 값 채우기
    chatLi.addClass(LR_className);
    chatLi.find('.sender span').text(senderName);
    chatLi.find('.message span').text(message);

    return chatLi;

}
