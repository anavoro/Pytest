from playwright.sync_api import Page
from pages.base_page import BasePage 

class SignupInfoPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        
        self.enter_account_info_heading = 'b:has-text("Enter Account Information")'
        self.gender_mr_radio = 'input[name="title"][id="id_gender1"]'
        self.gender_mrs_radio = 'input[name="title"][id="id_gender2"]'
        self.name_field = 'input[data-qa="name"][name="name"]'
        self.password_field = 'input[data-qa="password"][name="password"]'
        self.days_dropdown = 'select[data-qa="days"]'
        self.months_dropdown = 'select[data-qa="months"]'
        self.years_dropdown = 'select[data-qa="years"]'
        self.newsletter_checkbox = 'input[name="newsletter"][id="newsletter"]'
        self.optin_label = 'label[for="optin"]'
        self.first_name_field = 'input[data-qa="first_name"]'
        self.last_name = 'input[data-qa="last_name"]'
        self.company_field = 'input[data-qa="company"]'
        self.address1_field = 'input[data-qa="address"][name="address1"]'
        self.address2_field = 'input[name="address2"]'
        self.country_dropdown = 'select[data-qa="country"]'
        self.state_field = 'input[data-qa="state"]'
        self.city_field = 'input[data-qa="city"]'
        self.zipcode_field = 'input[data-qa="zipcode"]'
        self.mobile_number_field = 'input[data-qa="mobile_number"]'
        self.create_account_button = 'button[data-qa="create-account"]'

    def verify_enter_account_info_is_visible(self):
        return self.is_visible(self.enter_account_info_heading)

    def select_gender(self, gender: str):
        if gender.lower() == 'mr':
            self.click(self.gender_mr_radio)
        elif gender.lower() == 'mrs':
            self.click(self.gender_mrs_radio)
        else:
            raise ValueError(f"Invalid gender: {gender}. Use 'Mr' or 'Mrs'.")

    def enter_name(self, name: str):
        self.fill(self.name_field, name)

    def enter_password(self, password: str):
        self.fill(self.password_field, password)

    def select_option(self, locator, value=None, label=None, index=None):
        """
        Select an option from a dropdown element.
        
        Args:
            locator: The locator for the dropdown element
            value: Select by value attribute
            label: Select by visible text
            index: Select by index
        """
        dropdown = self.page.locator(locator)
        
        if value is not None:
            dropdown.select_option(value=value)
        elif label is not None:
            dropdown.select_option(label=label)
        elif index is not None:
            dropdown.select_option(index=index)
        else:
            raise ValueError("You must provide either value, label, or index to select an option")  

    def select_date(self, day: str):
        self.select_option(self.days_dropdown, value=day)

    def select_month(self, month: str):
        self.select_option(self.months_dropdown, value=month)

    def select_year(self, year: str):
        self.select_option(self.years_dropdown, value=year)

    def subscribe_newsletter(self):
        self.click(self.newsletter_checkbox)

    def receive_special_offers(self):
        self.click(self.optin_label)

    def enter_first_name(self, firstName: str):
        self.fill(self.first_name_field, firstName)

    def enter_last_name(self, lastName: str):
        self.fill(self.last_name, lastName)

    def enter_company(self, company: str):
        self.fill(self.company_field, company)

    def enter_address1(self, address: str):
        self.fill(self.address1_field, address)

    def enter_address2(self, address: str):
        self.fill(self.address2_field, address)

    def select_country(self, country: str):
        self.select_option(self.country_dropdown, value=country)

    def enter_state(self, state: str):
        self.fill(self.state_field, state)

    def enter_city(self, city: str):
        self.fill(self.city_field, city)

    def enter_zipcode(self, zipcode: str):
        self.fill(self.zipcode_field, zipcode)

    def enter_mobile_number(self, mobileNumber: str):
        self.fill(self.mobile_number_field, mobileNumber)

    def click_create_account_button(self):
        self.click(self.create_account_button)
    
    def subscribe_newsletter(self):
        self.click(self.newsletter_checkbox)
    
    def receive_special_offers(self):
        self.click(self.optin_label)