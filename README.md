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
