# Examples

## Python

We can get the package version via Python:

```python
from dinject.version import get_version

print(get_version())
```

!!! info
    `-1.-1.-1` means I built this page on a local development build.

<!--dinject as=markdown host=shell range=start-->

```text
-1.-1.-1
```

<!--dinject range=end-->

## Bash

We can also get the version via Bash:

```bash
python -m dinject --version
```

<!--dinject as=markdown host=shell range=start-->

```text
-1.-1.-1
```

<!--dinject range=end-->

## HTML and pseudo terminals

If we were to run `pipenv --help` right now, we'd get beautifully coloured and formatted page of information.

However, if we try to embed it:

```bash
pipenv --help
```

...then it's quite plain:

<!--dinject as=markdown host=shell range=start-->

```text
Usage: pipenv [OPTIONS] COMMAND [ARGS]...

Options:
  --where                         Output project home information.
  --venv                          Output virtualenv information.
  --py                            Output Python interpreter information.
  --envs                          Output Environment Variable options.
  --rm                            Remove the virtualenv.
  --bare                          Minimal output.
  --completion                    Output completion (to be executed by the
                                  shell).

  --man                           Display manpage.
  --support                       Output diagnostic information for use in
                                  GitHub issues.

  --site-packages / --no-site-packages
                                  Enable site-packages for the virtualenv.
                                  [env var: PIPENV_SITE_PACKAGES]

  --python TEXT                   Specify which version of Python virtualenv
                                  should use.

  --three / --two                 Use Python 3/2 when creating virtualenv.
  --clear                         Clears caches (pipenv, pip, and pip-tools).
                                  [env var: PIPENV_CLEAR]

  -v, --verbose                   Verbose mode.
  --pypi-mirror TEXT              Specify a PyPI mirror.
  --version                       Show the version and exit.
  -h, --help                      Show this message and exit.


Usage Examples:
   Create a new project using Python 3.7, specifically:
   $ pipenv --python 3.7

   Remove project virtualenv (inferred from current directory):
   $ pipenv --rm

   Install all dependencies for a project (including dev):
   $ pipenv install --dev

   Create a lockfile containing pre-releases:
   $ pipenv lock --pre

   Show a graph of your installed dependencies:
   $ pipenv graph

   Check your installed dependencies for security vulnerabilities:
   $ pipenv check

   Install a local setup.py into your virtual environment/Pipfile:
   $ pipenv install -e .

   Use a lower-level pip command:
   $ pipenv run pip freeze

Commands:
  check      Checks for PyUp Safety security vulnerabilities and against PEP
             508 markers provided in Pipfile.

  clean      Uninstalls all packages not specified in Pipfile.lock.
  graph      Displays currently-installed dependency graph information.
  install    Installs provided packages and adds them to Pipfile, or (if no
             packages are given), installs all packages from Pipfile.

  lock       Generates Pipfile.lock.
  open       View a given module in your editor.
  run        Spawns a command installed into the virtualenv.
  scripts    Lists scripts in current environment config.
  shell      Spawns a shell within the virtualenv.
  sync       Installs all packages specified in Pipfile.lock.
  uninstall  Uninstalls a provided package and removes it from Pipfile.
  update     Runs lock, then sync.
```

<!--dinject range=end-->

The trick is to inject it as HTML via a pseudo terminal, like this:

```text
<!--dinject as=html host=terminal-->
```

Now, what do we get?

```bash
pipenv --help
```

<!--dinject as=html host=terminal range=start-->

