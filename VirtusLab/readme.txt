I understood "executable program" as the use of a console application together with the given command from the task. So to enable it you should type:

main.py join file_path file_path column_name join_type

As a solution, I adopted the use of the pandas library, which links the given files, using the merge() method with its necessary arguments.

Default join type is set to inner. 