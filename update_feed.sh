#!/bin/bash


rm -f /app/uglyfeeds/*
python3 main.py &> rss.log
cd /app/.streamlit/static/uglyfeeds && cp /app/uglyfeeds/uglyfeed.xml .


