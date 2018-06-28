# analysis_questionnaire.py
# function to read out information, create and save data frames to .csv
# files from results .json files from the music
# genre stimuli questionnaire

def analysis_questionnaire(json_file):
    '''inputs should be a participant specific questionnaire file (in .json)
        e.g. analysis_questionnaire(test_participant.json)'''

    # import important modules
    import os
    import json
    import pandas as pd

    # open and load .json file, creating a dict
    q_json=json.load(open(json_file))

    # assign id
    id=str(json_file.split('ergebnisstring_', 1)[1].split('.json',1)[0])

    # open an error log file to store all missing values, etc. 
    f = open("error_log" + id + ".txt", "w")

    # create pandas data frame to store converted information
    q_data = pd.DataFrame(columns=['age', 'sex', 'handedness', 'education', 'job', 'hearing', 'hearing_dis',
                                 'neuro_psych', 'music_pref_all', 'music_pref', 'band_pref', 'dur_music_day', \
                                 'purpose_music', 'occasion_music', 'active_music_cur', 'active_music_cur_dur', \
                                 'active_music_past', 'active_music_past_dur', 'importance_music', 'chills_often', 'chills_int', \
                                 'punk_sortable', 'punk_sortable_sure', 'punk_know', \
                                 'alternative_sortable', 'alternative_sortable_sure', 'alternative_know', \
                                 'heavymetal_sortable', 'heavymetal_sortable_sure', 'heavymetal_know', \
                                 'psychedelic_sortable', 'psychedelic_sortable_sure', 'psychedelic_know', \
                                 'rocknroll_sortable', 'rocknroll_sortable_sure', 'rocknroll_know', 'rock_all', \
                                 'funk_sortable', 'funk_sortable_sure', 'funk_know', \
                                 'hiphop_sortable', 'hiphop_sortable_sure', 'hiphop_know', \
                                 'reggae_sortable', 'reggae_sortable_sure', 'reggae_know', \
                                 'rnb_sortable', 'rnb_sortable_sure', 'rnb_know', \
                                 'soul_sortable', 'soul_sortable_sure', 'soul_know', 'african_american_all', \
                                 'baroque_sortable', 'baroque_sortable_sure', 'baroque_know', \
                                 'viennese_classic_sortable', 'viennese_classic_sortable_sure', 'viennese_classic_know', \
                                 'modern_classic_sortable', 'modern_classic_sortable_sure', 'modern_classic_know', \
                                 'renaissance_sortable', 'renaissance_sortable_sure', 'renaissance_know', \
                                 'romantic_sortable', 'romantic_sortable_sure', 'romantic_know', 'classic_all', \
                                 'deephouse_sortable', 'deephouse_sortable_sure', 'deephouse_know', \
                                 'drumnbass_sortable', 'drumnbass_sortable_sure', 'drumnbass_know', \
                                 'dubstep_sortable', 'dubstep_sortable_sure', 'dubstep_know', \
                                 'techno_sortable', 'techno_sortable_sure', 'techno_know', \
                                 'trance_sortable', 'trance_sortable_sure', 'trance_know', 'electro_all'], index=[list(range(0,10))])

    ## read out demographic information
    # id has to be added manually to the result file when data is copied from online results
    if 'id' in q_json:
        q_data['id'][0] = int(q_json['id'])

    if 'Alter' in q_json:
        q_data['age'][0] = str(q_json['Alter'])
    else:
        f.write('missing_value_age\n')

    if 'Geschlecht' in q_json:
        q_data['sex'][0] = str(q_json['Geschlecht'])
    else:
        f.write('missing_value_sex\n')

    if 'Haendigkeit' in q_json:
        q_data['handedness'][0] = str(q_json['Haendigkeit'])
    else:
        f.write('missing_value_handedness\n')

    if 'Hoechster Bildungsabschluss' in q_json:
        q_data['education'][0] = str(q_json['Hoechster Bildungsabschluss'])
    else:
        f.write('education\n')

    if 'Beruf (wenn Student: Studienfach)' in q_json:
        q_data['job'][0] = str(q_json['Beruf (wenn Student: Studienfach)'])
    else:
        f.write('missing_value_job\n')

    if 'Wie wuerden Sie Ihre Hoerfaehigkeit einschaetzen?' in q_json:
        q_data['hearing'][0] = str(q_json['Wie wuerden Sie Ihre Hoerfaehigkeit einschaetzen?'])
    else:
        f.write('missing_value_hearing\n')

    if 'Hatten Sie schon mal oder haben Sie...' in q_json:
        q_data['hearing_dis'][0] = str(q_json['Hatten Sie schon mal oder haben Sie...'])
    else:
        f.write('missing_value_hearing_dis\n')

    if 'Hatten oder haben Sie eine neurologische oder psychiatrische Erkrankung?' in q_json:
        q_data['neuro_psych'][0] = str(q_json['Hatten oder haben Sie eine neurologische oder psychiatrische Erkrankung?'])
    else:
        f.write('missing_value_neuro_psych\n')

    if 'Bitte geben Sie Ihre generelle Praeferenz fuer jedes der folgenden Musikgenres anhand der bereitgestellten Skala an.' in q_json:
        q_data_music_pref_all = q_json['Bitte geben Sie Ihre generelle Praeferenz fuer jedes der folgenden Musikgenres anhand der bereitgestellten Skala an.']
        if len(q_data_music_pref_all)==23:
            for i in range(1,len(q_data_music_pref_all)+1):
                q_data['music_pref_all'][i-1]=int(q_data_music_pref_all[str(i)])
        else:
            f.write('music pref all not complete\n')
    else:
        f.write('music pref all missing\n')

    if 'Welche von den angegebenen Musikstilen bevorzugen Sie?' in q_json:
        q_data_music_pref = q_json['Welche von den angegebenen Musikstilen bevorzugen Sie?']
        if len(q_data_music_pref)==11:
            for i in range(1,len(q_data_music_pref)):
                q_data['music_pref'][i-1]=int(q_data_music_pref[str(i)])
        else:
            f.write('music_pref_not_complete\n')
    else:
        f.write('music_pref_missing\n')


    if 'Welches ist Ihre Lieblingsband/Musikgruppe und welchem Musikstil ist diese zuzuordnen (max. 3)?' in q_json:
        q_data['band_pref'][0] = str(q_json['Welches ist Ihre Lieblingsband/Musikgruppe und welchem Musikstil ist diese zuzuordnen (max. 3)?'])
    else:
        f.write('missing_value_band_pref\n')

    if 'Wie lange hoeren Sie an einem typischen Tag Musik?' in q_json:
        q_data['dur_music_day'][0] = str(q_json['Wie lange hoeren Sie an einem typischen Tag Musik?'])
    else:
        f.write('missing_value_dur_music_day\n')

    if 'Zu welchem Zweck hoeren Sie Musik?' in q_json:
        q_data_purpose_music = q_json['Zu welchem Zweck hoeren Sie Musik?']
        if len(q_data_purpose_music)==10:
            for i in range(1,len(q_data_purpose_music)):
                q_data['purpose_music'][i-1]=int(q_data_purpose_music[str(i)])
        else:
            f.write('purpose_music_not_complete\n')
    else:
        f.write('purpose_music_missing\n')

    if 'Zu welchen Anlaessen bzw. in welchen Situationen hoeren Sie Musik?' in q_json:
        q_data_occasion_music = q_json['Zu welchen Anlaessen bzw. in welchen Situationen hoeren Sie Musik?']
        if len(q_data_occasion_music)==8:
            for i in range(1,len(q_data_occasion_music)):
                q_data['occasion_music'][i-1]=int(q_data_occasion_music[str(i)])
        else:
            f.write('occasion_music_not_complete\n')
    else:
        f.write('occasion_purpose_music_missing\n')

    if 'Machen Sie im Moment aktiv Musik?' in q_json:
        q_data['active_music_cur'][0] = str(q_json['Machen Sie im Moment aktiv Musik?'])
    else:
        f.write('missing_value_neuro_active_music_cur\n')

    if 'Wenn Sie ein Instrument spielen, welches ist es und wie lange spielen Sie schon? Wenn Sie in einem Chor oder einer Band singen, wie lange schon?' in q_json:
        q_data['active_music_cur_dur'][0] = str(q_json['Wenn Sie ein Instrument spielen, welches ist es und wie lange spielen Sie schon? Wenn Sie in einem Chor oder einer Band singen, wie lange schon?'])
    else:
        f.write('missing_value_active_music_cur_dur\n')

    if 'Haben Sie frueher aktiv Musik gemacht?' in q_json:
        q_data['active_music_past'][0] = str(q_json['Haben Sie frueher aktiv Musik gemacht?'])
    else:
        f.write('missing_value_active_music_past\n')

    if 'Wenn Sie ein Instrument spielten, welches war es und wie lange spielten Sie es? Wenn Sie in einem Chor oder einer Band sangen, wie lange?' in q_json:
        q_data['active_music_past_dur'][0] = str(q_json['Wenn Sie ein Instrument spielten, welches war es und wie lange spielten Sie es? Wenn Sie in einem Chor oder einer Band sangen, wie lange?'])
    else:
        f.write('missing_value_active_music_dur\n')

    if 'Wie wichtig ist Musik in Ihrem Leben?' in q_json:
        q_data['importance_music'][0] = int(q_json['Wie wichtig ist Musik in Ihrem Leben?'])
    else:
        f.write('missing_value_importance_music\n')

    if 'Mit der naechsten Frage moechten wir gerne herausfinden, wie oft und wie stark Sie sogenannte Chills erleben. Chills sind koerperliche Reaktionen, ein Schaudern oder Froesteln, das sich vom Kopf her ueber den Ruecken und/oder andere Teile des Koerpers ausbreitet. Es gibt diese Reaktionen in Zusammenhang mit vielen Erlebnissen wie z.B. bei Angst, Erschrecken oder beim Betrachten von Kunst. Wir moechten Sie aber bitten, dass Sie sich auf Chills beschraenken, welche Sie ausschliesslich beim Musikhoeren erleben.' in q_json:
        q_data_chills_often = q_json['Mit der naechsten Frage moechten wir gerne herausfinden, wie oft und wie stark Sie sogenannte Chills erleben. Chills sind koerperliche Reaktionen, ein Schaudern oder Froesteln, das sich vom Kopf her ueber den Ruecken und/oder andere Teile des Koerpers ausbreitet. Es gibt diese Reaktionen in Zusammenhang mit vielen Erlebnissen wie z.B. bei Angst, Erschrecken oder beim Betrachten von Kunst. Wir moechten Sie aber bitten, dass Sie sich auf Chills beschraenken, welche Sie ausschliesslich beim Musikhoeren erleben.']
        if len(q_data_chills_often)==1:
           q_data['chills_often'][0]=q_data_chills_often['1']
        else:
            f.write('missing_value_chills_often\n')
    else:
        f.write('missing_value_chills_often\n')

    if 'Falls Sie Chills erleben, geben Sie bitte an, wie intensiv Ihre erlebten Chills sind' in q_json:
        q_data['chills_int'][0] = int(q_json['Falls Sie Chills erleben, geben Sie bitte an, wie intensiv Ihre erlebten Chills sind'])
    else:
        f.write('missing_value_chills_int\n')


    ### read out sortables

    ## read out sortables rock

    # read out sortables rock - punk
    q_data_punk_sortable = q_json['punk_sortable']
    if len(q_data_punk_sortable)==10:
        for i in range(0, len(q_json['punk_sortable'])):
            q_data['punk_sortable'][i] = str(q_json['punk_sortable'][i])
    else:
        f.write('missing_value_punk_sortable')

    if 'Wie sicher sind Sie sich bei dieser Zuordnung (Punk)?' in q_json:
        q_data['punk_sortable_sure'][0] = int(q_json['Wie sicher sind Sie sich bei dieser Zuordnung (Punk)?'])
    else:
        f.write('missing_value_punk_sortable_sure\n')

    if 'Wie gut kennen Sie sich im Genre Punk aus?' in q_json:
        q_data['punk_know'][0] = int(q_json['Wie gut kennen Sie sich im Genre Punk aus?'])
    else:
        f.write('missing_value_punk_know\n')

    # read out sortables rock - alternative
    q_data_alternative_sortable = q_json['alternative_sortable']
    if len(q_data_alternative_sortable)==10:
        for i in range(0, len(q_json['alternative_sortable'])):
            q_data['alternative_sortable'][i] = str(q_json['alternative_sortable'][i])
    else:
        f.write('missing_value_alternative_sortable')

    if 'Wie sicher sind Sie sich bei dieser Zuordnung (Alternative)?' in q_json:
        q_data['alternative_sortable_sure'][0] = int(q_json['Wie sicher sind Sie sich bei dieser Zuordnung (Alternative)?'])
    else:
        f.write('missing_value_alternative_sortable_sure\n')

    if 'Wie gut kennen Sie sich im Genre Alternative aus?' in q_json:
        q_data['alternative_know'][0] = int(q_json['Wie gut kennen Sie sich im Genre Alternative aus?'])
    else:
        f.write('missing_value_alternativ_know\n')

    # read out sortables rock - heavymetal
    q_data_heavymetal_sortable = q_json['heavymetal_sortable']
    if len(q_data_heavymetal_sortable)==10:
        for i in range(0, len(q_json['heavymetal_sortable'])):
            q_data['heavymetal_sortable'][i] = str(q_json['heavymetal_sortable'][i])
    else:
        f.write('missing_value_heavymetal_sortable')

    if 'Wie sicher sind Sie sich bei dieser Zuordnung (Heavy Metal)?' in q_json:
        q_data['heavymetal_sortable_sure'][0] = int(q_json['Wie sicher sind Sie sich bei dieser Zuordnung (Heavy Metal)?'])
    else:
        f.write('missing_value_heavymetal_sortable_sure\n')

    if 'Wie gut kennen Sie sich im Genre Heavy Metal aus?' in q_json:
        q_data['heavymetal_know'][0] = int(q_json['Wie gut kennen Sie sich im Genre Heavy Metal aus?'])
    else:
        f.write('missing_value_heavymetal_know\n')

    # read out sortables rock - psychedelic
    q_data_psychedelic_sortable = q_json['psychedelic_sortable']
    if len(q_data_psychedelic_sortable)==10:
        for i in range(0, len(q_json['psychedelic_sortable'])):
            q_data['psychedelic_sortable'][i] = str(q_json['psychedelic_sortable'][i])
    else:
        f.write('missing_value_psychedelic_sortable')

    if 'Wie sicher sind Sie sich bei dieser Zuordnung (Psychedelic)?' in q_json:
        q_data['psychedelic_sortable_sure'][0] = int(q_json['Wie sicher sind Sie sich bei dieser Zuordnung (Psychedelic)?'])
    else:
        f.write('missing_value_psychedelic_sortable_sure\n')

    if 'Wie gut kennen Sie sich im Genre Psychedelic aus?' in q_json:
        q_data['psychedelic_know'][0] = int(q_json['Wie gut kennen Sie sich im Genre Psychedelic aus?'])
    else:
        f.write('missing_value_psychedelic_know\n')

    # read out sortables rock - rocknroll
    q_data_rocknroll_sortable = q_json['rocknroll_sortable']
    if len(q_data_rocknroll_sortable)==10:
        for i in range(0, len(q_json['rocknroll_sortable'])):
            q_data['rocknroll_sortable'][i] = str(q_json['rocknroll_sortable'][i])
    else:
        f.write('missing_value_rocknroll_sortable')

    if 'Wie sicher sind Sie sich bei dieser Zuordnung (RocknRoll)?' in q_json:
        q_data['rocknroll_sortable_sure'][0] = int(q_json['Wie sicher sind Sie sich bei dieser Zuordnung (RocknRoll)?'])
    else:
        f.write('missing_value_rocknroll_sortable_sure\n')

    if 'Wie gut kennen Sie sich im Genre RocknRoll aus?' in q_json:
        q_data['rocknroll_know'][0] = int(q_json['Wie gut kennen Sie sich im Genre RocknRoll aus?'])
    else:
        f.write('missing_value_rocknroll_know\n')

    # read out sortables rock - all
    if 'rock' in q_json:
        q_data_rock_all = q_json['rock']
        if len(q_data_rock_all)==5:
            for i in range(0, len(q_json['rock'])):
                q_data['rock_all'][i] = str(q_json['rock'][i])
        else:
            f.write('rock_all_not_complete\n')
    else:
        f.write('rock_all_missing\n')

    ## read out sortables african-american

    # read out sortables african-american - funk
    q_data_funk_sortable = q_json['funk_sortable']
    if len(q_data_funk_sortable)==10:
        for i in range(0, len(q_json['funk_sortable'])):
            q_data['funk_sortable'][i] = str(q_json['funk_sortable'][i])
    else:
        f.write('missing_value_funk_sortable')

    if 'Wie sicher sind Sie sich bei dieser Zuordnung (Funk)?' in q_json:
        q_data['funk_sortable_sure'][0] = int(q_json['Wie sicher sind Sie sich bei dieser Zuordnung (Funk)?'])
    else:
        f.write('missing_value_funk_sortable_sure\n')

    if 'Wie gut kennen Sie sich im Genre Funk aus?' in q_json:
        q_data['funk_know'][0] = int(q_json['Wie gut kennen Sie sich im Genre Funk aus?'])
    else:
        f.write('missing_value_funk_know\n')

    # read out sortables african-american - hiphop
    q_data_hiphop_sortable = q_json['hiphop_sortable']
    if len(q_data_hiphop_sortable)==10:
        for i in range(0, len(q_json['hiphop_sortable'])):
            q_data['hiphop_sortable'][i] = str(q_json['hiphop_sortable'][i])
    else:
        f.write('missing_value_hiphop_sortable')

    if 'Wie sicher sind Sie sich bei dieser Zuordnung (Hiphop)?' in q_json:
        q_data['hiphop_sortable_sure'][0] = int(q_json['Wie sicher sind Sie sich bei dieser Zuordnung (Hiphop)?'])
    else:
        f.write('missing_value_hiphop_sortable_sure\n')

    if 'Wie gut kennen Sie sich im Genre Hiphop aus?' in q_json:
        q_data['hiphop_know'][0] = int(q_json['Wie gut kennen Sie sich im Genre Hiphop aus?'])
    else:
        f.write('missing_value_hiphop_know\n')

    # read out sortables african-american - reggae
    q_data_reggae_sortable = q_json['reggae_sortable']
    if len(q_data_reggae_sortable)==10:
        for i in range(0, len(q_json['reggae_sortable'])):
            q_data['reggae_sortable'][i] = str(q_json['reggae_sortable'][i])
    else:
        f.write('missing_value_reggae_sortable')

    if 'Wie sicher sind Sie sich bei dieser Zuordnung (Reggae)?' in q_json:
        q_data['reggae_sortable_sure'][0] = int(q_json['Wie sicher sind Sie sich bei dieser Zuordnung (Reggae)?'])
    else:
        f.write('missing_value_reggae_sortable_sure\n')

    if 'Wie gut kennen Sie sich im Genre Reggae aus?' in q_json:
        q_data['reggae_know'][0] = int(q_json['Wie gut kennen Sie sich im Genre Reggae aus?'])
    else:
        f.write('missing_value_reggae_know\n')

    # read out sortables african-american - rnb
    q_data_rnb_sortable = q_json['rnb_sortable']
    if len(q_data_rnb_sortable)==10:
        for i in range(0, len(q_json['rnb_sortable'])):
            q_data['rnb_sortable'][i] = str(q_json['rnb_sortable'][i])
    else:
        f.write('missing_value_rnb_sortable')

    if 'Wie sicher sind Sie sich bei dieser Zuordnung (RnB)?' in q_json:
        q_data['rnb_sortable_sure'][0] = int(q_json['Wie sicher sind Sie sich bei dieser Zuordnung (RnB)?'])
    else:
        f.write('missing_value_rnb_sortable_sure\n')

    if 'Wie gut kennen Sie sich im Genre RnB aus?' in q_json:
        q_data['rnb_know'][0] = int(q_json['Wie gut kennen Sie sich im Genre RnB aus?'])
    else:
        f.write('missing_value_rnb_know\n')

    # read out sortables african-american - soul
    q_data_soul_sortable = q_json['soul_sortable']
    if len(q_data_soul_sortable)==10:
        for i in range(0, len(q_json['soul_sortable'])):
            q_data['soul_sortable'][i] = str(q_json['soul_sortable'][i])
    else:
        f.write('missing_value_soul_sortable')

    if 'Wie sicher sind Sie sich bei dieser Zuordnung (Soul)?' in q_json:
        q_data['soul_sortable_sure'][0] = int(q_json['Wie sicher sind Sie sich bei dieser Zuordnung (Soul)?'])
    else:
        f.write('missing_value_soul_sortable_sure\n')

    if 'Wie gut kennen Sie sich im Genre Soul aus?' in q_json:
        q_data['soul_know'][0] = int(q_json['Wie gut kennen Sie sich im Genre Soul aus?'])
    else:
        f.write('missing_value_soul_know\n')

    # read out sortables african-american - all
    if 'african_american' in q_json:
        q_data_african_american_all = q_json['african_american']
        if len(q_data_african_american_all)==5:
            for i in range(0, len(q_json['african_american'])):
                q_data['african_american_all'][i] = str(q_json['african_american'][i])
        else:
            f.write('african_american_all_not_complete\n')
    else:
        f.write('african_american_all_missing\n')


    ## read out sortables classic

    # read out sortables classic - baroque
    q_data_baroque_sortable = q_json['baroque_sortable']
    if len(q_data_baroque_sortable)==10:
        for i in range(0, len(q_json['baroque_sortable'])):
            q_data['baroque_sortable'][i] = str(q_json['baroque_sortable'][i])
    else:
        f.write('missing_value_baroque_sortable')

    if 'Wie sicher sind Sie sich bei dieser Zuordnung (Barock)?' in q_json:
        q_data['baroque_sortable_sure'][0] = int(q_json['Wie sicher sind Sie sich bei dieser Zuordnung (Barock)?'])
    else:
        f.write('missing_value_baroque_sortable_sure\n')

    if 'Wie gut kennen Sie sich im Genre Barock aus?' in q_json:
        q_data['baroque_know'][0] = int(q_json['Wie gut kennen Sie sich im Genre Barock aus?'])
    else:
        f.write('missing_value_baroque_know\n')

    # read out sortables classic - viennese_classic
    q_data_viennese_classic_sortable = q_json['viennese_classic_sortable']
    if len(q_data_viennese_classic_sortable)==10:
        for i in range(0, len(q_json['viennese_classic_sortable'])):
            q_data['viennese_classic_sortable'][i] = str(q_json['viennese_classic_sortable'][i])
    else:
        f.write('missing_value_viennese_classic_sortable')

    if 'Wie sicher sind Sie sich bei dieser Zuordnung (Wiener Klassik)?' in q_json:
        q_data['viennese_classic_sortable_sure'][0] = int(q_json['Wie sicher sind Sie sich bei dieser Zuordnung (Wiener Klassik)?'])
    else:
        f.write('missing_value_viennese_classic_sortable_sure\n')

    if 'Wie gut kennen Sie sich im Genre Wiener Klassik aus?' in q_json:
        q_data['viennese_classic_know'][0] = int(q_json['Wie gut kennen Sie sich im Genre Wiener Klassik aus?'])
    else:
        f.write('missing_value_viennese_classic_know\n')

    # read out sortables classic - modernclassic
    q_data_modern_classic_sortable = q_json['modernclassic_sortable']
    if len(q_data_modern_classic_sortable)==10:
        for i in range(0, len(q_json['modernclassic_sortable'])):
            q_data['modern_classic_sortable'][i] = str(q_json['modernclassic_sortable'][i])
    else:
        f.write('missing_value_modern_classic_sortable')

    if 'Wie sicher sind Sie sich bei dieser Zuordnung (Moderne Klassik)?' in q_json:
        q_data['modern_classic_sortable_sure'][0] = int(q_json['Wie sicher sind Sie sich bei dieser Zuordnung (Moderne Klassik)?'])
    else:
        f.write('missing_value_modern_classic_sortable_sure\n')

    if 'Wie gut kennen Sie sich im Genre Moderne Klassik aus?' in q_json:
        q_data['modern_classic_know'][0] = int(q_json['Wie gut kennen Sie sich im Genre Moderne Klassik aus?'])
    else:
        f.write('missing_value_modern_classic_know\n')

    # read out sortables classic - renaissance
    q_data_renaissance_sortable = q_json['renaissance_sortable']
    if len(q_data_renaissance_sortable)==10:
        for i in range(0, len(q_json['renaissance_sortable'])):
            q_data['renaissance_sortable'][i] = str(q_json['renaissance_sortable'][i])
    else:
        f.write('missing_value_renaissance_sortable')

    if 'Wie sicher sind Sie sich bei dieser Zuordnung (Renaissance Musik)?' in q_json:
        q_data['renaissance_sortable_sure'][0] = int(q_json['Wie sicher sind Sie sich bei dieser Zuordnung (Renaissance Musik)?'])
    else:
        f.write('missing_value_renaissance_sortable_sure\n')

    if 'Wie gut kennen Sie sich im Genre Renaissance Musik aus?' in q_json:
        q_data['renaissance_know'][0] = int(q_json['Wie gut kennen Sie sich im Genre Renaissance Musik aus?'])
    else:
        f.write('missing_value_renaissance_know\n')

    # read out sortables classic - romantic
    q_data_romantic_sortable = q_json['romantic_sortable']
    if len(q_data_romantic_sortable)==10:
        for i in range(0, len(q_json['romantic_sortable'])):
            q_data['romantic_sortable'][i] = str(q_json['romantic_sortable'][i])
    else:
        f.write('missing_value_romantic_sortable')

    if 'Wie sicher sind Sie sich bei dieser Zuordnung (Romantik)?' in q_json:
        q_data['romantic_sortable_sure'][0] = int(q_json['Wie sicher sind Sie sich bei dieser Zuordnung (Romantik)?'])
    else:
        f.write('missing_value_romantic_sortable_sure\n')

    if 'Wie gut kennen Sie sich im Genre Musik der Romantik aus?' in q_json:
        q_data['romantic_know'][0] = int(q_json['Wie gut kennen Sie sich im Genre Musik der Romantik aus?'])
    else:
        f.write('missing_value_romantic_know\n')

    # read out sortables classic - all
    if 'classic' in q_json:
        q_data_classic_all = q_json['classic']
        if len(q_data_classic_all)==5:
            for i in range(0, len(q_json['classic'])):
                q_data['classic_all'][i] = str(q_json['classic'][i])
        else:
            f.write('classic_all_not_complete\n')
    else:
        f.write('classic_all_missing\n')


    ## read out sortables electro

    # read out sortables electro - deephouse
    q_data_deephouse_sortable = q_json['deephouse_sortable']
    if len(q_data_deephouse_sortable)==10:
        for i in range(0, len(q_json['deephouse_sortable'])):
            q_data['deephouse_sortable'][i] = str(q_json['deephouse_sortable'][i])
    else:
        f.write('missing_value_deephouse_sortable')

    if 'Wie sicher sind Sie sich bei dieser Zuordnung (Deep House)?' in q_json:
        q_data['deephouse_sortable_sure'][0] = int(q_json['Wie sicher sind Sie sich bei dieser Zuordnung (Deep House)?'])
    else:
        f.write('missing_value_deephouse_sortable_sure\n')

    if 'Wie gut kennen Sie sich im Genre Deep House aus?' in q_json:
        q_data['deephouse_know'][0] = int(q_json['Wie gut kennen Sie sich im Genre Deep House aus?'])
    else:
        f.write('missing_value_deephouse_know\n')

    # read out sortables electro - drumnbass
    q_data_drumnbass_sortable = q_json['drumnbass_sortable']
    if len(q_data_drumnbass_sortable)==10:
        for i in range(0, len(q_json['drumnbass_sortable'])):
            q_data['drumnbass_sortable'][i] = str(q_json['drumnbass_sortable'][i])
    else:
        f.write('missing_value_drumnbass_sortable')

    if 'Wie sicher sind Sie sich bei dieser Zuordnung (DrumnBass)?' in q_json:
        q_data['drumnbass_sortable_sure'][0] = int(q_json['Wie sicher sind Sie sich bei dieser Zuordnung (DrumnBass)?'])
    else:
        f.write('missing_value_drumnbass_sortable_sure\n')

    if 'Wie gut kennen Sie sich im Genre DrumnBass aus?' in q_json:
        q_data['drumnbass_know'][0] = int(q_json['Wie gut kennen Sie sich im Genre DrumnBass aus?'])
    else:
        f.write('missing_value_drumnbass_know\n')

    # read out sortables electro - dubstep
    q_data_dubstep_sortable = q_json['dubstep_sortable']
    if len(q_data_dubstep_sortable)==10:
        for i in range(0, len(q_json['dubstep_sortable'])):
            q_data['dubstep_sortable'][i] = str(q_json['dubstep_sortable'][i])
    else:
        f.write('missing_value_dubstep_sortable')

    if 'Wie sicher sind Sie sich bei dieser Zuordnung (Dubstep)?' in q_json:
        q_data['dubstep_sortable_sure'][0] = int(q_json['Wie sicher sind Sie sich bei dieser Zuordnung (Dubstep)?'])
    else:
        f.write('missing_value_dubstep_sortable_sure\n')

    if 'Wie gut kennen Sie sich im Genre Dubstep aus?' in q_json:
        q_data['dubstep_know'][0] = int(q_json['Wie gut kennen Sie sich im Genre Dubstep aus?'])
    else:
        f.write('missing_value_dubstep_know\n')

    # read out sortables electro - techno
    q_data_techno_sortable = q_json['techno_sortable']
    if len(q_data_techno_sortable)==10:
        for i in range(0, len(q_json['techno_sortable'])):
            q_data['techno_sortable'][i] = str(q_json['techno_sortable'][i])
    else:
        f.write('missing_value_techno_sortable')

    if 'Wie sicher sind Sie sich bei dieser Zuordnung (Techno)?' in q_json:
        q_data['techno_sortable_sure'][0] = int(q_json['Wie sicher sind Sie sich bei dieser Zuordnung (Techno)?'])
    else:
        f.write('missing_value_techno_sortable_sure\n')

    if 'Wie gut kennen Sie sich im Genre Techno aus?' in q_json:
        q_data['techno_know'][0] = int(q_json['Wie gut kennen Sie sich im Genre Techno aus?'])
    else:
        f.write('missing_value_techno_know\n')

    # read out sortables electro - trance
    q_data_trance_sortable = q_json['trance_sortable']
    if len(q_data_trance_sortable)==10:
        for i in range(0, len(q_json['trance_sortable'])):
            q_data['trance_sortable'][i] = str(q_json['trance_sortable'][i])
    else:
        f.write('missing_value_trance_sortable')

    if 'Wie sicher sind Sie sich bei dieser Zuordnung (Trance)?' in q_json:
        q_data['trance_sortable_sure'][0] = int(q_json['Wie sicher sind Sie sich bei dieser Zuordnung (Trance)?'])
    else:
        f.write('missing_value_trance_sortable_sure\n')

    if 'Wie gut kennen Sie sich im Genre Trance aus?' in q_json:
        q_data['trance_know'][0] = int(q_json['Wie gut kennen Sie sich im Genre Trance aus?'])
    else:
        f.write('missing_value_trance_know\n')

    # read out sortables electro - all
    if 'electro' in q_json:
        q_data_electro_all = q_json['electro']
        if len(q_data_electro_all)==5:
            for i in range(0, len(q_json['electro'])):
                q_data['electro_all'][i] = str(q_json['electro'][i])
        else:
            f.write('electro_all_not_complete\n')
    else:
        f.write('electro_all_missing\n')

    ### save data frame to csv
    # read out id
    id=str(json_file.split('ergebnisstring_', 1)[1].split('.json',1)[0])

    # assign id
    q_data['id']=id
    q_data.to_csv('data_questionnaire_' + id + '.csv')
    return q_data
    f.close()
