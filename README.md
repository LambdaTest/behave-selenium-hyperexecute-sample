# How to run Selenium automation tests on HyperTest (using Behave framework)

* [Pre-requisites](#pre-requisites)
   - [Download Concierge](#download-concierge)
   - [Configure Environment Variables](#configure-environment-variables)
   
* [Matrix Execution with Behave](#matrix-execution-with-behave)
   - [Core](#core)
   - [Pre Steps and Dependency Caching](#pre-steps-and-dependency-caching)
   - [Post Steps](#post-steps)
   - [Artefacts Management](#artefacts-management)
   - [Test Execution](#test-execution)

* [Auto-Split Execution with Behave](#auto-split-execution-with-behave)
   - [Core](#core-1)
   - [Pre Steps and Dependency Caching](#pre-steps-and-dependency-caching-1)
   - [Post Steps](#post-steps-1)
   - [Artefacts Management](#artefacts-management-1)
   - [Test Execution](#test-execution-1)

* [Secrets Management](#secrets-management)
* [Navigation in Automation Dashboard](#navigation-in-automation-dashboard)

# Pre-requisites

Before using HyperTest, you have to download Concierge CLI corresponding to the host OS. Along with it, you also need to export the environment variables *LT_USERNAME* and *LT_ACCESS_KEY* that are available in the [LambdaTest Profile](https://accounts.lambdatest.com/detail/profile) page.

## Download Concierge

Concierge is a CLI for interacting and running the tests on the HyperTest Grid. Concierge provides a host of other useful features that accelerate test execution. In order to trigger tests using Concierge, you need to download the Concierge binary corresponding to the platform (or OS) from where the tests are triggered:

Also, it is recommended to download the binary in the project's parent directory. Shown below is the location from where you can download the Concierge binary: 

* Mac: https://downloads.lambdatest.com/concierge/darwin/concierge
* Linux: https://downloads.lambdatest.com/concierge/linux/concierge
* Windows: https://downloads.lambdatest.com/concierge/windows/concierge.exe

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

# Matrix Execution with Behave

Matrix-based test execution is used for running the same tests across different test (or input) combinations. The Matrix directive in HyperTest YAML file is a *key:value* pair where value is an array of strings.

Also, the *key:value* pairs are opaque strings for HyperTest. For more information about matrix multiplexing, check out the [Matrix Getting Started Guide](https://www.lambdatest.com/support/docs/getting-started-with-hypertest/#matrix-based-build-multiplexing)

### Core

In the current example, matrix YAML file (*yaml/behave_hypertest_matrix_sample.yaml*) in the repo contains the following configuration:

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

Feature files are located in the *features* folder (i.e. *lt_todo_app.feature* and *lt_selenium_playground.feature*). In the matrix YAML file, *files* specifies a list (or array) of *.feature* files that have to be executed on the HyperTest grid.

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

Steps (or commands) that need to run after the test execution are listed in the *post* step. In the example, we *cat* the contents of *yaml/behave_hypertest_matrix_sample.yaml*

```yaml
post:
  - cat yaml/behave_hypertest_matrix_sample.yaml
```

### Artefacts Management

The *mergeArtifacts* directive (which is by default *false*) is set to *true* for merging the artefacts and combing artefacts generated under each task.

The *uploadArtefacts* directive informs HyperTest to upload artefacts [files, reports, etc.] generated after task completion. In the example, *path* consists of a regex for parsing the directory (i.e. *reports*) that contains the test reports.

```yaml
mergeArtifacts: true

uploadArtefacts:
  [
    {
      "name": "reports",
      "path": ["reports/**"]
    }
  ]
```

HyperTest also facilitates the provision to download the artefacts on your local machine. To download the artefacts, click on Artefacts button corresponding to the associated TestID.

<img width="1423" alt="behave_matrix_artefacts_1" src="https://user-images.githubusercontent.com/1688653/152790522-ad149cca-1226-4285-ae7b-c843ed151286.png">

Now, you can download the artefacts by clicking on the Download button as shown below:

<img width="1423" alt="behave_matrix_artefacts_2" src="https://user-images.githubusercontent.com/1688653/152790546-3fade60d-ce39-4b2b-b321-839718820995.png">

## Test Execution

The CLI option *--config* is used for providing the custom HyperTest YAML file (i.e. *yaml/behave_hypertest_matrix_sample.yaml*). Run the following command on the terminal to trigger the tests in Python files on the HyperTest grid. The *--download-artifacts* option is used to inform HyperTest to download the artefacts for the job.

```bash
./concierge --download-artifacts --config --verbose yaml/behave_hypertest_matrix_sample.yaml
```

Visit [HyperTest Automation Dashboard](https://automation.lambdatest.com/hypertest) to check the status of execution:

<img width="1414" alt="behave_matrix_execution" src="https://user-images.githubusercontent.com/1688653/152790522-ad149cca-1226-4285-ae7b-c843ed151286.png">

Shown below is the execution screenshot when the YAML file is triggered from the terminal:

<img width="1423" alt="behave_cli1_execution" src="https://user-images.githubusercontent.com/1688653/152791630-44a1c98d-e1d1-4d82-9c1e-6a4cf00ed4d1.png">

<img width="1406" alt="behave_cli2_execution" src="https://user-images.githubusercontent.com/1688653/152791655-a824a05f-0ea4-4c17-b3ac-ec7c095eebd0.png">

## Auto-Split Execution with Behave

Auto-split execution mechanism lets you run tests at predefined concurrency and distribute the tests over the available infrastructure. Concurrency can be achieved at different levels - file, module, test suite, test, scenario, etc.

For more information about auto-split execution, check out the [Auto-Split Getting Started Guide](https://www.lambdatest.com/support/docs/getting-started-with-hypertest/#smart-auto-test-splitting)

### Core

Auto-split YAML file (*yaml/behave_hypertest_autosplit_sample.yaml*) in the repo contains the following configuration:

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

*retryOnFailure* is set to true, instructing HyperTest to retry failed command(s). The retry operation is carried out till the number of retries mentioned in *maxRetries* are exhausted or the command execution results in a *Pass*. In addition, the concurrency (i.e. number of parallel sessions) is set to 2.

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

Steps (or commands) that need to run after the test execution are listed in the *post* step. In the example, we *cat* the contents of *yaml/behave_hypertest_matrix_sample.yaml*

```yaml
post:
  - cat yaml/behave_hypertest_autpsplit_sample.yaml
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

### Artefacts Management

The *mergeArtifacts* directive (which is by default *false*) is set to *true* for merging the artefacts and combing artefacts generated under each task.

The *uploadArtefacts* directive informs HyperTest to upload artefacts [files, reports, etc.] generated after task completion. In the example, *path* consists of a regex for parsing the directory (i.e. *reports*) that contains the test reports.

```yaml
mergeArtifacts: true

uploadArtefacts:
  [
    {
      "name": "reports",
      "path": ["reports/**"]
    }
  ]
```

HyperTest also facilitates the provision to download the artefacts on your local machine. To download the artefacts, click on Artefacts button corresponding to the associated TestID.

<img width="1427" alt="behave_autosplit_artefacts_1" src="https://user-images.githubusercontent.com/1688653/152794671-044cfe72-df63-4608-b8d4-91351c9f64ed.png">

Now, you can download the artefacts by clicking on the Download button as shown below:

<img width="1427" alt="behave_autosplit_artefacts_2" src="https://user-images.githubusercontent.com/1688653/152794693-6f7f6300-7dd5-4ac9-8fa1-07685ed5e5db.png">

### Test Execution

The CLI option *--config* is used for providing the custom HyperTest YAML file (i.e. *yaml/behave_hypertest_autosplit_sample.yaml*). Run the following command on the terminal to trigger the tests in Python files on the HyperTest grid. The *--download-artifacts* option is used to inform HyperTest to download the artefacts for the job.

```bash
./concierge --download-artifacts --verbose --config yaml/behave_hypertest_autosplit_sample.yaml
```

Visit [HyperTest Automation Dashboard](https://automation.lambdatest.com/hypertest) to check the status of execution

<img width="1414" alt="behave_autosplit_execution" src="https://user-images.githubusercontent.com/1688653/152794671-044cfe72-df63-4608-b8d4-91351c9f64ed.png">

Shown below is the execution screenshot when the YAML file is triggered from the terminal:

<img width="1406" alt="behave_cli1_autosplit_execution" src="https://user-images.githubusercontent.com/1688653/152793083-e09403f9-6b8a-41a8-954f-bad2f539626e.png">

<img width="1402" alt="behave_cli2_autosplit_execution" src="https://user-images.githubusercontent.com/1688653/152793111-4b0c4f6d-fc3b-4487-8a63-06cc71028ad1.png">

## Secrets Management

In case you want to use any secret keys in the YAML file, the same can be set by clicking on the *Secrets* button the dashboard.

<img width="703" alt="behave_secrets_key_1" src="https://user-images.githubusercontent.com/1688653/152540968-90e4e8bc-3eb4-4259-856b-5e513cbd19b5.png">

Now create *secrets* that you can use in the HyperTest YAML file.

<img width="362" alt="behave_secrets_key_2" src="https://user-images.githubusercontent.com/1688653/152540977-436a8ba8-0ded-44db-8407-b3fb21b1f98d.png">

## Navigation in Automation Dashboard

HyperTest lets you navigate from/to *Test Logs* in Automation Dashboard from/to *HyperTest Logs*. You also get relevant get relevant Selenium test details like video, network log, commands, Exceptions & more in the Dashboard. Effortlessly navigate from the automation dashboard to HyperTest logs (and vice-versa) to get more details of the test execution.

Shown below is the HyperTest Automation dashboard which also lists the tests that were executed as a part of the test suite:

<img width="1238" alt="behave_hypertest_automation_dashboard" src="https://user-images.githubusercontent.com/1688653/152794671-044cfe72-df63-4608-b8d4-91351c9f64ed.png">

Here is a screenshot that lists the automation test that was executed on the HyperTest grid:

<img width="1427" alt="behave_testing_automation_dashboard" src="https://user-images.githubusercontent.com/1688653/152795407-5dfdb323-3c13-4119-8b43-891d7affcb05.png">

## We are here to help you :)
* LambdaTest Support: [support@lambdatest.com](mailto:support@lambdatest.com)
* Lambdatest HomePage: https://www.lambdatest.com
* HyperTest HomePage: https://www.lambdatest.com/support/docs/getting-started-with-hypertest/
