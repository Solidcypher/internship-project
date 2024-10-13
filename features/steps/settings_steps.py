from behave import given, when, then


@when('Click on Change Password option')
def change_password_option(context):
    context.app.settings_page.click_change_password_option()


@then('Verify there are {number} settings options')
def verify_settings_option(context, number):
    context.app.settings_page.verify_settings_options(number)


@then('Verify Connect the Company button is available')
def verify_connect_the_company_button(context):
    context.app.settings_page.verify_connect_the_company_button()
