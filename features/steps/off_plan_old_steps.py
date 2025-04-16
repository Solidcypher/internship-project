from behave import given, when, then


@when('Click through all Off Plan pages')
def click_through_off_plan_pages(context):
    context.app.off_plan_old_page.click_through_off_plan_pages()


@when('Return to first page using last page button')
def click_back_through_off_plan_pages(context):
    context.app.off_plan_old_page.click_back_through_off_plan_pages()


@then('Verify old Off-Plan page opens')
def verify_off_plan_page_opens(context):
    context.app.off_plan_old_page.verify_old_off_plan_page_opens()
