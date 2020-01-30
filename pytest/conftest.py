import pytest

def pytest_addoption(parser):
    # Method to add the option to ini
    parser.addini("rp_uuid",'help',type="pathlist")
    parser.addini("rp_endpoint",'help',type="pathlist")
    parser.addini("rp_project",'help',type="pathlist")
    parser.addini("rp_launch",'help',type="pathlist")

@pytest.hookimpl()
def pytest_configure(config):
    # Sets the launch name based on the marker selected.
    suite = config.getoption("markexpr")
    try:
#        config._inicache["rp_uuid"]="4d2513ae-fe50-42a4-99de-90cb613ed9f2"
        config._inicache["rp_uuid"]="30ed8f89-5fc1-4c90-a7ad-b98678f7ea50"
        config._inicache["rp_endpoint"]="http://web.demo.reportportal.io"
        config._inicache["rp_project"]="slingsports_personal"
        if suite == "gui_test":
            config._inicache["rp_launch"]="gui_test"
        elif suite == "api_test":
            config._inicache["rp_launch"]="api_test"

    except Exception as e:
        print (str(e))
