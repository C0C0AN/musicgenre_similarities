#!/bin/bash

# NC2U_mindboggle.sh
# Run complete mindboggle pipeline including FreeSurfer, ANTs and mindboggle itself on a BIDS dataset.
# This script should be run from within the mindboggle docker image (http://mindboggle.readthedocs.io/en/latest/#installation).

# Start the docker container as described here: http://mindboggle.readthedocs.io/en/latest/#run-separate-commands and mount
# the paths as follows.
# HOST=path/to/BIDS/dataset
# DOCK=/home/jovyan/work

FREESURFER_OUT=/home/jovyan/work/derivatives/mindboggle/freesurfer_subjects # set FreeSurfer output directory 
ANTS_OUT=/home/jovyan/work/derivatives/mindboggle/ants_subjects # set ANTs output directory
TEMPLATE=/opt/data/OASIS-30_Atropos_template # set template to use within mindboggle

# list of participants to analyse
declare -a participants=()

# loop over all participants included in the list
for part in "${participants[@]}"
do

	T1_id=_T1w.nii.gz # set T1w image identifier
	T2_id=_T2w.nii.gz # set T2w image identifier
	IMAGE=/home/jovyan/work/$part/anat/$part$T1_id # set path to T1w image
	IMAGE_T2=/home/jovyan/work/$part/anat/$part$T2_id # set path to T2w image
	ID=$part # set ID

	# run recon-all 
	recon-all -all -i $IMAGE -s $ID -sd $FREESURFER_OUT -T2 $IMAGE_T2 -nuintensitycor-3T 

	# run antsCorticalThickness 
	antsCorticalThickness.sh -d 3 -a $IMAGE -o $ANTS_OUT/$ID/ants \
  		-e $TEMPLATE/T_template0.nii.gz \
  		-t $TEMPLATE/T_template0_BrainCerebellum.nii.gz \
  		-m $TEMPLATE/T_template0_BrainCerebellumProbabilityMask.nii.gz \
  		-f $TEMPLATE/T_template0_BrainCerebellumExtractionMask.nii.gz \
  		-p $TEMPLATE/Priors2/priors%d.nii.gz

  	# set FreeSurfer/ANTs subject and output directory for mindboggle
	FREESURFER_SUBJECT=$FREESURFER_OUT/$ID
	ANTS_SUBJECT=$ANTS_OUT/$ID
	OUT=/home/jovyan/work/mindboggled

	# run mindboggle
	mindboggle $FREESURFER_SUBJECT --out $OUT --ants $ANTS_SUBJECT/antsBrainSegmentation.nii.gz --roygbiv


done
