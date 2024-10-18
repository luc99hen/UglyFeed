#!/bin/bash


rm -f /app/uglyfeeds/*
python3 main.py
cd /app/.streamlit/static/uglyfeeds && cp /app/uglyfeeds/uglyfeed.xml .


