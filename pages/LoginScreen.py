class LoginScreen:

    def __init__(self, driver):
        self.driver = driver

    # Locators in login screen - locator_strategy
    enterEmail_id = "com.cashfree.merchant.debug:id/account_mail"
    enterPassword_id = "com.cashfree.merchant.debug:id/agent_pass"
    forgotPassword_id = "com.cashfree.merchant:id/btn_forgot_password"
    loginButton_id = "com.cashfree.merchant.debug:id/loginBtn"
    aliasLoginButton_id = "com.cashfree.merchant:id/aliasBtn"
    createAccountButton_id = "com.cashfree.merchant:id/creteAccountBtn"
    emailError_xpath = "//android.widget.TextView[@text='Enter a valid email ID']"
    pwdError_xpath = "//android.widget.TextView[@text='Enter a valid Password.']"
    errorMsg_id = "com.cashfree.merchant.debug:id/errorMsg"

    # method to enter email id - pass email in test
    def enter_email(self, email):
        self.driver.find_element_by_id(self.enterEmail_id).clear()
        self.driver.find_element_by_id(self.enterEmail_id).send_keys(email)

    # method to enter password - pass password in test
    def enter_password(self, pwd):
        self.driver.find_element_by_id(self.enterPassword_id).clear()
        self.driver.find_element_by_id(self.enterPassword_id).send_keys(pwd)

    # method to click login button
    def click_login(self):
        self.driver.find_element_by_id(self.loginButton_id).click()

    # method to get generic error message
    def get_error(self):
        return self.driver.find_element_by_id(self.errorMsg_id).text

    # method to get email error message
    def get_email_error(self):
        return self.driver.find_element_by_xpath(self.emailError_xpath).text
