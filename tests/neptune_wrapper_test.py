import pytest
from pathlib import Path
import shutil
from ..neptune_wrapper.neptune_wrapper import NeptuneWrapper
from ..neptune_wrapper.utils import Params

@pytest.fixture
def parameters_dict():
    return {
        'param1': 1,
        'param2': 2
    }

@pytest.fixture
def parameters():
    return Params(param1=1, param2=2)

@pytest.fixture
def neptune_wrapper_with_dict_params(parameters_dict):
    wrapper = NeptuneWrapper(projectName='dummy_project', params=parameters_dict)
    return wrapper

@pytest.fixture
def neptune_wrapper_params(parameters):
    wrapper = NeptuneWrapper(projectName='dummy_project', params=parameters)
    return wrapper

def test_neptune_wrapper_logs_right_projects(neptune_wrapper_params):
    assert neptune_wrapper_params.projectName == 'dummy_project'

@pytest.mark.parametrize('nwrapper',
                         ['neptune_wrapper_with_dict_params', 'neptune_wrapper_params'])
def test_create_run_valid(nwrapper, request):
    # Creating a Neptune run in offline mode to avoid sending requests to the Neptune server
    wrapper = request.getfixturevalue(nwrapper)
    wrapper.create_run(mode='offline')
    id = wrapper.run._id
    wrapper.stop_run() # to kill the process
    # Run folder could have any suffixes. Test whether we have the folder in offline with id
    testpath = Path('.neptune/offline/')
    listpath = [str(i) for i in testpath.glob('*')] # list of all folders in offline
    boolpath = [id in i for i in listpath] # check if id is in any of the folders
    assert any(boolpath)

def test_create_run_invalid(neptune_wrapper_params):
    with pytest.raises(ValueError):
        neptune_wrapper_params.create_run(mode='invalid')

def test_tensorflow_callback_is_created(neptune_wrapper_params):
    neptune_wrapper_params.create_run(mode='offline')
    callback = neptune_wrapper_params.get_tensorflow_keras_callback()
    neptune_wrapper_params.stop_run() # to kill the process
    assert callback.__class__.__name__ == 'NeptuneCallback'

def test_pytorch_callback_is_created(neptune_wrapper_params):
    import torch
    model = torch.nn.Sequential(torch.nn.Linear(1, 1))
    neptune_wrapper_params.create_run(mode='offline')
    callback = neptune_wrapper_params.get_pytorch_callback(model)
    neptune_wrapper_params.stop_run() # to kill the process
    assert callback.__class__.__name__ == 'NeptuneLogger'


@pytest.fixture(scope="session", autouse=True)
def cleanup(request):
    """Cleanup a testing directory once we are finished."""
    def remove_test_dir():
        shutil.rmtree('.neptune', ignore_errors=True)
    request.addfinalizer(remove_test_dir)
