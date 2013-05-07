#Python RCA

## Requirements

* Python 3.2

##Usage

```python
>>> import rca
>>> rca.send_rca("http://192.168.56.1:3000/commands", "volume", {"action":"up"})
(201, 'OK')
```

##Packaging

The module rca can be moved around freely in your project and has no further dependencies.

If required though a package can be built and installed system wide by executing

```bash
easy_install-3.2 .
```

in the checkout directory. `easy_install-3.2`'s specific name can vary depending your system setup.