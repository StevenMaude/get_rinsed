#!/usr/bin/env python
# encoding: utf-8
import lxml.html
import requests_cache
from dshelpers import download_url

BASE_URL = 'http://rinse.fm/podcasts/?page='


def extract_podcast_data_from_page(page_data):
    """ Extract podcast data from a page. """
    etree = lxml.html.fromstring(page_data)
    podcast_results = etree.xpath('//div[@class="borderbottom left '
                                  'podcast-list-item"]')

    for podcast_result in podcast_results:
        # data-air_day is canonical; site may list podcast visibly as being
        # on previous day (e.g. if aired at 1 AM), which is incorrect
        air_date = podcast_result.xpath('./@data-air_day')
        air_time = podcast_result.xpath('.//div[@class="date monobold '
                                        'grey px11 mt4"]')
        show_title = podcast_result.xpath('.//h3[@class="darkgrey headline '
                                          'px14 mb8"]')
        download_link = podcast_result.xpath('.//div[@class="download icon"]'
                                             '/a/@href')

        print air_date[0], air_time[0].text_content().strip(), \
            show_title[0].text_content().strip(), download_link[0]


def main():
    """ Process Rinse FM podcast pages. """
    requests_cache.install_cache(expire_after=600)
    page_url = BASE_URL + '1'
    page_content = download_url(page_url)
    extract_podcast_data_from_page(page_content.read())


if __name__ == '__main__':
    main()
