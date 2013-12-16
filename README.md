decentscraper
=============

A decent scraper of useful things.

Scrapers register themselves via a decorator:

    @scraper('wikipedia', 'x-astro-object-json')
    def wikipedia_astro_object(url):
        opener = build_opener()
        infobox, body = _parse_page(simplejson.loads(opener.open(url).read()))

        astro = {
            'name': _get_infobox_value(infobox, 'name'),
            'type': _get_infobox_value(infobox, 'type'),
            'constellation': _get_infobox_value(infobox, 'constellation'),
            'radius_ly': _get_infobox_value(infobox, 'radius_ly'),
        }

        return astro

And clients can request a scrape as follows:

    api_url = 'http://en.wikipedia.org/w/api.php?format=json&action=query&titles=%s'
    wiki_name = "Rosette_Nebula"
    astro_object_json = scrape('wikipedia', 'x-astro-object-json', API_URL % wiki_name)