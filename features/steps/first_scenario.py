from behave import given, when, then
from scanner import Scanner
from hamcrest import assert_that

@given('a user has a package of oat flackes with description in foreign language')
def step_impl(context):
    pass

@when('the user scannes a QR-code or a barcode of the product')
def step_impl(context):
    context.scanner = Scanner()
    context.scanner.new_session()


@then('the system opens up a window with information about amount of calories and the proportion of proteins, fats and carbohydrates of the product')
def step_impl(context):
    calories_ = context.scanner.new_session.product.get(calories, None)
    if not calories_:
        assert_that(False, "Calories of the product are unknown")

    proteins_ = context.scanner.new_session.product.get(proteins, None)
    if not proteins_:
        assert_that(False, "Proteins amount of the product is unknown")

    fats_ = context.scanner.new_session.product.get(fats, None)
    if not fats_:
        assert_that(False, "Fats amount of the product is unknown")

    carbs_ = context.scanner.new_session.product.get(carbs, None)
    if not carbs_:
        assert_that(False, "Carbohydrates amount of the product is unknown")