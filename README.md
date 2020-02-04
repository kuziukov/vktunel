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
```
