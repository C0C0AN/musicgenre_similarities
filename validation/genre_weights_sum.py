# genre_weights_sum.py
# script to compute validation weights per (sub)genre example

# import necessary modules
import glob, os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from natsort import natsorted, ns

# read in the concatenated data frame, which should include all data from all participants & get a list of the columns
df = pd.read_csv('/path/to/data/frame')
print(df.columns)

# define a list of all (sub)genre sortables which is later on used to create sub data frames
df_sortables = ['punk_sortable', 'alternative_sortable','heavymetal_sortable','psychedelic_sortable', 'rocknroll_sortable'
,'funk_sortable','hiphop_sortable', 'reggae_sortable', 'rnb_sortable', 'soul_sortable','baroque_sortable','viennese_classic_sortable', 'modern_classic_sortable',
'renaissance_sortable', 'romantic_sortable', 'deephouse_sortable', 'drumnbass_sortable','dubstep_sortable','techno_sortable','trance_sortable']

# create sub data frame only containing the values for all sortables
df_sub_sortables=df[df_sortables]

# create empty data frame which later on will contain the weights for all examples across all sortables
df_sortables_weights=pd.DataFrame()

# set columns in newly created data frame, one for the sortables and their examples, as well as one corresponding for weights
for column in df_sub_sortables.columns:
   df_sortables_weights[column]=df_sub_sortables[column]
   df_sortables_weights[column+'_weights']=0

# drop all rows that include NANs
df_sortables_weights_dropna=df_sortables_weights.dropna(0)

# assign values in weights column, ranging from 10 to 1, descending, repeating every 10 rows
for column in df_sortables_weights_dropna.columns:
   df_sortables_weights_dropna[column+'_weights']=list(list(reversed(list(range(1,11))))*int(len(df_sortables_weights_dropna['punk_sortable'])/10))

# create new data frame which later on will contain the summed weights for all examples across all sortables
df_sortables_weights_sum=pd.DataFrame()

# set columns in newly created data frame, on for the sortables and their examples, as well as one corresponding for the summed weights
for genre in df_sortables:
    df_sortables_weights_sum[genre.split('_')[0]]=genre.split('_')[0]
    df_sortables_weights_sum[genre.split('_')[0] + '_weight'] = 0

# reset index and drop the old index (the dropna function from before doesn't reset the index which will create problems for subsequent functions, e.g. for loops)
df_sortables_weights_dropna=df_sortables_weights_dropna.reset_index()
del df_sortables_weights_dropna['index']

# create empty lists for all examples across all sortables which later on will contain the weights participants assigned them
for sortable in df_sortables:
        for array_sum in df_sortables_weights_dropna[sortable].unique():
            locals()[str(array_sum) + '_sum'] = []

# loop over all sortables, read out all examples per sortables and assign their respective weights to their list
for sortable in df_sortables:
    df_sortables_weights_sum[sortable.split('_')[0]] = natsorted(df_sortables_weights_dropna[sortable].unique())
    for ex in enumerate(df_sortables_weights_dropna[sortable]):
        for array_sum in natsorted(df_sortables_weights_dropna[sortable].unique()):
            if ex[1] == array_sum:
                globals()[str(array_sum) + '_sum'].append(df_sortables_weights_dropna[sortable + '_weights'][ex[0]])

# loop over examples across sortables, sum their weights and write the results in the respective data frame position
for sortable in df_sortables:
    for column in enumerate(df_sortables_weights_sum[sortable.split('_')[0]]):
        df_sortables_weights_sum[sortable.split('_')[0] + '_weight'][column[0]] = sum(globals()[column[1] + '_sum'])

# save csv-file with stimuli and weights
df_sortables_weights_sum.to_csv('stimuli_weights_dataframe.csv')

# visualisation - create some (hopefully) informative plots showing weights per (sub)genre

# bar plots

# create factor plots for the summed weights - punk
fp = sns.factorplot(x='punk', y='punk_weight', data=df_sortables_weights_sum, palette="YlGnBu", kind='bar')
fp.set_xticklabels(rotation=45)

# create factor plots for the summed weights - alternative
fp = sns.factorplot(x='alternative', y='alternative_weight', data=df_sortables_weights_sum, palette="YlGnBu", kind='bar')
fp.set_xticklabels(rotation=45)

# create factor plots for the summed weights - heavymetal
fp = sns.factorplot(x='heavymetal', y='heavymetal_weight', data=df_sortables_weights_sum, palette="YlGnBu", kind='bar')
fp.set_xticklabels(rotation=45)

# create factor plots for the summed weights - psychedelic
fp = sns.factorplot(x='psychedelic', y='psychedelic_weight', data=df_sortables_weights_sum, palette="YlGnBu", kind='bar')
fp.set_xticklabels(rotation=45)

