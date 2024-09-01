from models import db, Work, Performance


def seed_database():
    work1 = Work(
        title='The wet centre is bottomless', 
        medium='ambisonic fixed media', 
        year='2019', 
        description1='Assembled from field recordings, extracted and synthesized frog advertisement calls, and hybridized and invented species, the work attempts to get at the decentered perspective of an environment. The piece was written alongside a paper for the journal Organised Sound. Higher-order ambisonics (HOA) files available upon request.', 
        description2='', 
        image1='/static/wetCenterSwamp1.jpeg', 
        image2='/static/wetCenterSwamp2.jpg', 
        image3='/static/wetCenterMsp1.png', 
        image4='', 
        soundcloud_header='Stereo Mix', 
        soundcloud_track_id='744445654', 
        downdload_link='',
        img_filter=''
    )
    
    work2 = Work(
        title=' Almost an Ocean', 
        medium='stereo fixed media', 
        year='2019', 
        description1='All sounds recorded January 2019 along the south shore of Lake Superior, on travel funded by grants from Oberlin Conservatory and Oberlin Environmental Studies. Produced in collaboration with Isaac Shalit. Image taken on South Bay in Munising, MI. The work is constructed along morphological affinities between the sounds encountered, and its form explores the simultaneous diversity and unity of the little places we came across in this vast soundscape. Over small changes in time or location, the dynamics of ice and water are completely transformed but underlying this stunning diversity are shared tides and conditions.', 
        description2='', 
        image1='/static/almostAnOcean1.jpeg', 
        image2='', 
        image3='', 
        image4='', 
        soundcloud_header='Stereo Mix', 
        soundcloud_track_id='583136832', 
        downdload_link='',
        img_filter=''
    )
    
    work3 = Work(
        title='The Big Lamp', 
        medium='installation/performance', 
        year='2018', 
        description1='The Big Lamp was an interdisciplinary, collaborative installation and performance in an empty racquetball court at Oberlin College in Ohio. It used cloth, metal, sine tones, bodies, a chord organ, fluorescent lights, a trombone, and various other soundmakers to convey a sense of concealed and emerging immensity.', 
        description2='', 
        image1='/static/bigLamp1.png', 
        image2='', 
        image3='', 
        image4='', 
        soundcloud_header='', 
        soundcloud_track_id='', 
        downdload_link='',
        img_filter='filter-off'
    )
    
    work4 = Work(
        title='Dregs-Magic', 
        medium='audiovisual fixed media', 
        year='2017', 
        description1='Sound recorded by Leah Bertrand and Ricky Covell; audio created by Leah Bertrand and video created by Ricky Covell in Fall 2017. A thematization of residue, dregs-magic functions like a microscope,  revealing streams of subterranean texture and movement, freeing some  ordinary metal to reveal its internal world. Unlike the microscope,  however, the work does not purport to depict a viewer-independent world –  rather, it is the residue of the encounter itself which is interrogated  – the bumping of the microphone, the texture of the chalk and charcoal.  Its microscope is one of nakedness, its object, vision. Dregs-Magic has been programmed at the 2018 MFA Media Arts Annual,  National Students in Electronic Music Event (NSEME) 2019, and the  Society for Electroacoustic Music in the United States (SEAMUS) 2019.', 
        description2='', 
        image1='/static/dregsMagic1.png', 
        image2='', 
        image3='', 
        image4='', 
        soundcloud_header='', 
        soundcloud_track_id='', 
        downdload_link='',
        img_filter='filter-off'
    )
    
    performance1 = Performance(
        title='Beg’d',
        medium='performance',
        year='2018',
        description1='Beg’d was a free improvisation ensemble formed in the spring of 2018. The instrumentation consisted of bowed metals, melodica, midi guitar, toy synthesizer, ocarina, and enough whirlies to go around. Audio excerpts above, full video below.',
        description2='', 
        image1='/static/Begd.jpeg',
        image2='',
        image3='',
        image4='', 
        soundcloud_header='Stereo Mix',
        soundcloud_track_id='415367730',
        downdload_link='',
        img_filter='filter-off'
    )
    
    db.session.add_all([work1, work2, work3, work4, performance1])
    db.session.commit()



            # Template
# work = Work(
#     title='', 
#     medium='', 
#     year='', 
#     description1='', 
#     description2='', 
#     image1='', 
#     image2='', 
#     image3='', 
#     image4='', 
#     soundcloud_header='', 
#     soundcloud_url='', 
#     downdload_link='' 
# )
