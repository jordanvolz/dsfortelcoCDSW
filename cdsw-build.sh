#!/bin/bash

#!/bin/bash

if [ -d "models/spark/" ] 
then
  rm -r -f models/spark/*
  if [ -f "models/spark_rf.tar"]
  then tar -xf models/spark_rf.tar 
  fi
fi

