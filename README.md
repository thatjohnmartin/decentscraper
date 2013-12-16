decentscraper
=============

A decent scraper of useful things.

About
-----

This is a blue collar scraper of HTML websites and JSON/XML APIs. It uses any and all manner of dirty text munging
and beautiful soup-ing to get to the good stuff.

It uses a simple system of providers and "x-" mimetypes to organize what types of things are available from where.

All values are returned as dictionaries of simple Python types, perfect for JSON-ification.

Example usage
-------------

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