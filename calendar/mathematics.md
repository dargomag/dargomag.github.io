Математика - первый месяц года

Изначально слово «математика» на древнегреческом языке означало «изучение» или «наука». Оно исторически сложилось на основе измерения и описания природы - творений Бога. 
Современная математика не столько наука, сколько язык естественных наук, но широко используется в них как для точной формулировки их содержания, так и для получения новых результатов. Математика предоставляет язык другим наукам, тем самым выявляет их структурную взаимосвязь и способствует нахождению самых общих законов Вселенной – законов Бога.


<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<title>Математика — Дарго календарь</title>

<style>
body {
    margin: 0;
    background: #f2f2f2;
    font-family: "Segoe UI", Arial, sans-serif;
}

.calendar {
    display: flex;
    max-width: 1100px;
    margin: 60px auto;
    background: #ffffff;
    box-shadow: 0 20px 50px rgba(0,0,0,0.08);
}

/* Левая часть */
.left {
    width: 55%;
    background: #0e1a22;
    color: rgba(255,255,255,0.08);
    display: flex;
    align-items: center;
    justify-content: center;
}

.math-pattern {
    font-size: 42px;
    line-height: 1.8;
    text-align: center;
}

/* Правая часть */
.right {
    width: 45%;
    padding: 30px 25px;
}

/* Заголовки */
.month-title {
    font-size: 30px;
    letter-spacing: 1px;
    margin-bottom: 5px;
}

.date-range {
    font-size: 13px;
    color: #777;
    margin-bottom: 25px;
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
    color: #888;
    letter-spacing: 1px;
}

/* номер недели */
.week-num {
    font-size: 11px;
    background: #e8e8e8;
    border-radius: 6px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #555;
}

/* дни */
.day {
    text-align: center;
    padding: 14px 0;
    font-size: 22px; /* увеличено примерно вдвое */
    background: #fafafa;
    border-radius: 6px;
    transition: 0.2s;
}

.day:hover {
    background: #1f3a4a;
    color: white;
}

/* пустые */
.empty {
    background: transparent;
}

/* адаптив */
@media (max-width: 800px) {
    .calendar {
        flex-direction: column;
    }
    .left, .right {
        width: 100%;
    }
}
</style>

</head>

<body>

<div class="calendar">

    <!-- Левая часть -->
    <div class="left">
        <div class="math-pattern">
            ∑<br>
            ∫<br>
            π<br>
            e^{iπ}+1=0
        </div>
    </div>

    <!-- Правая часть -->
    <div class="right">

        <div class="month-title">Математика</div>
        <div class="date-range">(22 декабря — 21 января по григорианскому стилю)</div>

        <div class="grid">

            <!-- заголовок -->
            <div></div>
            <div class="day-name">ПН</div>
            <div class="day-name">ВТ</div>
            <div class="day-name">СР</div>
            <div class="day-name">ЧТ</div>
            <div class="day-name">ПТ</div>
            <div class="day-name">СБ</div>
            <div class="day-name">ВС</div>

            <!-- неделя 1 -->
            <div class="week-num">1</div>
            <div class="day">1</div><div class="day">2</div><div class="day">3</div><div class="day">4</div><div class="day">5</div><div class="day">6</div><div class="day">7</div>

            <!-- неделя 2 -->
            <div class="week-num">2</div>
            <div class="day">8</div><div class="day">9</div><div class="day">10</div><div class="day">11</div><div class="day">12</div><div class="day">13</div><div class="day">14</div>

            <!-- неделя 3 -->
            <div class="week-num">3</div>
            <div class="day">15</div><div class="day">16</div><div class="day">17</div><div class="day">18</div><div class="day">19</div><div class="day">20</div><div class="day">21</div>

            <!-- неделя 4 -->
            <div class="week-num">4</div>
            <div class="day">22</div><div class="day">23</div><div class="day">24</div><div class="day">25</div><div class="day">26</div><div class="day">27</div><div class="day">28</div>

            <!-- неделя 5 -->
            <div class="week-num">5</div>
            <div class="day">29</div><div class="day">30</div><div class="day">31</div>
            <div class="empty"></div><div class="empty"></div><div class="empty"></div><div class="empty"></div>

        </div>

    </div>

</div>

</body>
</html>
