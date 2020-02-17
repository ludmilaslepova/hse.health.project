"""
Функция достаёт из БД записи пользователя за последний месяц и сравнивает среднее потребление калорий в день с данными за два месяца до (например, по окончании февраля, данные февраля будут сравнены с январём и декабрём)

Если разница есть, то пользователю отправляется уведомление.

"""

### генерация месячного отчёта о питании
 
# триггер, который вызовется каким-то scheduler'ом в определённое время (конец месяца)
def trigger_monthly_report(user_id):
    # выбираем все приёмы пищи пользователя
    user_meals = Meal
        .select()
        .where(Meal.user_id == user_id)
     
    # выбираем все entries пользователя за последние 3 месяца
    user_entries_3_months = DiaryEntry
        .select()
        .join(user_meals, on=(DiaryEntry.meal_id == user_meals.id))
        .join(Food, on=(Food.id == DiaryEntry.food_id))
        .where(current_date - date(DiaryEntry.timestamp).days <= 90)
 
    # выбираем все entries пользователя только за последний месяц
    user_entries_last_month = user_entries_3_months
        .select()
        .where(current_date - date(user_entries_3_months.timestamp).days <= 30)
 
    # выбираем все entries пользователя за два месяца перед последним месяцем
    user_entries_last_month = user_entries_3_months
        .select()
        .where(current_date - date(user_entries_3_months.timestamp).days > 30)
 
    # считаем среднее количество калорий за прошедший месяц
    user_avg_daily_intake_last_month = 0
 
    for entry of user_entries_last_month:
        user_avg_daily_intake_last_month = user_avg_daily_intake_last_month + (entry.calories * entry.amount / 30)
 
    # считаем среднее количество калорий за 2 предыдущих месяца
    user_avg_daily_intake_prev_months = 0
 
    for entry of user_entries_last_month:
        user_avg_daily_intake_prev_months = user_avg_daily_intake_prev_months + (entry.calories * entry.amount / 60)
 
    diff = user_avg_daily_intake_prev_months - user_avg_daily_intake_last_month
    diff_abs = abs(diff)
    diff_percentage = diff_abs / user_avg_daily_intake_prev_months
 
    report_text_more = 'Looks like you consumed more calories this month than two months before' +
        'On average, you consumed {0} more calories ({1}% more)'
 
    report_text_less = 'Looks like you consumed less calories this month than two months before' +
        'On average, you consumed {0} less calories ({1}% less)'
 
    report_text_final = report_text_more if diff < 0 else report_text_less
 
    if diff != 0:
        send_notification(user_id, report_text_final.format(diff_abs, diff_percentage))