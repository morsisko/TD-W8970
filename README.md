# TD-W8970
Python library for scraping ADSL connection statistics from TD-W8970 router.

# Create router object
```python
router = router.Router(username="admin", password="admin")
```
You need to specify:
* Username - your router login (default: admin)
* Password - your router password (default: admin)
* Host - default gateway (default: 192.168.1.1)

# Get data
```python
stats = router.get(timeout=60)
```

You may specify:
* Timeout - in sec (default: 10s)

You may retrieve
* status_code - http status code (200 == OK)
* downstreamCurrRate
* downstreamMaxRate
* upstreamCurrRate
* upstreamMaxRate
* downstreamNoiseMargin
* downstreamAttenuation
* upstreamNoiseMargin
* upstreamAttenuation
* downstreamPower
* upstreamPower
