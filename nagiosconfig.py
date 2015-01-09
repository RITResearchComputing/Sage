#/usr/bin/python

# All of the defaults and exceptions to host configuration goes here

# Data structure constants
DEFAULTS = 'defaults'
EXCEPTIONS = 'exceptions'
SERVICE_NAME = 'service-name'
CHECK_COMMAND = 'check-command'
LIMIT_TO = 'limit-to'

x64b_nix_hosts = [
    '129.21.204.139',#epenguin-04
    'firehose.rc.rit.edu', #runs wowza VOD, monitors streams, bridges, site for viewing web streams
    'pelican-00.rit.edu', #transcoder
    #'larry.rc.rit.edu', #Test wowza server
    'salsa.rit.edu', #Test wowza server
    'epenguin-03.rit.edu', # Global Studies office node
    #'epenguin-04.rit.edu', # in closet old gccis deans office
    #'epenguin-06.rit.edu', #Saunders College of Business Atrium
    #'epenguin-09.rit.edu', #Wallace Library (Sue Mee)
    'epenguin-11.rit.edu', #VPR Office Global Village sender
    'epenguin-14.rit.edu', #KGCOE Clean Room
    'epenguin-19.rit.edu', #GCCIS Deans office doing timelapse
    'ostrich-01.rit.edu', #Wallace
    #'ostrich-03.rit.edu', #RPL Send AND Recieve
    #'ostrich-06.rit.edu', #Innovation center kiosk
    'ostrich-07.rit.edu', #RACK
    'ostrich-08.rit.edu', #NTID Carey Lab
    'ostrich-09.rit.edu', #NTID GCCIS lab
    #'ostrich-14.rit.edu',
]
icewall_tilenodes = [
    'epenguin-13.rit.edu', #Video Wall TileNode 1 (2,0)
    'epenguin-16.rit.edu', #Video Wall TileNode 1 (2,1)
    'epenguin-18.rit.edu', #Video Wall TileNode 1 (1,0)
    'epenguin-10.rit.edu', #Video Wall TileNode 1 (1,1)
    '129.21.47.80', #epenguin-02
    '129.21.47.11', #epenguin-07 (0,0)
]
x32b_nix_hosts = [
    #'epenguin-01.rit.edu', #NTID Video Wall
    #'epenguin-03.rit.edu', #RC Lab (Network Testing)
    #'epenguin-04.rit.edu', # in closet old gccis deans office
    #'epenguin-05.rit.edu', #College of Science
    #'epenguin-06.rit.edu', #Saunders College of Business Atrium
    #'epenguin-08.rit.edu', #RC Lab (Network Testing)
    #'epenguin-09.rit.edu', #Wallace Library (Sue Mee)
    #'epenguin-10.rit.edu', #NTID GCCIS Lab (Temp)
    #'epenguin-11.rit.edu', #VPR Office Global Village sender
    #'epenguin-12.rit.edu', #NTID Video Wall HD Sender
    #'epenguin-14.rit.edu', #KGCOE Clean Room
    #'epenguin-15.rit.edu', #Global Village HD Sender
    #'epenguin-16.rit.edu', #CSI HD Sender
    #'epenguin-17.rit.edu', #RC Lab (formerly Izzie's)
    #'epenguin-19.rit.edu', #GCCIS Deans office doing timelapse

    'lovelace.rit.edu', #Virtual host
    #'thrasher.rit.edu', #timelapse
    #'rc.rit.edu', #web server

    #'ostrich-00.rit.edu', #Andrew's Testbed
    #'ostrich-01.rit.edu', #Wallace
    'ostrich-02.rit.edu', #CSI Video Wall 1
    #'ostrich-03.rit.edu', #RPL Send AND Recieve
    #'ostrich-04.rit.edu', #BioMed Photo Lab (sender)
    #'ostrich-05.rit.edu', #
    #'ostrich-06.rit.edu', #Innovation center kiosk
    #'ostrich-07.rit.edu', #RACK
    #'ostrich-08.rit.edu', #NTID Carey Lab
    #'ostrich-09.rit.edu', #NTID GCCIS lab
    #'ostrich-11.rit.edu', #CSI Video Wall 2
    #'ostrich-12.rit.edu', #CoB Dean's Office
]

