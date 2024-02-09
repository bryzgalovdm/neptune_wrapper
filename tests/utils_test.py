# Generated together with Professional Coder plugin of chatGPT

from neptune_wrapper.utils import Params, manage_folders
from neptune_wrapper.utils import name_output_folder, find_dir_number
import pytest
import pathlib
import shutil

def test_initialization_with_arguments():
    """ Test if Params can be instantiated with arguments """
    params = Params(chans=32, epochs=10)
    assert params is not None
    assert params.chans == 32
    assert params.epochs == 10

def test_initialization_without_arguments():
    """ Test if Params can be instantiated without arguments """
    params = Params()
    assert params is not None

def test_add_parameters_new_parameter():
    """ Test adding a new parameter """
    params = Params()
    params.add_parameters(new_param=0.5)
    assert hasattr(params, 'new_param')
    assert params.new_param == 0.5

def test_add_parameters_update_existing():
    """ Test updating an existing parameter """
    params = Params(initial_param=1.0)
    params.add_parameters(initial_param=2.0)
    assert params.initial_param == 2.0

# ------------------- manage_folders ------------------- #

@pytest.fixture
def folder_setup_no_model():
    curDir = pathlib.Path().absolute()
    dirModelNoIn, dirLogNoIn, dirResultNoIn = manage_folders()
    yield curDir, dirModelNoIn, dirLogNoIn, dirResultNoIn
    shutil.rmtree(dirModelNoIn)
    shutil.rmtree(dirLogNoIn)
    shutil.rmtree(dirResultNoIn)

@pytest.fixture
def folder_setup_only_model():
    curDir = pathlib.Path().absolute()
    dirModelNoIn, dirLogNoIn, dirResultNoIn = manage_folders(dirModel='damngreatmodel')
    yield curDir, dirModelNoIn, dirLogNoIn, dirResultNoIn
    shutil.rmtree(dirModelNoIn)
    shutil.rmtree(dirLogNoIn)
    shutil.rmtree(dirResultNoIn)

@pytest.fixture
def folder_setup_only_log():
    curDir = pathlib.Path().absolute()
    dirModelOnlyLog, dirLogOnlyLog, dirResultOnlyLog = manage_folders(dirLog='damngreatLog')
    yield curDir, dirModelOnlyLog, dirLogOnlyLog, dirResultOnlyLog
    shutil.rmtree(dirModelOnlyLog)
    shutil.rmtree(dirLogOnlyLog)
    shutil.rmtree(dirResultOnlyLog)

@pytest.fixture
def folder_setup_only_result():
    curDir = pathlib.Path().absolute()
    dirModelOnlyResults, dirLogOnlyResults, dirResultOnlyResults = manage_folders(dirResult='damngreatresults')
    yield curDir, dirModelOnlyResults, dirLogOnlyResults, dirResultOnlyResults
    shutil.rmtree(dirModelOnlyResults)
    shutil.rmtree(dirLogOnlyResults)
    shutil.rmtree(dirResultOnlyResults)

@pytest.fixture
def folder_setup_eegnet():
    curDir = pathlib.Path().absolute()
    dirModelEEGNet, dirLogEEGNet, dirResultEEGNet = manage_folders(nameModel='eegnet')
    yield curDir, dirModelEEGNet, dirLogEEGNet, dirResultEEGNet
    shutil.rmtree(dirModelEEGNet)
    shutil.rmtree(dirLogEEGNet)
    shutil.rmtree(dirResultEEGNet)

def test_no_inputs_model_output(folder_setup_no_model):
    curDir, dirModelNoIn, _, _ = folder_setup_no_model
    strToMatch = str(curDir.joinpath('defaultnet_model'))
    assert dirModelNoIn == strToMatch

def test_no_inputs_model_folder_exists(folder_setup_no_model):
    curDir, dirModelNoIn, _, _ = folder_setup_no_model
    pathToFind = curDir.joinpath('defaultnet_model')
    assert pathToFind.exists()

def test_no_inputs_log_output(folder_setup_no_model):
    curDir, _, dirLogNoIn, _ = folder_setup_no_model
    strToMatch = str(curDir.joinpath('defaultnet_log'))
    assert dirLogNoIn == strToMatch

def test_no_inputs_log_folder_exists(folder_setup_no_model):
    curDir, _, dirLogNoIn, _ = folder_setup_no_model
    pathToFind = curDir.joinpath('defaultnet_log')
    assert pathToFind.exists()

def test_no_inputs_results_output(folder_setup_no_model):
    curDir, _, _, dirResultNoIn = folder_setup_no_model
    strToMatch = str(curDir.joinpath('defaultnet_results'))
    assert dirResultNoIn == strToMatch

def test_no_inputs_results_folder_exists(folder_setup_no_model):
    curDir, _, _, dirResultNoIn = folder_setup_no_model
    pathToFind = curDir.joinpath('defaultnet_results')
    assert pathToFind.exists()

def test_onlyModel_model_output(folder_setup_only_model):
    curDir, dirModelOnlyIn, _, _ = folder_setup_only_model
    strToMatch = str(curDir.joinpath('damngreatmodel'))
    assert dirModelOnlyIn == strToMatch

