import newspaper
import time

slate_paper = newspaper.build('http://slate.com', memoize_articles=False)
tc_paper = newspaper.build('http://techcrunch.com', memoize_articles=False)
espn_paper = newspaper.build('http://espn.com', memoize_articles=False)

papers = [slate_paper, tc_paper, espn_paper]

start_time = time.time()
for paper in papers:
    for content in paper.articles:
        content.download()
print(f"Time taken: {time.time() - start_time}")
