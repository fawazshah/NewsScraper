import collections
import json
import newspaper

year_freqs = collections.defaultdict(lambda: 0)

with open('EMNLP18NewsSources.json') as f:
    news_sources = json.load(f)

for i, (company, value) in enumerate(news_sources.items()):
    url = value["link"]
    paper = newspaper.build(url, memoize_articles=False)
    print(f"NEWS SITE {i+1} OUT OF {len(news_sources)}")
    print(f"Number of articles: {len(paper.articles)}")

    error_count = 0

    article_count = 0
    for content in paper.articles:
        if error_count > 5:
            break

        try:
            content.download()
            content.parse()
        except Exception as err:
            print(err)
            error_count += 1
            print("continuing...")
            continue

        if content.publish_date is None or content.publish_date == '':
            print(f"Can't find article publish date, skipping...")
            error_count += 1
            continue

        year_freqs[content.publish_date.year] += 1
    
    print(sorted(year_freqs.items()))

# for prop, value in vars(content).items():
#     print(f"{prop}")
