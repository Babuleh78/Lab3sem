from behave import given, when, then
from Struct import Red, Blue, Square, Circle

@given('I have a red color')
def step_given_red_color(context):
    context.color = Red()

@when('I create a square with that color')
def step_when_create_square(context):
    context.shape = Square(context.color)

@then('it should return "{expected_output}"')
def step_then_check_output(context, expected_output):
    assert context.shape.info() == expected_output
   
