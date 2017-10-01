ttrss_install_path = node.metadata.get('tt-rss', {}).get('install_path')
ttrss_url = node.metadata.get('tt-rss', {}).get('url')
ttrss_database = node.metadata.get('tt-rss', {}).get('database').get('name')
ttrss_database_user = node.metadata.get('tt-rss', {}).get('database').get('user')
ttrss_database_password = node.metadata.get('tt-rss', {}).get('database').get('password')

svc_systemd = {
    'tt-rss': {
        'needs': ['file:/etc/systemd/system/tt-rss.service'],
    },
}

git_deploy = {
    '{}'.format(ttrss_install_path): {
        'needs': ['directory:{}'.format(ttrss_install_path)],
        'repo': 'https://tt-rss.org/git/tt-rss.git',
        'rev': 'master',
    },
}

directories = {
    '{}'.format(ttrss_install_path): {
        'mode': '0755',
    },
    '{}/cache'.format(ttrss_install_path): {
        'mode': '0755',
        'owner': 'nginx',
        'needs': ['git_deploy:{}'.format(ttrss_install_path)],
    },
    '{}/cache/js'.format(ttrss_install_path): {
        'mode': '0755',
        'owner': 'nginx',
        'needs': ['git_deploy:{}'.format(ttrss_install_path)],
    },
    '{}/cache/images'.format(ttrss_install_path): {
        'mode': '0755',
        'owner': 'nginx',
        'needs': ['git_deploy:{}'.format(ttrss_install_path)],
    },
    '{}/cache/upload'.format(ttrss_install_path): {
        'mode': '0755',
        'owner': 'nginx',
        'needs': ['git_deploy:{}'.format(ttrss_install_path)],
    },
    '{}/cache/export'.format(ttrss_install_path): {
        'mode': '0755',
        'owner': 'nginx',
        'needs': ['git_deploy:{}'.format(ttrss_install_path)],
    },
    '{}/feed-icons'.format(ttrss_install_path): {
        'mode': '0755',
        'owner': 'nginx',
        'needs': ['git_deploy:{}'.format(ttrss_install_path)],
    },
    '{}/lock'.format(ttrss_install_path): {
        'mode': '0755',
        'owner': 'nginx',
        'needs': ['git_deploy:{}'.format(ttrss_install_path)],
    },
}

files = {
    '{}/config.php'.format(ttrss_install_path): {
        'source': 'config.php',
        'owner': 'nginx',
        'mode': '0644',
        'content_type': 'mako',
        'context': {
            'ttrss_url': ttrss_url,
            'ttrss_database': ttrss_database,
            'ttrss_database_user': ttrss_database_user,
            'ttrss_database_password': ttrss_database_password,
        },
        'needs': ['git_deploy:{}'.format(ttrss_install_path)],
    },
    '/etc/systemd/system/tt-rss.service': {
        'source': 'tt-rss.service',
        'mode': '0644',
        'content_type': 'mako',
        'context': {
            'ttrss_install_path': ttrss_install_path,
        },
    },
}
