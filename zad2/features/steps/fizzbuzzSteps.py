from behave import *

from fizzbuzz.FizzBuzz import FizzBuzz

use_step_matcher("re")


@given("FizzBuzz")
def step_impl(context):
    context.FizzBuzz = FizzBuzz()


@then("chcecking if 3 gives Fizz")
def step_impl(context):
    assert context.FizzBuzz.game(3) == "Fizz"


@then("chcecking if 9 gives Fizz")
def step_impl(context):
    assert context.FizzBuzz.game(9) == "Fizz"


@then("chcecking if 27 gives Fizz")
def step_impl(context):
    assert context.FizzBuzz.game(27) == "Fizz"


@then("chcecking if 5 gives Buzz")
def step_impl(context):
    assert context.FizzBuzz.game(5) == "Buzz"


@then("chcecking if 125 gives Buzz")
def step_impl(context):
    assert context.FizzBuzz.game(125) == "Buzz"


@then("chcecking if 65 gives Buzz")
def step_impl(context):
    assert context.FizzBuzz.game(65) == "Buzz"


@then("chcecking if 15 gives FizzBuzz")
def step_impl(context):
    assert context.FizzBuzz.game(15) == "FizzBuzz"


@then("chcecking if 90 gives FizzBuzz")
def step_impl(context):
    assert context.FizzBuzz.game(90) == "FizzBuzz"


@then("chcecking if 150 gives FizzBuzz")
def step_impl(context):
    assert context.FizzBuzz.game(150) == "FizzBuzz"
