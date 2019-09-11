# Cloud Alchemy demo monitoring site

[![Build Status](https://travis-ci.org/cloudalchemy/demo-site.svg?branch=master)](https://travis-ci.org/cloudalchemy/demo-site)
[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![IRC](https://img.shields.io/badge/irc.freenode.net-%23cloudalchemy-yellow.svg)](https://kiwiirc.com/nextclient/#ircs://irc.freenode.net/#cloudalchemy)

## [demo.cloudalchemy.org](https://demo.cloudalchemy.org)

This repository provides an integration testing suite for our ansible roles as well as a demo site for [grafana](https://github.com/grafana/grafana), [prometheus](https://github.com/prometheus/prometheus), [alertmanager](https://github.com/prometheus/alertmanager) and [node_exporter](https://github.com/prometheus/node_exporter) (possibly more in the future).
Site is provisioned with ansible running every day and on almost all commits to master branch. Everything is fully automated with travis ci pipeline. If you want to check `ansible-playbook` output, go to [last build](https://travis-ci.org/cloudalchemy/demo-site).

Have a look at the configuration file [group_vars/all/vars](group_vars/all/vars).

## Applications

All applications should be running on their default ports.

| App name          | Address (HTTP)                                       | Address (HTTPS)                                           | Status                       |  Uptime                     |
|-------------------|------------------------------------------------------|-----------------------------------------------------------|-----------------------------|-----------------------------|
| node_exporter     | [demo.cloudalchemy.org:9100][node_exporter_http]     | [node.demo.cloudalchemy.org][node_exporter_https]         | ![node_exporter_status]     | ![node_exporter_uptime]     |
| snmp_exporter     | [demo.cloudalchemy.org:9116][snmp_exporter_http]     | [snmp.demo.cloudalchemy.org][snmp_exporter_https]         | ![snmp_exporter_status]     | ![snmp_exporter_uptime]     |
| blackbox_exporter | [demo.cloudalchemy.org:9115][blackbox_exporter_http] | [blackbox.demo.cloudalchemy.org][blackbox_exporter_https] | ![blackbox_exporter_status] | ![blackbox_exporter_uptime] |
| prometheus        | [demo.cloudalchemy.org:9090][prometheus_http]        | [prometheus.demo.cloudalchemy.org][prometheus_https]      | ![prometheus_status]        | ![prometheus_uptime]        |
| alertmanager      | [demo.cloudalchemy.org:9093][alertmanager_http]      | [alertmanager.demo.cloudalchemy.org][alertmanager_https]  | ![alertmanager_status]      | ![alertmanager_uptime]      |
| grafana           | [demo.cloudalchemy.org:3000][grafana_http]           | [grafana.demo.cloudalchemy.org][grafana_https]            | ![grafana_status]           | ![grafana_uptime]           |

## Important notice

This repository consists of two playbooks:
  - [site.yml](site.yml) - which deploys basic prometheus/grafana stack without additional http proxies and with software listening on default ports

## Run yourself

You can easily run such setup yourself without much knowledge how any part of this works. You just need to do the following things:

#### Install go on the control host and add it to your path

Download the offical go binaries and extract them somewhere (see: https://golang.org/dl/)

Export the path:
```
export PATH=$PATH:~/blobs/go/bin/
````

#### Run as usual Ansible playbook

```bash
# Download roles
ansible-galaxy install -r roles/requirements.yml

# Run playbook
ansible-playbook site.yml
# or when using vault encrypted variables
ansible-playbook --vault-id @prompt site.yml
```