from peewee import *
 
db = SqliteDatabase('people.db')
 
class User(Model):
    id = AutoField()
    username = CharField()
    birthday = DateField()
    weight = DoubleField()
    height = DoubleField()
    activity_level = IntegerField()
    calorie_daily_limit = IntegerField()
 
    class Meta:
        database = db
         
class Meal(Model):
    id = AutoField()
    user_id = ForeignKeyField(User, backref='meals')
    name = CharField()
    position = IntegerField()
     
    class Meta:
        database = db
         
class Category(Model):
    id = AutoField()
    name = CharField()
     
    class Meta:
        database = db
 
         
class Allergy(Model):
    id = AutoField()
    allergy_category = CharField()
     
    class Meta:
        database = db
 
         
class Food(Model):
    id = AutoField()
    description = CharField()
    category = ForeignKeyField(Category, backref='food')
    rating = IntegerField()
    allergies = ManyToManyField(Allergy, backref='food')
    calories = IntegerField() # per 100g
    fats = IntegerField() # per 100g
    carbohydrates = IntegerField() # per 100g
    proteins = IntegerField() # per 100g
     
    class Meta:
        database = db
         
class DiaryEntry(Model):
    id = AutoField()
    meal_id = ForeignKeyField(Meal, backref='entries')
    food_id = ForeignKeyField(Food, backref='entries')
    amount = IntegerField()
    units = CharField()
    timestamp = DateTimeField()
     
    class Meta:
        database = db
 
db.connect()