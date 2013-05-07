#Python RCA

## Requirements

* Python 3.2

##Usage

```python
>>> import rca
>>> rca.send_rca("http://192.168.56.1:3000/commands", "volume", {"action":"up"})
(201, 'OK')
```