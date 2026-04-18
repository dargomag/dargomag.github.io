---
title: Календарь
---

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

/* Поля в строку, каждое — своей ширины */
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

/* Ширины полей */
.conv-field-group.f-day   { width: 50px; }
.conv-field-group.f-month { width: 120px; }
.conv-field-group.f-year  { width: 60px; }
.conv-field-group.f-era   { width: 60px; }

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
  background: #e8e8e8;
  color: #888;
}

/* Кнопка */
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

/* Результат */
.conv-result {
  margin-top: 16px;
  padding: 14px 16px;
  border: 1px solid #000;
  background: #fff;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 48px;
  min-height: 52px;
  text-align: center;
}

.conv-result-label {
  font-size: 10px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: #555;
  display: block;
  margin-bottom: 4px;
}

.conv-result-value {
  font-size: 16px;
  font-weight: 700;
  color: #000;
  display: block;
}

.conv-hint {
  margin-top: 8px;
  font-size: 12px;
  color: #cc0000;
  font-weight: 600;
  min-height: 16px;
}
</style>

<div class="conv-wrap">
  <div class="conv-title">Конвертер дат</div>

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
          <input type="number" id="gk-year" min="1" placeholder="2026">
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

  <div class="conv-result" id="conv-result">
    <div>
      <span class="conv-result-label">Григорианский календарь</span>
      <span class="conv-result-value" id="res-gk">—</span>
    </div>
   <div style="font-size:24px; font-weight:700; align-self:center;">=</div> 
    <div>
      <span class="conv-result-label">Календарь Дарго</span>
      <span class="conv-result-value" id="res-kd">—</span>
    </div>
  </div>
</div>

