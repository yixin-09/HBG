#!/usr/bin/env bash
racket herbie/src/herbie.rkt report --timeout '10800' --threads "yes" High_level.fpcore graphsHigh/
racket herbie/src/herbie.rkt report --timeout '10800' --threads "yes" Middle_level.fpcore graphsMiddle/
racket herbie/src/herbie.rkt report --timeout '10800' --threads "yes" Low_level.fpcore graphsLow/
