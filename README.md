# Drone fleet

Test for Musala

## Setting up project

### Install dependencies

tbd

### Run migrations

```
./manage.py migrate
```

## Start project (in dev)

```
./manage.py runserver 8000
```

## Endpoints documentation

- `GET api/drones`: get list of drones
- `GET drones/<drone_id>/medications`: get list of medications by drone id (drone_id)
- `GET api/medications`: get list of medications

> Note: The postman collections can be found in the directory *./postman*

## Author

- [Raciel](http://website)
