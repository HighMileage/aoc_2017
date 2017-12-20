# Day 16

I found this day particularly challenging. I initially wasted cycles trying to compute a direct
mapping between the input and output. Sadly, I had not considered how indexed references throw a
wrench in any sort of deterministic solution given an input. I finally settled on splitting
movements into `Spin`s and `Exchanges` in one group and `Partner`s in another. After this failed to
give me a performance bump, I investigated the possibility that the pattern might be cycling. To my
good fortune, my pattern was cycling and it was fairly easy to avoid _many_ iterations and exit
early with a pre-computed value in hand. I'm curious to research a bit more and see if that pattern
holds up at all outside of my unique input.
