def search(search_queries):
    row = {}
    for i in search_queries:
        length = len(i.split())
        if length in row:
            row[length] += 1
        else:
            row[length] = 1
    total_q = len(search_queries)
    res = {key: round(val/total_q * 100) for key, val in row.items()}
    return res

search_queries = [
    "watch new movies",
    "coffee near me",
    "how to find the determinant",
    "python",
    "data science jobs in UK",
    "courses for data science",
    "taxi",
    "OpenAI",
    "yandex",
    "bing",
    "foreign exchange rates USD/BYN",
    "Netflix movies watch online free",
    "Statistics courses online from top universities"
]

res = search(search_queries)
for k, v in sorted(res.items()):
    print(f'{k} слов: {v}%')