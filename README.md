# Ansible Module: GitHub Release Metadata

## Options

- `owner`: The GitHub account that owns the repository (Aliases: `user`, mandatory)
- `repo`: Repository name (mandatory)
- `tag`: Tag to retrieve, defaults to `latest`


## Examples

```yaml
- name: Get metadata for latest Ansible release
  github_release_metadata:
    owner: ansible
    repo: ansible

- name: Get metadata for specific Ansible release
  github_release_metadata:
    owner: ansible
    repo: ansible
    tag: v2.5.0b1
```

## Return values

```yaml
metadata:
  description: GitHub release metadata
  returned: always
  type: dict
status:
  description: The HTTP status code from the request.
  returned: always
  type: int
url:
  description: The actual URL used for the request.
  returned: always
  type: str
```

## Example output

```yaml
metadata:
  url: https://api.github.com/repos/ansible/ansible/releases/9604973
  assets_url: https://api.github.com/repos/ansible/ansible/releases/9604973/assets
  upload_url: https://uploads.github.com/repos/ansible/ansible/releases/9604973/assets{?name,label}
  html_url: https://github.com/ansible/ansible/releases/tag/v2.5.0b1
  id: 9604973
  node_id: MDc6UmVsZWFzZTk2MDQ5NzM=
  tag_name: v2.5.0b1
  target_commitish: devel
  name: v2.5.0 Beta 1
  draft: false
  author:
    login: nitzmahone
    id: 6775756
    node_id: MDQ6VXNlcjY3NzU3NTY=
    avatar_url: https://avatars1.githubusercontent.com/u/6775756?v=4
    gravatar_id: ''
    url: https://api.github.com/users/nitzmahone
    html_url: https://github.com/nitzmahone
    followers_url: https://api.github.com/users/nitzmahone/followers
    following_url: https://api.github.com/users/nitzmahone/following{/other_user}
    gists_url: https://api.github.com/users/nitzmahone/gists{/gist_id}
    starred_url: https://api.github.com/users/nitzmahone/starred{/owner}{/repo}
    subscriptions_url: https://api.github.com/users/nitzmahone/subscriptions
    organizations_url: https://api.github.com/users/nitzmahone/orgs
    repos_url: https://api.github.com/users/nitzmahone/repos
    events_url: https://api.github.com/users/nitzmahone/events{/privacy}
    received_events_url: https://api.github.com/users/nitzmahone/received_events
    type: User
    site_admin: false
  prerelease: true
  created_at: '2018-02-09T02:46:30Z'
  published_at: '2018-02-09T06:51:40Z'
  assets: []
  tarball_url: https://api.github.com/repos/ansible/ansible/tarball/v2.5.0b1
  zipball_url: https://api.github.com/repos/ansible/ansible/zipball/v2.5.0b1
  body: ''
status: 200
url: https://api.github.com/repos/ansible/ansible/releases/tags/v2.5.0b1
```

## License

[MIT](LICENSE)
