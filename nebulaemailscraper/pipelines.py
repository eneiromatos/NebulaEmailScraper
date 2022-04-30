from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class EmailsDetailsPipeline:
    domains_black_list = [
        "twitter.com",
        "google.com",
        "youtube.com",
        "wikipedia.com",
        "facebook.com",
        "instagram.com",
        ".jpg",
        ".jpeg",
        ".png",
        ".webp",
        ".pdf",
        ".zip",
        ".rar",
    ]

    saved_emails = []

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        emails = adapter.get("emails")
        url = adapter.get("url")[0]

        if emails == [] or emails is None:
            raise DropItem(f"Droping item, no valid emails found in {url}")
        else:
            emails = set(emails)
            emails = list(emails)
            clean_emails = list()

            for email in emails:
                is_black_listed = False
                for domain in self.domains_black_list:
                    if domain in email:
                        is_black_listed = True
                        break
                if not is_black_listed:
                    clean_emails.append(email)
            if clean_emails == []:
                raise DropItem(f"Droping item, no valid emails found in {url}")
            else:
                adapter["emails"] = clean_emails

                url = "/".join(url.split("/")[:3])
                adapter["url"] = url

                return item
