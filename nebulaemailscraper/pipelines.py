import json
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

    saved_emails = []

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        emails = adapter.get("emails")
        url = adapter.get("url")[0]

        if emails == [] or emails is None:
            raise DropItem(f"Droping item, no valid emails found in {url}")
        else:
            # Clean duplicate emails in the actual item
            emails = set(emails)
            emails = list(emails)
            clean_emails = list()

            # Drop items if contains blacklisted domains or file extensions.
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

            # Check if the actual item has been saved before
            else:
                url = "/".join(url.split("/")[:3])
                dict_domain = [data for data in self.saved_emails if data["url"] == url]
                if dict_domain == []:
                    # Not registered
                    self.saved_emails.append({"url": url, "emails": clean_emails})
                else:
                    # Registered
                    index_domain = self.saved_emails.index(dict_domain[0])
                    if clean_emails == self.saved_emails[index_domain]["url"]:
                        raise DropItem(f"Droping item, duplicate emails found in {url}")
                    else:
                        # Fuse old register with new register
                        clean_emails.extend(self.saved_emails[index_domain]["emails"])
                        clean_emails = set(clean_emails)
                        clean_emails = list(clean_emails)
                        self.saved_emails[index_domain]["emails"] = clean_emails

    def close_spider(self, spider):
        with open('emails.json', 'w') as file:
            file.write(json.dumps(self.saved_emails, indent=4))
