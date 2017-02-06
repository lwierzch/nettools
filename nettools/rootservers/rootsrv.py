#!/usr/bin/python3

import re

class RootServers:
    """This is class for parsing locally cached root server hints file (ROOTHINTFILE) and exposing the list for further processing """

    ROOTHINTFILE = 'named.root'

    roothints = []
    rootservers = {}

    def __init__(self):
        try:
            with open(self.ROOTHINTFILE, 'r') as hintfile:
                self.roothints = hintfile.readlines()
        except Exception as error:
            print("oh no!", error)
        re_root_a = re.compile('([A-M]).ROOT-SERVERS.NET.      3600000      A     (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\n')
        re_root_aaaa = re.compile('([A-M]).ROOT-SERVERS.NET.      3600000      AAAA  (([0-9A-Fa-f]{1,4}:{1,2}){1,7}[0-9A-Fa-f]{1,4})\n')
        for line in self.roothints:
            match_v4 = re_root_a.match(line)
            if match_v4:
                if not match_v4.group(1) in self.rootservers:
                    self.rootservers[match_v4.group(1)] = {}
                self.rootservers[match_v4.group(1)]['v4'] = match_v4.group(2)
            match_v6 = re_root_aaaa.match(line)
            if match_v6:
                if not match_v6.group(1) in self.rootservers:
                    self.rootservers[match_v6.group(1)] = {}
                self.rootservers[match_v6.group(1)]['v6'] = match_v6.group(2)

    def printRootsV4(self):
        for rootserver in self.rootservers.keys():
            print(rootserver + ".ROOT-SERVERS.NET has IPv4 address " + self.rootservers[rootserver]['v4'])

    def printRootsV6(self):
        for rootserver in self.rootservers.keys():
            print(rootserver + ".ROOT-SERVERS.NET has IPv6 address " + self.rootservers[rootserver]['v6'])

    def getRootsV4(self):
        v4list = []
        for rootserver in self.rootservers.keys():
            v4list.append(self.rootservers[rootserver]['v4'])
        return v4list

    def getRootsV6(self):
        v6list = []
        for rootserver in self.rootservers.keys():
            v6list.append(self.rootservers[rootserver]['v6'])
        return v6list

    def getRoots(self):
        return self.getRootsV4() + self.getRootsV6()