# create factor plots for the summed weights - rocknroll
fp = sns.factorplot(x='rocknroll', y='rocknroll_weight', data=df_sortables_weights_sum, palette="YlGnBu", kind='bar')
fp.set_xticklabels(rotation=45)

# create factor plots for the summed weights - funk
fp = sns.factorplot(x='funk', y='funk_weight', data=df_sortables_weights_sum, palette="YlGnBu", kind='bar')
fp.set_xticklabels(rotation=45)

# create factor plots for the summed weights - soul
fp = sns.factorplot(x='soul', y='soul_weight', data=df_sortables_weights_sum, palette="YlGnBu", kind='bar')
fp.set_xticklabels(rotation=45)

# create factor plots for the summed weights - hiphop
fp = sns.factorplot(x='hiphop', y='hiphop_weight', data=df_sortables_weights_sum, palette="YlGnBu", kind='bar')
fp.set_xticklabels(rotation=45)

# create factor plots for the summed weights - rnb
fp = sns.factorplot(x='rnb', y='rnb_weight', data=df_sortables_weights_sum, palette="YlGnBu", kind='bar')
fp.set_xticklabels(rotation=45)

# create factor plots for the summed weights - reggae
fp = sns.factorplot(x='reggae', y='reggae_weight', data=df_sortables_weights_sum, palette="YlGnBu", kind='bar')
fp.set_xticklabels(rotation=45)

# create factor plots for the summed weights - baroque
fp = sns.factorplot(x='baroque', y='baroque_weight', data=df_sortables_weights_sum, palette="YlGnBu", kind='bar')
fp.set_xticklabels(rotation=45)

# create factor plots for the summed weights - renaissance
fp = sns.factorplot(x='renaissance', y='renaissance_weight', data=df_sortables_weights_sum, palette="YlGnBu", kind='bar')
fp.set_xticklabels(rotation=45)

# create factor plots for the summed weights - viennese_classic
fp = sns.factorplot(x='viennese', y='viennese_weight', data=df_sortables_weights_sum, palette="YlGnBu", kind='bar')
fp.set_xticklabels(rotation=45)

# create factor plots for the summed weights - modern_classic
fp = sns.factorplot(x='modern', y='modern_weight', data=df_sortables_weights_sum, palette="YlGnBu", kind='bar')
fp.set_xticklabels(rotation=45)

# create factor plots for the summed weights - romantic
fp = sns.factorplot(x='romantic', y='romantic_weight', data=df_sortables_weights_sum, palette="YlGnBu", kind='bar')
fp.set_xticklabels(rotation=45)

# create factor plots for the summed weights - trance
fp = sns.factorplot(x='trance', y='trance_weight', data=df_sortables_weights_sum, palette="YlGnBu", kind='bar')
fp.set_xticklabels(rotation=45)

# create factor plots for the summed weights - techno
fp = sns.factorplot(x='techno', y='techno_weight', data=df_sortables_weights_sum, palette="YlGnBu", kind='bar')
fp.set_xticklabels(rotation=45)

# create factor plots for the summed weights - deephouse
fp = sns.factorplot(x='deephouse', y='deephouse_weight', data=df_sortables_weights_sum, palette="YlGnBu", kind='bar')
fp.set_xticklabels(rotation=45)

# create factor plots for the summed weights - drumnbass
fp = sns.factorplot(x='drumnbass', y='drumnbass_weight', data=df_sortables_weights_sum, palette="YlGnBu", kind='bar')
fp.set_xticklabels(rotation=45)

# create factor plots for the summed weights - dubstep
fp = sns.factorplot(x='dubstep', y='dubstep_weight', data=df_sortables_weights_sum, palette="YlGnBu", kind='bar')
fp.set_xticklabels(rotation=45)


# violin plots

# create combined violin-swarm plots for the distribution of the weights - punk
xy = sns.violinplot(x="punk_sortable", y="punk_sortable_weights", data=df_sortables_weights_dropna.sort_values(by='punk_sortable'), inner=None)
xy = sns.swarmplot(x="punk_sortable", y="punk_sortable_weights", data=df_sortables_weights_dropna.sort_values(by='punk_sortable'), color="w", alpha=.5)
xy.set_xticklabels(xy.get_xticklabels(), rotation=45)

# create combined violin-swarm plots for the distribution of the weights - alternative
xy = sns.violinplot(x="alternative_sortable", y="alternative_sortable_weights", data=df_sortables_weights_dropna.sort_values(by='alternative_sortable'), inner=None)
xy = sns.swarmplot(x="alternative_sortable", y="alternative_sortable_weights", data=df_sortables_weights_dropna.sort_values(by='alternative_sortable'), color="w", alpha=.5)
xy.set_xticklabels(xy.get_xticklabels(), rotation=45)

