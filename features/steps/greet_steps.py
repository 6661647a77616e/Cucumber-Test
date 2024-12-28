from behave import given, when, then
from app import greet_user

@given('a user named "{name}"')
def step_given_user_name(context, name):
    context.name = name

@given('an empty name')
def step_given_empty_name(context):
    context.name = ""

@when('the user is greeted')
def step_when_user_is_greeted(context):
    context.response = greet_user(context.name)

@then('the response should be "{expected_response}"')
def step_then_response_should_be(context, expected_response):
    assert context.response == expected_response, \
        f"Expected '{expected_response}' but got '{context.response}'"
