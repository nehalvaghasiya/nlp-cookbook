# pip install newspaper3k nltk

from newspaper import Article
import nltk

nltk.download("punkt")

url = "https://mathdatasimplified.com/2023/05/08/build-an-efficient-data-pipeline-is-dbt-the-key/"
article = Article(url)
article.download()
article.parse()

print(article.title) # 'What is dbt (data build tool) and When should you use it?'

print(article.publish_date) # 2023-05-08 00:00:00

print(article.top_image) # article.top_image

print(article.nlp())

print(article.keywords) 
"""['tool',
 'changes',
 'build',
 'dbt',
 'model',
 'documentation',
 'sql',
 'data',
 'select',
 'models',
 'property_type']"""

print(article.summary)
"""
One tool that has gained popularity in recent years for managing data pipelines is dbt (data build tool).
When Should You Consider dbtYou should consider using dbt when:You have a data warehouse: dbt is an effective tool for organizing, transforming, and testing data in a data warehouse environment.
Your data changes frequently: dbt’s snapshot allows you to track changes in data over time.
Other tools are needed for tasks such as data extraction, data cleansing, and data loading.
You want to visualize your data: dbt is not a data visualization tool.
"""

