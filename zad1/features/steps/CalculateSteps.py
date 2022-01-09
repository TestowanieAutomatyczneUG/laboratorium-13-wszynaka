from behave import *

from Calcualte import Calculate

use_step_matcher("re")


@given("Calculate")
def step_impl(context):
    context.calc = Calculate()


@then("chcecking if 3/1 gives 3")
def step_impl(context):
    assert context.calc.dividingints(3, 1) == 3

@then("chcecking if 66/2 gives 33")
def step_impl(context):
    assert context.calc.dividingints(66, 2) == 33

@then("chcecking if 80/40 gives 2")
def step_impl(context):
    assert context.calc.dividingints(80, 40) == 2

@then("chcecking if 333/111 gives 3")
def step_impl(context):
    assert context.calc.dividingints(333, 111) == 3

@then("chcecking if float gives error")
def step_impl(context):
    assert context.calc.dividingints(100.5, 2) == "Invalid type"