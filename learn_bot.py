from scrape_linkedin import ProfileScraper
from scrape_linkedin import CompanyScraper


with ProfileScraper(
        cookie='AQEDAS_CpVgAZJtdAAABctX1xfEAAAFy-gJJ8U0Aw3faemVsziA2wOqaZZoexUuShwyibcvMf3TuQK5qnTAAiJDpMxfs3B2'
               'z0Fq0l-xdyf9d_0CJOcZ4gvLfL14thtyH2a6EbQXM-Ueh3tEQ00xiuXWA') as scraper:
    profile = scraper.scrape(user='austinoboyle')

print(help(profile))
