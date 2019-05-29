from behave import *

use_step_matcher('parse')

@then('There is a "{link_text}" link')
def step_impl(context, link_text):
        #assert 

@then('There is no "{link_text}" link')
def step_impl(context, link_text):
        #assert 