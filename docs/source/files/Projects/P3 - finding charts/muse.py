# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------

import numpy as np

# ---------------- Define the MUSE WFM field of view -------------------------------------
# From the MUSE manual, march 2014
muse_in = np.array([[0.0086683878,   0.0084439565],
                    [359.99128-360., 0.008499508],
                    [359.99172-360.,-0.0082782215],
                    [0.0080579666,  -0.008389310]])
muse_in *= 3600 # make it in arcsec

muse_out = np.zeros((16,2))
muse_out = np.array([[0.012835385,0.0085544861],
                    [0.0085551081,0.012277302],
                    [0.00027758977,0.012],
                    [359.99189-360.,0.012277352],
                    [359.98778-360.,0.0091101444],
                    [359.98739-360.,-0.0091121412],
                    [359.98955-360.,-0.010111818],
                    [359.99417-360.,-0.01050022],
                    [359.99422-360.,-0.011722438],
                    [359.99611-360.,-0.01172232],
                    [359.99622-360.,-0.012166759],
                    [0.004002035,-0.012222326],
                    [0.0040555527,-0.011777885],
                    [0.0060549064,-0.011833571],
                    [0.0060015071,-0.010611345],
                    [0.0090006082,-0.010444971],
                    [0.012444522,-0.0095565611]])
muse_out *= 3600 # make it in arcsec

# ----------------------------------------------------------------------------------------

# GS valid search radius in arcsec
outer_GS_search = 11. * 60. 
inner_GS_search = 120. 

# TTS validity area
inner_TTS_search = 1.725/2.*60 # in arcsec
outer_TTS_search = 3.590/2.*60 # in arcsec


# List the supported MUSE observing templates
muse_templates = [# WFM-NOAO
                  'MUSE_wfm-noao_acq_preset',
                  'MUSE_wfm-noao_acq_movetopixel',
                  'MUSE_wfm-noao_obs_genericoffset',
                  # WFM-AO
                  'MUSE_wfm-ao_acq_movetopixelLGS',
                  'MUSE_wfm-ao_obs_genericoffsetLGS',
                  # WFM_cal
                  'MUSE_wfm_cal_specphot',
                  'MUSE_wfm_cal_astrom',
                  ]

              
                    
                    
                    
                    