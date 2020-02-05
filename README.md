# vktunel


```
Установить время жизни файлов в GridFS
db.files.ensureIndex({"uploadDate" : 1},{expireAfterSeconds : XXX})
```

Mongo

```
use admin
db.createUser(
  {
    user: "myUserAdmin",
    pwd: passwordPrompt(), // or cleartext password
    roles: [ { role: "userAdminAnyDatabase", db: "admin" }, "readWriteAnyDatabase" ]
  }
)
```


```
use admin
db.plans.insert(
  {
    "number": 0,
    "title": "Бесплатно",
    "desc": "Тариф бесплатный",
    "price": 0,
    "limits": {
      "numberOfAlbums": 10,
      "numberOfPhotos": 1000,
     },
     "active": true
  }
)

db.plans.insert(
  {
    "number": 1,
    "title": "Чашечка кофе",
    "desc": "Тариф по стоимости чешечки кофе открывает более широкие возможности",
    "price": 100,
    "limits": {
      "numberOfAlbums": 20,
      "numberOfPhotos": 20000,
     },
     "active": true
  }
)

db.plans.insert(
  {
    "number": 2,
    "title": "Кофе с пироженкой",
    "desc": "Неограниченные возможности использования сервиса",
    "price": 200,
    "limits": {
      "numberOfAlbums": 20000,
      "numberOfPhotos": 20000,
     },
     "active": true
  }
)
```
