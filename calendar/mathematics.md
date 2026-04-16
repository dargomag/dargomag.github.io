<html lang="ru">
<head>
<meta charset="UTF-8">
<title>Математика — первый месяц года</title>

<style>
body {
    margin: 0;
    background: #f2f2f2;
    font-family: "Segoe UI", Arial, sans-serif;
}

.wrapper {
    max-width: 1100px;
    margin: 40px auto;
}

/* Заголовок */
.header {
    font-size: 28px;
    margin-bottom: 15px;
}

/* Контейнер */
.calendar {
    display: flex;
    background: white;
    box-shadow: 0 20px 50px rgba(0,0,0,0.08);
}

/* Левая часть */
.left {
    width: 55%;
    padding: 30px;
    color: #ffffff;
    line-height: 1.6;

    background:
        linear-gradient(rgba(0,0,0,0.55), rgba(0,0,0,0.55)),
        url('https://images.unsplash.com/photo-1483664852095-d6cc6870702d?q=80&w=1200');
    background-size: cover;
    background-position: center;
}

.text {
    font-size: 15px;
}

/* Правая часть */
.right {
    width: 45%;
    padding: 25px;
}

/* Сетка */
.grid {
    display: grid;
    grid-template-columns: 45px repeat(7, 1fr);
    gap: 6px;
}

/* дни недели */
.day-name {
    font-size: 11px;
    text-align: center;
}

.day-name a {
    text-decoration: none;
    color: #555;
}

.day-name a:hover {
    text-decoration: underline;
}

/* номер недели */
.week-num {
    font-size: 11px;
    background: #e8e8e8;
    border-radius: 6px;
    display: flex;
    align-items: center;
    justify-content: center;
}

/* дни */
.day {
    background: #fafafa;
    border-radius: 6px;
    text-align: center;
    padding: 8px 0;
    line-height: 1.2;
}

.day:hover {
    background: #1f3a4a;
    color: white;
}

/* дробь */
.top {
    font-size: 22px;
    display: block;
}

.bottom {
    font-size: 11px;
    color: #777;
}

/* пустые */
.empty {
    background: transparent;
}
</style>

</head>

<body>

<div class="wrapper">

<div class="header">Математика — первый месяц года</div>

<div class="calendar">

    <!-- Левая часть -->
    <div class="left">
        <div class="text">
        Изначально слово «математика» на древнегреческом языке означало «изучение» или «наука». 
        Оно исторически сложилось на основе измерения и описания природы — творений Бога. 
        Современная математика не столько наука, сколько язык естественных наук, но широко 
        используется в них как для точной формулировки их содержания, так и для получения 
        новых результатов. Математика предоставляет язык другим наукам, тем самым выявляет 
        их структурную взаимосвязь и способствует нахождению самых общих законов Вселенной — 
        законов Бога.
        </div>
    </div>

    <!-- Правая часть -->
    <div class="right">

        <div class="grid">

            <!-- заголовок -->
            <div></div>
            <div class="day-name"><a href="mon.html">ПН</a></div>
            <div class="day-name"><a href="tue.html">ВТ</a></div>
            <div class="day-name"><a href="wed.html">СР</a></div>
            <div class="day-name"><a href="thu.html">ЧТ</a></div>
            <div class="day-name"><a href="fri.html">ПТ</a></div>
            <div class="day-name"><a href="sat.html">СБ</a></div>
            <div class="day-name"><a href="sun.html">ВС</a></div>

            <!-- неделя 1 -->
            <div class="week-num">1</div>
            <div class="day"><span class="top">1</span><span class="bottom">22</span></div>
            <div class="day"><span class="top">2</span><span class="bottom">23</span></div>
            <div class="day"><span class="top">3</span><span class="bottom">24</span></div>
            <div class="day"><span class="top">4</span><span class="bottom">25</span></div>
            <div class="day"><span class="top">5</span><span class="bottom">26</span></div>
            <div class="day"><span class="top">6</span><span class="bottom">27</span></div>
            <div class="day"><span class="top">7</span><span class="bottom">28</span></div>

            <!-- неделя 2 -->
            <div class="week-num">2</div>
            <div class="day"><span class="top">8</span><span class="bottom">29</span></div>
            <div class="day"><span class="top">9</span><span class="bottom">30</span></div>
            <div class="day"><span class="top">10</span><span class="bottom">31</span></div>
            <div class="day"><span class="top">11</span><span class="bottom">1</span></div>
            <div class="day"><span class="top">12</span><span class="bottom">2</span></div>
            <div class="day"><span class="top">13</span><span class="bottom">3</span></div>
            <div class="day"><span class="top">14</span><span class="bottom">4</span></div>

            <!-- неделя 3 -->
            <div class="week-num">3</div>
            <div class="day"><span class="top">15</span><span class="bottom">5</span></div>
            <div class="day"><span class="top">16</span><span class="bottom">6</span></div>
            <div class="day"><span class="top">17</span><span class="bottom">7</span></div>
            <div class="day"><span class="top">18</span><span class="bottom">8</span></div>
            <div class="day"><span class="top">19</span><span class="bottom">9</span></div>
            <div class="day"><span class="top">20</span><span class="bottom">10</span></div>
            <div class="day"><span class="top">21</span><span class="bottom">11</span></div>

            <!-- неделя 4 -->
            <div class="week-num">4</div>
            <div class="day"><span class="top">22</span><span class="bottom">12</span></div>
            <div class="day"><span class="top">23</span><span class="bottom">13</span></div>
            <div class="day"><span class="top">24</span><span class="bottom">14</span></div>
            <div class="day"><span class="top">25</span><span class="bottom">15</span></div>
            <div class="day"><span class="top">26</span><span class="bottom">16</span></div>
            <div class="day"><span class="top">27</span><span class="bottom">17</span></div>
            <div class="day"><span class="top">28</span><span class="bottom">18</span></div>

            <!-- неделя 5 -->
            <div class="week-num">5</div>
            <div class="day"><span class="top">29</span><span class="bottom">19</span></div>
            <div class="day"><span class="top">30</span><span class="bottom">20</span></div>
            <div class="day"><span class="top">31</span><span class="bottom">21</span></div>
            <div class="empty"></div><div class="empty"></div><div class="empty"></div><div class="empty"></div>

        </div>

    </div>

</div>

</div>

</body>
</html>
