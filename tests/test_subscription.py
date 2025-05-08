from faker import Faker

def test_subscription_in_home_page(test_setup):
    page = test_setup["page"]
    home_page = test_setup["home_page"]

    assert home_page.is_home_page_visible()

    page.locator('footer').scroll_into_view_if_needed()
    assert home_page.is_subscription_text_visible(), "'SUBSCRIPTION' text not visible"

    fake_email = Faker().email()
    home_page.subscribe_with_email(fake_email)
    assert home_page.is_subscription_success_visible(), "Subscription success message not visible"
