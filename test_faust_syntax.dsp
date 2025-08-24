// FAUST Syntax Highlighting Test File
import("stdfaust.lib");

declare name "SynthTest";
declare author "Test";

// Comments should be gray/green
/* Block comment test */

// Numbers should be purple: 440, 0.5, 1.0, 48000
freq = 440;
amp = 0.5;
sampleRate = 48000;

// Strings should be yellow
title = "My Synth";

// Keywords should be pink/red: import, declare, process, with, library
// Functions should be green: sin, cos, fi.lowpass, de.delay
osc = os.osc(freq);
filter = fi.lowpass(1, 1000);
delay = de.delay(48000, 0.1 * ma.SR);

// Operators should be pink: =, +, -, *, /, <:, :>
mix = osc * amp;
stereo = mix <: _, _;
output = stereo :> _;

// Library prefixes should be orange: fi. os. ma. de.
envelope = en.adsr(0.01, 0.1, 0.8, 0.2);
noise = no.noise;
route = ro.interleave(2,2);

// Main process
process = osc * envelope;