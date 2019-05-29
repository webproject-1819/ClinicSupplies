from behave import *

use_step_matcher('parse')

@when('I go to the home page')
def step_iml(context):
        context.browser.visit(context.get_url('/home'))