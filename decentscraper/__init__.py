__title__ = 'decentscraper'
__author__ = 'John Martin, Sam Wainwright, John Wainwright'
__license__ = 'MIT'
__copyright__ = 'Copyright 2013 John Martin, Sam Wainwright, John Wainwright'

from collections import defaultdict

# the list of registered scrapers
_SCRAPERS = defaultdict(dict)

def scrape(provider, resource, url):
    """Scrapes a resource at the provider with the URL."""
    return _SCRAPERS[provider][resource](url)

# import and register (via decorator) various scrapers
import mountain_project
import simbad
import super_topo
import wikipedia
