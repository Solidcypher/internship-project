from behave import given, when, then
from time import sleep


@when('Click through all {number} pages')
def click_through_all_pages(context, number):
    context.app.secondary_page.click_through_all_pages(number)


@then('Verify that the Secondary page opens')
def verify_secondary_page_opens(context):
    context.app.secondary_page.verify_secondary_pages_opens()