# SI Video Wall 1

has_bad_or_no_sensors = [
    'lovelace.rit.edu',
    'firehose.rc.rit.edu',
    'ostrich-00.rit.edu',
    'ostrich-01.rit.edu',
    'ostrich-02.rit.edu',
    'ostrich-03.rit.edu',
    'ostrich-04.rit.edu',
    'ostrich-05.rit.edu',
    'ostrich-06.rit.edu',
    'ostrich-07.rit.edu',
    'ostrich-08.rit.edu',
    'ostrich-09.rit.edu',
    'ostrich-11.rit.edu',
    'ostrich-12.rit.edu',
    'larry.rc.rit.edu',
]

# List of hosts that *should* be running grav
grav_hosts = [
    'epenguin-01.rit.edu',
    'epenguin-03.rit.edu',
    'epenguin-05.rit.edu',
    'epenguin-06.rit.edu',
    #'epenguin-09.rit.edu',
    #'epenguin-10.rit.edu',
    #'epenguin-12.rit.edu',

    'ostrich-01.rit.edu',
    # 'ostrich-02.rit.edu',
    'ostrich-03.rit.edu',
    #'ostrich-05.rit.edu',
    'ostrich-06.rit.edu',
    #'ostrich-07.rit.edu',
    'ostrich-08.rit.edu',
    'ostrich-09.rit.edu',
    #'ostrich-11.rit.edu',
    #'ostrich-12.rit.edu',
]

# List of hosts that *should* be running vic
vic_hosts = [
    #'epenguin-02.rit.edu',
    'epenguin-04.rit.edu',
    'epenguin-11.rit.edu',
    'epenguin-12.rit.edu',
    'epenguin-14.rit.edu',
    #'epenguin-15.rit.edu',
    'epenguin-19.rit.edu',

    #'ostrich-02.rit.edu', #temporary
    'ostrich-03.rit.edu',
    'ostrich-04.rit.edu',
    'ostrich-06.rit.edu',
    'ostrich-08.rit.edu',
    'ostrich-09.rit.edu',
]

# List of hosts that *should* be running gstreamer
gst_hosts = [
    'epenguin-05.rit.edu',
    'epenguin-06.rit.edu',
]

# None right now
all_win_hosts = []

host_base, service_base = {}, {}
for h in x64b_nix_hosts:
    host_base[h] = 'rc-server'
    service_base[h] = 'rc-service'

for h in icewall_tilenodes:
    host_base[h] = 'rc-server'
    service_base[h] = 'rc-service'

for h in x32b_nix_hosts:
    host_base[h] = 'ag-server'
    service_base[h] = 'ag-service'

for h in all_win_hosts:
    host_base[h] = 'ag-server'
    service_base[h] = 'ag-service'

all_nix_hosts = x64b_nix_hosts + x32b_nix_hosts + icewall_tilenodes
all_hosts = all_nix_hosts + all_win_hosts

ag_sending_nodes = [
    #'epenguin-06.rit.edu',
    #'epenguin-08.rit.edu',
    #'penguin-04.rit.edu',
]

critical_hosts = ['lovelace.rit.edu']

# All ICELAB machines are physical
physical_hosts = all_nix_hosts

# ICELAB doesn't have any virtual machines, so these are empty
virt_heads = []
virt_guests_mapping = {}

nagios_hosts = []
# You have no sge or slurm installations.  Don't worry about it.
# Its here for posterity.
sge_heads = []
sge_nodes = []
slurm_heads = []
slurm_nodes = []

web_servers = {
    'lovelace.rit.edu' : [
        [False, 'lovelace.rit.edu'],
    ],
}
sql_servers = {}

