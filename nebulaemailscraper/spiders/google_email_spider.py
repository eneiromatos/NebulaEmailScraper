"""
Nebula Email Scraper: is designed to scrape emails based on specific keyword
using major search engines like Google.

Copyright (C) 2022.  Eneiro A. Matos B.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import scrapy
from scrapy.exceptions import CloseSpider
from scrapy.loader import ItemLoader
from ..items import EmailItem


class GoogleEmailSpiderSpider(scrapy.Spider):
    name = "google_email_spider"

    KW_FILE = "keywords.txt"

    def start_requests(self):
        try:
            keywords = open(self.KW_FILE, encoding="utf-8").readlines()
        except FileNotFoundError:
            with open(self.KW_FILE, mode="w", encoding="utf-8"):
                pass
            raise CloseSpider(
                "Put your keywords in the keywords file and run again the spider."
            )

        for keyword in keywords:
            if keyword == "\n":
                continue
            keyword = keyword.strip().rstrip("\n").casefold()
            url = f"https://www.google.com/search?q={keyword}&num=100&start=0"
            yield scrapy.Request(url, self.parse_google, priority=2)

    def parse_google(self, response):
        CONTACT_URLS = [
            "/contacto",
            "/contact",
            "/contact-us",
        ]

        target_urls = response.css("a[data-ved]::attr(href)").getall()
        target_domains = [
            f'https://{url.split("/")[2]}' for url in target_urls if "://" in url
        ]
        contact_domains = [
            url + urlc for url in target_domains for urlc in CONTACT_URLS
        ]
        next_url = response.css("a#pnnext::attr(href)").getall()

        yield from response.follow_all(target_domains, self.parse_emails, priority=1)
        yield from response.follow_all(contact_domains, self.parse_emails, priority=3)
        yield from response.follow_all(next_url, self.parse_google, priority=4)

    def parse_emails(self, response, **kwargs):
        selector = response.css("body")
        email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,20}"

        item = ItemLoader(EmailItem(), selector)
        item.add_value("url", response.url)
        item.add_css("emails", "body", re=email_pattern)
        yield item.load_item()
