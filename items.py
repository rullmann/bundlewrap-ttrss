ttrss_install_path = node.metadata.get('tt-rss', {}).get('install_path')
ttrss_url = node.metadata.get('tt-rss', {}).get('url')
ttrss_database = node.metadata.get('tt-rss', {}).get('database').get('name')
ttrss_database_user = node.metadata.get('tt-rss', {}).get('database').get('user')
ttrss_database_password = node.metadata.get('tt-rss', {}).get('database').get('password')

directories = {
    "{}".format(ttrss_install_path): {
        "mode": "0755",
    },
    "{}/cache".format(ttrss_install_path): {
        "mode": "0755",
        "owner": "nginx",
    },
    "{}/cache/js".format(ttrss_install_path): {
        "mode": "0755",
        "owner": "nginx",
    },
    "{}/cache/images".format(ttrss_install_path): {
        "mode": "0755",
        "owner": "nginx",
    },
    "{}/cache/upload".format(ttrss_install_path): {
        "mode": "0755",
        "owner": "nginx",
    },
    "{}/cache/export".format(ttrss_install_path): {
        "mode": "0755",
        "owner": "nginx",
    },
    "{}/feed-icons".format(ttrss_install_path): {
        "mode": "0755",
        "owner": "nginx",
    },
    "{}/lock".format(ttrss_install_path): {
        "mode": "0755",
        "owner": "nginx",
    },
}

git_deploy = {
    "{}".format(ttrss_install_path): {
        'needs': [
            "directory:{}".format(ttrss_install_path),
        ],
        'repo': "https://tt-rss.org/git/tt-rss.git",
        'rev': "master",
    },
}

files = {
    "{}/config.php".format(ttrss_install_path): {
        'source': "config.php",
        'owner': "nginx",
        'mode': "0644",
        'content_type': "mako",
        'context': {
            'ttrss_url': ttrss_url,
            'ttrss_database': ttrss_database,
            'ttrss_database_user': ttrss_database_user,
            'ttrss_database_password': ttrss_database_password,
        },
    },
    "/etc/systemd/system/tt-rss.service": {
        'source': "tt-rss.service",
        'owner': "root",
        'mode': "0644",
        'content_type': "mako",
        'context': {
            'ttrss_install_path': ttrss_install_path,
        },
    },
}

svc_systemd = {
    'tt-rss': {
        'enabled': True,
    },
}
