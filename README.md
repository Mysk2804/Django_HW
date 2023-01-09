# Типовые команды для управлнием Умный дом


```json
{   
  "name": "Датчик 1",
  "description": "На кухне."
}
```

```json
POST "http://127.0.0.1:7070/api/measurements/":
{ 
  "id_sensor": "1",
  "temperature": "32"
}
```

```python
GET "http://127.0.0.1:7070//api/sensors/1"
```
