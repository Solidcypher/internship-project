from behave import given, when, then


@given('Open Reelly login page')
def open_reelly_login_page(context):
    context.app.login_page.open_login_page()


@when('Input email address')
def input_email(context):
    context.app.login_page.input_email()


@when('Input password')
def input_password(context):
    context.app.login_page.input_password()


@when('Click on login button')
def click_login_button(context):
    context.app.login_page.click_login_button()


