#!/usr/bin/python3

from ... import rootservers.RootServer as rs
from dns.resolver import dns
from random import randint as ri
import sys

rootservers = rs()
nameserver=rootservers.getRoots()[ri(0,len(rootservers.getRoots())-1)]
querytype = sys.argv[1]
query = sys.argv[2]
print("Asking for", querytype, "on", nameserver)
request = dns.message.make_query(query, dns.rdatatype._by_text[querytype])
response = dns.query.udp(request, nameserver)
print(response)

