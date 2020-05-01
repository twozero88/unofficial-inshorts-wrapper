# unofficial-inshorts-API
Unofficial Inshorts API.Just adds headers to the already existing API and returns a clearer result

**You can skip The Story**
## The Story
So I was checking if there were any free APIs to get news from, couldn't find anything.
Thought of inshorts and scraped it using beautifulSoup.Returned a json with flask.
This worked well but had a limitation.It returned just top news items.

Then used a mobile and saw the requests,found an undocumneted api.Used it with headers of a mobile - device.
Cleaned some useless cuttlery.
Returned the json using flask.

## Usage
- Install Dependencies
- Run read.py

```localhost/<lang>/<category>/<number>```
  - categories -> 'top_stories','trending','all_news'
  - number-> number of news items you want
  
```localhost/topic/<lang>/<category>/<number>```
  - categories -> 'india','business','politics','sports','technology','startups','entertainment','hatke','international','automobile','science','travel','miscellaneous','fashion'
  - number-> Page Number of results that you want.

- lang can be 'en'(glish) or 'hi'(ndi)

### Dependencies
- Flask
- flask-cors
- requestss

*Try not calling the api again and again.Instead save results in your local database and fetch results from there.*
*Don't know anything about legal matter here.The API was pretty open*

