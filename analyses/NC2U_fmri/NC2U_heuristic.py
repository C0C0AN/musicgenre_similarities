import os

def create_key(template, outtype=('nii.gz',), annotation_classes=None):
    if template is None or not template:
        raise ValueError('Template must be a valid format string')
    return template, outtype, annotation_classes

def infotodict(seqinfo):
    t1w = create_key('sub-{subject}/anat/sub-{subject}_T1w')
    t2w = create_key('sub-{subject}/anat/sub-{subject}_T2w')
    func = create_key('sub-{subject}/func/sub-{subject}_task-NC2U_run-{item:01d}_bold')
    func_wh = create_key('sub-{subject}/func/sub-{subject}_task-NC2UWH_bold')

    info = {t1w: [], t2w: [], func: [], func_wh: []}

    for s in seqinfo:
        if (s.dim3 == 176) and (s.dim4 == 1) and ('t1' in s.protocol_name):
          info[t1w] = [s.series_id] # assign if a single series meets criteria
        if (s.dim2 == 512) and (s.dim4 == 1) and ('t2' in s.protocol_name):
          info[t2w].append(s.series_id) # append if multiple series meet criteria
        if (s.dim4 > 6) and ('TR1500' in s.protocol_name):
          info[func].append({'item': s.series_id})
        if (s.dim4 < 6) and ('TR4000' in s.protocol_name):
          info[func_wh].append({'item': s.series_id})



    return info
