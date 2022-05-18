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
from scrapy.loader.processors import Compose, TakeFirst
from scrapy.exceptions import DropItem


def discard_email(email: str):
    BLACK_LIST = [
        "twitter.com",
        "google.com",
        "youtube.com",
        "wikipedia.com",
        "facebook.com",
        "instagram.com",
        "scribd.com",
        "fiverr.com",
        ".jpg",
        ".jpeg",
        ".png",
        ".webp",
        ".pdf",
        ".zip",
        ".rar",
        ".txt",
    ]
    for domain in BLACK_LIST:
        if domain in email:
            raise DropItem('email with domain in black list')


class EmailItem(scrapy.Item):
    url = scrapy.Field(output_processor=TakeFirst())
    emails = scrapy.Field(output_processor=Compose(discard_email))