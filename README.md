![LambdaTest Logo](https://www.lambdatest.com/static/images/logo.svg)
---

# python-behave-todo
behave integration with LambdaTest<br/>


### Setup
Install depedencies ```pip install -r requirements.txt```
### Configuration steps
##### Setting locally
- Update `user.json` with your LambdaTest username and access key. It can be obtained from [LambdaTest dashbaord](https://automation.lambdatest.com/)
example:
```
     {
        "username":"Your Username",
        "access_key":"Your Access Key"
     }
```
-For setting capaibilies,Update `config.json`  (List of supported OS platfrom, Browser, resolutions can be found at [LambdaTest capability generator](https://www.lambdatest.com/capabilities-generator/))
 example:
```
   [
     {
        "platform": "win10",
        "browserName": "chrome",
        "version": "67.0",
        "resolution": "1024x768",
        "name": "this is the behave test",
        "build": "behave-test-lambdatest"
     }
   ]
```
##### Setting test through jenkins
Please refer this [url](https://www.lambdatest.com/support/docs/display/TD/Selenium+with+Jenkins)
#####  Routing traffic through your local machine
- Set tunnel value to `true` in test capabilities
> OS specific instructions to download and setup tunnel binary can be found at the following links.
>    - [Windows](https://www.lambdatest.com/support/docs/display/TD/Local+Testing+For+Windows)
>    - [Mac](https://www.lambdatest.com/support/docs/display/TD/Local+Testing+For+MacOS)
>    - [Linux](https://www.lambdatest.com/support/docs/display/TD/Local+Testing+For+Linux)

### Run tests
##### through local
```bash
paver run 
```

##### through jenkins
```bash
paver run jenkins
```

