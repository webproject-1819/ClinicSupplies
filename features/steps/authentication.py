from behave import *

use_step_matcher('parse')

@given('User "{username}" with password "{password}" exists')
def step_impl(context, username, password):
    from django.contrib.auth.models import User
    User.objects.create_user(username=username, email='user@example.com', password=password)

@when('I log in as user "{username}" with password "{password}"')
def step_impl(context, username, password):
    context.browser.visit(context.get_url('/ingresar'))
    form = context.browser.find_by_tag('form').first
    context.browser.fill('username', username)
    context.browser.fill('password', password)
    form.find_by_value('Ingresar').first.click()

@given('I am not logged in')
def step_impl(context):
    context.browser.visit(context.get_url('/cerrar'))

@when('I log out')
def step_impl(context):
    context.browser.visit(context.get_url('/cerrar'))
