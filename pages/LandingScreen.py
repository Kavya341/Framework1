class LandingScreen:

    def __init__(self, driver):
        self.driver = driver

    title_id = "com.cashfree.merchant:id/toolbarTitle"
    pgcard_id = "com.cashfree.merchant:id/payoutCard"
    navigationBar_accessibility_id = "Open navigation drawer"
    home_id = "com.cashfree.merchant:id/home"
    pgSummary_id = "com.cashfree.merchant:id/pggatway"
    settlements_id = "com.cashfree.merchant:id/nav_settlement"
    profile_id = "com.cashfree.merchant:id/profile"
    support_id = "com.cashfree.merchant:id/support"
    logout_id = "com.cashfree.merchant:id/logout"
    closeNavbar_id = "com.cashfree.merchant:id/icon"

    def get_page_title(self):
        return self.driver.find_element_by_id(self.title_id).text