#!/bin/bash

for i in $(seq 1 1000); do host -t A $1 $2 & done
