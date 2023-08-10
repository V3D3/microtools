#!/usr/bin/env bash
curl -s https://www.confirmtkt.com/pnr-status/$1 | grep $1 | cut -c 8- | tail -n 1 | rev | cut -c 3- | rev | jq ".PassengerStatus[] .CurrentStatus"
