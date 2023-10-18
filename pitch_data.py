import pandas as pd
import os 

def load_data(wd = os.getcwd()):
    """
    Load pitch data from in working directory.

    Parameters
    ----------
    wd : str | default : 'os.cwd()'
        The working directory in which the pitch data is located. 

    Returns
    -------
    Provided Pitch.csv and Metadata.csv as Pandas DataFrames
    """

    try:
        metadata = pd.read_csv(wd + '/pitch_by_pitch_metadata.csv' ,encoding = "windows_1258",  low_memory=False) # error loading as UTF-8
        pitches = pd.read_csv(wd + '/pitches.csv',encoding="windows_1258",  low_memory=False) # error loading as UTF-8
        print("Data Loaded!")
        return pitches, metadata

    except FileNotFoundError as e:
        raise Exception('Pass the working directory with pitch data to load_data()') from e
        