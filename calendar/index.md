---
title: Календарь
---
## Календарь Дарго

Если вас не смущает, что названия первых месяцев действующего григорианского календаря уводят к языческим временам, а девятый месяц называется седьмым (сент - семь), десятый - восьмым (окта - восемь), одиннадцатый - девятым (нов - девять), двенадцатый - десятым (дека - десять) - можете дальше не читать. ))

По календарю Дарго́ День зимнего солнцестояния – нулевой день календаря. Новый год начинается на следующий день после зимнего солнцестояния. 365 дней (366 в високосный год) разделены на четыре квартала по 91 дню, в свою очередь поделенных на один месяц 31 день и два месяца по 30 дней. Плюс один нулевой день (два дня в високосный год). Каждый квартал начинается с понедельника 01 числа. Каждая неделя из 52 посвящена одной главе [Пути Дарго](https://dargomag.github.io/path-dargo/)

0. [Нулевой День](zero.md) – (21 декабря)   
1. [Математика](mathematics.md) 	(22 Декабрь - 21 Январь)
2. [Физика](physics.md)	(22 Январь – 20 Февраль)
3. [Химия](chemistry.md)		(21 Февраль – 22 Март)
4. [Ботаника](botany.md)		(23 Март – 22 Апрель)
5. [Зоология](zoology.md)		(23 Апрель – 22 Май)
6. [Антропология](anthropology.md)	(23 Май – 21 Июнь)
7. [История](history.md)		(22 Июнь – 22 Июль)
8. [Психология](psychology.md)	(23 Июль – 21 Август)
9. [Экология](ecology.md)		(22 Август – 20 Сентябрь)     
10. [Культура](culture.md)		(21 Сентябрь – 21 Октябрь)
11. [Поэзия](poetry.md)		(22 Октябрь – 20 Ноябрь) 
12. [Музыка](music.md)		(21 Ноябрь – 20 Декабрь)  

Летоисчисление календаря Дарго начинается 12 000 лет назад - с началом Голоцена, текущего межледникового периода. С Голоценом началось и развитие нашей цивилизации, о чем свидетельствуют археологические раскопки Гёбекли-тепе.
При создании календаря учтены разработки Густава Армелина.  

## Каждый уважающий себя народ имеет свой календарь для себя. А каждый великий народ имеет такой календарь, которым захотят воспользоваться все народы. 


<!-- ══════════════════════════════════════════════
     КОНВЕРТЕР ДАТ — вставить в начало index.md
     ══════════════════════════════════════════════ -->

<style>
.conv-wrap {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  max-width: 900px;
  margin: 32px auto;
  border: 1px solid #000;
  padding: 24px 28px 28px;
  box-sizing: border-box;
}

.conv-title {
  font-size: 13px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin-bottom: 20px;
  color: #000;
}

.conv-row {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  gap: 20px;
  align-items: start;
}

.conv-block-title {
  font-size: 12px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: #000;
  margin-bottom: 8px;
}

.conv-fields {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  align-items: flex-end;
}

.conv-field-group {
  display: flex;
  flex-direction: column;
  gap: 3px;
}

.conv-field-group label {
  font-size: 10px;
  color: #000;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.conv-field-group.f-day   { width: 48px; }
.conv-field-group.f-month { width: 110px; }
.conv-field-group.f-year  { width: 72px; }
.conv-field-group.f-era   { width: 56px; }

.conv-fields input,
.conv-fields select {
  font-family: inherit;
  font-size: 14px;
  padding: 6px 7px;
  border: 1px solid #000;
  background: #f6f8fa;
  color: #000;
  width: 100%;
  box-sizing: border-box;
  -webkit-appearance: none;
  appearance: none;
}

.conv-fields select {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='10' height='6'%3E%3Cpath d='M0 0l5 6 5-6z' fill='%23000'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 6px center;
  padding-right: 20px;
}

input[disabled], select[disabled] {
  background: #e8e8e8 !important;
  color: #888 !important;
}

.conv-btn-wrap {
  display: flex;
  align-items: center;
  justify-content: center;
  padding-top: 26px;
}

.conv-btn {
  font-family: inherit;
  font-size: 13px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  background: #000;
  color: #fff;
  border: none;
  padding: 10px 16px;
  cursor: pointer;
  white-space: nowrap;
}

.conv-btn:hover { background: #0969da; }

.conv-result {
  margin-top: 16px;
  padding: 14px 20px;
  border: 1px solid #000;
  background: #fff;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 16px;
  min-height: 52px;
  text-align: center;
}

.conv-result-item {
  display: flex;
  flex-direction: column;
  gap: 3px;
}

.conv-result-label {
  font-size: 10px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: #555;
}

.conv-result-value {
  font-size: 16px;
  font-weight: 700;
  color: #000;
}

.conv-equals {
  font-size: 24px;
  font-weight: 300;
  color: #000;
  line-height: 1;
  padding-top: 12px;
}

.conv-hint {
  margin-top: 8px;
  font-size: 12px;
  color: #cc0000;
  font-weight: 600;
  min-height: 16px;
}

/* ── Мобильная версия ── */
@media (max-width: 600px) {
  .conv-wrap {
    margin: 16px 8px;
    padding: 18px 16px 20px;
  }

  .conv-row {
    grid-template-columns: 1fr;
    gap: 16px;
  }

  .conv-btn-wrap {
    padding-top: 0;
  }

  .conv-btn {
    width: 100%;
    padding: 12px;
  }

  .conv-field-group.f-day   { width: 48px; }
  .conv-field-group.f-month { width: calc(100% - 48px - 70px - 78px - 18px); min-width: 120px; }
  .conv-field-group.f-year  { width: 70px; }
  .conv-field-group.f-era   { width: 78px; }

  .conv-result {
    flex-direction: column;
    gap: 8px;
  }

  .conv-equals {
    padding-top: 0;
  }

  .conv-result-value {
    font-size: 14px;
  }
}
</style>

<div class="conv-wrap">
  <div class="conv-title">Конвертер дат от начала человеческой цивилизации</div>

  <div class="conv-row">

    <!-- ГК -->
    <div class="conv-block">
      <div class="conv-block-title">Григорианский календарь</div>
      <div class="conv-fields">
        <div class="conv-field-group f-day">
          <label>Число</label>
          <input type="number" id="gk-day" min="1" max="31" placeholder="1">
        </div>
        <div class="conv-field-group f-month">
          <label>Месяц</label>
          <select id="gk-month">
            <option value="1">Январь</option>
            <option value="2">Февраль</option>
            <option value="3">Март</option>
            <option value="4">Апрель</option>
            <option value="5">Май</option>
            <option value="6">Июнь</option>
            <option value="7">Июль</option>
            <option value="8">Август</option>
            <option value="9">Сентябрь</option>
            <option value="10">Октябрь</option>
            <option value="11">Ноябрь</option>
            <option value="12">Декабрь</option>
          </select>
        </div>
        <div class="conv-field-group f-year">
          <label>Год</label>
          <input type="number" id="gk-year" placeholder="2026">
        </div>
        <div class="conv-field-group f-era">
          <label>Эра</label>
          <select id="gk-era">
            <option value="ce">н.э.</option>
            <option value="bce">до н.э.</option>
          </select>
        </div>
      </div>
    </div>

    <!-- Кнопка -->
    <div class="conv-btn-wrap">
      <button class="conv-btn" onclick="convertDate()">Конвертировать</button>
    </div>

    <!-- КД -->
    <div class="conv-block">
      <div class="conv-block-title">Календарь Дарго</div>
      <div class="conv-fields">
        <div class="conv-field-group f-day">
          <label>Число</label>
          <input type="number" id="kd-day" min="0" max="31" placeholder="1">
        </div>
        <div class="conv-field-group f-month">
          <label>Месяц</label>
          <select id="kd-month" onchange="kdMonthChanged()">
            <option value="0">Нулевой день</option>
            <option value="0r">День радости</option>
            <option value="1">Математика</option>
            <option value="2">Физика</option>
            <option value="3">Химия</option>
            <option value="4">Ботаника</option>
            <option value="5">Зоология</option>
            <option value="6">Антропология</option>
            <option value="7">История</option>
            <option value="8">Психология</option>
            <option value="9">Экология</option>
            <option value="10">Культура</option>
            <option value="11">Поэзия</option>
            <option value="12">Музыка</option>
          </select>
        </div>
        <div class="conv-field-group f-year">
          <label>Год КД</label>
          <input type="number" id="kd-year" min="1" placeholder="12026">
        </div>
        <div class="conv-field-group f-era">
          <label>Эра</label>
          <input type="text" value="КД" disabled>
        </div>
      </div>
    </div>

  </div>

  <div class="conv-hint" id="conv-hint"></div>

  <div class="conv-result">
    <div class="conv-result-item">
      <span class="conv-result-label">Григорианский календарь</span>
      <span class="conv-result-value" id="res-gk">—</span>
    </div>
    <div class="conv-equals">=</div>
    <div class="conv-result-item">
      <span class="conv-result-label">Календарь Дарго</span>
      <span class="conv-result-value" id="res-kd">—</span>
    </div>
  </div>
</div>

<script>
(function () {

  var KD_MONTHS = [
    null,
    ['Математика',   31,   0],
    ['Физика',       30,  31],
    ['Химия',        30,  61],
    ['Ботаника',     31,  91],
    ['Зоология',     30, 122],
    ['Антропология', 30, 152],
    ['История',      31, 182],
    ['Психология',   30, 213],
    ['Экология',     30, 243],
    ['Культура',     31, 273],
    ['Поэзия',       30, 304],
    ['Музыка',       30, 334]
  ];

  var GK_MONTHS_RU = ['января','февраля','марта','апреля','мая','июня',
                       'июля','августа','сентября','октября','ноября','декабря'];

  // Опорная точка: Нулевой день 12 026 КД = 21 декабря 2025 ГК
  var ANCHOR_MS      = Date.UTC(2025, 11, 21);
  var ANCHOR_KD_YEAR = 12026;

  function isLeapGK(y) {
    return (y % 4 === 0 && y % 100 !== 0) || (y % 400 === 0);
  }

  // Год КД Y високосный если в нём есть 29 февраля ГК
  // Год КД Y охватывает февраль григорианского года Y - 10000
  function isLeapKD(y) {
    return isLeapGK(y - 10000);
  }

  function kdYearLen(y) {
    return isLeapKD(y) ? 366 : 365;
  }

  function gkToDays(utcMs) {
    return Math.round((utcMs - ANCHOR_MS) / 86400000);
  }

  function daysToKD(totalDays) {
    var kdYear = ANCHOR_KD_YEAR;
    var d = totalDays;

    if (d >= 0) {
      while (true) {
        var ylen = kdYearLen(kdYear);
        if (d < ylen) break;
        d -= ylen;
        kdYear++;
      }
    } else {
      while (d < 0) {
        kdYear--;
        d += kdYearLen(kdYear);
      }
    }

    var leap = isLeapKD(kdYear);
    var ylen = kdYearLen(kdYear);

    if (d === 0) return { type: 'zero', year: kdYear };
    if (leap && d === ylen - 1) return { type: 'joy', year: kdYear };

    var dayInMonths = d;
    for (var m = 1; m <= 12; m++) {
      var mlen = KD_MONTHS[m][1];
      if (dayInMonths <= mlen) {
        return { type: 'normal', month: m, day: dayInMonths, year: kdYear };
      }
      dayInMonths -= mlen;
    }
    return null;
  }

  function kdToDays(kdYear, monthVal, day) {
    var days = 0;
    if (kdYear >= ANCHOR_KD_YEAR) {
      for (var y = ANCHOR_KD_YEAR; y < kdYear; y++) days += kdYearLen(y);
    } else {
      for (var y = kdYear; y < ANCHOR_KD_YEAR; y++) days -= kdYearLen(y);
    }
    if (monthVal === '0')  return days;
    if (monthVal === '0r') return days + kdYearLen(kdYear) - 1;
    var m = parseInt(monthVal);
    return days + 1 + KD_MONTHS[m][2] + (day - 1);
  }

  function formatGK(utcMs) {
    var d    = new Date(utcMs);
    var day  = d.getUTCDate();
    var mon  = d.getUTCMonth();
    var yr   = d.getUTCFullYear();
    if (yr <= 0) {
      // Астрономический год 0 = 1 до н.э., -1 = 2 до н.э. и т.д.
      return day + ' ' + GK_MONTHS_RU[mon] + ' ' + (1 - yr) + ' до н.э. ГК';
    }
    return day + ' ' + GK_MONTHS_RU[mon] + ' ' + yr + ' н.э. ГК';
  }

  function fmtYear(y) {
    var s = String(y);
    return s.length > 3 ? s.slice(0, -3) + '\u00a0' + s.slice(-3) : s;
  }

  function formatKD(kd) {
    if (!kd) return '—';
    var yr = fmtYear(kd.year);
    if (kd.type === 'zero') return 'Нулевой день ' + yr + ' КД';
    if (kd.type === 'joy')  return 'День радости ' + yr + ' КД';
    return kd.day + ' ' + KD_MONTHS[kd.month][0] + ' ' + yr + ' КД';
  }

  function fillGKFields(utcMs) {
    var d = new Date(utcMs);
    var yr = d.getUTCFullYear();
    if (yr <= 0) {
      document.getElementById('gk-day').value   = d.getUTCDate();
      document.getElementById('gk-month').value = d.getUTCMonth() + 1;
      document.getElementById('gk-year').value  = 1 - yr;
      document.getElementById('gk-era').value   = 'bce';
    } else {
      document.getElementById('gk-day').value   = d.getUTCDate();
      document.getElementById('gk-month').value = d.getUTCMonth() + 1;
      document.getElementById('gk-year').value  = yr;
      document.getElementById('gk-era').value   = 'ce';
    }
  }

  function fillKDFields(kd) {
    if (!kd) return;
    var dayField = document.getElementById('kd-day');
    if (kd.type === 'zero') {
      document.getElementById('kd-month').value = '0';
      dayField.value    = 0;
      dayField.disabled = true;
    } else if (kd.type === 'joy') {
      document.getElementById('kd-month').value = '0r';
      dayField.value    = 0;
      dayField.disabled = true;
    } else {
      document.getElementById('kd-month').value = kd.month;
      dayField.value    = kd.day;
      dayField.disabled = false;
    }
    document.getElementById('kd-year').value = kd.year;
  }

  function showResult(utcMs, kd) {
    document.getElementById('res-gk').textContent = formatGK(utcMs);
    document.getElementById('res-kd').textContent = formatKD(kd);
  }

  function initToday() {
    var now   = new Date();
    var utcMs = Date.UTC(now.getFullYear(), now.getMonth(), now.getDate());
    var days  = gkToDays(utcMs);
    var kd    = daysToKD(days);
    fillGKFields(utcMs);
    fillKDFields(kd);
    showResult(utcMs, kd);
  }

  window.kdMonthChanged = function () {
    var val      = document.getElementById('kd-month').value;
    var dayField = document.getElementById('kd-day');
    if (val === '0' || val === '0r') {
      dayField.value    = 0;
      dayField.disabled = true;
    } else {
      dayField.disabled = false;
    }
  };

  window.convertDate = function () {
    var hint = document.getElementById('conv-hint');
    hint.textContent = '';

    var gkDay  = parseInt(document.getElementById('gk-day').value);
    var gkMon  = parseInt(document.getElementById('gk-month').value);
    var gkYear = parseInt(document.getElementById('gk-year').value);
    var gkEra  = document.getElementById('gk-era').value;

    var kdDay  = parseInt(document.getElementById('kd-day').value) || 1;
    var kdMon  = document.getElementById('kd-month').value;
    var kdYear = parseInt(document.getElementById('kd-year').value);

    var useGK = !!(gkDay && gkMon && gkYear);

    if (!useGK && !kdYear) return;

    if (useGK) {
      // Перевод года ГК в астрономический (до н.э.: 1 до н.э. = год 0, 2 до н.э. = год -1)
      var astroYear = (gkEra === 'bce') ? (1 - gkYear) : gkYear;
      var utcMs = Date.UTC(astroYear, gkMon - 1, gkDay);
      // Date.UTC не корректно для отрицательных лет, используем setUTCFullYear
      var tmp = new Date(0);
      tmp.setUTCFullYear(astroYear, gkMon - 1, gkDay);
      utcMs = tmp.getTime();

      var days = gkToDays(utcMs);
      var kd   = daysToKD(days);

      if (kd && kd.year < 9000) {
        hint.textContent = 'Нахрена козе баян?';
      }

      fillKDFields(kd);
      showResult(utcMs, kd);

    } else {
      // КД → ГК
      if (kdYear < 9000) {
        hint.textContent = 'Нахрена козе баян?';
      }

      var days  = kdToDays(kdYear, kdMon, kdDay);
      var utcMs = ANCHOR_MS + days * 86400000;

      fillGKFields(utcMs);
      showResult(utcMs, daysToKD(days));
    }
  };

  initToday();

})();
</script>

<!-- ══════════════════════════════════════════════
     КОНЕЦ КОНВЕРТЕРА
     ══════════════════════════════════════════════ -->
