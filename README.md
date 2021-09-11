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

- `POST` `localhost:5000/shopee/item`

  payload: `JSON`
  ```
  {"url": "https://shopee.co.id/Logitech-G102-Lightsync-Gaming-Mouse-i.39400356.3840449468"}
  ```
  
- `POST` `localhost:5000/shopee/shop`

  payload: `JSON`
  ```
  {"url": "https://shopee.co.id/chiqofficial"}
  ```
  
- Swagger API Docs `localhost:5000/docs`

# Deployed to Heroku

URL: [API docs](https://scrapper-harga.herokuapp.com/docs)
