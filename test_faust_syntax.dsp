// Simple FAUST reverb example with syntax highlighting test
import("stdfaust.lib");

declare name "SimpleReverb";
declare author "Test Author";
declare description "A simple reverb effect";

// Control parameters
wetdry = hslider("Wet/Dry", 0.3, 0, 1, 0.01);
roomsize = hslider("Room Size", 0.5, 0, 1, 0.01);
damp = hslider("Damp", 0.5, 0, 1, 0.01);

// Simple delay-based reverb
delay1 = de.delay(48000, int(0.030 * ma.SR));
delay2 = de.delay(48000, int(0.022 * ma.SR)); 
delay3 = de.delay(48000, int(0.0134 * ma.SR));

allpass1 = fi.allpass_comb(1024, 0.131 * ma.SR, 0.7);
allpass2 = fi.allpass_comb(1024, 0.149 * ma.SR, 0.7);

reverb = _ <: delay1, delay2, delay3 :> 
         + : allpass1 : allpass2 : 
         fi.lowpass(1, 5000) * roomsize;

// Main process with wet/dry mix
process = _ <: _, reverb : ro.interleave(2,2) : 
          +, + : par(i, 2, *(wetdry)) : 
          ro.interleave(2,2) : +, +;