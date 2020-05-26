import argparse
from pathlib import Path
import pandas as pd
import matplotlib  
import matplotlib.pyplot as plt 
import datetime

# to avoid chained warnings
pd.options.mode.chained_assignment = None

''' simple inspection of the data frame '''
def inspect(data):
    # get overall info of the data frame object
    print(data.info()) # OBSERVATION : File has 259200 entries. ADC in proximitysensor is analog-to-digital converter(for discete values)
    
    # look at some sample rows
    print(data.head(5)) # OBSERVATION : EpochTimeStamp is not in user friendly format. Convert it !

    # get mean, variance, min and so on for the columns
    print(data.describe())
    # OBSERVATION : ProximitySensor has negative values(remove), max value is too high (remove outliers); 
    # OBSERVATION : SampleNumber goes uptill 65k. It Probably repeats 4 times !

    # Analyse the values of the quartiles of  var ProximitySensor
    l = [0.9, 0.95, 0.97, 0.99 , 1]
    for i, n in enumerate(l):
        print(f"Value at quartile {n} is {data['ProximitySensor_ADC_12Bits'].quantile(n)}")

    # find the number of negatives 
    print(f"The number of negative values in ProximitySensor are :{sum(n < 0 for n in data['ProximitySensor_ADC_12Bits'])}")
    # OBSERVATION :  360 negative values found - remove them in the preprocessing step

    # Find index of value 0 in 'SampleNumber'
    for i, n in enumerate(data['SampleNumber_16Bits']):
        if(n == 0):
            print(i)
    # OBSERVATION : Zero indices found at : 0, 65536, 131072, 196608. However thats because we reach a limit of sample number since its 16bits

    # check if entire data frame has NaN values 
    print(f"Are there any NaN values in the DF :{data.isnull().values.any()}")  # OBSERVATION : no NaN values were found

    # OBSERVATION : The data is collected on 3 days, 2019-05-06, 2019-05-07, 2019-05-08. The last observation for 9th May can be removed

''' function performs the preproceesing of the data frame'''
def preprocess(data):
    # change 10 digit time column to proper date-time format.
    data['EpochTimestamp'] = pd.to_datetime(data['EpochTimestamp'], unit='s')

    # last row is dropped since it is the only data for day 2019-05-09
    data = data[:-1]
    
    # find the mean ProximitySensor
    mean_dist = data['ProximitySensor_ADC_12Bits'].mean()
    std_dist = data['ProximitySensor_ADC_12Bits'].std()

    # Convert the negative values  and values > mean + std from var [ProximitySensor] to mean value.
    data['ProximitySensor_ADC_12Bits'][(data['ProximitySensor_ADC_12Bits'] < 0) | (data['ProximitySensor_ADC_12Bits'] > mean_dist+std_dist)] = mean_dist

    # Split 'EpochTimestamp' col into two others which capture the date and time respectively. Time converted to str to enable plotting
    data['Date'] = [d.date() for d in data['EpochTimestamp']]
    data['Time'] = [d.strftime("%H:%M") for d in data['EpochTimestamp']]
    # data['Time'] = [d.time() for d in data['EpochTimestamp']]
    
    return data

def generate_save_plot(data, save_path):
    # # manual inspection of the data
    # inspect(data)

    # perform preprocessing steps
    data = preprocess(data)
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