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
    name = "googleemailspider"

    KW_FILE = "keywords.txt"

    EMAIL_PATTERN = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,20}"

    CONTACT_URLS = [
        "/contacto",
        "/contact",
        "/contact-us",
    ]

    GOOGLE_HEADERS = {
        "authority": "www.google.com",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "es-ES,es;q=0.9,en;q=0.8,pt;q=0.7",
        "cookie": "AEC=AakniGOe-i-la-2Idsu90SaVYRCfzN0F8RcEiJkg4qB78IAj_a2UrkFkAw; SID=KAjWnwdMtFbB4PZARVvsjuiYx_zY9l58JAphgzTJn8Lo12jlJVsKLQ9kqm0sNgUwlVD04Q.; __Secure-1PSID=KAjWnwdMtFbB4PZARVvsjuiYx_zY9l58JAphgzTJn8Lo12jlNJEste1m-2qgUAwbUNMVuQ.; __Secure-3PSID=KAjWnwdMtFbB4PZARVvsjuiYx_zY9l58JAphgzTJn8Lo12jl_jQL_UzmgRtNwdwuJj21aw.; HSID=AYg5dCqSdg2-oqH0Y; SSID=AReHTR-8wES7gk-f6; APISID=1sp7rlwto8xISLzy/AxLydknUjOCYN0PtK; SAPISID=ayymuOGNEq-vZNAf/AojHa1ztOOGUt0WmU; __Secure-1PAPISID=ayymuOGNEq-vZNAf/AojHa1ztOOGUt0WmU; __Secure-3PAPISID=ayymuOGNEq-vZNAf/AojHa1ztOOGUt0WmU; NID=511=dE2j4Cx533VNbg1yJj6WahAr_De83__Sa4_kulEX2kBvpNiTwMqyZb0SXk7uMuD9OgUdD4ORE-we7zw35g8R2ChFv2V9rGUviHyspS_ogaNwlIBkNinyzsl_PCs4bQGkXv-XCvkc23KIWEcvvXIofn0M9E7ZZcAvTt4Kqoz6Tftq-DbC1R5MWArZjLzI9V5G49l1E7072vlcCF2sjrwB2qXfAE2VtVmzzy-EOgjCY1i3yPAhQm4J2PcVqnzxbuLSygrXPCAJ4JF1lvOe5W0; 1P_JAR=2022-05-18-19; DV=ExmPqzBraHobMGXCIkB2f6jwmcqJDRg; SIDCC=AJi4QfEjpPOo6TboB7188UDHVhyzvgKW6qhewy-95noFjhYBP5cdQkgVZyobqYMVoDfX-I5QOw; __Secure-3PSIDCC=AJi4QfHRlqQEUsIRaZhdNMCcNG70jHEUYaeOLthiPVGSpvBanV3GLsquQFZedZFmIs1-s3bneQ",
        "dnt": "1",
        "referer": "https://www.google.com/",
        "sec-ch-dpr": "1",
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        "sec-ch-ua-arch": '"x86"',
        "sec-ch-ua-bitness": '"64"',
        "sec-ch-ua-full-version": '"101.0.4951.67"',
        "sec-ch-ua-full-version-list": '" Not A;Brand";v="99.0.0.0", "Chromium";v="101.0.4951.67", "Google Chrome";v="101.0.4951.67"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-model": '""',
        "sec-ch-ua-platform": '"Windows"',
        "sec-ch-ua-platform-version": '"7.0.0"',
        "sec-ch-ua-wow64": "?0",
        "sec-ch-viewport-width": "1366",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36",
        "x-client-data": "CI22yQEIpbbJAQjBtskBCKmdygEIydLKAQj+5MoBCJOhywEI2+/LAQie+csBCOaEzAEIi5TMAQiyqcwBCP+qzAEI6qvMAQjDrMwBCLKuzAEIpK/MARirqcoB",
    }

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
            yield scrapy.Request(url, self.parse_google, headers = self.GOOGLE_HEADERS)

    def parse_google(self, response):
        target_urls = response.css("a[data-ved]::attr(href)").getall()
        target_domains = [
            f'https://{url.split("/")[2]}' for url in target_urls if "://" in url
        ]
        next_url = response.css("a#pnnext::attr(href)").getall()

        yield from response.follow_all(target_domains, self.parse_emails)
        yield from response.follow_all(next_url, self.parse_google)

    def parse_emails(self, response):
        contact_domains = [response.urljoin(url) for url in self.CONTACT_URLS]

        item = ItemLoader(EmailItem(), response)
        item.add_value("url", response.url)
        item.add_css("emails", "body", re=self.EMAIL_PATTERN)
        yield item.load_item()

        yield from response.follow_all(contact_domains, self.parse_emails)