# create combined violin-swarm plots for the distribution of the weights - heavymetal
xy = sns.violinplot(x="heavymetal_sortable", y="heavymetal_sortable_weights", data=df_sortables_weights_dropna.sort_values(by='heavymetal_sortable'), inner=None)
xy = sns.swarmplot(x="heavymetal_sortable", y="heavymetal_sortable_weights", data=df_sortables_weights_dropna.sort_values(by='heavymetal_sortable'), color="w", alpha=.5)
xy.set_xticklabels(xy.get_xticklabels(), rotation=45)

# create combined violin-swarm plots for the distribution of the weights - psychedelic
xy = sns.violinplot(x="psychedelic_sortable", y="psychedelic_sortable_weights", data=df_sortables_weights_dropna.sort_values(by='psychedelic_sortable'), inner=None)
xy = sns.swarmplot(x="psychedelic_sortable", y="psychedelic_sortable_weights", data=df_sortables_weights_dropna.sort_values(by='psychedelic_sortable'), color="w", alpha=.5)
xy.set_xticklabels(xy.get_xticklabels(), rotation=45)

# create combined violin-swarm plots for the distribution of the weights - rocknroll
xy = sns.violinplot(x="rocknroll_sortable", y="rocknroll_sortable_weights", data=df_sortables_weights_dropna.sort_values(by='rocknroll_sortable'), inner=None)
xy = sns.swarmplot(x="rocknroll_sortable", y="rocknroll_sortable_weights", data=df_sortables_weights_dropna.sort_values(by='rocknroll_sortable'), color="w", alpha=.5)
xy.set_xticklabels(xy.get_xticklabels(), rotation=45)

# create combined violin-swarm plots for the distribution of the weights - funk
xy = sns.violinplot(x="funk_sortable", y="funk_sortable_weights", data=df_sortables_weights_dropna.sort_values(by='funk_sortable'), inner=None)
xy = sns.swarmplot(x="funk_sortable", y="funk_sortable_weights", data=df_sortables_weights_dropna.sort_values(by='funk_sortable'), color="w", alpha=.5)
xy.set_xticklabels(xy.get_xticklabels(), rotation=45)

# create combined violin-swarm plots for the distribution of the weights - soul
xy = sns.violinplot(x="soul_sortable", y="soul_sortable_weights", data=df_sortables_weights_dropna.sort_values(by='soul_sortable'), inner=None)
xy = sns.swarmplot(x="soul_sortable", y="soul_sortable_weights", data=df_sortables_weights_dropna.sort_values(by='soul_sortable'), color="w", alpha=.5)
xy.set_xticklabels(xy.get_xticklabels(), rotation=45)

# create combined violin-swarm plots for the distribution of the weights - hiphop
xy = sns.violinplot(x="hiphop_sortable", y="hiphop_sortable_weights", data=df_sortables_weights_dropna.sort_values(by='hiphop_sortable'), inner=None)
xy = sns.swarmplot(x="hiphop_sortable", y="hiphop_sortable_weights", data=df_sortables_weights_dropna.sort_values(by='hiphop_sortable'), color="w", alpha=.5)
xy.set_xticklabels(xy.get_xticklabels(), rotation=45)

# create combined violin-swarm plots for the distribution of the weights - rnb
xy = sns.violinplot(x="rnb_sortable", y="rnb_sortable_weights", data=df_sortables_weights_dropna.sort_values(by='rnb_sortable'), inner=None)
xy = sns.swarmplot(x="rnb_sortable", y="rnb_sortable_weights", data=df_sortables_weights_dropna.sort_values(by='rnb_sortable'), color="w", alpha=.5)
xy.set_xticklabels(xy.get_xticklabels(), rotation=45)

# create combined violin-swarm plots for the distribution of the weights - reggae
xy = sns.violinplot(x="reggae_sortable", y="reggae_sortable_weights", data=df_sortables_weights_dropna.sort_values(by='reggae_sortable'), inner=None)
xy = sns.swarmplot(x="reggae_sortable", y="reggae_sortable_weights", data=df_sortables_weights_dropna.sort_values(by='reggae_sortable'), color="w", alpha=.5)
xy.set_xticklabels(xy.get_xticklabels(), rotation=45)

# create combined violin-swarm plots for the distribution of the weights - baroque
xy = sns.violinplot(x="baroque_sortable", y="baroque_sortable_weights", data=df_sortables_weights_dropna.sort_values(by='baroque_sortable'), inner=None)
xy = sns.swarmplot(x="baroque_sortable", y="baroque_sortable_weights", data=df_sortables_weights_dropna.sort_values(by='baroque_sortable'), color="w", alpha=.5)
xy.set_xticklabels(xy.get_xticklabels(), rotation=45)

