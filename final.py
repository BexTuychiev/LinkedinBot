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

    def _get_full_data(self, mode, value):
        """
        A function method that is called in self.__init__ to get full information about the profile in a dictionary
        :param mode: Defines the type of info that is going to be scraped, either company or individual
        :param value: Username if individual profile is desired, or company name for otherwise
        :return: a dictionary object containing the results of the scraper
        """
        if mode == 'company':
            with CompanyScraper(self.cookie) as scraper:
                data = scraper.scrape(company=value)
        if mode == 'individual' or mode == 'in':
            with ProfileScraper(self.cookie) as scraper:
                data = scraper.scrape(user=value)
        return data.to_dict()

    def personal_info(self, *args):
        """
        A method to return all possible fields under personal_info section of the results dictionary
        :param args: Any number of string parameters which corresponds to personal info fields
        :return: prints out values corresponding to the string parameters in args
        """
        possible_info_fields = [
            'name', 'headline', 'company', 'school', 'location', 'summary', 'image', 'followers',
            'email', 'phone', 'connected', 'websites', 'current_company_link'
        ]
        if self.mode.lower() == 'individual' or self.mode.lower() == 'in':
            for field in args:
                if field not in possible_info_fields:
                    print("Possible info include: {}".format(possible_info_fields))
                else:
                    print({field: self.results['personal_info'][field]})
        else:
            print("This method is only accessible for scraping individual profiles. "
                  "See the similar method for company profiles: ")
