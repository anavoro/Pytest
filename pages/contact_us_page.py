from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class ContactUsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        
        self.get_in_touch_header = page.locator('h2.title.text-center:has-text("Get In Touch")')
        self.name_input = page.locator("[data-qa='name']")
        self.email_input = page.locator("[data-qa='email']")
        self.subject_input = page.locator("[data-qa='subject']")
        self.message_textarea = page.locator("[data-qa='message']")
        self.file_upload_input = page.locator("input[type='file'][name='upload_file']")
        self.submit_button = page.locator("[data-qa='submit-button']")
        self.success_message = page.locator("#contact-page .alert-success")
        self.home_button = self.page.locator("a[href='/']:text('Home')")

    def is_contact_page_visible(self):
         return self.get_in_touch_header.is_visible()
    
    def fill_contact_form(self, name, email, subject, message):
        """Fill all fields in the contact form"""
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.subject_input.fill(subject)
        self.message_textarea.fill(message)
    
    def upload_file(self, file_path):
        """Upload a file to the contact form"""
        self.file_upload_input.set_input_files(file_path)

    def click_submit_button(self):
        self.submit_button.click()
  
    def handle_alert(self):
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.submit_button.click()
 
    def verify_success_message(self):
        success_text = "Success! Your details have been submitted successfully."
        expect(self.success_message).to_be_visible()
        expect(self.success_message).to_contain_text(success_text)
 
    def click_home_button(self):
        self.home_button.wait_for(state="visible")  
        self.home_button.click()