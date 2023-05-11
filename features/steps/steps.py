from behave import *
from app import BankAccount

@given("an bank account exists")
def step_impl(context):
    context.sut = BankAccount(123,100)

@when("depositing money")
def step_impl(context):
    context.sut.deposit(50)

@then("balance should be increased")
def step_impl(context):
    assert(context.sut.balance == 150)



