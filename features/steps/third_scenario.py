from behave import given, when, then
from scanner import Scanner


@given('a user has a receipt from the grocerie store')
def step_impl(context):
    pass

@when('the user scannes a QR-code of the receipt')
def step_impl(context):
    context.scanner = Scanner()
    context.scanner.new_session()
    

@then('the system shows a window with the list of products that can be added in the planned menu')
def step_impl(context):
    context.scanner.receipt.add_entry()