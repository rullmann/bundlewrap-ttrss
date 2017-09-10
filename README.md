# tt-rss

`tt-rss` clones the `master` of [tt-rss](https://tt-rss.org/), an open source, web-based news feed reader.
Feeds are being updated by the [systemd daemon](https://tt-rss.org/gitlab/fox/tt-rss/wikis/UpdatingFeeds).

Currently this bundle is made to work with PostgreSQL.

## Requirements

* nginx, an open-source webserver
* PHP

* Bundlewrap Plugins
  * [item_git_deploy](https://github.com/bundlewrap/plugins/tree/master/item_git_deploy)

## Integrations

* Bundles:
  * [PostgreSQL](https://github.com/rullmann/bundlewrap-postgresql)
    * tt-rss requires a PostgreSQL database

## Metadata

All of the below is required.

    'metadata': {
        'tt-rss': {
            'install_path': "/var/www/tt-rss/",
            'url': "https://example.org/tt-rss/",
            'database': {
                'name': 'ttrss',
                'user': 'ttrss',
                'password': 'ttrss',
            },
        },
    }
