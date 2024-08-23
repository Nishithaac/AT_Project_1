

# Importing necessary modules

import pytest
from selenium.webdriver import Keys

from TestData.HomepageData import Homepage
from TestLocators.HomepageLocators import Locators
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Define a test class
class Test_OrangeHRM:

    # Define a fixture for setting up and tearing down the test environment
    @pytest.fixture
    # Define a booting function
    def booting_function(self):
        # Initialize the Firefox WebDriver and set up the environment
        self.driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        # Navigate to the URL specified in the Homepage data
        self.driver.get(Homepage().url)
        # Maximize the browser window
        self.driver.maximize_window()
        # Create a WebDriverWait instance with a 10-second timeout
        self.wait=WebDriverWait(self.driver,10)
        # Yield control to the test function
        yield
        # Close the browser window after the test is done
        self.driver.close()


    # Define the test function for login functionality
    def test_TC_Login_01(self,booting_function):
        try:


            # Wait until the username input box is visible and then enter the username
            username=self.wait.until(EC.visibility_of_element_located((By.NAME,Locators().username_input_box)))
            username.send_keys(Homepage().username)

            # Wait until the password input box is visible and then enter the password
            password=self.wait.until(EC.visibility_of_element_located((By.NAME,Locators().password_input_box)))
            password.send_keys(Homepage().password)

            # Wait until the submit button is clickable and then click it
            submit_button=self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators().submit_button)))
            submit_button.click()

            # Assert that the current URL matches the dashboard URL, indicating a successful login
            assert self.driver.current_url == Homepage().dashboard_url

            # Print an error message if login was successful
            print(f"SUCCESS : Logged in successfully with username {Homepage().username} and password {Homepage().password}")

        except NoSuchElementException as e:
            # Print the exception if an element was not found
            print(e)

    # Define the test function for login functionality
    def test_TC_Login_02(self,booting_function):
        try:


            # Locate the username input box and enter a valid username
            username = self.wait.until(EC.visibility_of_element_located((By.NAME, Locators().username_input_box)))
            username.send_keys(Homepage().username)

            # Locate the password input box and enter an invalid password
            password = self.wait.until(EC.visibility_of_element_located((By.NAME, Locators().password_input_box)))
            password.send_keys(Homepage().invalid_password)

            # Locate the submit button and click it to attempt login
            submit_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators().submit_button)))
            submit_button.click()

            # Wait for the invalid credentials message to be visible
            invalid_credentials=self.wait.until(EC.visibility_of_element_located((By.XPATH,Locators().invalid_credentials)))
            # Print the text of the invalid credentials message for verification
            print(invalid_credentials.text)

            # Assert that the text of the invalid credentials message is "Invalid credentials"
            assert invalid_credentials.text == "Invalid credentials"

            # Assert that the current URL is not the dashboard URL, confirming login was unsuccessful
            assert self.driver.current_url != Homepage().dashboard_url

            # Print an error message if login was unsuccessful
            print(f"ERROR  : Logg in unsuccessful with username {Homepage().username} and password {Homepage().invalid_password}")

        except NoSuchElementException as e:
            # Print the exception if any of the expected elements are not found
            print(e)






    # Define a test for adding a new employee in PIM module and verify the addition.
    def test_TC_PIM_01(self,booting_function):

       try:
           # Locate the username input box and enter the username from the Homepage object
           username = self.wait.until(EC.visibility_of_element_located((By.NAME, Locators().username_input_box)))
           username.send_keys(Homepage().username)

           # Locate the password input box and enter the password from the Homepage object
           password = self.wait.until(EC.visibility_of_element_located((By.NAME, Locators().password_input_box)))
           password.send_keys(Homepage().password)

           # Locate and click the submit button to log in
           submit_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators().submit_button)))
           submit_button.click()

           # Locate and click the PIM button to navigate to the PIM module
           pim_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators().pim_button)))
           pim_button.click()

           # Locate and click the "Add Employee" button
           add_employee_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators().add_employee_button)))
           add_employee_button.click()

           # Locate the first name input box and enter the first name from the Homepage object
           first_name = self.wait.until(EC.visibility_of_element_located((By.XPATH,Locators().first_name_input_box)))
           first_name.send_keys(Homepage().first_name)

           # Locate the middle name input box and enter the middle name from the Homepage object
           middle_name=self.wait.until(EC.visibility_of_element_located((By.XPATH,Locators.middle_name_input_box)))
           middle_name.send_keys(Homepage().middle_name)

           # Locate the last name input box and enter the last name from the Homepage object
           last_name=self.wait.until(EC.visibility_of_element_located((By.XPATH,Locators().last_name_input_box)))
           last_name.send_keys(Homepage().lastname)

           # Locate the employee ID input box, clear any existing text, and enter the new employee ID
           employee_id=self.wait.until(EC.visibility_of_element_located((By.XPATH,Locators().employee_id_input_box)))

           # Select all text
           employee_id.send_keys(Keys.CONTROL + "a")
           # Clear the text
           employee_id.send_keys(Keys.BACKSPACE)

           # Enter the new employee ID
           employee_id.send_keys(Homepage().employee_id)

           # Locate and click the save button to save the employee details
           save_button=self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators().save_button)))
           save_button.click()

           # Locate the other ID input box and enter the other ID from the Homepage object
           other_id_input_box=self.wait.until(EC.presence_of_element_located((By.XPATH,Locators().other_id_input_box)))
           other_id_input_box.send_keys(Homepage().other_id)

           # Locate the driver license number input box and enter the driver license number from the Homepage object
           driver_license_number_input_box=self.wait.until(EC.visibility_of_element_located((By.XPATH,Locators().driver_license_number_input_box)))
           driver_license_number_input_box.send_keys(Homepage().driver_license_number)

           # Locate the license expiry date input box and enter the license expiry date from the Homepage object
           license_expiry_date_input_box=self.wait.until(EC.visibility_of_element_located((By.XPATH,Locators().license_expiry_date_input_box)))
           license_expiry_date_input_box.send_keys(Homepage().license_expiry_date)

           # Locate the date of birth input box and enter the date of birth from the Homepage object
           date_of_birth=self.wait.until(EC.visibility_of_element_located((By.XPATH,Locators().date_of_birth)))
           date_of_birth.send_keys(Homepage().date_of_birth)

           # Locate and click the gender radio button (assuming it's a clickable option)
           gender=self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators().gender)))
           gender.click()

           # Locate and click the second save button to save all the details
           save_button_2=self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators().save_button2)))
           save_button_2.click()

           # Locate and click the employee list button to navigate to the employee list
           employee_list_button = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, Locators().employee_list_button)))
           employee_list_button.click()

           # Locate the employee name element and print its text
           name=self.wait.until(EC.presence_of_element_located((By.XPATH,Locators().name)))
           print(name.text)

           # Assert that the displayed name matches the expected name
           assert name.text == "anand michael"
           print("SUCCESS : Employee added successfully")

           # Locate the employee information input box and enter the employee ID for searching
           employee_information = self.wait.until(EC.visibility_of_element_located((By.XPATH, Locators().employee_information)))
           employee_information.send_keys(Homepage().employee_id)

           # Locate and click the search button
           search_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators().search_button)))
           search_button.click()

           # Locate and print the records found text
           records_found = self.wait.until(EC.visibility_of_element_located((By.XPATH, Locators().records_found)))
           print(records_found.text)

           # Assert that the records found text matches the expected result
           assert records_found.text == "(1) Record Found"
           print("Employee added successfully")

       except NoSuchElementException  and ElementClickInterceptedException   as  e:
           # Catch any exceptions related to element not found or click intercepted and print the exception message
           print(e)


  # Define a test for editing an existing employee information in PIM module
    def test_TC_PIM_02(self,booting_function):
        try:

            # Locate the username input box and enter the username from the Homepage object
            username = self.wait.until(EC.visibility_of_element_located((By.NAME, Locators().username_input_box)))
            username.send_keys(Homepage().username)

            # Locate the password input box and enter the password from the Homepage object
            password = self.wait.until(EC.visibility_of_element_located((By.NAME, Locators().password_input_box)))
            password.send_keys(Homepage().password)

            # Locate and click the submit button to log in
            submit_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators().submit_button)))
            submit_button.click()

            # Locate and click the PIM button to navigate to the PIM module
            pim_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators().pim_button)))
            pim_button.click()

            # Locate and click the employee list button to view the list of employees
            employee_list_button=self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT,Locators().employee_list_button)))
            employee_list_button.click()

            # Locate and click the edit button for the employee whose details are to be updated
            edit_button=self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators().edit_button)))
            edit_button.click()

            # Locate the employee ID field in the edit form, clear its current value
            edit_id=self.wait.until(EC.presence_of_element_located((By.XPATH,Locators().edit_id)))
            # Select all text in the field
            edit_id.send_keys(Keys.CONTROL + "a")
            # Delete the selected text
            edit_id.send_keys(Keys.BACKSPACE)

            # Enter the new employee ID from the Homepage object
            edit_id.send_keys(Homepage().edited_id)



            # Locate and click the save button to apply the changes
            save_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators().save_button2)))
            save_button.click()

            # Locate and verify the success message indicating the update was successful
            successfully_updated=self.wait.until(EC.visibility_of_element_located((By.XPATH,Locators().successfully_updated)))
            print(successfully_updated.text)

            # Assert that the success message is displayed to confirm the update was successful
            assert successfully_updated.is_displayed()
            print("Successfully edited employee information")



        except NoSuchElementException as e:
            # Catch exceptions related to elements not being found and print the exception message
            print(e)



