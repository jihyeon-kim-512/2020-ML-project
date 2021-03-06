<!DOCTYPE html>
<html lang="ko">
<head>
  <title>chat-main</title>
  <link rel="stylesheet" type="text/css" href="../static/css/money_detail.css">
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
     <button type="button" id="chart_btn"
      onclick="location.href='http://localhost:5000/piechart'">
       <img src="../static/image/chart_btn.png" style=" width : 35px; ">
     </button>
     <button type="button" id="new_btn"
      onClick="location.href='http://localhost:5000/inputform/'">
       <img src="../static/image/new_btn.png" style=" width : 35px; ">
     </button>
    </div>
	</header>

  <div class="show_main" >
    <div class="show_cnt">
      <div id="summ">
      <div class="scroll_box">
          {%for i in range(0, IM|length) %}
          {% set d = IM[i-1][0] %}
            {% if IM[i][0]!=d %}
            <p class="txt_date">{{IM[i][0]}}</p>
            {% endif %}
        <button type="button" id="money_btn" style="width:100%; height:70px;"
         onClick="location.href='http://localhost:5000/updateform/'+{{IM[i][4]}}
         +'/'+encodeURI('{{IM[i][0]}}','UTF-8')
         {% if IM[i][3] == '' %}
         +'/'+encodeURI('{{IM[i][2]}}','UTF-8')
         {% else %}
         +'/'+encodeURI('{{IM[i][3]}}','UTF-8')
         {% endif %}
         +'/'+{{IM[i][1]}}
         +'/'+{{IM[i][5]}}
         +'/'+{{IM[i][6]}}">
           <div style="width:40%; float:left; text-align: left; margin-left:9%;">
             {% if IM[i][3] == '' %}
             <p style="margin-bottom:5px;">{{IM[i][2]}}</p>
             {% else %}
             <p style="margin-bottom:5px;">{{IM[i][3]}}</p>
             {% endif %}
             <p style="font-size: 12px;">{{IM[i][0]}}</p>
           </div>

           <div style="width:40%; height: 100%; display: flex;
           align-items: center; text-align:right; margin-right:9%;">
           {% if IM[i][4]==1 %}
             <p style="width:100%; color:#0914e6;">{{IM[i][1]}}원</p>
            {% elif IM[i][4]==-1 %}
             <p style="width:100%;">- {{IM[i][1]}}원</p>
             {% endif %}
           </div>
        </button>

       {% endfor %}
               </div>
    </div>
    </div >
  </div >

</body>
</html>
