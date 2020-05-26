import argparse
from pathlib import Path
import pandas as pd
import matplotlib  
import matplotlib.pyplot as plt 
import datetime

# to avoid chained warnings
pd.options.mode.chained_assignment = None



def generate_save_plot(data, save_path):
    return 1


if __name__ == "__main__":
    # user defined command line argument
    parser = argparse.ArgumentParser()
    # adding optional argument 
    parser.add_argument("-f", "--filepath", type=str,
                help="enter the file path for reading json data file")
    # inspects the command line and reads the arguments, assigning them as attributes to "args"
    args = parser.parse_args()
    # reading the --filepath argument
    file_path = args.filepath
    # checks is a filepath has been entered 
    if args.filepath:
        print(f"The json data file will be read from file path :{file_path}")
    else:
        print("File path not entered. Please enter filepath using flag -f.")

    # check if json file exists at filepath specified 
    input_file_path = Path(file_path)
    try:
        my_abs_path = input_file_path.resolve(strict=True)
    except FileNotFoundError:
        print(f"Json data file not found at filepath :{input_file_path}")
    else:
        print("File being read.")
        # input json file and store it as data frame
        data = pd.read_json(input_file_path)
        # function generates plot and saves it in the file path specified
        generate_save_plot(data, str(input_file_path.parent)+"/SensorData.png")

    # p = "/Users/swarajdalmia/Desktop/source/nishtha/SensorData.json"
    # data = pd.read_json(p)
    # pos = p.rfind('.')
    # generate_save_plot(data, p[0:pos]+".png")