# Price History Scrapper

# Build and Run your image

```
docker build -t price-history-scrapper .
```

```
docker run -p 5000:5000 price-history-scrapper
```

# Run Unit test

```
pytest
```

# Endpoints

- `POST` `localhost:5000/shopee/item` payload: `JSON` {"url": "https://shopee.co.id/CHiQ-43-Inch-Newest-Android-11-Frameless-Smart-TV-Digital-LED-TV-(L43G7P)-FHD-TV-i.505142432.11136823715"}
- `POST` `localhost:5000/shopee/shop` payload: `JSON` {"url": "https://shopee.co.id/chiqofficial"}
- `Swagger API Docs` `localhost:5000/docs`

# Deployed to Heroku

URL: [Here the API docs](https://scrapper-harga.herokuapp.com/docs)
