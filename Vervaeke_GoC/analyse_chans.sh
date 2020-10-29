# This script requires pyNeuroML (https://github.com/NeuroML/pyNeuroML) to run

CHANNELS="Golgi_Ca_HVA.channel.nml  Golgi_hcn1f.channel.nml  Golgi_hcn2f.channel.nml  Golgi_KA.channel.nml    Golgi_KC.channel.nml     Golgi_KV.channel.nml   Golgi_NaR.channel.nml  Golgi_Ca_LVA.channel.nml  Golgi_hcn1s.channel.nml  Golgi_hcn2s.channel.nml  Golgi_Kslow.channel.nml  Golgi_NaP.channel.nml  Golgi_NaT.channel.nml"

# Ignoring Golgi_KAHP.channel.nml - KS channel...

pynml-channelanalysis  $CHANNELS\
                      -caConc 5e-4 -temperature 20 -datSuffix '.20' -html -md -minV -75 # -75 as NaT has tau ~= 0 at <= -80 mV

pynml-channelanalysis  $CHANNELS\
                      -caConc 5e-4 -temperature 23 -datSuffix '.23' -html -md -minV -75 # -75 as NaT has tau ~= 0 at <= -80 mV

