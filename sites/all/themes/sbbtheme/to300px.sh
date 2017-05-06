#!/bin/bash

for file in *.png;
do
  convert "$file" -resize '300x300>' "$file";
  echo "scaled $file";
done

for file in *.jpg;
do
  convert "$file" -resize '300x300>' "$file";
  echo "scaled $file";
done
