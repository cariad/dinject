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

<style type="text/css">.thtml { --yellow: #CC0; --red: #C00; --magenta: #C0C; --green: #0C0; } .foreground-default { border-color: var(--white); color: var(--white); } .weight-heavy { font-weight: 700; } .foreground-yellow { border-color: var(--yellow); color: var(--yellow); } .foreground-red { border-color: var(--red); color: var(--red); } .foreground-magenta { border-color: var(--magenta); color: var(--magenta); } .foreground-green { border-color: var(--green); color: var(--green); } .background-default { background: var(--black); }</style><pre class="nohighlight thtml"><code class="thtml-code">Usage: <span class="foreground-default weight-heavy">pipenv</span><span class="foreground-default"> [OPTIONS] COMMAND [ARGS]...<br /><br /></span><span class="foreground-default weight-heavy">Options:</span><span class="foreground-default"><br />  --where                         Output project home information.<br />  --venv                          Output virtualenv information.<br />  --py                            Output Python interpreter<br />                                  information.<br /><br />  --envs                          Output Environment Variable<br />                                  options.<br /><br />  --rm                            Remove the virtualenv.<br />  --bare                          Minimal output.<br />  --completion                    Output completion (to be executed<br />                                  by the shell).<br /><br />  --man                           Display manpage.<br />  --support                       Output diagnostic information for<br />                                  use in GitHub issues.<br /><br />  --site-packages / --no-site-packages<br />                                  Enable site-packages for the<br />                                  virtualenv.  [env var:<br />                                  PIPENV_SITE_PACKAGES]<br /><br />  --python TEXT                   Specify which version of Python<br />                                  virtualenv should use.<br /><br />  --three / --two                 Use Python 3/2 when creating<br />                                  virtualenv.<br /><br />  --clear                         Clears caches (pipenv, pip, and<br />                                  pip-tools).  [env var:<br />                                  PIPENV_CLEAR]<br /><br />  -v, --verbose                   Verbose mode.<br />  --pypi-mirror TEXT              Specify a PyPI mirror.<br />  --version                       Show the version and exit.<br />  -h, --help                      Show this message and exit.<br /><br /><br />Usage Examples:<br />   Create a new project using Python 3.7, specifically:<br />   $ </span><span class="foreground-yellow">pipenv --python 3.7</span><span class="foreground-default"><br /><br />   Remove project virtualenv (inferred from current directory):<br />   $ </span><span class="foreground-yellow">pipenv --rm</span><span class="foreground-default"><br /><br />   Install all dependencies for a project (including dev):<br />   $ </span><span class="foreground-yellow">pipenv install --dev</span><span class="foreground-default"><br /><br />   Create a lockfile containing pre-releases:<br />   $ </span><span class="foreground-yellow">pipenv lock --pre</span><span class="foreground-default"><br /><br />   Show a graph of your installed dependencies:<br />   $ </span><span class="foreground-yellow">pipenv graph</span><span class="foreground-default"><br /><br />   Check your installed dependencies for security vulnerabilities:<br />   $ </span><span class="foreground-yellow">pipenv check</span><span class="foreground-default"><br /><br />   Install a local setup.py into your virtual environment/Pipfile:<br />   $ </span><span class="foreground-yellow">pipenv install -e .</span><span class="foreground-default"><br /><br />   Use a lower-level pip command:<br />   $ </span><span class="foreground-yellow">pipenv run pip freeze</span><span class="foreground-default"><br /><br />Commands:<br /></span><span class="foreground-red weight-heavy">  check</span><span class="foreground-default">      Checks for PyUp Safety security vulnerabilities and<br />             against PEP 508 markers provided in Pipfile.<br /><br /></span><span class="foreground-red weight-heavy">  clean</span><span class="foreground-default">      Uninstalls all packages not specified in Pipfile.lock.<br /></span><span class="foreground-red weight-heavy">  graph</span><span class="foreground-default">      Displays currently-installed dependency graph<br />             information.<br /><br /></span><span class="foreground-magenta weight-heavy">  install</span><span class="foreground-default">    Installs provided packages and adds them to Pipfile,<br />             or (if no packages are given), installs all packages<br />             from Pipfile.<br /><br /></span><span class="foreground-green weight-heavy">  lock</span><span class="foreground-default">       Generates Pipfile.lock.<br /></span><span class="foreground-red weight-heavy">  open</span><span class="foreground-default">       View a given module in your editor.<br /></span><span class="foreground-yellow weight-heavy">  run</span><span class="foreground-default">        Spawns a command installed into the virtualenv.<br /></span><span class="foreground-yellow weight-heavy">  scripts</span><span class="foreground-default">    Lists scripts in current environment config.<br /></span><span class="foreground-yellow weight-heavy">  shell</span><span class="foreground-default">      Spawns a shell within the virtualenv.<br /></span><span class="foreground-green weight-heavy">  sync</span><span class="foreground-default">       Installs all packages specified in Pipfile.lock.<br /></span><span class="foreground-magenta weight-heavy">  uninstall</span><span class="foreground-default">  Uninstalls a provided package and removes it from<br />             Pipfile.<br /><br /></span><span class="foreground-green weight-heavy">  update</span><span class="foreground-default">     Runs lock, then sync.<br /></span><span class="background-default"><br /></span></code></pre>

<!--dinject range=end-->

Huzzah!
