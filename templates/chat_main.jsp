<!DOCTYPE html>
<html lang="ko">
<head>
  <title>chat-main</title>
  <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/chat_main.css') }}">
	<script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/2.2.0/socket.io.js"
        integrity="sha256-yr4fRk/GU1ehYJPAs8P4JlTgu0Hdsp4ZKrx8bDEDC3I="
        crossorigin="anonymous" charset='UTF-8'></script>
</head>
<body>
  <header>
    <div class="title_head">
    <div class="title">
      <button type="button" id="home_btn"
      onClick="location.href='http://localhost:5000/chatmain/'">AI 자산관리 프로젝트</button>
     </div>
      <button type="button" id="st_btn"
       onclick="location.href='http://localhost:5000/chatsetting'">
        <img src="../static/image/setting_btn.png" style=" width : 35px; ">
      </button>
    </div>
	</header>

  <div class="show_main">
    <div class="show_cnt">
      <div id="summ">

        <button type="button" id="money_btn" style="width:80%; height:70px;"
         onClick="location.href='http://localhost:5000/summoney'">
         {% if moneySum == None %}
           {% if iMoney == None %}
           <p><b>합계: </b> {{0-eMoney}} 원</p>
           {% elif eMoney == None %}
           <p><b>합계: </b> {{iMoney-0}} 원</p>
           {% else %}
           <p><b>합계: </b> 0 원</p>
           {% endif %}
         {% else %}
         <p><b>합계: </b> {{moneySum}} 원</p>
         {% endif %}
        </button>
        <button type="button" id="money_btn" style="width:80%; height:70px;"
         onClick="location.href='http://localhost:5000/inmoney'">
         {% if iMoney == None %}
         <p><b>수입: </b> 0 원</p>
         {% else %}
         <p><b>수입: </b> {{iMoney}} 원</p>
         {% endif %}
        </button>
        <button type="button" id="money_btn" style="width:80%; height:70px;"
         onClick="location.href='http://localhost:5000/exmoney'">
         {% if eMoney == None %}
         <p><b>지출: </b> 0 원</p>
         {% else %}
         <p><b>지출: </b> {{eMoney}} 원</p>
         {% endif %}
        </button>

      </div>
    </div>
  </div>
  <div class="show_main">
    <div id="money_notice">
      {% if limit != None %}
        {% if limit < eMoney %}
        <p>
          목표지출액 {{limit}}원에서 {{limit-eMoney}}원 넘어섰습니다 (｡•́︿•̀｡)
        </p>
        {% elif limit*0.4 < (limit-eMoney) %}
        <p>
          목표지출액은 {{limit}}원 입니다. 남은 금액은 {{limit-eMoney}}원 입니다.<br/>
          잘하고 있어요! (๑و•̀Δ•́)و
        </p>
        {% else %}
        <p>
          목표지출액은 {{limit}}원 입니다. 남은 금액은 {{limit-eMoney}}원 입니다.<br/>
          자제하세요 ヽ(ಠ_ಠ)ノ
        </p>
        {% endif %}
      {% else %}
      <p>
        목표지출액을 설정하시면 경고 알림을 드립니다 ✧*.◟(ˊᗨˋ)◞.*✧
      </p>
      {% endif %}
    </div>
  </div>
  <div class="show_main">
    <div class="show_btn">
      <button type="button" id="page_btn" style=" margin-right: 3%; "
       onClick="location.href='http://localhost:5000/chatimage'">
        <img src="../static/image/image_btn.png" style="width:220px;">
      </button>
      <button type="button" id="page_btn"
       onClick="location.href='http://localhost:5000/chatbot'">
        <img src="../static/image/chat_btn.png" style="width:220px;">
      </button>
    </div>
  </div>

</body>
</html>
