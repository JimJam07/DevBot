import click
import os
import pathlib
import pytest
import time

@click.command()
@click.option('--filename', prompt="Enter Your Test File(make sure to be in your cwd)")
@click.option('--function', prompt="Enter Your Function to be Tested")
@click.option('--arguments', prompt="number of arguments")
def test(filename,function,arguments):
    arg = "" #for getting arguments of an array
    print(f"\033[31mEnter the Arguments each in different line: \033[0m")
    for i in range(int(arguments)):
        a=input()
        arg+=a+","
    result = int(input("enter desired o/p: "))#for storing the desired o/p value
    current_directory = os.getcwd()
    if(not pathlib.Path(f"{filename}.py").exists()):
        print(f"\033[31mFatal Error: file {filename} does not Exist\033[0m")
    elif(function in dir(os)):
        print(f"\033[31mFatal Error: function {function} does not Exist in {filename}\033[0m")
    else:
        file = os.path.join(current_directory,filename+"_test.py")
        new_file = open(file,'w+')
        print(f"\033[92m{file} created succesfully\033[0m")
        content = f"""import pytest
from importlib.machinery import SourceFileLoader

foo = SourceFileLoader("{filename}.py", f"{os.getcwd()}/{filename}.py").load_module()

def test_method():
    assert foo.{function}({arg}) == {result}"""
        new_file.write(content)
        new_file.close()
        time.sleep(2)
        print(f"\033[92mTests are being conducted on {file}\033[0m")
        time.sleep(5)
        os.system(f"pytest {filename}_test.py")