#!/bin/bash

for file in *.png;
do
  convert "$file" -resize '190x190>' "$file";
  echo "scaled $file";
done

for file in *.jpg;
do
  convert "$file" -resize '190x190>' "$file";
  echo "scaled $file";
done