hostgroups = {
    'ag-sending-nodes' : {
        'alias' : 'AG Sending Nodes',
        'members' : ag_sending_nodes,
    },
    #'physical' : {
    #    'alias' : 'Physical Machines',
    #    'members' : physical_hosts,
    #},
    'virtual' : {
        'alias' : 'Virtual Machines',
        'members' : [h for h in all_nix_hosts if not h in physical_hosts],
    },
    'critical' : {
        'alias' : 'Critical Machines',
        'members' : critical_hosts,
    },
    'noncritical' : {
        'alias' : 'Non-critical Machines',
        'members' : [h for h in all_hosts if not h in critical_hosts],
    },
    'nix' : {
        'alias' : '*nix Machines',
        'members' : all_nix_hosts,
    },
    'libvirt' : {
        'alias' : 'Virtualizers',
        'members' : virt_heads,
    },
    #'win' : {
    #    'alias' : 'win machines',
    #    'members' : all_win_hosts,
    #},
    'web' : {
        'alias' : 'Web Servers',
        'members' : web_servers.keys(), # Its a dict!
    },
    'nagios' : {
        'alias' : 'Nagios Servers', 
        'members' : nagios_hosts,
    },
    #'sql' : {
    #    'alias' : 'SQL Servers',
    #    'members' : sql_servers.keys(), # Its a dict!
    #},
    '64bit' : {
        'alias' : '64 bit machines',
        'members' : x64b_nix_hosts,
    },

    'icewall_tilenodes' : {
        'alias' : 'Icewall Tilenodes',
        'members' : icewall_tilenodes,
    },

    '32bit' : {
        'alias' : '32 bit machines',
        'members' : x32b_nix_hosts,
    },
    'ICE/CASCI' : {
        'alias' : 'ICE/CASCI machines',
        'members' : x32b_nix_hosts + all_win_hosts,
    },
}


win_service_parameters = {
    'ping' : {
        DEFAULTS : [100.0, "20%", 500.0, "60%"],
        EXCEPTIONS : {},
        SERVICE_NAME : 'Ping',
        CHECK_COMMAND : 'check_ping!%f,%s!%f,%s',
    },
    'check_vic' : {
        DEFAULTS : [],   EXCEPTIONS : {},
        SERVICE_NAME : 'VIC',
        CHECK_COMMAND : 'check_nrpe_no_args!check_vic',
        LIMIT_TO : all_win_hosts,
    },
    'check_rat' : {
        DEFAULTS : [],   EXCEPTIONS : {},
        SERVICE_NAME : 'RAT',
        CHECK_COMMAND : 'check_nrpe_no_args!check_rat',
        LIMIT_TO : [],
    },
    'check_dvts' : {
        DEFAULTS : [],   EXCEPTIONS : {},
        SERVICE_NAME : 'DVTS',
        CHECK_COMMAND : 'check_nrpe_no_args!check_dvts',
        LIMIT_TO : [],
    },
}

