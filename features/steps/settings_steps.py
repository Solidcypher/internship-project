from behave import given, when, then


@when('Click on Change Password option')
def change_password_option(context):
    context.app.settings_page.click_change_password_option()
