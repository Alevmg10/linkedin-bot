from linkedin.jobs_filtrations import JobsFiltration
from selenium import webdriver
import linkedin.constants as const
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


class Linkedin(webdriver.Chrome):

	def __init__(self, teardown=False):
		option = Options()
		brave_path = "/usr/bin/brave-browser"
		option.binary_location=brave_path
		driver_path = "/usr/bin/chromedriver"

		super(Linkedin, self).__init__(options=option, executable_path=driver_path)
		self.teardown=teardown
		self.implicitly_wait(30)
		self.maximize_window()

	def __exit__(self, exc_type, exc_val, exc_tb):
		if self.teardown:
			self.quit()

	def home_page(self):
		self.get(const.URL)
	
	def log_in_button(self):
		log_in = self.find_element_by_class_name("nav__button-secondary")
		log_in.click()

	def log_in_credentials(self, user_email, user_password):
		email = self.find_element_by_id("username")
		email.clear()
		email.send_keys(user_email)

		password = self.find_element_by_id("password")
		password.clear()
		password.send_keys(user_password)

		entry_button = self.find_element_by_css_selector(
			'button[type="submit"]'
			)
		entry_button.click()

	def search_button(self, search_input):
		star_search = self.find_element_by_css_selector(
			'button[type="button"]'
			)
		star_search.click()

		search_click = self.find_element_by_css_selector(
			'input[class="search-global-typeahead__input always-show-placeholder"]'
			)
		search_click.clear()
		search_click.send_keys(search_input, Keys.RETURN)

	def apply_filtrations(self):
		filtration = JobsFiltration(driver=self)
		filtration.display_all_filters()
		filtration.filter_resent_relevant(most_relevant=False)
		filtration.date_posted_filter()
		filtration.show_filters_results()