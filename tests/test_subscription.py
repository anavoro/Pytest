from faker import Faker

def test_subscription_in_home_page(test_setup):
    page = test_setup["page"]
    home_page = test_setup["home_page"]

    assert home_page.is_home_page_visible()
 
    # Step 4: Scroll to footer
    page.locator('footer').scroll_into_view_if_needed()

    # Step 5: Verify text 'SUBSCRIPTION'
    assert home_page.is_subscription_text_visible(), "'SUBSCRIPTION' text not visible"

    # Step 6: Enter email and submit
    fake_email = Faker().email()
    home_page.subscribe_with_email(fake_email)

    # Step 7: Verify success message
    assert home_page.is_subscription_success_visible(), "Subscription success message not visible"
