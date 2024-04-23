import scrapy

class PokemonWikiSpider(scrapy.Spider):
    name = 'pokemon_wiki_spider'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Pokémon']
    max_pages = 100  # Adjusted max_pages parameter
    max_depth = 2  # Added max_depth parameter

    def parse(self, response):
        # Improved title extraction logic
        title = response.css('h1.firstHeading::text').get(default='').strip()
        
        paragraphs = response.css('div#bodyContent p::text').getall()

        yield {
            'title': title,
            'content': ' '.join(paragraphs).strip()  # Assuming this is your intended concatenation of paragraph texts
        }
