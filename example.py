from TDW8970 import router
import time

router = router.Router(username="admin", password="admin")

while True:
    stats = router.get(timeout=60)
    print(stats.downstreamCurrRate, "/", stats.downstreamMaxRate)
    print(stats.upstreamCurrRate, "/", stats.upstreamMaxRate)
    print(stats.downstreamNoiseMargin, "/", stats.upstreamNoiseMargin)
    print(stats.downstreamAttenuation, "/", stats.upstreamAttenuation)
    print(stats.downstreamPower, "/", stats.upstreamPower)

    print("\n\n")
    time.sleep(30)