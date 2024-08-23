class Locators:
    # TC_Login_01
    username_input_box="username"
    password_input_box="password"
    submit_button="//button[@type='submit']"

    # TC_Login_02
    invalid_credentials="//div[@role='alert']"

    # TC_PIM_01
    pim_button="//ul[@class='oxd-main-menu']/li[2]"
    add_employee_button="//ul//li[@class='oxd-topbar-body-nav-tab'][1]"
    first_name_input_box="//input[@name='firstName']"
    middle_name_input_box="//input[@name='middleName']"
    last_name_input_box="//input[@name='lastName']"
    employee_id_input_box="//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']"
    save_button="//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]"
    other_id_input_box="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input"
    driver_license_number_input_box="(//input)[7]"
    license_expiry_date_input_box="(//input[@placeholder='yyyy-dd-mm'])[1]"
    date_of_birth="(//input[@placeholder='yyyy-dd-mm'])[2]"
    gender="/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span"
    save_button2="//div[@class='orangehrm-custom-fields']//button[@type='submit'][normalize-space()='Save']"
    employee_list_button="Employee List"
    name="//div[text()='anand michael']"
    employee_information = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input"
    search_button = "//button[@type='submit']"
    records_found = "//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//span"

    # TC_PIM_02
    edit_button="//div[text()='0306']/parent::div/following-sibling::div/div/button[1]"
    edit_id="//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[1]/div/div[2]/input"
    successfully_updated = "//div[@id='oxd-toaster_1']"

    # TC_PIM_03
    delete_button="//div[text()='0306']/parent::div/following-sibling::div/div/button[2]"
    yes_delete="//div[@class='orangehrm-modal-footer']//button[2]"
    successfully_deleted_message="//div[@id='oxd-toaster_1']"
    id="//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div"
    employee_information_2="//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input"
    no_records_found="//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//span"