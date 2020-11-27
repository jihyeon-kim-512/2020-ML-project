<!DOCTYPE html>
<html lang="en">
<head>
    <title>chat-setting</title>
    <link rel="stylesheet" type="text/css" href="../static/css/chat_setting.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/2.2.0/socket.io.js"
            integrity="sha256-yr4fRk/GU1ehYJPAs8P4JlTgu0Hdsp4ZKrx8bDEDC3I="
            crossorigin="anonymous" charset='UTF-8'></script>
        <script src="{{ url_for('static', filename = 'js/waring_modal.js') }}"></script>

</head>

<body>
    <script>
      var a = '{{ limit }}';
    </script>
    <header>
      <div class="title_head">
      <div class="title">
        <button type="button" id="home_btn"
        onClick="location.href='http://localhost:5000/chatmain/'">AI 자산관리 프로젝트</button>
       </div>
     </div>
    </header>
    <form action="/limitmoney/" method="post">
    <div class="wrapper">
      <ul>
        <li>
            <button type="button" id="page_btn" onclick="location.href='http://localhost:5000/chatmember'">
              <div class="box">
              <p>개인정보 수정 및 탈퇴</p>
              </div>
            </button>
        </li>
        <li>
          <div class="box">
            <span>경고알림</span>
            <div style="width:420px; height:80px; margin-top:-80px; padding-left: 83%; padding-top: 23px;">
              {% if limit != None %}
              <label class="switch"><input type="checkbox" checked onclick="toggleclick()"><span class="slider round"></span></label>
              {% else %}
              <label class="switch"><input type="checkbox" onclick="toggleclick()"><span class="slider round"></span></label>
              {% endif %}
            </div>
            <div class="get_money_contents">
              <ul>
                <li>
                  <label><b>금액입력칸</b></label>
                </li>
                <li>
                  <span>목표지출액: </span>
                  {% if limit != None %}
                  <input type="text" name="limit" style="height:30px;" value={{limit}}>
                  {% else %}
                  <input type="text" name="limit" style="height:30px;">
                  {% endif %}
                </li>
                <li>
                  <button type="submit" id="accept">확인</button>
                </li>
              </ul>
            </div>
          </div>
        </li>
        <li>
            <button type="button" id="page_btn" onclick="location.href='http://localhost:5000/excelExport'">
              <div class="box">
              <p>엑셀 내보내기</p>
              </div>
            </button>
        </li>
        <li>
            <button type="button" id="page_btn" onclick="location.href='http://localhost:5000/logout'">
              <div class="box">
              <p>로그아웃</p>
              </div>
            </button>
        </li>
      </ul>
    </div>

  </form>

  </body>
</html>
