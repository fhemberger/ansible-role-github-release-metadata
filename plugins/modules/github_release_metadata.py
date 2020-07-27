#!/usr/bin/python

# Copyright: (c) 2020, Frederic Hemberger
# MIT License

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: github_release_metadata
short_description: Retrieves metadata of a release from GitHub
version_added: "2.9"
description:
  - "Retrieves metadata of a release from GitHub"
options:
  owner:
    description:
      - The GitHub account that owns the repository
    aliases: ['user']
    required: true
    type: str
  repo:
    description:
      - Repository name
    required: true
    type: str
  tag:
    description:
      - Tag to retrieve, defaults to `latest`
    default: latest
    type: str
author:
    - Frederic Hemberger (@fhemberger)
'''

EXAMPLES = '''
- name: Get metadata for latest Ansible release
  github_release_metadata:
    owner: ansible
    repo: ansible

- name: Get metadata for specific Ansible release
  github_release_metadata:
    owner: ansible
    repo: ansible
    tag: v2.5.0b1
'''

RETURN = '''
metadata:
  description: GitHub release metadata
  returned: always
  type: dict
status:
  description: The HTTP status code from the request.
  returned: always
  type: int
  sample: 200
url:
  description: The actual URL used for the request.
  returned: always
  type: str
  sample: https://api.github.com/
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_native, to_text
from ansible.module_utils.urls import fetch_url

import json


def format_message(err, resp):
    msg = resp.pop('msg')
    return err + (' %s' % msg if msg else '')


def main():
    module_args = dict(
        owner=dict(type='str', required=True, aliases=['user']),
        repo=dict(type='str', required=True),
        tag=dict(type='str', required=False, default='latest')
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.params['tag'] == 'latest':
        url = f"https://api.github.com/repos/{module.params['owner']}/{module.params['repo']}/releases/latest"
    else:
        url = f"https://api.github.com/repos/{module.params['owner']}/{module.params['repo']}/releases/tags/{module.params['tag']}"

    result = dict(
        changed=True,
        status=500,
        url=url,
        metadata=dict()
    )

    resp, info = fetch_url(module, url)
    status_code = int(info['status'])

    try:
        body = resp.read()
    except AttributeError:
        # there was no content, but the error read()
        # may have been stored in the info as 'body'
        body = info.pop('body', '')

    try:
        body = json.loads(to_text(body))
    except Exception as e:
        msg = format_message(
            "Failed to parse JSON respose from GitHub API: %s" % to_native(e), resp)
        module.fail_json(msg=msg, **resp)

    if status_code != 200:
        msg = body
        if isinstance(body, dict) and 'message' in body.keys():
            msg = body['message']
        module.fail_json(msg=msg)

    result['status'] = status_code
    result['metadata'] = body

    module.exit_json(**result)


if __name__ == '__main__':
    main()
