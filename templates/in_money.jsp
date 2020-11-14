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
    <div class="title">Ga Ge ViEW</div>
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
       onClick="location.href='#">
       <div style="width:40%; float:left; text-align: left; margin-left:9%;">
         <p style="margin-bottom:5px;">{{IM[i][2]}}</p>
         <p style="font-size: 12px;">{{IM[i][0]}}</p>
       </div>

       <div style="width:40%; height: 100%; display: flex;
       align-items: center; text-align:right; margin-right:9%;">
         <p style="width:100%;">{{IM[i][1]}}원</p>
       </div>
      </button>
     {% endfor %}
   </div>
    </div>
    </div >
  </div >

</body>
</html>
