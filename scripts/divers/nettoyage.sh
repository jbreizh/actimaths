#!/bin/bash
#nettoyage
find ../../ -name "*~"   -print -exec rm {} \;
find ../../ -name "*pyc" -print -exec rm {} \;
