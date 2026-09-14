# Packet Sniffer

A Python tool that captures and analyzes network traffic in real-time, breaking down packets by protocol, source/destination IP, and port.

## Why I built it
To understand how network traffic actually flows at the packet level, and how tools like Wireshark work under the hood.

## How it works
Uses Scapy to capture live packets on a network interface and inspect their IP/TCP/UDP layers, printing a summary of each one.

## Setup
```bash
pip install -r requirements.txt
python sniffer.py