# Define a test for deleting an existing employee in PIM module
    def test_TC_PIM_03(self,booting_function):
        try:

            # Locate the username input box and enter the username from the Homepage object
            username = self.wait.until(EC.visibility_of_element_located((By.NAME, Locators().username_input_box)))
            username.send_keys(Homepage().username)

            # Locate the password input box and enter the password from the Homepage object
            password = self.wait.until(EC.visibility_of_element_located((By.NAME, Locators().password_input_box)))
            password.send_keys(Homepage().password)

            # Locate and click the submit button to log in
            submit_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators().submit_button)))
            submit_button.click()

            # Locate and click the PIM button to navigate to the PIM module
            pim_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators().pim_button)))
            pim_button.click()

            # Locate and click the employee list button to view the list of employees
            employee_list_button = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, Locators().employee_list_button)))
            employee_list_button.click()

            # Locate and click the delete button for the employee to be deleted
            delete_button=self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators().delete_button)))
            delete_button.click()

            # Locate and click the confirmation button to confirm the deletion
            yes_delete_button=self.wait.until(EC.visibility_of_element_located((By.XPATH,Locators().yes_delete)))
            yes_delete_button.click()

            # Locate and verify the success message indicating that the employee was successfully deleted
            successfully_deleted_message=self.wait.until(EC.visibility_of_element_located((By.XPATH,Locators().successfully_deleted_message)))
            print(successfully_deleted_message.text)

            # Assert that the success message is displayed to confirm the deletion was successful
            assert successfully_deleted_message.is_displayed()
            print("Successfully deleted employee")

            # Navigate back to the employee list to verify the deletion
            employee_list_button = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, Locators().employee_list_button)))
            employee_list_button.click()

            # Locate the list of employee IDs and check that the deleted employee's ID is no longer present
            id_list=self.wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div")))

            # Iterate through the employee IDs to ensure the deleted ID is not found
            for id  in id_list.text:
                if id !=Homepage().edited_id:
                    break
            print("Successfully deleted employee")

            # Locate the employee information search field and enter the first name of the deleted employee
            employee_information=self.wait.until(EC.visibility_of_element_located((By.XPATH,Locators().employee_information_2)))
            employee_information.send_keys(Homepage().first_name)

            # Locate and click the search button to perform the search
            search_button=self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators().search_button)))
            search_button.click()

            # Locate and verify the message indicating no records are found
            no_records_found=self.wait.until(EC.visibility_of_element_located((By.XPATH,Locators().no_records_found)))
            print(no_records_found.text)

            # Assert that the "No Records Found" message is displayed
            assert no_records_found.text=='No Records Found'
            print("Successfully deleted employee")




        except NoSuchElementException as e:
            # Catch exceptions related to elements not being found and print the exception message
            print(e)










