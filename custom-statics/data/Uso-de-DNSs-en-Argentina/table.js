$(document).ready(function() {
	
    dataset =  [       

        ['SIN DNS', '46885'], 
['ns21.dattatec.com', '21898'], 
['ns3.hostmar.com', '21616'], 
['ns1.sedoparking.com', '14198'], 
['ns1.elserver.com', '12839'], 
['ns1.dnspoint.net', '10497'], 
['ns1.godns.net', '6580'], 
['dns1.servidoraweb.net', '6083'], 
['ns1.cdmon.net', '6002'], 
['ns01.000webhost.com', '4347'], 
['ns1.dreamhost.com', '4138'], 
['dns1.www.com.ar - 190.61.5.251', '4037'], 
['ns1.nuthost.com', '4008'], 
['ns1.allytech.com', '3846'], 
['ns1.donweb.com', '3680'], 
['ns1.mydomain.com', '3144'], 
['ns1.afraid.org', '3138'], 
['ns1.hostinger-ar.com', '3000'], 
['dns1.cvtci.com.ar - 24.232.0.17', '2663'], 
['ns1.wiroos.com', '2529'], 
['ns3.freeservers.com', '2448'], 
['ns1.mesi.com.ar - 69.25.11.11', '2394'], 
['dns1.sucursalonline.com', '2204'], 
['ns1.dixnet.com', '2050'], 
['ns1.lineadns.com', '2039'], 
['ns1.towebs.com', '1814'], 
['dns1.iplanisp.com.ar - 200.69.193.111', '1728'], 
['ns1.mediatemple.net', '1389'], 
['ns1.bluehost.com', '1310'], 
['ns1.datawebdns.com', '1250'], 
['ns1.outdns.net', '1224'], 
['ns1.wix.com', '1131'], 
['dns1.calu.net', '1085'], 
['ns1.unlugar.com', '1078'], 
['gulp.arnet.com.ar - 200.45.0.115', '989'], 
['ns10.hosting-ar.com', '986'], 
['ns1.sitelutions.com', '930'], 
['ns35.tudns35.info', '862'], 
['ns1.duplika.com', '853'], 
['dns1.dnslatino.com', '808'], 
['ns9.hostmar.com', '772'], 
['ns1.mesi.com.ar', '761'], 
['dns1.advance.com.ar - 209.13.119.20', '746'], 
['ns1.netfirms.com', '746'], 
['ns1.dnsprivados13.com', '738'], 
['dns1.cscdns.net', '731'], 
['dns1.stabletransit.com', '730'], 
['NS1.HOSTMONSTER.COM', '709'], 
['dns1.www.com.ar', '692'], 
['ns01.trademarkarea.com', '687'], 
['dns1.wavenet.com.ar - 181.119.19.5', '681'], 
['ns5.hostmar.com', '652'], 
['ns1.huxley.com.ar - 200.43.193.119', '627'], 
['dns1.grupoxmundo.com', '605'], 
['ns10.bahiaservers.com', '603'], 
['ns.rednetargentina.net', '602'], 
['dns1.alsolnet.com', '588'], 
['ns1.dnsprivados21.info', '586'], 
['ns1.sitioshispanos.com', '583'], 
['ns2.zoneedit.com', '574'], 
['ns.datamarkets.com.ar - 200.32.3.129', '555'], 
['ns1.digitalocean.com', '529'], 
['ns1.linode.com', '498'], 
['ns1.mardelhosting.net', '491'], 
['ns1.g2khosting.com', '482'], 
['ns3.zoneedit.com', '475'], 
['ns1.infocomercial.net', '471'], 
['ns1.gblx.net.ar - 200.0.194.44', '462'], 
['ns1.sinectis.com.ar - 216.244.192.2', '459'], 
['dinamic1.cdmon.net', '443'], 
['dns1.cvtci.com.ar', '439'], 
['ns1.ibizdns.com', '436'], 
['ns1.dnscheck.com.ar - 190.228.129.101', '432'], 
['ns3.networktechinternational.com', '425'], 
['ns1.webfaction.com', '422'], 
['dns1.hostingtelefonica.com.ar', '415'], 
['ns1.arsesco.com.ar - 190.228.129.103', '410'], 
['ns1.digitar.net', '397'], 
['ns1.awardspace.com', '383'], 
['dnsps1.mercadolibre.com', '373'], 
['ns1.justhost.com', '363'], 
['mns01.domaincontrol.com', '361'], 
['ns5.dixnet.com', '357'], 
['ns1.mimejorhosting.com', '355'], 
['ns1.cecenet.net', '352'], 
['ns1.bodis.com', '344'], 
['ns7.zoneedit.com', '344'], 
['ns1.byet.org', '339'], 
['dns1.iplanisp.com.ar', '336'], 
['ns1.hrdns.info', '335'], 
['ns1.dnsexit.com', '335'], 
['ns1.buscadorprop.com', '332'], 
['ns13.zoneedit.com', '330'], 
['ns1.markmonitor.com', '324'], 
['pdns05.domaincontrol.com', '321'], 
['ns1.hostingmatrix.net', '311'], 
['ns.pageimpact.com', '311'], 
['ns3.unlugarnet.com', '310'], 
['ns1.he.net', '309'], 
['ns1.aper.net', '307'], 
['ns-0.net', '306'], 
['ns1.abcweb.com.ar - 190.210.10.242', '304'], 
['ns1.ipage.com', '302'], 
['ns1.main-hosting.com', '299'], 
['ns8.zoneedit.com', '295'], 
['dns1.ipaddress.com.ar - 200.69.135.251', '295'], 
['ns1.raqdns.net', '291'], 
['ns1.fastpark.net', '291'], 
['ns1.telmex.net.ar - 200.61.33.2', '287'], 
['ns177.websitewelcome.com', '280'], 
['ns6.hosting-ar.com', '279'], 
['ns1.hostinger.es', '279'], 
['ns1.domainamesystem.com.ar - 108.59.251.202', '279'], 
['NS1.101DOMAIN.COM', '272'], 
['s2.redynet.com.ar - 200.69.11.10', '268'], 
['dns1.baehost.com.ar - 200.110.149.236', '266'], 
['o200.prima.com.ar - 200.42.0.108', '263'], 
['ns1.consulred.net', '258'], 
['ns0.sion.com', '253'], 
['ns11.unlugarnet.com', '253'], 
['ns5.microtech3.com', '250'], 
['ns4.zoneedit.com', '250'], 
['ns51.1and1.com', '250'], 
['ns3.nombre-del-dominio.com', '249'], 
['ns3.hosting-ar.com', '248'], 
['ns1.dywebhosting.com', '246'], 
['ns1-rock.serverdnspoint.com', '243'], 
['ns1.tanservers.com', '242'], 
['ns1.dns-principal.com', '242'], 
['ns9.unlugarnet.com', '237'], 
['dns1.localhost.net.ar - 181.177.200.5', '237'], 
['srv487.infranetworking.com', '235'], 
['ns1.tusitioya.com', '235'], 
['dns1.freehostia.com', '233'], 
['ns1.signalar.net', '233'], 
['ns12.zoneedit.com', '230'], 
['ns1.subituweb.com', '229'], 
['ns1.servidordetarsis.net', '225'], 
['ns1.netnames.net', '225'], 
['ns1.alpha2000.com.ar - 200.85.190.10', '224'], 
['ns1.aliasdns6.net', '223'], 
['ns1.gtodo.com.ar - 200.110.156.67', '223'], 
['ns.rackspace.com', '222'], 
['dns1.alias2.net', '217'], 
['ns1.astranetwork.net', '214'], 
['dns1.idp365.net', '213'], 
['ns3.opcionestelmex.com.ar - 200.69.128.104', '213'], 
['freedns1.registrar-servers.com', '211'], 
['ns1.aliasdns.net', '210'], 
['dns1.neosites.com', '209'], 
['ns7.unlugarnet.com', '209'], 
['dns1.topserverhome.net', '208'], 
['dns.site5.com', '208'], 
['ns1.santafenoc.com', '207'], 
['ns1.3tristestigres.com', '205'], 
['ns1.altomarketing.net', '202'], 
['ns1.raqlink.com', '202'], 
['dns1.baehost.com.ar', '198'], 
['mundo.netizen.com.ar - 200.49.96.16', '194'], 
['ns1.unlugarnet.com', '193'], 
['ns1.mapaprop.com', '193'], 
['ns3.tanservers.com', '192'], 
['ns5.ibumu.com', '191'], 
['ns1.dnsprivados27.info', '190'], 
['ns1.instradns.com', '189'], 
['ns1.oikoss.net', '189'], 
['ns1.net-dns.biz', '183'], 
['ns1.qobeda.com.ar - 200.69.246.129', '181'], 
['nsl13.geouniverse.com', '181'], 
['ns1.hoztingweb.com', '179'], 
['ns25.domaincontrol.com', '178'], 
['ns1.argentina-hosting.com', '177'], 
['ns1.techtel.com.ar - 200.69.128.1', '176'], 
['ns1.intermedia.com.ar - 200.69.1.130', '173'], 
['ns1.ibumu.com', '172'], 
['ns1.overdns.com', '172'], 
['ns1.aypdns.net', '171'], 
['ns1.milliwatt.com.ar - 88.198.21.194', '171'], 
['ns1.santafehost.com', '171'], 
['ns10.dnsmadeeasy.com', '170'], 
['ns1-rock.netservicesargentina.com', '168'], 
['dns01.ebox.com.ar - 190.210.166.81', '167'], 
['ns.inmotionhosting.com', '166'], 
['magma.avnam.net', '165'], 
['ns1.minuto21.com', '162'], 
['ns1.coninfo.net', '162'], 
['ns1.aliasdns4.net', '160'], 
['ns51.domaincontrol.com', '159'], 
['ns1.servidordetarsis.com', '159'], 
['ns16.zoneedit.com', '159'], 
['ns1.eurodns.com', '158'], 
['ns1.dns-principal-2.com', '158'], 
['cebra.avnam.net', '156'], 
['dns1.globalgate.com.ar - 200.0.185.100', '156'], 
['rcc0001.rcc.com.ar - 200.47.24.17', '156'], 
['ns1.merlintech.com.ar - 200.59.205.97', '154'], 
['ns18.zoneedit.com', '154'], 
['mandril.avnam.net', '153'], 
['ns1.dns-click.net', '153'], 
['gulp.arnet.com.ar', '153'], 
['ns1.powersite.com.ar - 88.198.25.139', '152'], 
['dns1.wilnet.com.ar - 200.2.127.145', '152'], 
['ns3.ibumu.com', '152'], 
['ns14.zoneedit.com', '152'], 
['dns1.wavenet.com.ar', '151'], 
['toro.avnam.net', '151'], 
['ns1.pipedns.com', '151'], 
['pdns03.domaincontrol.com', '150'], 
['ns0.dnsmadeeasy.com', '147'], 
['ns1.puentedigital.com', '146'], 
['ns1.servidoronline.net', '146'], 
['ns1.powered-hosting.com', '144'], 
['ns1.silice.biz', '144'], 
['ns1.grupo-todo.com', '143'], 
['ns1.lightfaro.com', '142'], 
['ns3.dns-principal-2.com', '141'], 
['ns1.dnsmaestro.com', '141'], 
['pdns1.cscdns.net', '141'], 
['ns1.panelboxmanager.com', '141'], 
['ns57.1and1.com', '140'], 
['ns1.viacero.net', '140'], 
['ns1.santafehost.net', '139'], 
['ns1.beewh.com', '139'], 
['ns5.unlugarnet.com', '138'], 
['ns1.empresacorp.com', '135'], 
['ns1.host-argentina.com', '134'], 
['nsl14.viafacil.com', '133'], 
['fox.avnam.net', '132'], 
['ns3.miwiredhosting.com', '132'], 
['ns1.bmsoluciones.com', '131'], 
['ns5.awardspace.com', '129'], 
['ns1.datasygma.com.ar - 200.58.120.232', '129'], 
['dns1.solunet.com.ar - 190.0.161.1', '129'], 
['ns1.zerohost.com.ar - 50.23.33.232', '128'], 
['ns5.hosting-ar.com', '127'], 
['NS1.WORDPRESS.COM', '127'], 
['ns1.nextsolution.net', '126'], 
['huemul.avnam.net', '125'], 
['ns1.cromadns.com', '125'], 
['ns7.xvserver.com', '124'], 
['puma.avnam.net', '123'], 
['ns1.hostcero.com', '123'], 
['ns9.dns-principal-2.com', '122'], 
['ns1.redcomser.com', '122'], 
['ns1.grupoargentinaweb.com.ar - 72.52.164.100', '122'], 
['ns13.dns-principal-2.com', '121'], 
['orca.avnam.net', '121'], 
['w01a.dnspriv.com', '120'], 
['ns1.hostsiete.com', '120'], 
['ns17.dns-principal-2.com', '120'], 
['ns1.hostingbaires.com', '120'], 
['a4.nstld.com', '120'], 
['ns5.xvserver.com', '118'], 
['ns1.hd02.net', '118'], 
['pdns1.ultradns.net', '118'], 
['ns1.aconcaguahost.com', '117'], 
['ns1.sinspam.com', '117'], 
['ns3.redcel.com.ar - 200.110.156.7', '116'], 
['ns1.bvconline.com.ar - 190.1.0.2', '116'], 
['ns4.hostmar.com', '116'], 
['pdns01.domaincontrol.com', '115'], 
['ns15.zoneedit.com', '115'], 
['ns1.everydns.net', '114'], 
['ns1.tekar.net', '114'], 
['dns1.mardelplatadigital.com', '114'], 
['ns1.dnsprincipal.com', '113'], 
['pampa.avnam.net', '113'], 
['ns9.dns-principal.com', '113'], 
['ns1.rafaela.net', '113'], 
['yaguar.avnam.net', '113'], 
['ns1.dnsprivados5.com', '113'], 
['avi.wrservidores.com', '112'], 
['ns23.dns-principal-2.com', '112'], 
['ns21.dns-principal-2.com', '111'], 
['ns15.dns-principal-2.com', '111'], 
['dns1.nettica.com', '111'], 
['ns1.dnsprivados11.com', '111'], 
['ns1741.websitewelcome.com', '111'], 
['camaleon.avnam.net', '110'], 
['Ns1.dnsprivados7.com', '110'], 
['lirio.avnam.net', '109'], 
['ns01.domaincontrol.com', '109'], 
['ns4.hosting-ar.com', '109'], 
['ns1.all-kom.com.ar - 200.43.193.85', '109'], 
['ns1.fatcow.com', '108'], 
['dns1.supremedns.com', '107'], 
['ns1.n1servers.com.ar - 108.161.131.242', '107'], 
['ns1.manifestozone.com', '106'], 
['ombu.avnam.net', '106'], 
['ns3.dns-principal-3.com', '106'], 
['ns1.avnam.net', '105'], 
['zorro.avnam.net', '105'], 
['ns0.xname.org', '105'], 
['ns3.cordobahost.com', '105'], 
['ns1.dedicadouno.com', '104'], 
['ns1.dns-principal-4.com', '104'], 
['ns1.dnscentrales.com', '104'], 
['ns25.dns-principal-2.com', '104'], 
['ns1-house.serverdnspoint.com', '103'], 
['ns1.develnet.net', '103'], 
['dns1.mimejorhosting.com', '101'], 
['dns1.lc-2.la.inter.net', '101'], 
['dns04.unilever.com', '100'], 
['ns1.cylarcom.net', '100'], 


        ];


    var table = $('#reservas').DataTable( {
        "order": [[ 1, "desc" ]],
        "data": dataset,
        "columns": [{ "title": "DNS" },{ "title": "Cantidad" }]
    } ); 
    
    $('a.toggle-vis').on( 'click', function (e) {
        e.preventDefault();
 
        // Get the column API object
        var column = table.column( $(this).attr('data-column') );
 
        // Toggle the visibility
        column.visible( ! column.visible() );
    } );
    
    
} );