def test_onlyModel_model_folder_exists(folder_setup_only_model):
    curDir, _, _, _ = folder_setup_only_model
    pathToFind = curDir.joinpath('damngreatmodel')
    assert pathToFind.exists()

def test_onlyModel_log_output(folder_setup_only_model):
    curDir, _, dirLogOneModelIn, _ = folder_setup_only_model
    strToMatch = str(curDir.joinpath('defaultnet_log'))
    assert dirLogOneModelIn == strToMatch

def test_onlyModel_log_folder_exists(folder_setup_only_model):
    curDir, _, _, _ = folder_setup_only_model
    pathToFind = curDir.joinpath('defaultnet_log')
    assert pathToFind.exists()

def test_onlyModel_result_output(folder_setup_only_model):
    curDir, _, _, dirResultOneModelIn = folder_setup_only_model
    strToMatch = str(curDir.joinpath('defaultnet_results'))
    assert dirResultOneModelIn == strToMatch

def test_onlyModel_results_folder_exists(folder_setup_only_model):
    curDir, _, _, _ = folder_setup_only_model
    pathToFind = curDir.joinpath('defaultnet_results')
    assert pathToFind.exists()

def test_onlyLog_model_output(folder_setup_only_log):
    curDir, dirModelOnlyLog, _, _ = folder_setup_only_log
    strToMatch = str(curDir.joinpath('defaultnet_model'))
    assert dirModelOnlyLog == strToMatch

def test_onlyLog_model_folder_exists(folder_setup_only_log):
    curDir, dirModelOnlyLog, _, _ = folder_setup_only_log
    pathToFind = curDir.joinpath('defaultnet_model')
    assert pathToFind.exists()

def test_onlyLog_log_output(folder_setup_only_log):
    curDir, _, dirLogOnlyLog, _ = folder_setup_only_log
    strToMatch = str(curDir.joinpath('damngreatLog'))
    assert dirLogOnlyLog == strToMatch

def test_onlyLog_log_folder_exists(folder_setup_only_log):
    curDir, _, dirLogOnlyLog, _ = folder_setup_only_log
    pathToFind = curDir.joinpath('damngreatLog')
    assert pathToFind.exists()

def test_onlyLog_results_output(folder_setup_only_log):
    curDir, _, _, dirResultOnlyLog = folder_setup_only_log
    strToMatch = str(curDir.joinpath('defaultnet_results'))
    assert dirResultOnlyLog == strToMatch

def test_onlyLog_results_folder_exists(folder_setup_only_log):
    curDir, _, _, dirResultOnlyLog = folder_setup_only_log
    pathToFind = curDir.joinpath('defaultnet_results')
    assert pathToFind.exists()

# Tests for onlyResult fixture
def test_onlyResult_model_output(folder_setup_only_result):
    curDir, dirModelOnlyResults, _, _ = folder_setup_only_result
    strToMatch = str(curDir.joinpath('defaultnet_model'))
    assert dirModelOnlyResults == strToMatch

def test_onlyResult_model_folder_exists(folder_setup_only_result):
    curDir, dirModelOnlyResults, _, _ = folder_setup_only_result
    pathToFind = curDir.joinpath('defaultnet_model')
    assert pathToFind.exists()

def test_onlyResult_log_output(folder_setup_only_result):
    curDir, _, dirLogOnlyResults, _ = folder_setup_only_result
    strToMatch = str(curDir.joinpath('defaultnet_log'))
    assert dirLogOnlyResults == strToMatch

def test_onlyResult_log_folder_exists(folder_setup_only_result):
    curDir, _, dirLogOnlyResults, _ = folder_setup_only_result
    pathToFind = curDir.joinpath('defaultnet_log')
    assert pathToFind.exists()

def test_onlyResult_results_output(folder_setup_only_result):
    curDir, _, _, dirResultOnlyResults = folder_setup_only_result
    strToMatch = str(curDir.joinpath('damngreatresults'))
    assert dirResultOnlyResults == strToMatch

def test_onlyResult_results_folder_exists(folder_setup_only_result):
    curDir, _, _, dirResultOnlyResults = folder_setup_only_result
    pathToFind = curDir.joinpath('damngreatresults')
    assert pathToFind.exists()

# Tests for eegnet fixture
def test_eegnet_model_output(folder_setup_eegnet):
    curDir, dirModelEEGNet, _, _ = folder_setup_eegnet
    strToMatch = str(curDir.joinpath('eegnet_model'))
    assert dirModelEEGNet == strToMatch

def test_eegnet_model_folder_exists(folder_setup_eegnet):
    curDir, dirModelEEGNet, _, _ = folder_setup_eegnet
    pathToFind = curDir.joinpath('eegnet_model')
    assert pathToFind.exists()

def test_eegnet_log_output(folder_setup_eegnet):
    curDir, _, dirLogEEGNet, _ = folder_setup_eegnet
    strToMatch = str(curDir.joinpath('eegnet_log'))
    assert dirLogEEGNet == strToMatch

