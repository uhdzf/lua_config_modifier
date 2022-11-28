"""tests the lua_config_modifier.lua_config_modifier module"""
from lua_config_modifier.lua_config_modifier import read_config_file
from lua_config_modifier.lua_config_modifier import modify_lua_config

# import os
from random import uniform

def test_read_config_file():
    assert len(read_config_file("tests/test_kitti_3d_modi.lua")) != 0

def test_modify_lua_config():
    ## Testing procedure
    # 0. generate random parameter value
    # 1. generate dictionary with random modified parameter
    # 1. use tested function on test file and with new dictionary
    # 3. read test file
    # 4. assert test line to modified line in test file
    test_file = "tests/test_kitti_3d_modi.lua"
    test_parameter = "POSE_GRAPH.constraint_builder.sampling_ratio"
    test_value = str(uniform(1e-2, 1e2))

    test_line = test_parameter + ' = ' + test_value + '\n'
    test_dict = { test_parameter : test_value }
    param_dict = {1: test_dict, 2: test_dict, 3: test_dict }

    modify_lua_config(test_file, param_dict)
    #os.system('lua_config_modifier/lua_config_modifier.py')

    f = open(test_file, "r")
    Lines = f.readlines()

    assert test_line in Lines
