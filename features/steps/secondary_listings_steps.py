from behave import given, when, then
from time import sleep


@when('Click through all {number} pages')
def click_through_all_pages(context, number):
    context.app.secondary_page.click_through_all_pages(number)


@when('Click on Filter button')
def click_filter_button(context):
    context.app.secondary_page.click_filter_button()


@when('Click on Want to Buy listing type')
def click_buy_listing_type(context):
    context.app.secondary_page.click_buy_listing_type()


@when('Input {number} into From price field')
def input_from_price(context, number):
    context.app.secondary_page.input_from_price(number)


@when('Input {number} into To price field')
def input_from_price(context, number):
    context.app.secondary_page.input_to_price(number)


@when('Click Apply Filter button')
def click_apply_filter_btn(context):
    context.app.secondary_page.click_apply_filter_btn()


@then('Verify that the Secondary page opens')
def verify_secondary_page_opens(context):
    context.app.secondary_page.verify_secondary_pages_opens()


@then('Click through all pages and verify all cards have "want to buy" tag')
def verify_card_want_to_buy_tag(context):
    context.app.secondary_page.verify_card_want_to_buy_tag()


@then('Click through all pages and verify price in all cards inside the range {number1} to {number2}')
def verify_card_price_range(context, number1, number2):
    context.app.secondary_page.verify_card_price_range(number1, number2)
