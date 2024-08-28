from behave import given, when, then


@when('Input test password into input fields')
def input_test_password(context):
    context.app.change_password_page.input_test_password()


@then('Verify Change Password page opens')
def verify_change_password_page(context):
    context.app.change_password_page.verify_change_password_page_appears()


@then('Verify Change Password button is available to click')
def verify_change_password_button(context):
    context.app.change_password_page.verify_change_password_button()
