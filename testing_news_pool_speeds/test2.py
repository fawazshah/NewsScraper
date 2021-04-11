import newspaper
from newspaper import news_pool
import time

slate_paper = newspaper.build('http://slate.com', memoize_articles=False)
tc_paper = newspaper.build('http://techcrunch.com', memoize_articles=False)
espn_paper = newspaper.build('http://espn.com', memoize_articles=False)

papers = [slate_paper, tc_paper, espn_paper]

news_pool.set(papers, threads_per_source=3)

start_time = time.time()
print(start_time)
news_pool.join()
print(time.time())
print(f"Time taken: {time.time() - start_time}")
