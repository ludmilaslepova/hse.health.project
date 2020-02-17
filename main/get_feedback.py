"""
Описывается фича, которая сравнивает последний приём пищи пользователя с этими же приёмами пищи за предыдущие дни. 

Если пользователь съел больше, чем обычно, ему приходит уведомление "You ate more...", если меньше - то "You ate less..."

Триггер - прошло 15 минут после последнего добавления entry в определённый meal.

"""


# сбрасываем текущий таймер
timeout.clear()
 
# создаём новый entry
DiaryEntry.create(
    meal_id = 12949848,
    food_id = 57494,
    amount = 100,
    units = 'gram',
    timestamp = '1580747815139'
)
 
# создаём новый таймер, который затриггерит код ниже через 15 минут
# если новый entry будет создан меньше чем через 15 минут, то этот код отменится и
# создастся новый таймер
timeout = new Delay(900000) # 15 min
 
meal = Meal.get_by_id(12949848)
user = User.get_by_id(meal.user_id)
current_date = date.now()
 
# выбираем записи в нужном Meal за последние 14 дней, группируем по дню
lastUserMealEntries = DiaryEntry
    .select()
    .where(
        DiaryEntry.meal_id == meal.id,
        (current_date - date(DiaryEntry.timestamp)).days <= 14
    )
    .group_by(date(DiaryEntry.timestamp).day)
 
# выбираем сегодняшние entries в нужном meal
currentMealEntries = DiaryEntry
    .select()
    .where(
        DiaryEntry.meal_id == meal.id,
        current_date.day === date(DiaryEntry.timestamp).day
    )
 
calories_total = 0
 
for day_meal in lastUserMealEntries:
    calories_total += sum(day_meal.calories)
 
avg_calories = calories_total / 14
current_meal_calories = sum(currentMealEntries.calories)
 
if (avg_calories > current_meal_calories):
    send_notification(user.id, 'You ate LESS calories for {0} than usually today'.format(meal.name) )
else:
    send_notification(user.id, 'You ate MORE calories for {0} than usually today'.format(meal.name))