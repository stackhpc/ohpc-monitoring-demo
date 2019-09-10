flow_definitions = [
{% if inventory_hostname in groups["cluster_gw"] %}
    {
        "class": "vpn",
        "flows": [
            {
                "flow": "vpn-inbound",
                "src_port": "1194"
            },
            {
                "flow": "vpn-outbound",
                "dst_port": "1194"
            },
        ],
    },
{% elif inventory_hostname in groups["cluster_ceph_osd"] %}
    # run this on the compute nodes
    {
        "class": "ceph",
        "flows": [
            {
                "flow": "ceph-mon",
                "dst_port": "6789",
            },
            {
                "flow": "ceph-mds",
                "dst_port": "6800",
            },
            # By default, Ceph OSD Daemons bind to the first available ports
            # on a Ceph Node beginning at port 6800
            {
                "flow": "ceph-osd-outbound",
                "dst_port": "6800:7300",
            },
            {
                "flow": "ceph-osd-inbound",
                "src_port": "6800:7300"
            },
        ]
    },
{% elif inventory_hostname in groups["cluster_ceph_mon"] %}
    # run this on the monitor nodes
    {
        "class": "ceph",
        "flows": [
            {
                "flow": "ceph-mon-inbound",
                "src_port": "6789",
            },
            {
                "flow": "ceph-mon-outbound",
                "dst_port": "6789",
            },
        ]
    },
{% elif inventory_hostname in groups["cluster_ceph_mds"] %}
    # run this on the mds nodes
    {
        "class": "ceph",
        "flows": [
            {
                "flow": "ceph-mds-inbound",
                "dst_port": "6800",
            },
            {
                "flow": "ceph-mds-outbound",
                "src_port": "6800",
            },
        ]
    },
{% endif %}
]
