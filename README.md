# How to run Selenium automation tests on Hypertest (using Behave framework)

Download the concierge binary corresponding to the host operating system. It is recommended to download the binary in the project's Parent Directory.

* Mac: https://downloads.lambdatest.com/concierge/darwin/concierge
* Linux: https://downloads.lambdatest.com/concierge/linux/concierge
* Windows: https://downloads.lambdatest.com/concierge/windows/concierge.exe

[Note - The current project has concierge for macOS. Irrespective of the host OS, the concierge will auto-update whenever there is a new version on the server]

## Running tests in Behave using the Matrix strategy

Matrix YAML file (behave_hypertest_matrix_sample.yaml) in the repo contains the following configuration:

```yaml
globalTimeout: 90
testSuiteTimeout: 90
testSuiteStep: 90
```

Global timeout, testsuite timeout, and suite step timeout are each set to 90 minutes.
 
The target platform is set to macOS

```yaml
os: [mac]
```

Environment variables *LT_USERNAME* and *LT_ACCESS_KEY* are added under *env* in the YAML file.

```yaml
env:
 LT_USERNAME: ${ YOUR_LAMBDATEST_USERNAME()}
 LT_ACCESS_KEY: ${ YOUR_LAMBDATEST_ACCESS_KEY()}
```

The feature files are located in the *features* folder (i.e. lt_todo_app.feature and lt_selenium_playground.feature). Steps correponding to the features are located in *features/steps* folder. In the matrix YAML file, *files* specifies a list (or array) of *.feature* files that have to be executed on the Hypertest grid.

```yaml
  files: ["features/lt_todo_app.feature", "features/lt_selenium_playground.feature"]
```

Content under the *pre* directive is the pre-condition that will be run before the tests are executed on Hypertest grid. The required packages are listed in *requirements.txt* All the required packages are also installed in this step using *pip3 install*.

```yaml
pre:
  -  pip3 install -r requirements.txt
```

The *testSuites* object contains a list of commands (that can be presented in an array). In the current YAML file, commands to be run for executing the tests are put in an array (with a '-' preceding each item). The *behave* command is used for executing the feature files located in the *features* folder. 

```yaml
testSuites:
  - behave  $files
```

The [user_name and access_key of LambdaTest](https://accounts.lambdatest.com/detail/profile) is appended to the *concierge* command using the *--user* and *--key* command-line options. The CLI option *--config* is used for providing the custom Hypertest YAML file (e.g. behave_hypertest_matrix_sample.yaml). Run the following command on the terminal to run the tests listed in the feature files on the Hypertest grid:

```bash
./concierge --user "${ YOUR_LAMBDATEST_USERNAME()}" --key "${ YOUR_LAMBDATEST_ACCESS_KEY()}" --config behave_hypertest_matrix_sample.yaml --verbose
```

Visit [Hypertest Automation Dashboard](https://automation.lambdatest.com/hypertest) to check the status of execution

## Running tests in Behave using the Auto-Split strategy

Auto-Split YAML file (behave_hypertest_autosplit_sample.yaml) in the repo contains the following configuration:

```yaml
globalTimeout: 90
testSuiteTimeout: 90
testSuiteStep: 90
```

Global timeout, testsuite timeout, and suite step timeout are each set to 90 minutes.
 
The *runson* key determines the platform (or operating system) on which the tests would be executed. Here we have set the target OS as macOS.

```yaml
 runson: mac
```

Auto-split is set to true in the YAML file. Retry on failure (*retryOnFailure*) is set to False. When set to true, failed test execution will be retried until the *maxRetries* are exhausted (or test execution is successful). Concurrency (i.e. number of parallel sessions) is set to 2.

```yaml
 autosplit: true
 retryOnFailure: false
 maxRetries: 5
 concurrency: 2
```

Environment variables *LT_USERNAME* and *LT_ACCESS_KEY* are added under *env* in the YAML file.

```yaml
env:
 LT_USERNAME: ${ YOUR_LAMBDATEST_USERNAME()}
 LT_ACCESS_KEY: ${ YOUR_LAMBDATEST_ACCESS_KEY()}
```

Content under the *pre* directive is the pre-condition that will be run before the tests are executed on Hypertest grid. The required packages are listed in *requirements.txt* All the required packages are also installed in this step using *pip3 install* command.

```yaml
pre:
  -  pip3 install -r requirements.txt
```

The *testDiscoverer* contains the command that gives information about the feature files present in the current project. Here, we are fetching the list of *.feature* files that would be further executed using the *value* passed in the *testRunnerCommand*

```bash
grep -nri 'Feature' features -ir --include=\*.feature | sed 's/:.*//'
```

Running the above command on the terminal gives the list of feature files present in the features folder:

```
features/lt_selenium_playground.feature
features/lt_todo_app.feature
```

The *testRunnerCommand* contains the command that is used for triggering the test. The output fetched from the *testDiscoverer* command acts as an input to the *testRunner* command.

```
make $test
```
Run the following command on the terminal to trigger the respective tests (using Behave) on the Hypertest grid.

```bash
./concierge --user "${ YOUR_LAMBDATEST_USERNAME()}" --key "${ YOUR_LAMBDATEST_ACCESS_KEY()}" --config behave_hypertest_autosplit_sample.yaml --verbose
``` 

Visit [Hypertest Automation Dashboard](https://automation.lambdatest.com/hypertest) to check the status of execution