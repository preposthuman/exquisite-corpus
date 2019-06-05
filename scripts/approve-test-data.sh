#!/bin/bash

input_directories="raw downloaded source-lists"
output_directories="extracted tokenized messy-counts counts freqs wordfreq"

echo "Copying input directories from tests/input_data"
for directory in $input_directories; do
    rm -r tests/data/$directory
    cp -r tests/input_data/$directory tests/data
done

echo "Running the build"
XC_BUILD_TEST="1" snakemake -j 4

echo "Copying the output directories to tests/reference"
rm -r tests/reference/*

for directory in $output_directories; do
    cp -r tests/data/$directory tests/reference
done

echo "Removing the output directories from tests/data"
for directory in $output_directories; do
    rm -r tests/data/$directory
done