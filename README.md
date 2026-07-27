# Notes MCP Server

A simple Model Context Protocol (MCP) project built with Python that allows Claude Desktop to interact with and manage local notes through custom MCP tools.

## Overview

This project was created to understand how the Model Context Protocol (MCP) works by building a practical local MCP server.

The server connects to Claude Desktop and exposes tools that allow Claude to interact with notes stored locally on the computer.

## Features

- Create notes
- Read notes
- List available notes
- Manage local note files
- Connect a Python MCP server with Claude Desktop
- Execute tools using natural-language requests

## Tech Stack

- Python
- Model Context Protocol (MCP)
- MCP Python SDK
- Claude Desktop
- JSON
- Git & GitHub

## Project Structure

notes-mcp/
- notes/
  - mcp_testing.md
  - to_do_list.md
- server.py
- requirements.txt
- .gitignore
- README.md

## How It Works

Claude Desktop -> MCP Client -> Python MCP Server -> MCP Tools -> Local Notes

Claude Desktop acts as the MCP client. It communicates with the Python MCP server using Model Context Protocol. The server provides tools that allow Claude to perform operations on locally stored notes.

## What I Learned

- Fundamentals of Model Context Protocol (MCP)
- MCP client-server architecture
- Creating MCP tools using Python
- Connecting Claude Desktop with a local MCP server
- Allowing an AI assistant to interact with local resources
- MCP server configuration and debugging

## Purpose

This project was developed as a hands-on learning project to understand MCP and how AI assistants can interact with external tools and local resources.
