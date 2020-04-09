# Analyses NC2U - EEG

Here you'll find all scripts related to the analyses run within the EEG part of the project
"Nothing compares to you - music genre perception similarities across modalities in humans & machines".

| processing step                        | script           | description  |
| ----------------------------- |:-------------:| :-----:|
| preprocessing | preprocessing_eeg.py | conducted preprocessing steps, including filtering, ICA and artifact detection  |
| Event related potentials (ERPs) | [erps.py]()  | computation of ERPs for each participant |
| Inter subject correlation (ISC) of channels | [isc_channels.py]() | computation of ISC across channels and selection of channel subset for subsequent analyses  |
| Representational Similarity analysis (RSA) across time points | [rsa_timepoints.py]() | computation of RDMs across timepoints for each participant  |
| RSA comparison between EEG timepoint and acoustic feature RDMs | [rsa_comparison_acousticfeatures.py]() | RSA comparison between EEG timepoint and acoustic feature RDMs |
| RSA comparison between EEG timepoint and behavior RDMs | [rsa_comparison_behavior.py]() | RSA comparison between EEG timepoint and behavior RDMs |
| RSA comparison between EEG timepoint and categorical RDMs | [rsa_comparison_categorical.py]() | RSA comparison between EEG timepoint and categorical RDMs |
