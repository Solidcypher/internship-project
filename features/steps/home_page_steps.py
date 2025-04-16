from behave import given, when, then


@when('Click on settings')
def click_settings(context):
    context.app.home_page.click_settings()


@when('Click on Secondary')
def click_secondary(context):
    context.app.home_page.click_secondary_listings()


@when('Click on Main Menu')
def click_main_menu(context):
    context.app.home_page.click_main_menu()


@when('Click on Off-Plan old')
def click_off_plan_old(context):
    context.app.home_page.click_off_plan_old()


@when('Click on user profile image')
def click_user_profile_image(context):
    context.app.home_page.click_user_profile_image()
