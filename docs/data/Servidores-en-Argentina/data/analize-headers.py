import json

fil='/home/junar/andres/devs/OpenDataCordoba/website/NICathon/data/works/servers-headers-final.json'

data = json.load(open(fil))
print '%d registros' % len(data)

fil_dest='servers.csv'
f = open(fil_dest, 'w')
f.write('"id", "domain", "server name", "server version", "powered name", "powered version", "server pure", "powered pure"')

servers={}
servers_version={}

powereds={}
powereds_version={}

for header in data:
    server = header.get('server','')
    if len(server.split(',')) > 1:
        server = server.split(',')[0] # ignore second server

    #Suposed SERVER/Version (space) +extras
    parts = server.split('/')
    s1 = parts[0]
    if len(parts) > 1:
        s2 = parts[1].split(' ')[0]
        #Change A.B.C to A.B
        ver = s2.split('.')
        if len(ver) > 2:
            s2 = '%s.%s' %(ver[0], ver[1])
    else:
        s2 = ''

    if s1 != '':
        if servers.get(s1, False):
            servers[s1] = servers[s1] + 1
        else:
            servers[s1] = 1

        sv = '%s_%s' % (s1, s2)
        if servers_version.get(sv, False):
            servers_version[sv] = servers_version[sv] + 1
        else:
            servers_version[sv] = 1
        
    powered = header.get('x-powered-by','')
    if len(powered.split(',')) > 1:
        powered = powered.split(',')[0] # ignore second powered

    #Suposed powered/Version (space) extras
    parts = powered.split('/')
    p1 = parts[0]
    if len(parts) > 1:
        p2 = parts[1].split(' ')[0]
    else:
        p2 = ''


    if p1 != '':
        if powereds.get(p1, False):
            powereds[p1] = powereds[p1] + 1
        else:
            powereds[p1] = 1

        pv = '%s_%s' % (p1, p2)
        if powereds_version.get(pv, False):
            powereds_version[pv] = powereds_version[pv] + 1
        else:
            powereds_version[pv] = 1


    f.write('\n')
    f.write('%s, "%s", "%s", "%s", "%s", "%s", "%s", "%s"' % (header['domain_id'], header['domain_name'], s1, s2, p1, p2, server, powered))
    

f.close()

resumen = 'servers_resumen.csv'
f2 = open(resumen, 'w')
f2.write('"server", "cantidad"')
for s,v in servers.iteritems():
    f2.write('\n')
    f2.write('%s, "%d"' % (s, v))
f2.close()

resumen = 'servers_version_resumen.csv'
f2 = open(resumen, 'w')
f2.write('"server_version", "cantidad"')
for s, v in servers_version.iteritems():
    f2.write('\n')
    f2.write('%s, "%d"' % (s, v))

f2.close()

resumen = 'powered_resumen.csv'
f2 = open(resumen, 'w')
f2.write('"powered", "cantidad"')
for s, v in powereds.iteritems():
    f2.write('\n')
    f2.write('%s, "%d"' % (s, v))
f2.close()

resumen = 'powered_version_resumen.csv'
f2 = open(resumen, 'w')
f2.write('"powered_version", "cantidad"')
for s, v in powereds_version.iteritems():
    f2.write('\n')
    f2.write('%s, "%d"' % (s, v))

f2.close()
