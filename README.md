# exchange-rate-spider
A spider for getting latest currency exchange rate from [Bank of Taiwan](https://rate.bot.com.tw/xrt?Lang=zh-TW), using Scrapy (Python).

## Usage
  
  * Scrape Without saving result:

    `scrapy crawl exchange_rate`
  
  * Scrape and save result as JSON format:
  
    `scrapy crawl exchange_rate -o exchange_rate_200116.json`
  
  * Scrape and save result as CSV format:
  
    `scrapy crawl exchange_rate -o exchange_rate_200116.csv`
    
## Reference

  1. [Scrapy](https://scrapy.org/)
