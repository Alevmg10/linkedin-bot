from selenium.webdriver.remote.webdriver import WebDriver


class JobsFiltration:

	def __init__(self, driver: WebDriver):
		self.driver = driver

	def display_all_filters(self):
		show_filters = self.driver.find_element_by_css_selector(
			'button[class="artdeco-pill artdeco-pill--slate artdeco-pill--2 artdeco-pill--choice artdeco-pill--selected ember-view search-reusables__filter-pill-button"]'
			)
		show_filters.click()

	def filter_resent_relevant(self, most_relevant=True):
		if most_relevant:
			pass
		else:
			most_resent_click = self.driver.find_element_by_css_selector(
				'label[for="advanced-filter-sortBy-DD"]'
				)
			most_resent_click.click()

	def date_posted_filter(self):
		past_24_hours = self.driver.find_element_by_css_selector(
			'label[for="advanced-filter-timePostedRange-r86400"]'
			)
		past_24_hours.click()

	def show_filters_results(self):
		results = self.driver.find_element_by_css_selector(
			'button[class="reusable-search-filters-buttons search-reusables__secondary-filters-show-results-button artdeco-button artdeco-button--2 artdeco-button--primary ember-view"]'
			)
		results.click()