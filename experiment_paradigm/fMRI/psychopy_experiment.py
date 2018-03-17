#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01),
    on Mon 27 Nov 2017 12:01:23 PM CET
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'nothing_compares_to_you'
expInfo = {u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/home/.../psychopy_experiment.py', # path to experiment script
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1360, 768], fullscr=True, screen=0,
    allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='norm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Start"
StartClock = core.Clock()
welcome_scr = visual.TextStim(win=win, name='welcome_scr',
    text='Willkommen!',
    font='Arial',
    pos=[0, .7], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Letsgo"
StartClock = core.Clock()
letsgo_scr = visual.TextStim(win=win, name='letsgo_scr',
    text='Es geht gleich los...',
    font='Arial',
    pos=[0, .7], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);                              
                              
# Initialize components for Routine "calibration"
calibrationClock = core.Clock()
calib_instruct = visual.TextStim(win=win, name='calib_instruct',
    text=u'                  Lautst\xe4rke-Einstellung...\nDie Musik sollte so laut wie m\xf6glich sein, ohne jedoch unangenehm zu werden oder zu \xfcbersteuern.\n<< leiser      [Taste f\xfcr \xc4nderung]      lauter >>',
    font='Arial',
    pos=[0, 0.7], height=0.1, wrapWidth=1.8, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
calib_sound = sound.Sound('A', secs=-1) # place holder for sound, duration and volume
calib_sound.setVolume(0.5)

# Initialize components for Routine "run_start"
run_startClock = core.Clock()
run_start_msg_screen = visual.TextStim(win=win, name='run_start_msg_screen',
    text=u'             Ein neuer Durchgang! Es geht gleich weiter...',
    font='Arial',
    units='norm', pos=[0, 0.7], height=0.12, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "run_trigger_sync"
run_trigger_syncClock = core.Clock()
run_start_msg = visual.TextStim(win=win, name='run_start_msg',
    text='Die Messung startet gleich...',
    font='Arial',
    units='norm', pos=[0, 0.7], height=0.15, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
run_start_fixation = visual.TextStim(win=win, name='run_start_fixation',
    text='+',
    font='Arial',
    units='norm', pos=[0, 0.7], height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()

sample = sound.Sound('A', secs=-1)
sample.setVolume(1)
movie = visual.MovieStim3(
    win=win, name='movie',units='pix', 
    noAudio = True,
    filename='/home/.../movie001.mkv', # path to one movie as a placeholder
    ori=0, pos=(0, 0), opacity=1,
    depth=0.0,)

# I deleted the components for questions here

# Initialize components for Routine "run_break"
run_breakClock = core.Clock()
run_break_msg = visual.TextStim(win=win, name='run_break_msg',
    text='Kurze Pause ... geht gleich weiter',
    font='Arial',
    pos=[0, 0.7], height=0.15, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "end"
endClock = core.Clock()
end_scr = visual.TextStim(win=win, name='end_scr',
    text=u'Das war es schon! Vielen Dank f\xfcr die Teilnahme!',
    font='Arial',
    pos=[0, .7], height=0.13, wrapWidth=1.8, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Start"-------
t = 0
StartClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
exp_start = event.BuilderKeyResponse()
# keep track of which components have finished
StartComponents = [welcome_scr, exp_start]
for thisComponent in StartComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Start"-------
while continueRoutine:
    # get current time
    t = StartClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcome_scr* updates
    if t >= 0.0 and welcome_scr.status == NOT_STARTED:
        # keep track of start time/frame for later
        welcome_scr.tStart = t
        welcome_scr.frameNStart = frameN  # exact frame index
        welcome_scr.setAutoDraw(True)
    
    # *exp_start* updates
    if t >= 0.0 and exp_start.status == NOT_STARTED:
        # keep track of start time/frame for later
        exp_start.tStart = t
        exp_start.frameNStart = frameN  # exact frame index
        exp_start.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if exp_start.status == STARTED:
        theseKeys = event.getKeys(keyList=['6'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start"-------
for thisComponent in StartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Letsgo"-------
t = 0
StartClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
letsgo_start = event.BuilderKeyResponse()
# keep track of which components have finished
StartComponents = [letsgo_scr, letsgo_start]
for thisComponent in StartComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Letsgo"-------
while continueRoutine:
    # get current time
    t = StartClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *letsgo_scr* updates
    if t >= 0.0 and letsgo_scr.status == NOT_STARTED:
        # keep track of start time/frame for later
        letsgo_scr.tStart = t
        letsgo_scr.frameNStart = frameN  # exact frame index
        letsgo_scr.setAutoDraw(True)
    
    # *letsgo_start* updates
    if t >= 0.0 and letsgo_start.status == NOT_STARTED:
        # keep track of start time/frame for later
        letsgo_start.tStart = t
        letsgo_start.frameNStart = frameN  # exact frame index
        letsgo_start.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if letsgo_start.status == STARTED:
        theseKeys = event.getKeys(keyList=['t'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Letsgo"-------
for thisComponent in StartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
calibration_sounds = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('intro.csv'),
    seed=None, name='calibration_sounds')
thisExp.addLoop(calibration_sounds)  # add the loop to the experiment
thisCalibration_sound = calibration_sounds.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCalibration_sound.rgb)
if thisCalibration_sound != None:
    for paramName in thisCalibration_sound.keys():
        exec(paramName + '= thisCalibration_sound.' + paramName)

# variable to save results of volume calibration
total_vol = 0.5

for thisCalibration_sound in calibration_sounds:
    currentLoop = calibration_sounds
    # abbreviate parameter names if possible (e.g. rgb = thisCalibration_sound.rgb)
    if thisCalibration_sound != None:
        for paramName in thisCalibration_sound.keys():
            exec(paramName + '= thisCalibration_sound.' + paramName)
    
    # ------Prepare to start Routine "calibration"-------
    t = 0
    calibrationClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    calib_stop = event.BuilderKeyResponse()
    calib_sound.setSound("stimuli/" + sound_file, secs=-1)
    
    # keep track of which components have finished
    calibrationComponents = [calib_stop, calib_instruct, calib_sound]
    for thisComponent in calibrationComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    

    # -------Start Routine "calibration"-------
    while continueRoutine:
        # get current time
        t = calibrationClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if calib_sound.status == FINISHED:
            calib_stop.keys.append('6')
        
        # *calib_stop* updates
        if t >= 0.0 and calib_stop.status == NOT_STARTED:
            # keep track of start time/frame for later
            calib_stop.tStart = t
            calib_stop.frameNStart = frameN  # exact frame index
            calib_stop.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(calib_stop.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if calib_stop.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if "6" in theseKeys:  # 6 ends calibration stimulus and goes on to the next
                continueRoutine = False
            # change volume:
            if "7" in theseKeys: # 7 turns down volume
                calib_sound.stop()
                vol = calib_sound.getVolume()
                total_vol = vol - 0.1
                calib_sound.setVolume(vol - 0.1)
                calib_sound.play()
            if "8" in theseKeys: # 8 turns up volume
                calib_sound.stop()
                vol = calib_sound.getVolume()
                total_vol = vol + 0.1
                calib_sound.setVolume(vol + 0.1)
                calib_sound.play()
        
        # *calib_instruct* updates
        if t >= 0.0 and calib_instruct.status == NOT_STARTED:
            # keep track of start time/frame for later
            calib_instruct.tStart = t
            calib_instruct.frameNStart = frameN  # exact frame index
            calib_instruct.setAutoDraw(True)
        # start/stop calib_sound
        if t >= 0.5 and calib_sound.status == NOT_STARTED:
            # keep track of start time/frame for later
            calib_sound.tStart = t
            calib_sound.frameNStart = frameN  # exact frame index
            calib_sound.setVolume(total_vol) # individual volume after calibration
            calib_sound.play()  # start the sound (it finishes automatically)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in calibrationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "calibration"-------
    for thisComponent in calibrationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    calib_sound.stop()
    calib_sound.stop()  # ensure sound has stopped at end of routine
    # the Routine "calibration" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'calibration_sounds'

# get names of stimulus parameters
if calibration_sounds.trialList in ([], [None], None):
    params = []
else:
    params = calibration_sounds.trialList[0].keys()
# save data for this loop
calibration_sounds.saveAsText(filename + 'calibration_sounds.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
runs = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('runs.csv'),
    seed=None, name='runs')
thisExp.addLoop(runs)  # add the loop to the experiment
thisRun = runs.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRun.rgb)
if thisRun != None:
    for paramName in thisRun.keys():
        exec(paramName + '= thisRun.' + paramName)

for thisRun in runs:
    currentLoop = runs
    # abbreviate parameter names if possible (e.g. rgb = thisRun.rgb)
    if thisRun != None:
        for paramName in thisRun.keys():
            exec(paramName + '= thisRun.' + paramName)
    
    # ------Prepare to start Routine "run_start"-------
    t = 0
    run_startClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    run_start_trigger_key = event.BuilderKeyResponse()
    # keep track of which components have finished
    run_startComponents = [run_start_msg_screen, run_start_trigger_key]
    for thisComponent in run_startComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "run_start"-------
    while continueRoutine:
        # get current time
        t = run_startClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *run_start_msg_screen* updates
        if t >= 0.0 and run_start_msg_screen.status == NOT_STARTED:
            # keep track of start time/frame for later
            run_start_msg_screen.tStart = t
            run_start_msg_screen.frameNStart = frameN  # exact frame index
            run_start_msg_screen.setAutoDraw(True)
        
        # *run_start_trigger_key* updates
        if t >= 0.0 and run_start_trigger_key.status == NOT_STARTED:
            # keep track of start time/frame for later
            run_start_trigger_key.tStart = t
            run_start_trigger_key.frameNStart = frameN  # exact frame index
            run_start_trigger_key.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if run_start_trigger_key.status == STARTED:
            theseKeys = event.getKeys(keyList=['6'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in run_startComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "run_start"-------
    for thisComponent in run_startComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "run_start" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "run_trigger_sync"-------
    t = 0
    run_trigger_syncClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    run_trigger_sync_ = event.BuilderKeyResponse()
    
    # keep track of which components have finished
    run_trigger_syncComponents = [run_trigger_sync_, run_start_msg, run_start_fixation]
    for thisComponent in run_trigger_syncComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "run_trigger_sync"-------
    while continueRoutine:
        # get current time
        t = run_trigger_syncClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *run_trigger_sync_* updates
        if t >= 0.0 and run_trigger_sync_.status == NOT_STARTED:
            # keep track of start time/frame for later
            run_trigger_sync_.tStart = t
            run_trigger_sync_.frameNStart = frameN  # exact frame index
            run_trigger_sync_.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(run_trigger_sync_.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if run_trigger_sync_.status == STARTED:
            theseKeys = event.getKeys(keyList=['t'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                run_trigger_sync_.keys = theseKeys[-1]  # just the last key pressed
                run_trigger_sync_.rt = run_trigger_sync_.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *run_start_msg* updates
        if t >= 0.0 and run_start_msg.status == NOT_STARTED:
            # keep track of start time/frame for later
            run_start_msg.tStart = t
            run_start_msg.frameNStart = frameN  # exact frame index
            run_start_msg.setAutoDraw(True)
        frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if run_start_msg.status == STARTED and t >= frameRemains:
            run_start_msg.setAutoDraw(False)
        
        # *run_start_fixation* updates
        if t >= 5 and run_start_fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            run_start_fixation.tStart = t
            run_start_fixation.frameNStart = frameN  # exact frame index
            run_start_fixation.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in run_trigger_syncComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "run_trigger_sync"-------
    for thisComponent in run_trigger_syncComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if run_trigger_sync_.keys in ['', [], None]:  # No response was made
        run_trigger_sync_.keys=None
    runs.addData('run_trigger_sync_.keys',run_trigger_sync_.keys)
    if run_trigger_sync_.keys != None:  # we had a response
        runs.addData('run_trigger_sync_.rt', run_trigger_sync_.rt)
    run_start_timestamp = StartClock.getTime()
    # the Routine "run_trigger_sync" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions("run%i.csv" % run_id),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    # start movie for whole run (loop over trials)
    movie.setMovie("visual_stimuli/"+movie_stim)
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial.keys():
                exec(paramName + '= thisTrial.' + paramName)
        
        # ------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        trial_start_timestamp = StartClock.getTime() - run_start_timestamp
        sample.setSound("stimuli/"+stim, secs=6.1)
        trigger_sync = event.BuilderKeyResponse()
        # keep track of which components have finished
        trialComponents = [movie, sample, trigger_sync]
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            
            # start/stop sample
            if t >= 0.0 and sample.status == NOT_STARTED:
                # keep track of start time/frame for later
                sample.tStart = t
                sample.frameNStart = frameN  # exact frame index
                sample.setVolume(total_vol) # individual volume
                sample.play()  # start the sound (it finishes automatically)
            frameRemains = 0.0 + 6.1- win.monitorFramePeriod * 0.75  # most of one frame period left
            if sample.status == STARTED and t >= frameRemains:
                sample.stop()  # stop the sound (if longer than duration)
            
            # *trigger_sync* updates
            if (t > (6 + delay -1)) and trigger_sync.status == NOT_STARTED:
                # keep track of start time/frame for later
                trigger_sync.tStart = t
                trigger_sync.frameNStart = frameN  # exact frame index
                trigger_sync.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(trigger_sync.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if trigger_sync.status == STARTED:
                theseKeys = event.getKeys(keyList=['t'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    trigger_sync.keys = theseKeys[-1]  # just the last key pressed
                    trigger_sync.rt = trigger_sync.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # *movie* updates
            if t >= 0.0 and movie.status == NOT_STARTED:
                # keep track of start time/frame for later
                movie.tStart = t
                movie.frameNStart = frameN  # exact frame index
                movie.setAutoDraw(True)
            frameRemains = 0.0 + 480.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if movie.status == STARTED and t >= frameRemains:
                movie.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('trial_start_run_time', trial_start_timestamp)
        sample.stop()  # ensure sound has stopped at end of routine
        # check responses
        if trigger_sync.keys in ['', [], None]:  # No response was made
            trigger_sync.keys=None
        trials.addData('trigger_sync.keys',trigger_sync.keys)
        if trigger_sync.keys != None:  # we had a response
            trials.addData('trigger_sync.rt', trigger_sync.rt)
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials'
    
    # get names of stimulus parameters
    if trials.trialList in ([], [None], None):
        params = []
    else:
        params = trials.trialList[0].keys()
    # save data for this loop
    trials.saveAsText(filename + 'trials.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "run_break"-------
    t = 0
    run_breakClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    exp_break = event.BuilderKeyResponse()
    run_breakComponents = [run_break_msg, exp_break]
    for thisComponent in run_breakComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "run_break"-------
    while continueRoutine:
        # get current time
        t = run_breakClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *run_break_msg* updates
        if t >= 0.0 and run_break_msg.status == NOT_STARTED:
            # keep track of start time/frame for later
            run_break_msg.tStart = t
            run_break_msg.frameNStart = frameN  # exact frame index
            run_break_msg.setAutoDraw(True)
        
        # *exp_break* updates
        if t >= 0.0 and exp_break.status == NOT_STARTED:
            # keep track of start time/frame for later
           exp_break.tStart = t
           exp_break.frameNStart = frameN  # exact frame index
           exp_break.status = STARTED
           # keyboard checking is just starting
           event.clearEvents(eventType='keyboard')
        if exp_break.status == STARTED:
            theseKeys = event.getKeys(keyList=['6'])
        
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in run_breakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "run_break"-------
    for thisComponent in run_breakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'runs'

# get names of stimulus parameters
if runs.trialList in ([], [None], None):
    params = []
else:
    params = runs.trialList[0].keys()
# save data for this loop
runs.saveAsText(filename + 'runs.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
end_keys = event.BuilderKeyResponse()
# keep track of which components have finished
endComponents = [end_scr, end_keys]
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_scr* updates
    if t >= 0.0 and end_scr.status == NOT_STARTED:
        # keep track of start time/frame for later
        end_scr.tStart = t
        end_scr.frameNStart = frameN  # exact frame index
        end_scr.setAutoDraw(True)
    
    # *end_keys* updates
    if t >= 0.0 and end_keys.status == NOT_STARTED:
        # keep track of start time/frame for later
        end_keys.tStart = t
        end_keys.frameNStart = frameN  # exact frame index
        end_keys.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if end_keys.status == STARTED:
        theseKeys = event.getKeys(keyList=['6'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
