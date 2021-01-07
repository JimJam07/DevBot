import click
import os

@click.command()
@click.option('--filename', prompt="Enter Your Test File(make sure to be in your cwd)")
@click.option('--function', prompt="Enter Your Function to be Tested")
@click.option('--path',default="../../")
def test(filename,function,path):
    current_directory = os.getcwd()
    file = os.path.join(current_directory,filename+"__test.py")
    new_file = open(file,'w+')
    print(f"\033[92m{file} created succesfully\033[0m")
    content = f"""from {filename} import {function}"""
    new_file.write(content)