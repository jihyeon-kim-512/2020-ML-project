<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>AI 재무관리 프로젝트</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/2.2.0/socket.io.js"
        integrity="sha256-yr4fRk/GU1ehYJPAs8P4JlTgu0Hdsp4ZKrx8bDEDC3I="
        crossorigin="anonymous" charset='UTF-8'></script>
    <!-- CSS connect -->
    <link rel="stylesheet" href="{{ url_for('static', filename='css/input_form.css') }}">
    <!-- JS connect -->
    <script src="{{ url_for('static', filename='js/input_form.js') }}"></script>
</head>
<body>
  <header>
      <div class="title">AI 자산관리 프로젝트</div>
  </header>
  <form  method="post">
    <div class = "main">
        <div class = "form">
            <select name = "whatmoney" class="what_money" onclick="categoryChange(this)">
                {% if p1=='-1' %}
                <option>수집/지출 선택</option>
                <option value="a" selected>지출</option>
                <option value="b">수입</option>
                {% endif %}
                {% if p1=='1' %}
                <option>수집/지출 선택</option>
                <option value="a">지출</option>
                <option value="b" selected>수입</option>
                {% endif %}
            </select>
        <!-- 지출일 경우의 category-->

        <select name = "mcategory" class ="m_category" id="categorize">
          {% if p5 == '1' %}
          <option>의류</option>
          {% elif p5 == '2' %}
          <option>뷰티</option>
          {% elif p5 == '3' %}
          <option>생활비</option>
          {% elif p5 == '4' %}
          <option>여행</option>
          {% elif p5 == '5' %}
          <option>교통비</option>
          {% elif p5 == '6' %}
          <option>식비</option>
          {% elif p5 == '7' %}
          <option>월급</option>
          {% elif p5 == '8' %}
          <option>용돈</option>
          {% elif p5 == '9' %}
          <option>기타</option>
          {% else %}
          <option>서브 카테고리</option>
          {% endif %}
        </select>

            <input name="date" id ="date" class = "date" type="date" value={{p2}} /> <!-- 날짜 입력 폼 -->
            <input name="content" id ="content" class = "content" placeholder="항목 입력" value={{p3}} />
            <input name="money" id ="money" class = "money" placeholder="금액 입력" value={{p4}} />
            <center>
            <input id ="input_btn" class="input_btn" type="submit" formaction="http://localhost:5000/dbdelete/{{p6}}" value="삭제"/>
            <input id ="input_btn" class="input_btn" type="submit" formaction="http://localhost:5000/dbupdate/{{p6}}" value="수정"/>
          </center>
        </div>
    </div>
  </form>
</body>
</html>
