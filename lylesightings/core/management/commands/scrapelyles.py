from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from core.models import Sighting
import os
import json
import datetime

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        scraped_instas_path = os.path.join(settings.BASE_DIR, 'scrapings', 'lylesighting.json')
        print("file is {file}".format(file=scraped_instas_path))
        scrapings = json.loads(open(scraped_instas_path).read())
        for item in scrapings:
            url = "https://www.instagram.com/p/{0}/".format(item['shortcode'])
            timestamp = datetime.datetime.fromtimestamp(item['taken_at_timestamp'])
            if len(item['edge_media_to_caption']['edges']):
                caption = item['edge_media_to_caption']['edges'][0]['node']['text']
            else:
                caption = ""
            sighter = "scraper-{0}".format(item['owner']['id'])
            print(timestamp, url, caption, sighter)