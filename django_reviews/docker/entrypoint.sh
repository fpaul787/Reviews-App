#!/bin/sh

while !  wget mysql:3306; do 
  sleep 1 
done