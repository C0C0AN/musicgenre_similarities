#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 14:02:31 2017

@author: mirjam
"""

import random
import copy

# stimuli
stimuli = ['punk', 'alternative', 'heavymetal', 'psychedelic', 'rocknroll',
           'funk', 'hiphop', 'reggae', 'rnb', 'soul',
           'baroque', 'classic', 'modernclassic', 'renaissance', 'romantic',
           'deephouse', 'drumandbass', 'dubstep', 'techno', 'trance']

# sequences (first level counterbalanced in OptSeq2, best 8 of 100.000)
sequences = [[1,  1,  3,  11,  5,  2,  16,  4,  6,  13,  11,  2,  17,  20,  9,  13,  18,  12,  14,  18,  3,  5,  19,  15,  20,  15,  19,  6,  14,  4,  17,  10,  16,  7,  9,  12,  7,  8,  10,  8],
             [5,  9,  3,  14,  2,  9,  20,  7,  10,  5,  10,  1,  1,  7,  15,  2,  16,  17,  11,  6,  8,  12,  11,  4,  12,  18,  17,  3,  18,  13,  4,  13,  6,  15,  8,  19,  16,  20,  19,  14],
             [17,  13,  1,  3,  5,  14,  10,  17,  14,  18,  4,  10,  4,  2,  7,  5,  15,  6,  9,  12,  1,  19,  12,  11,  16,  19,  3,  2,  20,  8,  11,  18,  15,  13,  9,  20,  16,  6,  8,  7],
             [13,  5,  16,  1,  9,  5,  10,  17,  10,  18,  19,  15,  6,  2,  9,  11,  18,  14,  20,  2,  12,  1,  6,  7,  4,  3,  13,  19,  20,  14,  11,  8,  4,  7,  17,  8,  16,  3,  12,  15],
             [18,  12,  10,  6,  12,  14,  9,  8,  18,  20,  13,  2,  15,  6,  15,  2,  7,  11,  4,  3,  3,  5,  8,  7,  20,  17,  10,  16,  4,  5,  13,  1,  17,  14,  9,  11,  19,  1,  16,  19],
             [2,  6,  14,  18,  10,  5,  17,  8,  3,  16,  18,  13,  8,  13,  12,  2,  4,  12,  20,  15,  1,  10,  14,  9,  19,  5,  16,  19,  11,  11,  20,  6,  17,  4,  7,  1,  3,  15,  7,  9],
             [6,  4,  5,  17,  3,  5,  11,  10,  7,  18,  19,  12,  8,  4,  14,  16,  11,  1,  15,  9,  2,  15,  7,  2,  8,  3,  9,  16,  17,  10,  20,  19,  1,  13,  13,  20,  14,  12,  18,  6],
             [8,  9,  3,  8,  4,  11,  4,  15,  19,  1,  12,  6,  7,  10,  13,  12,  6,  20,  1,  9,  14,  2,  5,  16,  17,  2,  18,  18,  15,  14,  20,  17,  10,  11,  5,  7,  19,  3,  13,  16]
             ]

# delays between stimuli (every delay equally often per run (13x))
delay_sequence = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 
                   6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 
                   8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]

# function creates 8 different runs
def gen_run(nmbr):
    # to number runfiles
    counter = 0 
    for j in sequences:
        # shuffle stimuli
        xy = copy.deepcopy(stimuli)
        random.shuffle(xy)
        # shuffle delay_sequence
        ab = copy.deepcopy(delay_sequence)
        random.shuffle(ab)
        # to make ab the same length as xy, we add a delay of 0 for the last stimulus
        # 0 has to be in the first position of the list because we later use pop to allocate the delays to the stimuli
        ab.insert(0, 0)
        # create output-file
        ofile = open('run%i.csv' % counter, 'w')
        ofile.write('run,stim,delay\n')
        # get inside the different sequences
        for i in j:
            genre = i
            # genre_stim is the stimuli at a certain position in the randomised stimuli-list xy
            genre_stim = xy[int(genre)-1]
            # allocate delay
            delay = ab.pop()
            ofile.write('%s,"%s.wav","%s"\n'
                    % (counter, genre_stim, delay)) # randomise delay_steps
        ofile.close()
        counter = counter + 1
        
gen_run(1)