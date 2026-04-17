---
layout: default
title: "Математика — первый месяц календаря Дарго"
---

<style>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
  --ink:      #000000;
  --paper:    #ffffff;
  --accent:   #0969da;
  --border:   #000000;
  --week-bg:  #ddf4ff;
  --day-bg:   #f6f8fa;
  --hover-bg: #0969da;
  --hover-fg: #ffffff;
}

body {
  background: var(--paper);
  color: var(--ink);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  min-height: 100vh;
}

/* ── навигация ── */
.nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 40px;
  border-bottom: 1px solid var(--border);
  font-size: 14px;
}

.nav a {
  color: var(--accent);
  text-decoration: none;
  font-weight: 600;
}

.nav a:hover { text-decoration: underline; }

.nav-center {
  color: var(--ink);
  font-weight: 600;
}

/* ── заголовок ── */
.page-header {
  padding: 32px 40px 24px;
  border-bottom: 1px solid var(--border);
}

.calendar-title {
  font-size: 40px;
  font-weight: 800;
  line-height: 1;
  color: var(--ink);
  text-transform: uppercase;
  margin-bottom: 10px;
}

.month-title {
  font-size: 26px;
  font-weight: 600;
  line-height: 1.2;
  color: var(--ink);
}

.month-subtitle {
  font-size: 16px;
  font-weight: 400;
  color: var(--ink);
  margin-top: 4px;
}

/* ── основной блок ── */
.calendar-body {
  display: grid;
  grid-template-columns: 1fr 1fr;
  min-height: calc(100vh - 200px);
}

