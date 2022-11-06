# Drone fleet

Test for Musala

## Setting up project

### Install dependencies

```
docker-compose build
```

### Run migrations

```
docker-compose exec web python manage.py migrate
```

## Start project (in dev)

```
docker-compose up -d
```

## Load data in db (fixtures)

```
docker-compose exec web python manage.py loaddata drones.json (optional, drone can be created by api)
docker-compose exec web python manage.py loaddata medications.json
```


## Endpoints documentation

- `GET api/drones`: get list of drones
- `GET api/drones/<drone_id>/medications`: get list of medications by drone id (drone_id)
- `POST api/drones/<drone_id>/add_medications`: Add list of medications to drone id (drone_id)
- `GET api/drones/<drone_id>/battery_level`: Check battery level of drone id (drone_id)
- `GET api/drones/availables`: Get available drones for load
- `GET api/drones/battery_level_history`: Check periodic task history of battery levels
- `GET api/medications`: get list of medications

> Note: The postman collections can be found in the directory *./postman*

## Author

- [Raciel](http://website)
