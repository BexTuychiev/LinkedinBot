from scrape_linkedin import ProfileScraper
from scrape_linkedin import CompanyScraper
import time
import random


class LinkedinBot:
    """
    A class built around scrape_linkedin package from GitHub.
    Purpose: Scrape publicly available user and company profiles from Linkedin in automated way.
    """

    def __init__(self, cookie, mode, value):
        """
        Initialize an instance of LinkedinBot class.

        :param cookie: LI_AT cookie that will be provided by the browser after logging in to Linkedin
        :param mode: Defines the type of info that is going to be scraped, either company or individual
        :param value: Contains target company or individual ID from Linkedin. Example: https://www.linkedin.com/in/ID
        """
        # Get the LI_AT cookie information from browser settings after logging in to Linkedin
        self.cookie = cookie
        # Mode defines the type of info you are scraping, either company or private profile
        self.mode = mode
        # Target Linkedin ID
        self.value = value

        # Get full data of a profile
        self.results = self._get_full_data(self.mode, self.value)
