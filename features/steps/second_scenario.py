from behave import given, when, then
from scanner import Scanner


@given('a user bought 15 meal products for the week')
def step_impl(context):
    pass

@when('the user scannes a QR-code or a barcode of the product')
def step_impl(context):
    context.scanner = Scanner()
    context.scanner.new_session()

@then('the system creates a planned menu that can be used in the future when the user will add a new record in a diary')
def step_impl(context):
    context.planned_menu = plannedMenu()
    context.planned_menu.activate()
  
    assert context.table, "REQUIRE: table"
    context.table.require_columns(["name", "calories", "proteins", "fats", "carbs"])

    for row in context.table.rows:
        name = row["name"]
        calories = row["calories"]
        proteins = row["proteins"]
        fats = row["fats"]
        carbs = row["carbs"]