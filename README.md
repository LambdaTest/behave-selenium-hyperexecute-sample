<img height="100" alt="hyperexecute_logo" src="https://user-images.githubusercontent.com/1688653/159473714-384e60ba-d830-435e-a33f-730df3c3ebc6.png">

HyperExecute is a smart test orchestration platform to run end-to-end Selenium tests at the fastest speed possible. HyperExecute lets you achieve an accelerated time to market by providing a test infrastructure that offers optimal speed, test orchestration, and detailed execution logs.

The overall experience helps teams test code and fix issues at a much faster pace. HyperExecute is configured using a YAML file. Instead of moving the Hub close to you, HyperExecute brings the test scripts close to the Hub!

* <b>HyperExecute HomePage</b>: https://www.lambdatest.com/hyperexecute
* <b>Lambdatest HomePage</b>: https://www.lambdatest.com
* <b>LambdaTest Support</b>: [support@lambdatest.com](mailto:support@lambdatest.com)

To know more about how HyperExecute does intelligent Test Orchestration, do check out [HyperExecute Getting Started Guide](https://www.lambdatest.com/support/docs/getting-started-with-hyperexecute/)

[<img alt="Try it now" width="200 px" align="center" src="images/Try it Now.svg" />](https://hyperexecute.lambdatest.com/?utm_source=github&utm_medium=repository&utm_content=python&utm_term=behave)

[<img alt="Run in Gitpod" width="200 px" align="center" src="images/Gitpod.svg" />](https://hyperexecute.lambdatest.com/?type=gitpod&framework=Behave)

Follow the below steps to run Gitpod button:

1. Click '**Open in Gitpod**' button (You will be redirected to Login/Signup page).
2. Login with Lambdatest credentials and it will be redirected to Gitpod editor in new tab and current tab will show hyperexecute dashboard.

<!---If logged in, it will be redirected to Gitpod editor in new tab where current tab will show hyperexecute dashboard.

If not logged in, it will be redirected to Login/Signup page and simultaneously redirected to Gitpod editor in a new tab where current tab will show hyperexecute dashboard.

If not signed up, you need to sign up and simultaneously redirected to Gitpod in a new tab where current tab will show hyperexecute dashboard.--->

# How to run Selenium automation tests on HyperExecute (using Behave framework)

* [Pre-requisites](#pre-requisites)
   - [Download HyperExecute CLI](#download-hyperexecute-cli)
   - [Configure Environment Variables](#configure-environment-variables)

* [Auto-Split Execution with Behave](#auto-split-execution-with-behave)
   - [Core](#core)
   - [Pre Steps and Dependency Caching](#pre-steps-and-dependency-caching)
   - [Post Steps](#post-steps)
   - [Artifacts Management](#artifacts-management)
   - [Test Execution](#test-execution)

* [Matrix Execution with Behave](#matrix-execution-with-behave)
   - [Core](#core-1)
   - [Pre Steps and Dependency Caching](#pre-steps-and-dependency-caching-1)
   - [Post Steps](#post-steps-1)
   - [Artifacts Management](#artifacts-management-1)
   - [Test Execution](#test-execution-1)

* [Secrets Management](#secrets-management)
* [Navigation in Automation Dashboard](#navigation-in-automation-dashboard)

# Pre-requisites

Before using HyperExecute, you have to download HyperExecute CLI corresponding to the host OS. Along with it, you also need to export the environment variables *LT_USERNAME* and *LT_ACCESS_KEY* that are available in the [LambdaTest Profile](https://accounts.lambdatest.com/detail/profile) page.

## Download HyperExecute CLI

HyperExecute CLI is the CLI for interacting and running the tests on the HyperExecute Grid. The CLI provides a host of other useful features that accelerate test execution. In order to trigger tests using the CLI, you need to download the HyperExecute CLI binary corresponding to the platform (or OS) from where the tests are triggered:

Also, it is recommended to download the binary in the project's parent directory. Shown below is the location from where you can download the HyperExecute CLI binary:

* Mac: https://downloads.lambdatest.com/hyperexecute/darwin/hyperexecute
* Linux: https://downloads.lambdatest.com/hyperexecute/linux/hyperexecute
* Windows: https://downloads.lambdatest.com/hyperexecute/windows/hyperexecute.exe

## Configure Environment Variables

Before the tests are run, please set the environment variables LT_USERNAME & LT_ACCESS_KEY from the terminal. The account details are available on your [LambdaTest Profile](https://accounts.lambdatest.com/detail/profile) page.

For macOS:

```bash
export LT_USERNAME=LT_USERNAME
export LT_ACCESS_KEY=LT_ACCESS_KEY
```

For Linux:

```bash
export LT_USERNAME=LT_USERNAME
export LT_ACCESS_KEY=LT_ACCESS_KEY
```

For Windows:

```bash
set LT_USERNAME=LT_USERNAME
set LT_ACCESS_KEY=LT_ACCESS_KEY
```

## Auto-Split Execution with Behave

Auto-split execution mechanism lets you run tests at predefined concurrency and distribute the tests over the available infrastructure. Concurrency can be achieved at different levels - file, module, test suite, test, scenario, etc.

For more information about auto-split execution, check out the [Auto-Split Getting Started Guide](https://www.lambdatest.com/support/docs/getting-started-with-hyperexecute/#smart-auto-test-splitting)

### Core

Auto-split YAML file (*yaml/win/behave_hyperexecute_autosplit_sample.yaml*) in the repo contains the following configuration:

```yaml
globalTimeout: 90
testSuiteTimeout: 90
testSuiteStep: 90
```

Global timeout, testSuite timeout, and testSuite timeout are set to 90 minutes.
 
The *runson* key determines the platform (or operating system) on which the tests are executed. Here we have set the target OS as Windows.

```yaml
runson: win
```

Auto-split is set to true in the YAML file.

```yaml
 autosplit: true
```

*retryOnFailure* is set to true, instructing HyperExecute to retry failed command(s). The retry operation is carried out till the number of retries mentioned in *maxRetries* are exhausted or the command execution results in a *Pass*. In addition, the concurrency (i.e. number of parallel sessions) is set to 2.

```yaml
retryOnFailure: true
maxRetries: 5
concurrency: 2
```

### Pre Steps and Dependency Caching

Dependency caching is enabled in the YAML file to ensure that the package dependencies are not downloaded in subsequent runs. The first step is to set the Key used to cache directories.

```yaml
cacheKey: '{{ checksum "requirements.txt" }}'
```

Set the array of files & directories to be cached. In the example, all the packages will be cached in the *CacheDir* directory.

```yaml
cacheDirectories:
  - pip_cache
```

Steps (or commands) that must run before the test execution are listed in the *pre* run step. In the example, the packages listed in *requirements.txt* are installed using the *pip3* command.

The *--cache-dir* option is used for specifying the location of the directory used for caching the packages (i.e. *CacheDir*). It is important to note that downloaded cached packages are securely uploaded to a secure cloud before the execution environment is auto-purged after build completion. Please modify *requirements.txt* as per the project requirements.

```yaml
pre:
  - pip3 install -r requirements.txt --cache-dir pip_cache
```

### Post Steps

Steps (or commands) that need to run after the test execution are listed in the *post* step. In the example, we *cat* the contents of *yaml/win/behave_hyperexecute_matrix_sample.yaml*

```yaml
post:
  - cat yaml/win/behave_hyperexecute_autosplit_sample.yaml
```

The *testDiscovery* directive contains the command that gives details of the mode of execution, along with detailing the command that is used for test execution. Here, we are fetching the list of Python files that would be further executed using the *value* passed in the *testRunnerCommand*

```yaml
testDiscovery:
  type: raw
  mode: dynamic
  command: grep -nri 'Feature' features -ir --include=\*.feature | sed 's/:.*//'

testRunnerCommand: behave -f json.pretty -o reports/test_report.json $test
```

The *testRunnerCommand* contains the command that is used for triggering the test. The output fetched from the *testDiscoverer* command acts as an input to the *testRunner* command.

```yaml
testRunnerCommand: behave -f json.pretty -o reports/test_report.json $test
```

### Artifacts Management

The *mergeArtifacts* directive (which is by default *false*) is set to *true* for merging the artifacts and combing artifacts generated under each task.

The *uploadArtefacts* directive informs HyperExecute to upload artifacts [files, reports, etc.] generated after task completion. In the example, *path* consists of a regex for parsing the directory (i.e. *reports*) that contains the test reports.

```yaml
mergeArtifacts: true

uploadArtefacts:
  - name: TestReports
    path:
    - reports/**
```

HyperExecute also facilitates the provision to download the artifacts on your local machine. To download the artifacts, click on Artifacts button corresponding to the associated TestID.

<img width="1427" alt="behave_autosplit_artefacts_1" src="https://user-images.githubusercontent.com/1688653/162381846-adc4620a-2f24-4203-ae0a-4d58cf6e25a9.png">

Now, you can download the artifacts by clicking on the Download button as shown below:

<img width="1427" alt="behave_autosplit_artefacts_2" src="https://user-images.githubusercontent.com/1688653/162381849-a8a0c1ab-16a8-41b7-8f17-31c493dcd9f2.png">

### Test Execution

The CLI option *--config* is used for providing the custom HyperExecute YAML file (i.e. *yaml/win/behave_hyperexecute_autosplit_sample.yaml* for Windows and *yaml/linux/behave_hyperexecute_autosplit_sample.yaml* for Linux).

#### Execute Behave tests using Autosplit mechanism on Windows platform

Run the following command on the terminal to trigger the tests in Python files with HyperExecute platform set to Windows. The *--download-artifacts* option is used to inform HyperExecute to download the artifacts for the job.

```bash
./hyperexecute --download-artifacts --verbose --config yaml/win/behave_hyperexecute_autosplit_sample.yaml
```

#### Execute Behave tests using Autosplit mechanism on Linux platform

Run the following command on the terminal to trigger the tests in Python files with HyperExecute platform set to Linux. The *--download-artifacts* option is used to inform HyperExecute to download the artifacts for the job.

```bash
./hyperexecute --download-artifacts --verbose --config yaml/linux/behave_hyperexecute_autosplit_sample.yaml
```

Visit [HyperExecute Automation Dashboard](https://automation.lambdatest.com/hyperexecute) to check the status of execution

<img width="1414" alt="behave_autosplit_execution" src="https://user-images.githubusercontent.com/1688653/162381846-adc4620a-2f24-4203-ae0a-4d58cf6e25a9.png">

Shown below is the execution screenshot when the YAML file is triggered from the terminal:

<img width="1406" alt="behave_cli1_autosplit_execution" src="https://user-images.githubusercontent.com/1688653/162381853-1d818885-2375-4614-8fdc-50aa56942d66.png">

<img width="1402" alt="behave_cli2_autosplit_execution" src="https://user-images.githubusercontent.com/1688653/162381859-9c5bc21c-b0a1-49dc-b67c-28b8d72147d3.png">

# Matrix Execution with Behave

Matrix-based test execution is used for running the same tests across different test (or input) combinations. The Matrix directive in HyperExecute YAML file is a *key:value* pair where value is an array of strings.

Also, the *key:value* pairs are opaque strings for HyperExecute. For more information about matrix multiplexing, check out the [Matrix Getting Started Guide](https://www.lambdatest.com/support/docs/getting-started-with-hyperexecute/#matrix-based-build-multiplexing)

### Core

In the current example, matrix YAML file (*yaml/win/behave_hyperexecute_matrix_sample.yaml*) in the repo contains the following configuration:

```yaml
globalTimeout: 90
testSuiteTimeout: 90
testSuiteStep: 90
```

Global timeout, testSuite timeout, and testSuite timeout are set to 90 minutes.
 
The target platform is set to Windows. Please set the *[runson]* key to *[mac]* if the tests have to be executed on the macOS platform.

```yaml
runson: win
```

Feature files are located in the *features* folder (i.e. *lt_todo_app.feature* and *lt_selenium_playground.feature*). In the matrix YAML file, *files* specifies a list (or array) of *.feature* files that have to be executed on the HyperExecute grid.

```yaml
files: ["features/lt_todo_app.feature", "features/lt_selenium_playground.feature"]
```

*Steps* (i.e. *lt_to_do_steps.py* and *lt_selenium_playground_steps.py*) corresponding to the respective *features* are located in the *features/steps* folder.
The *testSuites* object contains a list of commands (that can be presented in an array).

Commands to execute the tests are put in an array (with a '-' preceding each item). The *behave* command is used for executing the feature files located in the *features* folder.

```yaml
testSuites:
  - behave -f json.pretty -o reports/test_report.json $files
```

### Pre Steps and Dependency Caching

Dependency caching is enabled in the YAML file to ensure that the package dependencies are not downloaded in subsequent runs. The first step is to set the Key used to cache directories.

```yaml
cacheKey: '{{ checksum "requirements.txt" }}'
```

Set the array of files & directories to be cached. In the example, all the packages will be cached in the *CacheDir* directory.

```yaml
cacheDirectories:
  - pip_cache
```

Steps (or commands) that must run before the test execution are listed in the *pre* run step. In the example, the packages listed in *requirements.txt* are installed using the *pip3* command.

The *--cache-dir* option is used for specifying the location of the directory used for caching the packages (i.e. *CacheDir*). It is important to note that downloaded cached packages are securely uploaded to a secure cloud before the execution environment is auto-purged after build completion. Please modify *requirements.txt* as per the project requirements.

```yaml
pre:
  - pip3 install -r requirements.txt --cache-dir pip_cache
```

### Post Steps

Steps (or commands) that need to run after the test execution are listed in the *post* step. In the example, we *cat* the contents of *yaml/win/behave_hyperexecute_matrix_sample.yaml*

```yaml
post:
  - cat yaml/win/behave_hyperexecute_matrix_sample.yaml
```

### Artifacts Management

The *mergeArtifacts* directive (which is by default *false*) is set to *true* for merging the artifacts and combing artifacts generated under each task.

The *uploadArtefacts* directive informs HyperExecute to upload artifacts [files, reports, etc.] generated after task completion. In the example, *path* consists of a regex for parsing the directory (i.e. *reports*) that contains the test reports.

```yaml
mergeArtifacts: true

uploadArtefacts:
  - name: TestReports
    path:
    - reports/**
```

HyperExecute also facilitates the provision to download the artifacts on your local machine. To download the artifacts, click on Artifacts button corresponding to the associated TestID.

<img width="1423" alt="behave_matrix_artefacts_1" src="https://user-images.githubusercontent.com/1688653/162381830-ca705494-ffcf-4e40-bf0a-b1f6b9ab7f5c.png">

Now, you can download the artifacts by clicking on the Download button as shown below:

<img width="1423" alt="behave_matrix_artefacts_2" src="https://user-images.githubusercontent.com/1688653/162381839-14440a4a-7626-4454-91b4-622fb4dfc465.png">

## Test Execution

The CLI option *--config* is used for providing the custom HyperExecute YAML file (i.e. *yaml/win/behave_hyperexecute_matrix_sample.yaml* for Windows and *yaml/linux/behave_hyperexecute_matrix_sample.yaml* for Linux).

#### Execute Behave tests using Matrix mechanism on Windows platform

Run the following command on the terminal to trigger the tests in Python files with HyperExecute platform set to Windows. The *--download-artifacts* option is used to inform HyperExecute to download the artifacts for the job.

```bash
./hyperexecute --download-artifacts --verbose --config yaml/win/behave_hyperexecute_matrix_sample.yaml
```

#### Execute Behave tests using Matrix mechanism on Linux platform

Run the following command on the terminal to trigger the tests in Python files with HyperExecute platform set to Linux. The *--download-artifacts* option is used to inform HyperExecute to download the artifacts for the job.

```bash
./hyperexecute --download-artifacts --verbose --config yaml/linux/behave_hyperexecute_matrix_sample.yaml
```

Visit [HyperExecute Automation Dashboard](https://automation.lambdatest.com/hyperexecute) to check the status of execution:

<img width="1414" alt="behave_matrix_execution" src="https://user-images.githubusercontent.com/1688653/160461271-7c43ed21-f26f-43f1-b71f-1d1514b8417c.png">

Shown below is the execution screenshot when the YAML file is triggered from the terminal:

<img width="1423" alt="behave_cli1_execution" src="https://user-images.githubusercontent.com/1688653/162381867-d756c55c-1bb6-442a-8e85-e82434de2856.png">

<img width="1406" alt="behave_cli2_execution" src="https://user-images.githubusercontent.com/1688653/162381870-035d36ef-4753-4033-bcc9-8e87812626b6.png">

## Secrets Management

In case you want to use any secret keys in the YAML file, the same can be set by clicking on the *Secrets* button the dashboard.

<img width="703" alt="behave_secrets_key_1" src="https://user-images.githubusercontent.com/1688653/152540968-90e4e8bc-3eb4-4259-856b-5e513cbd19b5.png">

Now create a *secret* key that you can use in the HyperExecute YAML file.

<img width="359" alt="secrets_management_1" src="https://user-images.githubusercontent.com/1688653/153250877-e58445d1-2735-409a-970d-14253991c69e.png">

All you need to do is create an environment variable that uses the secret key:

```yaml
env:
  PAT: ${{ .secrets.testKey }}
```

## Navigation in Automation Dashboard

HyperExecute lets you navigate from/to *Test Logs* in Automation Dashboard from/to *HyperExecute Logs*. You also get relevant get relevant Selenium test details like video, network log, commands, Exceptions & more in the Dashboard. Effortlessly navigate from the automation dashboard to HyperExecute logs (and vice-versa) to get more details of the test execution.

Shown below is the HyperExecute Automation dashboard which also lists the tests that were executed as a part of the test suite:

<img width="1238" alt="behave_hyperexecute_automation_dashboard" src="https://user-images.githubusercontent.com/1688653/162381862-de75861e-f8ce-478b-8fee-1800f1e6c6f6.png">

Here is a screenshot that lists the automation test that was executed on the HyperExecute grid:

<img width="1427" alt="behave_testing_automation_dashboard" src="https://user-images.githubusercontent.com/1688653/162381863-fae33282-2ce2-494a-bfbc-1b34c0d7ee16.png">

## We are here to help you :)
* LambdaTest Support: [support@lambdatest.com](mailto:support@lambdatest.com)
* Lambdatest HomePage: https://www.lambdatest.com
* HyperExecute HomePage: https://www.lambdatest.com/support/docs/getting-started-with-hyperexecute/

## License
Licensed under the [MIT license](LICENSE).