def test_eegnet_log_folder_exists(folder_setup_eegnet):
    curDir, _, dirLogEEGNet, _ = folder_setup_eegnet
    pathToFind = curDir.joinpath('eegnet_log')
    assert pathToFind.exists()

def test_eegnet_results_output(folder_setup_eegnet):
    curDir, _, _, dirResultEEGNet = folder_setup_eegnet
    strToMatch = str(curDir.joinpath('eegnet_results'))
    assert dirResultEEGNet == strToMatch

def test_eegnet_results_folder_exists(folder_setup_eegnet):
    curDir, _, _, dirResultEEGNet = folder_setup_eegnet
    pathToFind = curDir.joinpath('eegnet_results')
    assert pathToFind.exists()

# ------------------- name_output_folder ------------------- #

@pytest.fixture
def folder_setup_name_output():
    curDir = pathlib.Path().absolute()
    testDirEEGModel1 = curDir.joinpath("eegnet_model5")
    testDirEEGModel2 = curDir.joinpath("eegnet_model2")
    testDirEEGResult = curDir.joinpath("eegnet_results7")
    testDirEEGLog = curDir.joinpath("eegnet_log3")
    testDirRandom = curDir.joinpath("random_pattern1h__23")

    # Setup
    testDirEEGModel1.mkdir(parents=True, exist_ok=True)
    testDirEEGModel2.mkdir(parents=True, exist_ok=True)
    testDirEEGResult.mkdir(parents=True, exist_ok=True)
    testDirEEGLog.mkdir(parents=True, exist_ok=True)
    testDirRandom.mkdir(parents=True, exist_ok=True)
    yield curDir

    # Teardown
    shutil.rmtree(testDirEEGModel1)
    shutil.rmtree(testDirEEGModel2)
    shutil.rmtree(testDirEEGResult)
    shutil.rmtree(testDirEEGLog)
    shutil.rmtree(testDirRandom)

def test_if_find_dir_gives_zero_if_no_matching_folders_are_found(folder_setup_name_output):
    curDir = folder_setup_name_output
    output = find_dir_number(curDir, 'nofolder')
    assert output == 0

def test_find_dir_number_finds_eegnet_model(folder_setup_name_output):
    curDir = folder_setup_name_output
    output = find_dir_number(curDir, "eegnet_model")
    assert output == 5

def test_find_dir_number_finds_eegnet_log(folder_setup_name_output):
    curDir = folder_setup_name_output
    output = find_dir_number(curDir, "eegnet_log")
    assert output == 3

def test_find_dir_number_finds_eegnet_results(folder_setup_name_output):
    curDir = folder_setup_name_output
    output = find_dir_number(curDir, "eegnet_results")
    assert output == 7

def test_find_dir_number_finds_random_pattern(folder_setup_name_output):
    curDir = folder_setup_name_output
    output = find_dir_number(curDir, "random_pattern1h__")
    assert output == 23

def test_find_dir_number_gives_error_if_after_pattern_no_int(folder_setup_name_output):
    curDir = folder_setup_name_output
    output = find_dir_number(curDir, "random_pattern")
    assert output == 0

def test_name_output_folder_gives_correct_predefined_name(folder_setup_name_output):
    curDir = folder_setup_name_output
    output = name_output_folder(folder='folderName', nameModel='rnn', typeFolder='model')
    strToMatch = str(curDir.joinpath('folderName'))
    assert output == strToMatch

def test_name_output_folder_counts_right_model(folder_setup_name_output):
    curDir = folder_setup_name_output
    output = name_output_folder(nameModel='eegnet', typeFolder='model')
    strToMatch = str(curDir.joinpath('eegnet_model6'))
    assert output == strToMatch

def test_name_output_folder_counts_right_results(folder_setup_name_output):
    curDir = folder_setup_name_output
    output = name_output_folder(nameModel='eegnet', typeFolder='results')
    strToMatch = str(curDir.joinpath('eegnet_results8'))
    assert output == strToMatch

def test_name_output_folder_counts_right_log(folder_setup_name_output):
    curDir = folder_setup_name_output
    output = name_output_folder(nameModel='eegnet', typeFolder='log')
    strToMatch = str(curDir.joinpath('eegnet_log4'))
    assert output == strToMatch

def test_name_output_folder_if_no_pattern_was_found(folder_setup_name_output):
    curDir = folder_setup_name_output
    output = name_output_folder(nameModel='random', typeFolder='something')
    strToMatch = str(curDir.joinpath('random_something'))
    assert output == strToMatch

def test_name_output_folder_if_no_pattern_was_found_no_name(folder_setup_name_output):
    curDir = folder_setup_name_output
    output = name_output_folder(typeFolder='something')
    strToMatch = str(curDir.joinpath('_something'))
    assert output == strToMatch

def test_name_output_folder_if_no_pattern_was_found_no_type(folder_setup_name_output):
    curDir = folder_setup_name_output
    output = name_output_folder(nameModel='something', typeFolder='')
    strToMatch = str(curDir.joinpath('something_'))
    assert output == strToMatch

def test_name_output_folder_if_no_pattern_was_found_nothing(folder_setup_name_output):
    with pytest.raises(ValueError):
        name_output_folder(nameModel='', typeFolder='')



