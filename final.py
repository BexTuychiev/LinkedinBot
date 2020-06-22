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
                data = scraper.scrape(company=value, jobs=True, insights=True)
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
        possible_fields = [
            'name', 'headline', 'company', 'school', 'location', 'summary', 'image', 'followers',
            'email', 'phone', 'connected', 'websites', 'current_company_link'
        ]
        # Check for the mode of the target information
        if self.mode.lower() == 'individual' or self.mode.lower() == 'in':
            for field in args:
                if field not in possible_fields:
                    print("No field named {}. Possible fields include: {}".format(field, possible_fields))
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
                    print("No field named {}. Possible fields include: {}".format(field, possible_fields))
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
                print(str(skill['name']) + ': ' + str(skill['endorsements']))
        else:
            print("This method is only accessible for scraping individual profiles. "
                  "See the similar method for company profiles: ")

    def get_accomplishments(self, *args):
        """
        A method to return all accomplishments listed in the results dictionary of an individual profile
        :param args: Any number of string parameters corresponding to the achievement names listed below
        :return: Prints out name of the accomplishment and its type
        """
        possible_fields = ['publications', 'certifications', 'patents', 'courses', 'projects', 'honors', 'test_scores',
                           'languages', 'organizations']

        # Check for the mode of the target information
        if self.mode.lower() == 'individual' or self.mode.lower() == 'in':
            for accomplishment in args:
                if accomplishment not in possible_fields:
                    print("No field named {}. Possible fields include: {}".format(accomplishment, possible_fields))
                else:
                    print({accomplishment: self.results['accomplishments'][accomplishment]})
        else:
            print("This method is only accessible for scraping individual profiles. "
                  "See the similar method for company profiles: ")

    def get_interests(self):
        """
        A method to return all interests listed in the results dictionary of an individual profile
        :return: Prints out all interests
        """
        # Check for the mode of the target information
        if self.mode.lower() == 'individual' or self.mode.lower() == 'in':
            for interest in self.results['interests']:
                print(interest)
        else:
            print("This method is only accessible for scraping individual profiles. "
                  "See the similar method for company profiles: ")

    def get_overview(self, *args):
        """
        A method to retrieve all fields under overview section of results dictionary for company profiles
        :param args: Any number of string parameters corresponding to field names listed below
        :return: prints out fields that match given parameters
        """
        possible_fields = ['description', 'name', 'company_size', 'website', 'industry', 'headquarters', 'type',
                           'specialties', 'num_employees', 'image']
        if self.mode.lower() == 'company':
            for field in args:
                if field not in possible_fields:
                    print("No field named {}. Possible fields include: {}".format(field, possible_fields))
                else:
                    print({field: self.results['overview'][field]})
        else:
            print("This method is only accessible to scrape company profiles.")

    def get_jobs(self):
        """
        A method to retrieve job listings belonging to that company profile
        :return: prints out all the job listings
        """
        if self.mode.lower() == 'company':
            print(self.results['jobs'])
        else:
            print("This method is only accessible to scrape company profiles.")


if __name__ == '__main__':
    bot = LinkedinBot(
        cookie='AQEDAS_CpVgAZJtdAAABctX1xfEAAAFy-gJJ8U0Aw3faemVsziA2wOqaZZoexUuShwyibcvMf3TuQK5qnTAAiJDpMxfs3B2'
               'z0Fq0l-xdyf9d_0CJOcZ4gvLfL14thtyH2a6EbQXM-Ueh3tEQ00xiuXWA', value='spacex', mode='company')

    bot.get_overview('name', 'num_employees')
