import slash

# Sample fixture
@slash.fixture
def device():
    details = {
        "Name": "Alpha",
        "Model": "X1",
        "Version": 3.0
    }
    return details

def test_device_data(device):
    slash.logger.info(device.keys())

# Fixture Parametrization
@slash.fixture
def SimpleDevice():
    details = {
        "Name": "Omega",
        "Version": 1.0
    }
    return details

@slash.fixture
def AdvancedDevice():
    details = {
        "Name": "Omega",
        "Version": 1.0
    }
    return details

@slash.parametrize('device_class', [SimpleDevice, AdvancedDevice])
def test_microwave(device_class):
    returned = device_class()
    slash.logger.info(returned.items())