# create combined violin-swarm plots for the distribution of the weights - renaissance
xy = sns.violinplot(x="renaissance_sortable", y="renaissance_sortable_weights", data=df_sortables_weights_dropna.sort_values(by='renaissance_sortable'), inner=None)
xy = sns.swarmplot(x="renaissance_sortable", y="renaissance_sortable_weights", data=df_sortables_weights_dropna.sort_values(by='renaissance_sortable'), color="w", alpha=.5)
xy.set_xticklabels(xy.get_xticklabels(), rotation=45)

# create combined violin-swarm plots for the distribution of the weights - viennese_classic
xy = sns.violinplot(x="viennese_classic_sortable", y="viennese_classic_sortable_weights", data=df_sortables_weights_dropna.sort_values(by='viennese_classic_sortable'), inner=None)
xy = sns.swarmplot(x="viennese_classic_sortable", y="viennese_classic_sortable_weights", data=df_sortables_weights_dropna.sort_values(by='viennese_classic_sortable'), color="w", alpha=.5)
xy.set_xticklabels(xy.get_xticklabels(), rotation=45)

# create combined violin-swarm plots for the distribution of the weights - modern_classic
xy = sns.violinplot(x="modern_classic_sortable", y="modern_classic_sortable_weights", data=df_sortables_weights_dropna.sort_values(by='modern_classic_sortable'), inner=None)
xy = sns.swarmplot(x="modern_classic_sortable", y="modern_classic_sortable_weights", data=df_sortables_weights_dropna.sort_values(by='modern_classic_sortable'), color="w", alpha=.5)
xy.set_xticklabels(xy.get_xticklabels(), rotation=45)

# create combined violin-swarm plots for the distribution of the weights - romantic
xy = sns.violinplot(x="romantic_sortable", y="romantic_sortable_weights", data=df_sortables_weights_dropna.sort_values(by='romantic_sortable'), inner=None)
xy = sns.swarmplot(x="romantic_sortable", y="romantic_sortable_weights", data=df_sortables_weights_dropna.sort_values(by='romantic_sortable'), color="w", alpha=.5)
xy.set_xticklabels(xy.get_xticklabels(), rotation=45)

# create combined violin-swarm plots for the distribution of the weights - trance
xy = sns.violinplot(x="trance_sortable", y="trance_sortable_weights", data=df_sortables_weights_dropna.sort_values(by='trance_sortable'), inner=None)
xy = sns.swarmplot(x="trance_sortable", y="trance_sortable_weights", data=df_sortables_weights_dropna.sort_values(by='trance_sortable'), color="w", alpha=.5)
xy.set_xticklabels(xy.get_xticklabels(), rotation=45)

# create combined violin-swarm plots for the distribution of the weights - techno
xy = sns.violinplot(x="techno_sortable", y="techno_sortable_weights", data=df_sortables_weights_dropna.sort_values(by='techno_sortable'), inner=None)
xy = sns.swarmplot(x="techno_sortable", y="techno_sortable_weights", data=df_sortables_weights_dropna.sort_values(by='techno_sortable'), color="w", alpha=.5)
xy.set_xticklabels(xy.get_xticklabels(), rotation=45)

# create combined violin-swarm plots for the distribution of the weights - deephouse
xy = sns.violinplot(x="deephouse_sortable", y="deephouse_sortable_weights", data=df_sortables_weights_dropna.sort_values(by='deephouse_sortable'), inner=None)
xy = sns.swarmplot(x="deephouse_sortable", y="deephouse_sortable_weights", data=df_sortables_weights_dropna.sort_values(by='deephouse_sortable'), color="w", alpha=.5)
xy.set_xticklabels(xy.get_xticklabels(), rotation=45)

# create combined violin-swarm plots for the distribution of the weights - drumnbass
xy = sns.violinplot(x="drumnbass_sortable", y="drumnbass_sortable_weights", data=df_sortables_weights_dropna.sort_values(by='drumnbass_sortable'), inner=None)
xy = sns.swarmplot(x="drumnbass_sortable", y="drumnbass_sortable_weights", data=df_sortables_weights_dropna.sort_values(by='drumnbass_sortable'), color="w", alpha=.5)
xy.set_xticklabels(xy.get_xticklabels(), rotation=45)

# create combined violin-swarm plots for the distribution of the weights - dubstep
xy = sns.violinplot(x="dubstep_sortable", y="dubstep_sortable_weights", data=df_sortables_weights_dropna.sort_values(by='dubstep_sortable'), inner=None)
xy = sns.swarmplot(x="dubstep_sortable", y="dubstep_sortable_weights", data=df_sortables_weights_dropna.sort_values(by='dubstep_sortable'), color="w", alpha=.5)
xy.set_xticklabels(xy.get_xticklabels(), rotation=45)
