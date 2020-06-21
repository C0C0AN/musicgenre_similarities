# NC2U - neuroimaging design

Here you will find the code and additional information concerning the design of the neuroimaging (fMRI & EGG) parts of this project, which was created using a two step procedure as outlined below.

#### Generate stimuli sequences

In order to create stimuli sequences per run for the planned stimulus rich event related design, we utilized the [FreeSurfer tool]() [OptSeq2](). While the stimulus time and number of repetition per run were set to 6 seconds and 2 respectively, we allowed the inter-stimulus-interval to vary between 4 and 8 seconds. We set the number of to be generated sequences to 1000 and the number of sequences to keep to 8. These settings are reflected in the bash script [optseq2_script.sh]().


##### Generate run files

The resulting output of the [optseq2_script.sh]() function, that is sequences and inter-stimulus-intervals, was utilized within [make_design.py](). Within this function `csv` files with run specific stimuli orders (sequences) and rest-periods (inter-stimulus-intervals) were created. 
