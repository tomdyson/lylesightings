# Lyle Sightings

Tracking Lyle sightings since 2018.

![Screenshot](lyles.jpg)

## Todo

 - [x] holding page
 - [x] sightings model
 - [ ] management command to import tagged instagrams
 - [ ] front-end styling
 - [ ] admin UI to approve / reject new photos
 - [ ] admin UI to override image data, e.g. location information
 - [ ] user whitelisting
 - [ ] map view
 - [ ] dokku deployment
 - [ ] apply for Instagram full API

## Developing

`pipenv shell`

## Notes

 - Instagram oEmbed options: https://www.instagram.com/developer/embedding/
 - Scraper, if necessary: https://github.com/rarcega/instagram-scraper
  - `instagram-scraper lylesighting --tag --media-metadata --latest --media-types=none -d scrapings`