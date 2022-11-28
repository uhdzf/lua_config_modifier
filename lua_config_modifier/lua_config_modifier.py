#!/usr/bin/env python3.10

import sys

# READ ME
# (1) Add or modify the entries in the dictionaries.
# (2) Add or remove dictionaries and map them in param_dict.
# (3) Skipps comments marked with '--'
# (4) Make sure any necessary additional text signs like commas or points are also set.
# (5) Call this program f.e. like this:
# python lua_config_modifier.py 1
# The number 1 is the programm argument.
# Currently the 1 maps to the dictionary it1
# The variables will then have their values replaced with the ones in that dictionary.

# Add here input and output file name.
config_file = "tests/test_kitti_3d_modi.lua"

# Add here the variable names and the value to be set per iteration.
# Make sure any necessary additional text signs like commas or points are also set.
# This script replaces the part on the right side of the equation with the set value in the dictionaries.
# Example
it1 = {
"POSE_GRAPH.constraint_builder.sampling_ratio" : "123456.0,",
"lookup_transform_timeout_sec" : "22222.0,",
"TRAJECTORY_BUILDER_3D.max_range" : "12sdf6.0,",
"POSE_GRAPH.constraint_builder.global_localization_min_score" : "123456.0,"
}

# Example
it2 = {
"test4" : "4",
"test5" : "5",
"test6" : "6"
}

# Example
it3 = {
"test7" : "7",
"test8" : "8",
"test9" : "9"
}

# Map here the python program argument to the dictionary.
param_dict = {
'1' : it1, 
'2' : it2,
'3' : it3
}

def read_config_file(config_file: str) -> list[str]:
    # Reads given config file and returns the files content as a list of strings
    file = open(config_file, "r")
    Lines = file.readlines()
    return Lines

def modify_lua_config(config_file: str, param_dict: dict) -> None:
    """
    Changes the values of choosen parameters in a lua configuration file.

    Args:
        config_file: the lua configuration file to modify
        param_dict: the diction

    Returns:
        None

    """
    Lines = read_config_file(config_file)
    # Argument is a number.
    # Number points to a dictionary.
    args = sys.argv[1:]
    args = [1]
    # TODO: add arg support for control of number of iteration through cli argument
    # if len(args) == 1:
    #     pass

    # if len(args) == 2:
    #     if args[1] == "test":
    #         pass
    #     else :
    #         sys.exit("[ERROR] Bad argument: if test mode is wished, type "test" as second argument. If not, no second argument is needed.")
    # if len(args) != 2:
    #     sys.exit("[ERROR] Bad argument: argument must be the number of the current iteration.")

    # Amount of changes
    changes_made = 0
    # Iterate through dictionary.
    for key, value in param_dict[args[0]].items():
        it = 0
        print("(" + str(it + 1) + ") " + "current key-value pair: " + key, '->', value)
        # Iterate through config file lines.
        for line in Lines:
            i = line.find(key, 0, len(line))
            # found a variable mapped in selected dictionary in the config file lines.
            if i > -1:
                print("(" + str(it + 1) + ") " + "found mapped variable.")
                # sort out commented lines.
                if (line[0] == '-' and line[1] == '-') :
                    print("(" + str(it + 1) + ") " + "skipping line: " + line.replace("\n", ""))
                else :
                    j = line.find('=', 0, len(line))
                    if j > -1:
                        # build new line with new value.
                        s1 = line[:j] + "= " + value + "\n"
                        print("(" + str(it + 1) + ") " + "before : " + line.replace("\n", ""))
                        print("(" + str(it + 1) + ") " + "after  : " + s1.replace("\n", ""))
                        # increment changes
                        Lines[int(it)] = s1

                        changes_made += 1

            it = int(it) + 1

    print("\nSelected dictionary length was " + str(len(param_dict[args[0]].items())) + ".")  
    print("\n{0} change(s) were made.".format(changes_made)) 

    # Save modified config file lines.
    with open(config_file, 'w') as the_file:
        the_file.write("".join(Lines))

if __name__ == "__main__":
    modify_lua_config(config_file, param_dict)

# Testcases
# - no programm argument -> no changes
# - multiple program arguments -> no changes
# - correct program argument -> possible changes
# - check output file can be input file
# - check changes in console are actually made in output file
