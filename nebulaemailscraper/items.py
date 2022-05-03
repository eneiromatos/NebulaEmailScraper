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


class EmailItem(scrapy.Item):
    url = scrapy.Field()
    emails = scrapy.Field()


class ProjectDetailsItem(scrapy.Item):
    scraped_at = scrapy.Field()
