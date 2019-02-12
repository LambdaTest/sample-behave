from selenium import webdriver
import os
import json

TASK_ID = int(os.environ['TASK_ID']) if 'TASK_ID' in os.environ else 0
if os.environ["env"] == "jenkins":
    desired_cap_dict = os.environ["LT_BROWSERS"]
    CONFIG = json.loads(desired_cap_dict)
else:
    json_file = "config/config.json"
    with open(json_file) as data_file:
        CONFIG = json.load(data_file)

with open("config/user.json") as data_file:
    USER_CONFIG = json.load(data_file)

username = os.environ["LT_USERNAME"] if "LT_USERNAME" in os.environ else USER_CONFIG["username"]
authkey = os.environ["LT_ACCESS_KEY"] if "LT_ACCESS_KEY" in os.environ else USER_CONFIG["access_key"]


def before_feature(context, feature):
    desired_cap = setup_desired_cap(CONFIG[TASK_ID])
    context.browser = webdriver.Remote(
        desired_capabilities=desired_cap,
        command_executor="https://%s:%s@hub.lambdatest.com:443/wd/hub" % (username, authkey)
    )


def after_feature(context, feature):
    context.browser.quit()


def setup_desired_cap(desired_cap):
    if os.environ['env'] == 'jenkins':
        desired_cap["platform"] = desired_cap["operatingSystem"]
        del desired_cap["operatingSystem"]
        desired_cap["version"] = desired_cap["browserVersion"]
        del desired_cap["browserVersion"]
        if "LT_TUNNEL_NAME" in os.environ:
            desired_cap["TunnelName"] = os.environ["LT_TUNNEL_NAME"]
    if "tunnel" in desired_cap:
        if desired_cap["tunnel"].lower() == "true":
            desired_cap["tunnel"] = True
        elif desired_cap["tunnel"].lower() == "false":
            desired_cap["tunnel"] = False
    if "console" in desired_cap:
        if desired_cap["console"].lower() == "true":
            desired_cap["console"] = True
        elif desired_cap["console"].lower() == "false":
            desired_cap["console"] = False
    if "network" in desired_cap:
        if desired_cap["network"].lower() == "true":
            desired_cap["network"] = True
        elif desired_cap["network"].lower() == "false":
            desired_cap["network"] = False
    if "visual" in desired_cap:
        if desired_cap["visual"].lower() == "true":
            desired_cap["visual"] = True
        elif desired_cap["visual"].lower() == "false":
            desired_cap["visual"] = False
    if "video" in desired_cap:
        if desired_cap["video"].lower() == "true":
            desired_cap["video"] = True
        elif desired_cap["video"].lower() == "false":
            desired_cap["video"] = False
    return desired_cap
