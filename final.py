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
        A method to return all possible fields under personal_info section of the results dictionary for individual
        profiles
        :param args: Any number of string parameters which corresponds to personal info fields
        :return: prints out values corresponding to the string parameters in args
        """
        # Specify a list of fields that appear in results dictionary for personal info section
        possible_info_fields = [
            'name', 'headline', 'company', 'school', 'location', 'summary', 'image', 'followers',
            'email', 'phone', 'connected', 'websites', 'current_company_link'
        ]
        # Check for the mode of the target information
        if self.mode.lower() == 'individual' or self.mode.lower() == 'in':
            for field in args:
                if field not in possible_info_fields:
                    print("No field named {}. Possible fields include: {}".format(field, possible_info_fields))
                else:
                    print({field: self.results['personal_info'][field]})
        else:
            print("This method is only accessible for scraping individual profiles. "
                  "See the similar method for company profiles: ")

    def get_experiences(self, *args):
        """
        A method to return all possible fields under experiences section of the results dictionary for individual
        profiles
        :param args: Any number of string parameters which corresponds to experience fields
        :return: prints out values corresponding to the string parameters in args
        """
        # Specify a list of fields that appear in results dictionary for experiences section
        possible_fields = ['jobs', 'education', 'volunteering']

        # Check for the mode of the target information
        if self.mode.lower() == 'individual' or self.mode.lower() == 'in':
            for field in args:
                if field not in possible_fields:
                    print("No field named {}. Possible fields include: {}".format(field, possible_info_fields))
                else:
                    print({field: self.results['experiences'][field]})
        else:
            print("This method is only accessible for scraping individual profiles. "
                  "See the similar method for company profiles: ")

    def get_skills(self):
        """
        A method to return all skill names and their number of endorsements under the skills section of results
         dictionary for individual profiles
        :return: prints out name of the skill and the number of endorsements
        """
        # Check for the mode of the target information
        if self.mode.lower() == 'individual' or self.mode.lower() == 'in':
            for skill in self.results['skills']:
                print(skill['name'] + ': ' + skill['endorsements'])
        else:
            print("This method is only accessible for scraping individual profiles. "
                  "See the similar method for company profiles: ")


if __name__ == '__main__':
    bot = LinkedinBot(
        cookie='AQEDAS_CpVgAZJtdAAABctX1xfEAAAFy-gJJ8U0Aw3faemVsziA2wOqaZZoexUuShwyibcvMf3TuQK5qnTAAiJDpMxfs3B2'
               'z0Fq0l-xdyf9d_0CJOcZ4gvLfL14thtyH2a6EbQXM-Ueh3tEQ00xiuXWA', value='spencernicol', mode='in')

    bot.get_skills()
