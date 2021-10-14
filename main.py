from linkedin.linkedin import Linkedin


with Linkedin() as bot:

	bot.home_page()
	bot.log_in_button()
	bot.log_in_credentials(user_email="example@gmail.com", 
						   user_password="password")
	bot.search_button(search_input="python developer")
	bot.apply_filtrations()