nix_service_parameters = {
    'check_sensors' : {
        DEFAULTS : [],
        EXCEPTIONS : {},
        SERVICE_NAME : 'CPU Sensors',
        CHECK_COMMAND : 'check_nrpe_no_args!check_sensors',
        LIMIT_TO : [
            h for h in x32b_nix_hosts + x64b_nix_hosts + icewall_tilenodes if h not in has_bad_or_no_sensors
        ],
    },
    'check_poli1_timelapse' : {
        DEFAULTS : ['poli1'],
        EXCEPTIONS : {},
        SERVICE_NAME : 'Polisseni_timelapse',
        CHECK_COMMAND : 'check_nrpe!check_timelapse!%s',
        LIMIT_TO : ['lovelace.rit.edu'],
    },
    'check_rc_sites' : {
        DEFAULTS : [],
        EXCEPTIONS : {'lovelace.rit.edu': ['lovelace.rit.edu'],
                     'testamajig.rc.rit.edu' : ['testamajig.rc.rit.edu'],
                     'firehose.rc.rit.edu' : ['firehose.rc.rit.edu'],},
        SERVICE_NAME : 'Webserver',
        CHECK_COMMAND : 'check_http!%s',
        LIMIT_TO : ['lovelace.rit.edu', 'testamajig.rc.rit.edu'],
    },
     'check_rc.rit.edu' : {
        DEFAULTS : ['rc.rit.edu'],
        EXCEPTIONS : {},
        SERVICE_NAME : 'Access to rc.rit.edu',
        CHECK_COMMAND : 'check_http!%s',
        LIMIT_TO : ['lovelace.rit.edu'],
    },
    'check_ram' : {
        DEFAULTS : [4000, 6000],
        EXCEPTIONS : {'testamajig.rc.rit.edu' : [12000,16000]},
        SERVICE_NAME : 'Memory',
        CHECK_COMMAND : 'check_nrpe!check_ram!%i!%i',
        LIMIT_TO : ['testamajig.rc.rit.edu'],
    },
    'check_poli2_timelapse' : {
        DEFAULTS: ['poli2'],
        EXCEPTIONS : {},
        SERVICE_NAME : 'Polisseni_timelapse_2',
        CHECK_COMMAND : 'check_nrpe!check_timelapse!%s',
        LIMIT_TO : ['lovelace.rit.edu'],
    },
    'check_vic' : {
        DEFAULTS : [],   EXCEPTIONS : {},
        SERVICE_NAME : 'VIC',
        CHECK_COMMAND : 'check_nrpe_no_args!check_vic',
        LIMIT_TO : vic_hosts,
    },
    'check_rat' : {
        DEFAULTS : [],   EXCEPTIONS : {},
        SERVICE_NAME : 'RAT',
        CHECK_COMMAND : 'check_nrpe_no_args!check_rat',
        LIMIT_TO : [
            #'ostrich-03.rit.edu',
            'ostrich-06.rit.edu',
        ],
    },
    'check_dvts' : {
        DEFAULTS : [],   EXCEPTIONS : {},
        SERVICE_NAME : 'DVTS',
        CHECK_COMMAND : 'check_nrpe_no_args!check_dvts',
        LIMIT_TO : [], # NOTE -- no hosts use dvts at the moment
    },
    'check_grav' : {
        DEFAULTS : [1],
	    EXCEPTIONS : {
		'ostrich-05.rit.edu' : [3],
	    },
        SERVICE_NAME : 'GRAV',
        CHECK_COMMAND : 'check_nrpe!check_grav!%i',
        LIMIT_TO : grav_hosts,
    },
    'check_gst' : {
        DEFAULTS : [],   EXCEPTIONS : {},
        SERVICE_NAME : 'GStreamer',
        CHECK_COMMAND : 'check_nrpe_no_args!check_gst',
        LIMIT_TO : gst_hosts,
    },
    'root-fs-ro' : {
        DEFAULTS : [],   EXCEPTIONS : {},
        SERVICE_NAME : 'Root_FS_is_read-only',
        CHECK_COMMAND : 'check_nrpe_no_args!check_root',
        LIMIT_TO : [h for h in all_nix_hosts if not h in physical_hosts],
    },
    'nagios' : {
        DEFAULTS : [],   EXCEPTIONS : {},
        SERVICE_NAME : 'Nagios_Itself',
        CHECK_COMMAND : 'check_nrpe_no_args!check_nagios',
        LIMIT_TO : nagios_hosts,
    },
    'ping' : {
        DEFAULTS : [100.0, "20%", 500.0, "60%"],
        EXCEPTIONS : {},
        SERVICE_NAME : 'Ping',
        CHECK_COMMAND : 'check_ping!%f,%s!%f,%s',
    },
    'disk' : {
        DEFAULTS : ["20%", "10%", "/dev/disk"],
        EXCEPTIONS : {},
        SERVICE_NAME : 'Root_Partition',
        CHECK_COMMAND : 'check_nrpe!check_disk!%s!%s!%s',
    },
    'user' : {
        DEFAULTS : [10, 15],
        EXCEPTIONS : {
            'brodie' : [20, 30],
            'epenguin-07.rit.edu' : [15, 20],
        },
        SERVICE_NAME : 'Current_Users',
        CHECK_COMMAND : 'check_nrpe!check_users!%i!%i',
    },
    'check-for-proc' : {
        DEFAULTS : None,
        EXCEPTIONS : {
            'media' : ['QuickBridge'],
        },
        SERVICE_NAME : 'Check for process',
        CHECK_COMMAND : 'check_nrpe!check_for_proc!%s',
        LIMIT_TO : ['media'],
    },
    'procs-per-user' : { #[Critical, Warning]
        DEFAULTS : [100, 160],
        EXCEPTIONS : {
        },
        SERVICE_NAME : 'Procs_per_User',
        CHECK_COMMAND : 'check_nrpe!check_procs_custom!%i!%i',
    },
    'user-unique' : {
        DEFAULTS : [5, 10],
        EXCEPTIONS : {
            'brodie'    : [10, 15],
            'solvay'    : [8,  12],
            'werner'    : [8,  12],
        },
        SERVICE_NAME : 'Current_Unique_Users',
        CHECK_COMMAND : 'check_nrpe!check_users_custom!%i!%i',

    },
    'zombie' : {
        DEFAULTS : [5, 10],
        EXCEPTIONS : {},
        SERVICE_NAME : 'Zombie_Processes',
        CHECK_COMMAND : 'check_nrpe!check_zombie_procs!%i!%i',
    },
    'total-procs' : { #[Critical, Warning]
        DEFAULTS : [280, 300],
        EXCEPTIONS : {
            'ostrich-00.rit.edu'    : [300, 350],
            'ostrich-07.rit.edu'    : [300, 350],
        },
        SERVICE_NAME : 'Total_Processes',
        CHECK_COMMAND : 'check_nrpe!check_total_procs!%i!%i',
    },
    'load' : {
        DEFAULTS : ['6,5,4', '7,6,5'],
        EXCEPTIONS : {
            'pelican-00.rit.edu' : ['6,5,4.5', '7,6,5'],
        },
        SERVICE_NAME : 'Current_Load',
        CHECK_COMMAND : 'check_nrpe!check_load!%s!%s'
    },
    'swap' : {
        DEFAULTS : ['20%', '10%'],
        EXCEPTIONS : {},
        SERVICE_NAME : 'Swap_Usage',
        CHECK_COMMAND : 'check_nrpe!check_swap!%s!%s',
    },
    'time' : {
        DEFAULTS : [30, 60],
        EXCEPTIONS : {
        },
        SERVICE_NAME : 'NTP_Sync',
        CHECK_COMMAND : 'check_nrpe!check_ntp_time!0.north-america.pool.ntp.org!%i!%i',
    },
    #'tcode-mgr' : {
    #    DEFAULTS : [],
    #    EXCEPTIONS : {},
    #    SERVICE_NAME : 'Transcode_Manager',
    #    CHECK_COMMAND : 'check_nrpe_no_args!check_transcode_manager',
    #     LIMIT_TO : ['testamajig.rc.rit.edu'],
    #},
    'poli-1' : {
        DEFAULTS : ['poli1'],
        EXCEPTIONS : {},
        SERVICE_NAME : 'Polisseni_Center_1',
        CHECK_COMMAND : 'check_nrpe!check_gstpipe!%s',
         LIMIT_TO : ['pelican-00.rit.edu'],
    },
    'streammon' : {
        DEFAULTS : [360, 660, '/home/user/streammon/lastrun.log'],
        EXCEPTIONS : {},
        SERVICE_NAME : 'Live_Stream_Monitor',
        CHECK_COMMAND : 'check_nrpe!check_file_age!%i!%i!%s',
         LIMIT_TO : ['pelican-00.rit.edu'],
    },
    'poli-2' : {
        DEFAULTS : ['poli2'],
        EXCEPTIONS : {},
        SERVICE_NAME : 'Polisseni_Center_2',
        CHECK_COMMAND : 'check_nrpe!check_gstpipe!%s',
         LIMIT_TO : ['pelican-00.rit.edu'],
    },
    'global-studies-bridge' : {
        DEFAULTS : ['224.2.243.48','52850'],
        EXCEPTIONS : {},
        SERVICE_NAME : 'Global_Studies_Bridge',
        CHECK_COMMAND : 'check_nrpe!check_bridge!%s!%s',
         LIMIT_TO : ['firehose.rc.rit.edu'],
    },
    #'web-server' : {
    #    DEFAULTS : [],
    #    EXCEPTIONS : {'testamajig.rc.rit.edu' : ['testamajig.rc.rit.edu'],
    #                  'firehose.rc.rit.edu' : ['firehose.rc.rit.edu']             
    #                 },
    #    SERVICE_NAME : 'Web_Service',
    #    CHECK_COMMAND : 'check_http!
    'main-venu-a-bridge' : {
        DEFAULTS : ['224.2.224.224','20000'],
        EXCEPTIONS : {},
        SERVICE_NAME : 'RIT_Main_Venu_Audio_Bridge',
        CHECK_COMMAND : 'check_nrpe!check_bridge!%s!%s',
         LIMIT_TO : ['firehose.rc.rit.edu'],
    },
    'main-venu-v-bridge' : {
        DEFAULTS : ['224.2.224.225','20002'],
        EXCEPTIONS : {},
        SERVICE_NAME : 'RIT_Main_Venu_Video_Bridge',
        CHECK_COMMAND : 'check_nrpe!check_bridge!%s!%s',
         LIMIT_TO : ['firehose.rc.rit.edu'],
    },
    'kosovo-a-bridge' : {
        DEFAULTS : ['224.2.136.118','55416'],
        EXCEPTIONS : {},
        SERVICE_NAME : 'Kosovo_Audio_Bridge',
        CHECK_COMMAND : 'check_nrpe!check_bridge!%s!%s',
        LIMIT_TO : ['firehose.rc.rit.edu'],
    },
    'check-global-village' : {
        DEFAULTS : ['GlobalVillage'],
        EXCEPTIONS : {},
        SERVICE_NAME : 'Global_Village_Stream',
        CHECK_COMMAND : 'check_nrpe!check_stream!%s',
         LIMIT_TO : ['lovelace.rit.edu'],
    },
    'check-poli-1' : {
        DEFAULTS : ['Poli1'],
        EXCEPTIONS : {},
        SERVICE_NAME : 'Polisseni_Center_1_Stream',
        CHECK_COMMAND : 'check_nrpe!check_stream!%s',
         LIMIT_TO : ['lovelace.rit.edu'],
    },
    'check-poli-2' : {
        DEFAULTS : ['Poli2'],
        EXCEPTIONS : {},
        SERVICE_NAME : 'Polisseni_Center_2_Stream',
        CHECK_COMMAND : 'check_nrpe!check_stream!%s',
         LIMIT_TO : ['lovelace.rit.edu'],
    },
    #'check-rpl' : {
    #    DEFAULTS : ['RPL'],
    #    EXCEPTIONS : {},
    #    SERVICE_NAME : 'RPL_Stream',
    #    CHECK_COMMAND : 'check_nrpe!check_stream!%s',
    #     LIMIT_TO : ['lovelace.rit.edu'],
    #},
   # 'check-csi-floor' : {
   #     DEFAULTS : ['CSIFloor'],
   #     EXCEPTIONS : {},
   #     SERVICE_NAME : 'CSI_Floor_Stream',
   #     CHECK_COMMAND : 'check_nrpe!check_stream!%s',
   #      LIMIT_TO : ['lovelace.rit.edu'],
   # },
   #'check-csi-wall' : {
   #     DEFAULTS : ['CSIWall'],
   #     EXCEPTIONS : {},
   #     SERVICE_NAME : 'CSI_Wall_Stream',
   #     CHECK_COMMAND : 'check_nrpe!check_stream!%s',
   #      LIMIT_TO : ['lovelace.rit.edu'],
   # },
    'check-ntid-carey' : {
        DEFAULTS : ['NTIDCareyLab'],
        EXCEPTIONS : {},
        SERVICE_NAME : 'Carey_Lab_Stream',
        CHECK_COMMAND : 'check_nrpe!check_stream!%s',
         LIMIT_TO : ['lovelace.rit.edu'],
    },
    'check-ntid-golisano' : {
        DEFAULTS : ['NTIDGolisano'],
        EXCEPTIONS : {},
        SERVICE_NAME : 'Golisano_Lab_Stream',
        CHECK_COMMAND : 'check_nrpe!check_stream!%s',
        LIMIT_TO : ['lovelace.rit.edu'],
    },
    'check-smfl' : {
        DEFAULTS : ['SMFL'],
        EXCEPTIONS : {},
        SERVICE_NAME : 'SMFL_Stream',
        CHECK_COMMAND : 'check_nrpe!check_stream!%s',
         LIMIT_TO : ['lovelace.rit.edu'],
    },

}

for host, guests in virt_guests_mapping.iteritems():
    for guest in guests:
        addition = {
            'check_virt_%s_for_%s' % (host, guest) : {
                DEFAULTS: [guest],   EXCEPTIONS: {},
                SERVICE_NAME: 'Check_virt_%s_for_%s' % (host, guest),
                CHECK_COMMAND: 'check_nrpe!check_virt_guest!%s',
                LIMIT_TO: [host],
            }
        }
        nix_service_parameters.update(addition)