/* ── левая часть ── */
.left-panel {
  padding: 40px;
  border-right: 1px solid var(--border);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.left-text {
  font-size: 17px;
  font-weight: 400;
  line-height: 1.8;
  color: var(--ink);
}

.left-text p + p { margin-top: 1.2em; }

.left-footer {
  margin-top: 40px;
  font-size: 13px;
  font-weight: 600;
  color: var(--ink);
  text-transform: uppercase;
  border-top: 1px solid var(--border);
  padding-top: 16px;
}

/* ── правая часть ── */
.right-panel {
  padding: 40px;
}

/* ── сетка ── */
.grid {
  display: grid;
  grid-template-columns: 52px repeat(7, 1fr);
  gap: 4px;
}

/* заголовок дней */
.day-header {
  text-align: center;
  font-size: 13px;
  font-weight: 600;
  color: var(--ink);
  padding: 4px 0 10px;
  text-transform: uppercase;
}

.day-header a {
  color: var(--ink);
  text-decoration: none;
}

.day-header a:hover { color: var(--accent); }

/* номер недели */
.week-num {
  background: var(--week-bg);
  border-radius: 4px;
  border: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: center;
}

.week-num a {
  font-size: 20px;
  font-weight: 700;
  color: var(--ink);
  text-decoration: none;
}

.week-num a:hover { color: var(--accent); }

/* ячейка дня */
.day {
  background: var(--day-bg);
  border-radius: 4px;
  border: 1px solid var(--border);
  text-align: center;
  padding: 9px 2px 7px;
  cursor: default;
  transition: background 0.15s;
}

.day:hover { background: var(--hover-bg); }
.day:hover .d-new { color: var(--hover-fg); }
.day:hover .d-old { color: var(--hover-fg); }

.d-new {
  display: block;
  font-size: 20px;
  font-weight: 700;
  line-height: 1.1;
  color: var(--ink);
}

.d-old {
  display: block;
  font-size: 11px;
  font-weight: 400;
  color: var(--ink);
  margin-top: 2px;
}

.day.empty {
  background: transparent;
  border: none;
  pointer-events: none;
}

/* ── адаптив ── */
@media (max-width: 800px) {
  .calendar-body { grid-template-columns: 1fr; }
  .left-panel { border-right: none; border-bottom: 1px solid var(--border); }
  .nav { padding: 14px 20px; }
  .page-header { padding: 24px 20px 18px; }
  .left-panel, .right-panel { padding: 24px 20px; }
  .calendar-title { font-size: 34px; }
  .month-title { font-size: 20px; }
  .d-new { font-size: 16px; }
}
</style>

<div class="nav">
  <a href="https://dargomag.github.io/calendar/">← Нулевой день</a>
  <span class="nav-center">Календарь Дарго</span>
  <a href="https://dargomag.github.io/calendar/physics.html">Физика →</a>
</div>

<div class="page-header">
  <div class="calendar-title">Календарь Дарго</div>
  <div class="month-title">Математика — первый месяц календаря</div>
  <div class="month-subtitle">(22 декабря — 21 января по григорианскому календарю)</div>
</div>

<div class="calendar-body">

  <div class="left-panel">
    <div class="left-text">
      <p>Изначально слово «математика» на древнегреческом языке означало «изучение» или «наука».
      Оно исторически сложилось на основе измерения и описания природы — творений Бога.</p>
      <p>Современная математика не столько наука, сколько язык естественных наук, но широко
      используется в них как для точной формулировки их содержания, так и для получения
      новых результатов.</p>
      <p>Математика предоставляет язык другим наукам, тем самым выявляет
      их структурную взаимосвязь и способствует нахождению самых общих законов Вселенной —
      законов Бога.</p>
    </div>
    <div class="left-footer">I квартал · 31 день</div>
  </div>

  <div class="right-panel">
    <div class="grid" id="cal-grid"></div>
  </div>

</div>

<script>
(function () {
  // ── параметры месяца ─────────────────────────────────────────
  var DAYS_IN_MONTH = 31;
  var WEEK_START    = 1;
  var GREG_START_D  = 22;
  var GREG_START_M  = 12;
  var GREG_START_Y  = 2025;
  // ─────────────────────────────────────────────────────────────

  // Названия глав Путь Дарго по номеру недели
  var WEEK_TITLES = {
    1: 'Гунны',
    2: 'Голос',
    3: 'Бог и Вселенная',
    4: 'Божья воля',
    5: 'Добро и зло'
  };

  var MONTH_NAMES_RU = ['янв','фев','мар','апр','май','июн','июл','авг','сен','окт','ноя','дек'];
  var DAY_NAMES = ['ПН','ВТ','СР','ЧТ','ПТ','СБ','ВС'];
  var DAY_LINKS = ['mon','tue','wed','thu','fri','sat','sun'];
  var BASE = 'https://dargomag.github.io';

  function gregDate(dayIndex) {
    var d = new Date(GREG_START_Y, GREG_START_M - 1, GREG_START_D + dayIndex);
    return { d: d.getDate(), m: d.getMonth() };
  }

  var grid = document.getElementById('cal-grid');

  // строка-заголовок
  grid.appendChild(document.createElement('div'));

  DAY_NAMES.forEach(function (name, i) {
    var cell = document.createElement('div');
    cell.className = 'day-header';
    var a = document.createElement('a');
    a.href = BASE + '/calendar/' + DAY_LINKS[i] + '.html';
    a.textContent = name;
    cell.appendChild(a);
    grid.appendChild(cell);
  });

  // строки с днями
  var dayIndex = 0;
  for (var row = 0; row < 5; row++) {
    var weekNum = WEEK_START + row;
    var weekPad = String(weekNum).padStart(2, '0');

    var wCell = document.createElement('div');
    wCell.className = 'week-num';
    var wLink = document.createElement('a');
    wLink.href = BASE + '/path-dargo/' + weekPad + '.html';
    wLink.textContent = weekNum;
    if (WEEK_TITLES[weekNum]) {
      wLink.title = WEEK_TITLES[weekNum];
    }
    wCell.appendChild(wLink);
    grid.appendChild(wCell);

    for (var col = 0; col < 7; col++) {
      var cell = document.createElement('div');
      if (dayIndex < DAYS_IN_MONTH) {
        cell.className = 'day';
        var g = gregDate(dayIndex);
        var spanNew = document.createElement('span');
        spanNew.className = 'd-new';
        spanNew.textContent = dayIndex + 1;
        var spanOld = document.createElement('span');
        spanOld.className = 'd-old';
        spanOld.textContent = g.d + ' ' + MONTH_NAMES_RU[g.m];
        cell.appendChild(spanNew);
        cell.appendChild(spanOld);
        dayIndex++;
      } else {
        cell.className = 'day empty';
      }
      grid.appendChild(cell);
    }
  }
})();
</script>
