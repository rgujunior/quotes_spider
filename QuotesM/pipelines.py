import os
import pandas as pd


class QuotesPipeline:
    def __init__(self):
        self.quotes = []

    def process_item(self, item, Quotes):
        self.quotes.append(item)
        return item

    def close_spider(self, Quotes):
        os.makedirs("quotes_txt", exist_ok=True)
        for index, quote in enumerate(self.quotes, start=1):
            with open(f"quotes_txt/quote_{index}.txt", "w", encoding="utf-8") as f:
                f.write(quote["text"])

        # Armazenar em arquivo CSV
        df = pd.DataFrame(self.quotes)
        df["page_number"] = Quotes.settings.get("CURRENT_PAGE_NUMBER")
        df["rule_number"] = Quotes.settings.get("CURRENT_RULE_NUMBER")
        df.to_csv("quotes.csv", sep=";", encoding="utf-8-sig", index=False)
