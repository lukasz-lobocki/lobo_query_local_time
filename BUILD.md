# lobo_query_local_time

## Typical build workflow

```bash
git add --update
```

```bash
git commit -m "fix: change"
```

```bash
poetry run semantic-release version
```

```bash
git push
```

## Cookiecutter initiation

```bash
cookiecutter \
  ssh://git@github.com/lukasz-lobocki/py-pkgs-cookiecutter.git \
  package_name="lobo_query_local_time"
```

### was run with following variables

- package_name: **`lobo_query_local_time`**;
package_short_description: `Queries worldtimeapi and returns RTC datetime tuple.`

- package_version: `0.0.0`; python_version: `3.10`

- author_name: `Lukasz Lobocki`;
open_source_license: `CC0 v1.0 Universal`

- __package_slug: `lobo_query_local_time`; include_github_actions: `no`

### on

`2023-08-04 12:29:38 +0200`