<style type="text/css">.thtml { --yellow: #CC0; --red: #C00; --magenta: #C0C; --green: #0C0; } .weight-heavy { font-weight: bold; } .foreground-yellow { border-color: var(--yellow); color: var(--yellow); } .foreground-red { border-color: var(--red); color: var(--red); } .foreground-magenta { border-color: var(--magenta); color: var(--magenta); } .foreground-green { border-color: var(--green); color: var(--green); }</style><pre class="nohighlight thtml"><code class="thtml-code">Usage: <span class="weight-heavy">pipenv</span> [OPTIONS] COMMAND [ARGS]...<br /><br /><span class="weight-heavy">Options:</span><br />  --where                         Output project home information.<br />  --venv                          Output virtualenv information.<br />  --py                            Output Python interpreter information.<br />  --envs                          Output Environment Variable options.<br />  --rm                            Remove the virtualenv.<br />  --bare                          Minimal output.<br />  --completion                    Output completion (to be executed by the<br />                                <span class="foreground-yellow weight-heavy">  shell</span>).<br /><br />  --man                           Display manpage.<br />  --support                       Output diagnostic information for use in<br />                                  GitHub issues.<br /><br />  --site-packages / --no-site-packages<br />                                  Enable site-packages for the virtualenv.<br />                                  [env var: PIPENV_SITE_PACKAGES]<br /><br />  --python TEXT                   Specify which version of Python virtualenv<br />                                  should use.<br /><br />  --three / --two                 Use Python 3/2 when creating virtualenv.<br />  --clear                         Clears caches (pipenv, pip, and pip-tools).<br />                                  [env var: PIPENV_CLEAR]<br /><br />  -v, --verbose                   Verbose mode.<br />  --pypi-mirror TEXT              Specify a PyPI mirror.<br />  --version                       Show the version and exit.<br />  -h, --help                      Show this message and exit.<br /><br /><br />Usage Examples:<br />   Create a new project using Python 3.7, specifically:<br />   $ <span class="foreground-yellow">pipenv --python 3.7</span><br /><br />   Remove project virtualenv (inferred from current directory):<br />   $ <span class="foreground-yellow">pipenv --rm</span><br /><br />   Install all dependencies for a project (including dev):<br />   $ <span class="foreground-yellow">pipenv install --dev</span><br /><br />   Create a lockfile containing pre-releases:<br />   $ <span class="foreground-yellow">pipenv lock --pre</span><br /><br />   Show a graph of your installed dependencies:<br />   $ <span class="foreground-yellow">pipenv graph</span><br /><br />   Check your installed dependencies for security vulnerabilities:<br />   $ <span class="foreground-yellow">pipenv check</span><br /><br />   Install a local setup.py into your virtual environment/Pipfile:<br />   $ <span class="foreground-yellow">pipenv install -e .</span><br /><br />   Use a lower-level pip command:<br />   $ <span class="foreground-yellow">pipenv run pip freeze</span><br /><br />Commands:<br /><span class="foreground-red weight-heavy">  check</span>      Checks for PyUp Safety security vulnerabilities and against PEP<br />             508 markers provided in Pipfile.<br /><br /><span class="foreground-red weight-heavy">  clean</span>      Uninstalls all packages not specified in Pipfile.lock.<br /><span class="foreground-red weight-heavy">  graph</span>      Displays currently-installed dependency graph information.<br /><span class="foreground-magenta weight-heavy">  install</span>    Installs provided packages and adds them to Pipfile, or (if no<br />             packages are given), installs all packages from Pipfile.<br /><br /><span class="foreground-green weight-heavy">  lock</span>       Generates Pipfile.lock.<br /><span class="foreground-red weight-heavy">  open</span>       View a given module in your editor.<br /><span class="foreground-yellow weight-heavy">  run</span>        Spawns a command installed into the virtualenv.<br /><span class="foreground-yellow weight-heavy">  scripts</span>    Lists scripts in current environment config.<br /><span class="foreground-yellow weight-heavy">  shell</span>      Spawns a shell within the virtualenv.<br /><span class="foreground-green weight-heavy">  sync</span>       Installs all packages specified in Pipfile.lock.<br /><span class="foreground-magenta weight-heavy">  uninstall</span>  Uninstalls a provided package and removes it from Pipfile.<br /><span class="foreground-green weight-heavy">  update</span>     Runs lock, then sync.<br /><br /></code></pre>

<!--dinject range=end-->

Huzzah!
