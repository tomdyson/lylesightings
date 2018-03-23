import json
import subprocess
import requests
import os
from datetime import datetime
from urllib.parse import urlparse
from django.core.management.base import BaseCommand, CommandError
from django.core.files import File
from django.conf import settings
from django.db.utils import IntegrityError
from core.models import Sighting

class Command(BaseCommand):
    help = 'Scrapes Instagram for posts tagged #lylesighting'

    scrapings_dir = os.path.join(settings.BASE_DIR, 'scrapings')

    def _fetchJSON(self):
        """instagram-scraper lylesighting --tag --media-metadata --latest --media-types=none -d scrapings"""
        subprocess.call([
            "instagram-scraper",
            "lylesighting",
            "--tag",
            "--media-metadata",
            "--latest",
            "--media-types=none",
            "-d",
            self.scrapings_dir
        ])



    def _parseJSON(self, file):
        posts = []
        items = json.loads(open(file).read())
        for item in items:
            post = {}
            url = "https://www.instagram.com/p/{0}/".format(item['shortcode'])
            timestamp = datetime.fromtimestamp(item['taken_at_timestamp'])
            edges = item['edge_media_to_caption']['edges']
            if len(edges):
                caption = edges[0]['node']['text']
            else:
                caption = ""
            sighter = "scraper-{0}".format(item['owner']['id'])
            post['url'] = url
            post['timestamp'] = timestamp
            post['caption'] = caption
            post['sighter'] = sighter
            post['photo'] = item['display_url']
            posts.append(post)
        return posts


    def handle(self, *args, **options):
        self._fetchJSON()
        scrapings_file = os.path.join(self.scrapings_dir, 'lylesighting.json')
        posts = self._parseJSON(scrapings_file)
        for post in posts:
            sighting = Sighting()
            sighting.url = post['url']
            sighting.datetime = post['timestamp']
            sighting.description = post['caption']
            sighting.sighter = post['sighter']
            # fetch the image
            print('fetching image ' + post['photo'])
            url = post['photo']
            r = requests.get(url)
            filename = os.path.basename(urlparse(url).path)
            with open(filename, 'wb') as f:
                f.write(r.content)
            reopen = open(filename, 'rb')
            django_file = File(reopen)
            sighting.photo = django_file
            try:
                sighting.save()
            except(IntegrityError):  # fail on duplicates
                print('could not insert sighting ' + sighting.url)
            os.remove(filename)