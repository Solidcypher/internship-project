from behave import given, when, then


@when('Click on settings')
def click_settings(context):
    context.app.home_page.click_settings()