<script>
(function () {

  // ── Данные месяцев КД ────────────────────────────────────────
  // [название, дней, смещение от 1 Математики в днях (0-based)]
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
  // (год КД 12026 начинается Нулевым днём 21 дек 2025)
  var ANCHOR_GK_MS   = Date.UTC(2025, 11, 21); // 21 декабря 2025
  var ANCHOR_KD_YEAR = 12026;

  // ── Вспомогательные функции ──────────────────────────────────

  function isLeapGK(y) {
    return (y % 4 === 0 && y % 100 !== 0) || (y % 400 === 0);
  }

  // Год КД является високосным если внутри него есть 29 февраля ГК.
  // Год КД Y начинается 21 дек (Y-10025 год ГК) и охватывает февраль (Y-10024 год ГК).
  // Пример: 12026 КД начинается 21 дек 2025 ГК, февраль внутри — 2026 ГК.
  // 12026 - 10000 = 2026 ✓
  function isLeapKD(kdY) {
    var gkFebYear = kdY - 10000;
    return isLeapGK(gkFebYear);
  }

  // Длина года КД в днях
  function kdYearLen(kdY) {
    return isLeapKD(kdY) ? 366 : 365;
  }

  // Дата ГК (Date объект, UTC) → смещение в днях от опорной точки
  function gkToDays(utcMs) {
    return Math.round((utcMs - ANCHOR_GK_MS) / 86400000);
  }

  // Смещение в днях → объект даты КД
  // день 0 = Нулевой день 12026 КД
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

    // d — день внутри года КД (0 = Нулевой день, 1..364/365 = месяцы, последний = День радости если високосный)
    var leap  = isLeapKD(kdYear);
    var ylen  = kdYearLen(kdYear);

    if (d === 0) return { type: 'zero', year: kdYear };
    if (leap && d === ylen - 1) return { type: 'joy', year: kdYear };

    // d=1..364 → месяцы
    var dayInMonths = d; // 1-based
    for (var m = 1; m <= 12; m++) {
      var mlen = KD_MONTHS[m][1];
      if (dayInMonths <= mlen) {
        return { type: 'normal', month: m, day: dayInMonths, year: kdYear };
      }
      dayInMonths -= mlen;
    }
    return null;
  }

  // Объект даты КД → смещение в днях от опорной точки
  function kdToDays(kdYear, monthVal, day) {
    // Количество дней от опорной точки до Нулевого дня kdYear
    var days = 0;
    if (kdYear >= ANCHOR_KD_YEAR) {
      for (var y = ANCHOR_KD_YEAR; y < kdYear; y++) days += kdYearLen(y);
    } else {
      for (var y = kdYear; y < ANCHOR_KD_YEAR; y++) days -= kdYearLen(y);
    }
    // days = смещение Нулевого дня kdYear
    if (monthVal === '0')  return days;
    if (monthVal === '0r') return days + kdYearLen(kdYear) - 1;
    var m = parseInt(monthVal);
    return days + 1 + KD_MONTHS[m][2] + (day - 1);
  }

  // Форматирование даты ГК
  function formatGK(utcMs) {
    var d = new Date(utcMs);
    var day  = d.getUTCDate();
    var mon  = d.getUTCMonth();
    var year = d.getUTCFullYear();
    return day + ' ' + GK_MONTHS_RU[mon] + ' ' + year + ' н.э. ГК';
  }

  // Год КД с пробелом-разделителем тысяч
  function fmtYear(y) {
    var s = String(y);
    return s.length > 3 ? s.slice(0, -3) + '\u00a0' + s.slice(-3) : s;
  }

  // Форматирование даты КД
  function formatKD(kd) {
    if (!kd) return '—';
    var yr = fmtYear(kd.year);
    if (kd.type === 'zero') return 'Нулевой день ' + yr + ' КД';
    if (kd.type === 'joy')  return 'День радости ' + yr + ' КД';
    return kd.day + ' ' + KD_MONTHS[kd.month][0] + ' ' + yr + ' КД';
  }

  // Показать результат
  function showResult(gkMs, kd) {
    document.getElementById('res-gk').textContent = formatGK(gkMs);
    document.getElementById('res-kd').textContent = formatKD(kd);
  }

  // ── Блокировка поля числа ────────────────────────────────────
  window.kdMonthChanged = function () {
    var val = document.getElementById('kd-month').value;
    var dayField = document.getElementById('kd-day');
    if (val === '0' || val === '0r') {
      dayField.value    = 0;
      dayField.disabled = true;
    } else {
      dayField.disabled = false;
    }
  };

  // ── Инициализация сегодняшней датой ─────────────────────────
  function initToday() {
    var now  = new Date();
    var utcMs = Date.UTC(now.getFullYear(), now.getMonth(), now.getDate());
    var days  = gkToDays(utcMs);
    var kd    = daysToKD(days);

    document.getElementById('gk-day').value   = now.getDate();
    document.getElementById('gk-month').value = now.getMonth() + 1;
    document.getElementById('gk-year').value  = now.getFullYear();
    document.getElementById('gk-era').value   = 'ce';

    if (kd) {
      if (kd.type === 'zero' || kd.type === 'joy') {
        document.getElementById('kd-month').value = kd.type === 'zero' ? '0' : '0r';
        document.getElementById('kd-day').value   = 0;
        document.getElementById('kd-day').disabled = true;
      } else {
        document.getElementById('kd-month').value = kd.month;
        document.getElementById('kd-day').value   = kd.day;
      }
      document.getElementById('kd-year').value = kd.year;
    }

    showResult(utcMs, kd);
  }

  // ── Конвертация ──────────────────────────────────────────────
  window.convertDate = function () {
    var hint = document.getElementById('conv-hint');
    hint.textContent = '';

    var gkDay   = parseInt(document.getElementById('gk-day').value);
    var gkMon   = parseInt(document.getElementById('gk-month').value);
    var gkYear  = parseInt(document.getElementById('gk-year').value);
    var gkEra   = document.getElementById('gk-era').value;

    var kdDay   = parseInt(document.getElementById('kd-day').value) || 1;
    var kdMon   = document.getElementById('kd-month').value;
    var kdYear  = parseInt(document.getElementById('kd-year').value);

    // Определяем направление: ГК → КД если заполнены поля ГК
    var useGK = (gkDay && gkMon && gkYear);

    if (useGK) {
      // Проверка эры
      if (gkEra === 'bce') {
        hint.textContent = 'Григорианский календарь введён в действие в 1582 году. Конвертация даты до 1582 года недоступна.';
        return;
      }
      if (gkYear < 1582) {
        hint.textContent = 'Григорианский календарь введён в действие в 1582 году. Конвертация даты до 1582 года недоступна.';
        return;
      }

      var utcMs = Date.UTC(gkYear, gkMon - 1, gkDay);
      var days  = gkToDays(utcMs);
      var kd    = daysToKD(days);

      if (kd && kd.year < 3000) {
        hint.textContent = 'Нахрена тебе это? Перепроверь дату — она относится к началу цивилизации.';
      }

      showResult(utcMs, kd);

    } else if (kdYear) {
      // КД → ГК
      if (kdYear < 3000) {
        hint.textContent = 'Нахрена тебе это? Перепроверь дату — она относится к началу цивилизации.';
      }

      var days  = kdToDays(kdYear, kdMon, kdDay);
      var utcMs = ANCHOR_GK_MS + days * 86400000;

      var gkY = new Date(utcMs).getUTCFullYear();
      if (gkY < 1582) {
        hint.textContent = 'Григорианский календарь введён в действие в 1582 году. Конвертация даты до 1582 года недоступна.';
        return;
      }

      showResult(utcMs, daysToKD(days));
    }
  };

  // Запуск
  initToday();

})();
</script>

<!-- ══════════════════════════════════════════════
     КОНЕЦ КОНВЕРТЕРА
     ══════════════════════════════════════════════ -->
## Календарь Дарго

Если вас не смущает, что названия первых месяцев действующего григорианского календаря уводят к языческим временам, а девятый месяц называется седьмым (сент - семь), десятый - восьмым (окта - восемь), одиннадцатый - девятым (нов - девять), двенадцатый - десятым (дека - десять) - можете дальше не читать. ))

По календарю Дарго́ День зимнего солнцестояния – нулевой день календаря. Новый год начинается на следующий день после зимнего солнцестояния. 365 дней (366 в високосный год) разделены на четыре квартала по 91 дню, в свою очередь поделенных на один месяц 31 день и два месяца по 30 дней. Плюс один нулевой день (два дня в високосный год). Каждый квартал начинается с понедельника 01 числа.

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


## Каждый уважающий себя народ имеет свой календарь для себя. А каждый великий народ имеет такой календарь, которым захотят воспользоваться все народы. 
