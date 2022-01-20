# YouLikeHits-Bot

[Github](https://github.com/i0Z3R0/YouLikeHits-Bot)

# Table of Contents
- [Table of Contents](#table-of-contents)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [About](#about)
- [Overview of Features](#overview-of-features)
- [Detailed Overview](#detailed-overview)

# Prerequisites
- Latest version of Python3
- Latest version of Pip
- Text editor to change some settings
- Twitch account linked to your YLH account
- Twitter account linked to your YLH account

# Installation
1. git clone https://github.com/i0Z3R0/YouLikeHits-Bot.git
2. cd YouLikeHits-Bot
3. pip3.9 install -r requirements.txt
4. Fill in info in settings.json
5. python3 YLH-Twitch.py / python3 YLH-Twitter.py
#### Note: ChromeDriver is NOT required, webdriver_manager will automatically download the matching version of ChromeDriver for your OS.

# About
This is a tool that will automatically earn you points on YouLikeHits. Currently, Twitch followers and Twitter followers are supported.

# Overview of Features
## Twitch Follower Bot
- Automatically enters login information for YLH and Twitch
- Automatically follow Twitch users to earn points
- After all the users on the first page are followed, refresh the page for more users
- Automatically skip users that can't be followed (Twitch account deleted etc.)
- Can be run for theoretically forever
## Twitter Follower Bot
- Automatically enters login information for YLH and Twitter
- Automatically follow Twitter users to earn points
- After all the users on the first page are followed, refresh the page for more users
- Automatically skip users that can't be followed (Error with button presses etc.)
- Can be run for theoretically forever

# Detailed Overview

## Twitch Follower Bot
### **Overview**
This tool will follow all the Twitch users on YouLikeHits' Twitch follower page, earning you lots of points. Minimal interaction is needed, and once running, can be left running forever.
### **Detailed Breakdown**
The bot will first navigate to the Twitch login page. Your info will be automatically submitted, but you will need to verify with a code from  your email when you sign in. Complete additional anti-bot captchas if necessary, this bot does not do that. After you're done, press enter. Then, the bot will sign in to the YouLikeHits website with your provided credentials. Press enter once you see the bot logged in successfully (hCaptcha sometimes shows up). The bot will navigate to the Twitch follower page, and follow each user, thus earning you a lot of points. After all the users have been followed, it will reload the page and continue following new users. If the bot is stuck on a page and can't follow, it will simply skip that user.

### **Settings**
- **YLH Username** - String (Line 2): Your username for YouLikeHits, found on the top right corner of any YLH page.
- **YLH Password** - String (Line 3): The password to your account.
- **Twitch Username** - String (Line 4): Your Twitch username.
- **Twitch Password** - String (Line 5): Your Twitch password.
- **Headless Mode** - Boolean (Line 6): Headless mode is buggy and only works some of the time. Would recommend setting this to false.

## Twitter Follower Bot
### **Overview**
This tool will follow all the Twitter users on YouLikeHits' Twitter follower page, earning you lots of points. Minimal interaction is needed, and once running, can be left running forever.
### **Detailed Breakdown**
The bot will first navigate to the Twitter login page. Your info will be automatically submitted, and there is usually no captcha (you only need to login once every time you run this). Then, the bot will sign in to the YouLikeHits website with your provided credentials. Press enter once you see the bot logged in successfully (hCaptcha sometimes shows up). The bot will navigate to the Twitter follower page, and follow each user, thus earning you a lot of points. After all the users have been followed, it will reload the page and continue following new users. If the bot is stuck on a page and can't follow, it will simply skip that user.

### **Settings**
- **YLH Username** - String (Line 2): Your username for YouLikeHits, found on the top right corner of any YLH page.
- **YLH Password** - String (Line 3): The password to your account.
- **Twitter Username** - String (Line 4): Your Twitter username.
- **Twitter Password** - String (Line 5): Your Twitter password.
- **Headless Mode** - Boolean (Line 6): Headless mode is buggy and only works some of the time. Would recommend setting this to false.
