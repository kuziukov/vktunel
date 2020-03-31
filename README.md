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
    "price": 99,
    "limits": {
      "numberOfAlbums": 20,
      "numberOfPhotos": 4000,
     },
     "active": true
  }
)

db.plans.insert(
  {
    "number": 2,
    "title": "Кофе с пироженкой",
    "desc": "Тариф по стоимости кофе с пироженкой подходит для большинства повседневных задач",
    "price": 199,
    "limits": {
      "numberOfAlbums": 60,
      "numberOfPhotos": 10000,
     },
     "active": true
  }
)

db.plans.insert(
  {
    "number": 3,
    "title": "Без ограничений",
    "desc": "Неограниченные возможности использования сервиса",
    "price": 299,
    "limits": {
      "numberOfAlbums": 20000,
      "numberOfPhotos": 20000,
     },
     "active": true
  }
)
```
