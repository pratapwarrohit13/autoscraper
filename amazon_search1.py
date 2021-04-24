#!/usr/bin/env python
# coding: utf-8


from autoscraper import AutoScraper
amazon_url = "https://www.amazon.in/s?i=aps&k=iphone"

wanted_list = ["New Apple iPhone 12 Pro Max (128GB) - Pacific Blue","₹1,25,900"]

scraper = AutoScraper()

result = scraper.build(amazon_url,wanted_list)

print(scraper.get_result_similar(amazon_url,grouped=True))




scraper.set_rule_aliases({"rule_1943":"Title",
                          "rule_1gc6":"MRP"})

scraper.keep_rules(["rule_1943","rule_1gc6"])
scraper.save("amazon_search")






