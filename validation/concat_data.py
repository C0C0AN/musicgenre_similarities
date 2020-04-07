# concat_data.py
# function to concatenate results data-frames/csv-files from the music genre stimuli validation questionnaire 
# to create one large data frame including data from all participants

def concat_data(inputpath, df_name):
    '''input path as string + name of new dataset as str 
    (avoid using data as the first letters of your result file, because it may lead to unexpected errors)'''
    
    import glob, os
	import pandas as pd

    # set path of input data frame(s)
    path = str(inputpath)
    
    # specify which files to concatenate (change 'data*' depending on how you've named your files)
    allFiles = glob.glob(os.path.join(path,'data*'))

    # concatenate all files starting with data*
    df = pd.concat((pd.read_csv(f) for f in allFiles))
    
    # drop unnecessary column
    df.drop(['Unnamed: 0'],axis=1, inplace=True)
    
    # write csv to directory
    df.to_csv(path + str(df_name) +'.csv')
    
    # print finish message
    print('done!')
