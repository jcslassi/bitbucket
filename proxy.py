#!/usr/bin/python
#
# awk '{print $1}' access.log | python % > /whatever/deny/ip/mechnism/u/use
#

import fileinput
from gevent import monkey
import urllib2
import gevent

monkey.patch_all()


def is_proxy(pip):    
    try:
        proxy_handler = urllib2.ProxyHandler({'http': pip})
        opener = urllib2.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib2.install_opener(opener)
        req = urllib2.Request('http://www.google.com')  # change the URL to test here
        urllib2.urlopen(req)
    except urllib2.HTTPError:
        return False
    except Exception:
        return False
    print pip


ips = []

for line in fileinput.input():
    ips.append(line.strip())

jobs = [gevent.spawn(is_proxy, ip) for ip in ips]
gevent.joinall(jobs)
