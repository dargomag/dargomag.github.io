---
title: Календарь
---

<!-- ══════════════════════════════════════════════
     КОНВЕРТЕР ДАТ — вставить в начало index.md
     ══════════════════════════════════════════════ -->

<style>
.conv-wrap {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  max-width: 860px;
  margin: 32px auto;
  border: 1px solid #000;
  padding: 24px 32px 28px;
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
  gap: 16px;
  align-items: start;
}

.conv-block {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.conv-block-title {
  font-size: 12px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: #000;
  margin-bottom: 2px;
}

.conv-fields {
  display: grid;
  grid-template-columns: 60px 1fr 80px 100px;
  gap: 6px;
}

.conv-fields input,
.conv-fields select {
  font-family: inherit;
  font-size: 14px;
  padding: 7px 8px;
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
  background-position: right 8px center;
  padding-right: 24px;
}

.conv-fields label {
  font-size: 10px;
  color: #000;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-top: 2px;
}

.conv-field-group {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.conv-btn-wrap {
  display: flex;
  align-items: center;
  justify-content: center;
  padding-top: 28px;
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
  padding: 10px 18px;
  cursor: pointer;
  white-space: nowrap;
}

.conv-btn:hover { background: #0969da; }

.conv-result {
  margin-top: 18px;
  padding: 14px 16px;
  border: 1px solid #000;
  background: #fff;
  font-size: 15px;
  font-weight: 600;
  color: #000;
  min-height: 48px;
  display: flex;
  align-items: center;
  gap: 32px;
}

.conv-result-item {
  display: flex;
  flex-direction: column;
  gap: 2px;
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

.conv-hint {
  margin-top: 10px;
  font-size: 12px;
  color: #cc0000;
  font-weight: 600;
  min-height: 18px;
}
</style>

<div class="conv-wrap">
  <div class="conv-title">Конвертер дат</div>

  <div class="conv-row">

    <!-- ГК -->
    <div class="conv-block">
      <div class="conv-block-title">Григорианский календарь</div>
      <div class="conv-fields">
        <div class="conv-field-group">
          <input type="number" id="gk-day" min="1" max="31" placeholder="день">
          <label>Число</label>
        </div>
        <div class="conv-field-group">
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
          <label>Месяц</label>
        </div>
        <div class="conv-field-group">
          <input type="number" id="gk-year" min="1" placeholder="год">
          <label>Год</label>
        </div>
        <div class="conv-field-group">
          <select id="gk-era">
            <option value="ce">н.э.</option>
            <option value="bce">до н.э.</option>
          </select>
          <label>Эра</label>
        </div>
      </div>
    </div>

    <!-- Кнопка -->
    <div class="conv-btn-wrap">
      <button class="conv-btn" onclick="convert()">Конвертировать</button>
    </div>

    <!-- КД -->
    <div class="conv-block">
      <div class="conv-block-title">Календарь Дарго</div>
      <div class="conv-fields">
        <div class="conv-field-group">
          <input type="number" id="kd-day" min="0" max="31" placeholder="день">
          <label>Число</label>
        </div>
        <div class="conv-field-group">
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
          <label>Месяц</label>
        </div>
        <div class="conv-field-group">
          <input type="number" id="kd-year" min="1" placeholder="год">
          <label>Год КД</label>
        </div>
        <div class="conv-field-group">
          <input type="text" value="КД" disabled style="background:#e8e8e8;color:#555;">
          <label>Эра</label>
        </div>
      </div>
    </div>

  </div>

  <div class="conv-hint" id="conv-hint"></div>

  <div class="conv-result" id="conv-result">
    <div class="conv-result-item">
      <span class="conv-result-label">Григорианский календарь</span>
      <span class="conv-result-value" id="res-gk">—</span>
    </div>
    <div class="conv-result-item">
      <span class="conv-result-label">Календарь Дарго</span>
      <span class="conv-result-value" id="res-kd">—</span>
    </div>
  </div>
</div>

<script>
(function () {

  // ── Данные месяцев КД ────────────────────────────────────────
  // [название, дней, смещение от 22 декабря в днях]
  var KD_MONTHS = [
    null,                          // 0 — не используется
    ['Математика',  31,   0],      // 1: 22 дек + 0
    ['Физика',      30,  31],      // 2: 22 дек + 31
    ['Химия',       30,  61],      // 3: 22 дек + 61
    ['Ботаника',    31,  91],      // 4: 22 дек + 91
    ['Зоология',    30, 122],      // 5: 22 дек + 122
    ['Антропология',30, 152],      // 6: 22 дек + 152
    ['История',     31, 182],      // 7: 22 дек + 182
    ['Психология',  30, 213],      // 8: 22 дек + 213
    ['Экология',    30, 243],      // 9: 22 дек + 243
    ['Культура',    31, 273],      // 10: 22 дек + 273
    ['Поэзия',      30, 304],      // 11: 22 дек + 304
    ['Музыка',      30, 334]       // 12: 22 дек + 334
  ];

  var GK_MONTHS_RU = ['января','февраля','марта','апреля','мая','июня',
                       'июля','августа','сентября','октября','ноября','декабря'];

  // Опорная точка: Нулевой день 12 025 КД = 21 декабря 2025 ГК
  var ANCHOR_GK  = new Date(2025, 11, 21); // 21 декабря 2025
  var ANCHOR_KD_YEAR = 12025;

  // ── Вспомогательные функции ──────────────────────────────────

  // Является ли григорианский год високосным
  function isLeapGK(y) {
    return (y % 4 === 0 && y % 100 !== 0) || (y % 400 === 0);
  }

  // Является ли год КД високосным
  // Год КД високосный если внутри него есть 29 февраля ГК
  // Год КД начинается 21 декабря (ГК год-1) и заканчивается 20 декабря (ГК год)
  function isLeapKD(kdYear) {
    // Григорианский год, февраль которого попадает внутрь года КД
    // Год КД kdYear охватывает февраль григорианского года (kdYear - 10004)
    var gkYear = kdYear - 10004; // смещение: 12025 КД = 2025 ГК → 12025-10004=2021? нет
    // Пересчёт: 12025 КД начинается 21 дек 2024 ГК, февраль 2025 внутри → gkYear = kdYear - 10000
    gkYear = kdYear - 10000;
    return isLeapGK(gkYear);
  }

  // Перевод даты ГК в число дней от опорной точки (21 дек 2025)
  function gkToDays(date) {
    return Math.round((date - ANCHOR_GK) / 86400000);
  }

  // Число дней от опорной точки → дата КД
  function daysToKD(days) {
    // Определяем год КД
    // Нулевой день 12025 КД = день 0
    // Нулевой день 12026 КД = день 365 (или 366 если 12025 - високосный)
    var kdYear = ANCHOR_KD_YEAR;
    var d = days;

    if (d >= 0) {
      // Вперёд
      while (true) {
        var yearLen = isLeapKD(kdYear) ? 366 : 365;
        if (d < yearLen) break;
        d -= yearLen;
        kdYear++;
      }
    } else {
      // Назад
      while (d < 0) {
        kdYear--;
        var yearLen = isLeapKD(kdYear) ? 366 : 365;
        d += yearLen;
      }
    }

    // d — день внутри года КД (0 = Нулевой день)
    var leap = isLeapKD(kdYear);
    var yearLen = leap ? 366 : 365;

    if (d === 0) {
      return { type: 'zero', year: kdYear };
    }
    if (leap && d === yearLen - 1) {
      return { type: 'joy', year: kdYear };
    }

    // Обычный день: d=1 → 1 Математики
    var dayInYear = d; // 1-based внутри 364 дней месяцев
    for (var m = 1; m <= 12; m++) {
      var mDays = KD_MONTHS[m][1];
      if (dayInYear <= mDays) {
        return { type: 'normal', month: m, day: dayInYear, year: kdYear };
      }
      dayInYear -= mDays;
    }
    return null;
  }

  // Дата КД → число дней от опорной точки
  function kdToDays(kdYear, monthVal, day) {
    // Считаем дни от опорной точки до Нулевого дня kdYear
    var days = 0;
    if (kdYear >= ANCHOR_KD_YEAR) {
      for (var y = ANCHOR_KD_YEAR; y < kdYear; y++) {
        days += isLeapKD(y) ? 366 : 365;
      }
    } else {
      for (var y = kdYear; y < ANCHOR_KD_YEAR; y++) {
        days -= isLeapKD(y) ? 366 : 365;
      }
    }
    // Нулевой день = days
    if (monthVal === '0') return days;        // Нулевой день
    if (monthVal === '0r') {                  // День радости
      var leap = isLeapKD(kdYear);
      return days + (leap ? 365 : 364);
    }
    // Обычный месяц
    var m = parseInt(monthVal);
    var offset = KD_MONTHS[m][2]; // смещение от начала месяцев (от 1 Математики = день 1)
    return days + 1 + offset + (day - 1);
  }

  // Форматирование даты ГК
  function formatGK(date) {
    var d = date.getDate();
    var m = date.getMonth(); // 0-based
    var y = date.getFullYear();
    if (y > 0) {
      return d + ' ' + GK_MONTHS_RU[m] + ' ' + y + ' н.э. ГК';
    } else {
      return d + ' ' + GK_MONTHS_RU[m] + ' ' + Math.abs(y - 1) + ' до н.э. ГК';
    }
  }

  // Форматирование года КД с пробелом-разделителем тысяч
  function formatKDYear(y) {
    var s = String(y);
    if (s.length > 3) {
      return s.slice(0, -3) + '\u00a0' + s.slice(-3);
    }
    return s;
  }

  // Форматирование даты КД
  function formatKD(kd) {
    if (!kd) return '—';
    var yr = formatKDYear(kd.year);
    if (kd.type === 'zero') return 'Нулевой день ' + yr + ' КД';
    if (kd.type === 'joy')  return 'День радости ' + yr + ' КД';
    return kd.day + ' ' + KD_MONTHS[kd.month][0] + ' ' + yr + ' КД';
  }

  // ── Инициализация полей сегодняшней датой ────────────────────
  function initToday() {
    var today = new Date();
    today.setHours(0,0,0,0);

    // ГК поля
    document.getElementById('gk-day').value   = today.getDate();
    document.getElementById('gk-month').value = today.getMonth() + 1;
    document.getElementById('gk-year').value  = today.getFullYear();
    document.getElementById('gk-era').value   = 'ce';

    // КД поля
    var days = gkToDays(today);
    var kd   = daysToKD(days);
    if (kd) {
      if (kd.type === 'zero') {
        document.getElementById('kd-month').value = '0';
        document.getElementById('kd-day').value   = 0;
        document.getElementById('kd-year').value  = kd.year;
      } else if (kd.type === 'joy') {
        document.getElementById('kd-month').value = '0r';
        document.getElementById('kd-day').value   = 0;
        document.getElementById('kd-year').value  = kd.year;
      } else {
        document.getElementById('kd-month').value = kd.month;
        document.getElementById('kd-day').value   = kd.day;
        document.getElementById('kd-year').value  = kd.year;
      }
    }

    // Показать результат
    document.getElementById('res-gk').textContent = formatGK(today);
    document.getElementById('res-kd').textContent = formatKD(kd);
  }

  // ── Блокировка поля числа для Нулевого дня и Дня радости ────
  window.kdMonthChanged = function () {
    var val = document.getElementById('kd-month').value;
    var dayField = document.getElementById('kd-day');
    if (val === '0' || val === '0r') {
      dayField.value = 0;
      dayField.disabled = true;
    } else {
      dayField.disabled = false;
    }
  };

  // ── Конвертация ──────────────────────────────────────────────
  window.convert = function () {
    var hint = document.getElementById('conv-hint');
    hint.textContent = '';

    // Определяем, какое поле заполнено последним — по фокусу не отследить,
    // поэтому конвертируем ГК → КД если год ГК заполнен, иначе КД → ГК.
    // Простое правило: если пользователь менял ГК — конвертируем ГК→КД,
    // если КД — КД→ГК. Реализуем через последний активный блок.
    // Для простоты: всегда конвертируем оба направления от ГК,
    // если год ГК валиден; иначе от КД.

    var gkYearVal  = parseInt(document.getElementById('gk-year').value);
    var gkMonthVal = parseInt(document.getElementById('gk-month').value);
    var gkDayVal   = parseInt(document.getElementById('gk-day').value);
    var gkEra      = document.getElementById('gk-era').value;

    var kdYearVal  = parseInt(document.getElementById('kd-year').value);
    var kdMonthVal = document.getElementById('kd-month').value;
    var kdDayVal   = parseInt(document.getElementById('kd-day').value);

    // Пробуем ГК → КД
    if (gkYearVal && gkMonthVal && gkDayVal) {

      var gkY = gkEra === 'bce' ? -(gkYearVal - 1) : gkYearVal;

      // Проверка: до 1582 года
      if ((gkEra === 'ce' && gkYearVal < 1582) || gkEra === 'bce') {
        hint.textContent = 'Григорианский календарь введён в действие в 1582 году. Конвертация даты до 1582 года недоступна.';
        return;
      }

      // Проверка: до 1000 лет до н.э. (для КД < ~3000)
      // Для ГК это до 1000 г. до н.э. → уже отсечено выше

      var gkDate = new Date(gkY, gkMonthVal - 1, gkDayVal);
      gkDate.setFullYear(gkY); // для отрицательных лет

      var days = gkToDays(gkDate);
      var kd   = daysToKD(days);

      // Проверка «нахрена»: КД год < 3000
      if (kd && kd.year < 3000) {
        hint.textContent = 'Нахрена тебе это? Перепроверь дату — она относится к началу цивилизации.';
      }

      document.getElementById('res-gk').textContent = formatGK(gkDate);
      document.getElementById('res-kd').textContent = formatKD(kd);
      return;
    }

    // КД → ГК
    if (kdYearVal && kdMonthVal !== undefined) {

      // Проверка «нахрена»: КД год < 3000
      if (kdYearVal < 3000) {
        hint.textContent = 'Нахрена тебе это? Перепроверь дату — она относится к началу цивилизации.';
      }

      var days = kdToDays(kdYearVal, kdMonthVal, kdDayVal || 1);
      var gkDate = new Date(ANCHOR_GK.getTime() + days * 86400000);

      // Проверка: до 1582 года ГК
      if (gkDate.getFullYear() < 1582) {
        hint.textContent = 'Григорианский календарь введён в действие в 1582 году. Конвертация даты до 1582 года недоступна.';
        return;
      }

      document.getElementById('res-gk').textContent = formatGK(gkDate);
      document.getElementById('res-kd').textContent = formatKD(daysToKD(days));
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
