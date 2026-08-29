#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import sys
from colorama import Fore, Back, Style, init

# Colorama ইনিশিয়ালাইজ করুন
init(autoreset=True)

def show_welcome():
    """স্বাগত অ্যানিমেশন দেখান"""
    welcome_text = """
╔═════════════════════════════════════════════════════════════╗
║                                                             ║
║       🎬 সোশ্যাল মিডিয়া ডাউনলোডার 🎵                ║
║                                                             ║
║           সব প্ল্যাটফর্ম থেকে ভিডিও/অডিও             ║
║                  ডাউনলোড করুন সহজেই                   ║
║                                                             ║
╚═════════════════════════════════════════════════════════════╝
    """
    
    # লাইন বাই লাইন প্রিন্ট করুন
    for line in welcome_text.split('\n'):
        print(f"{Fore.CYAN}{line}{Style.RESET_ALL}")
        time.sleep(0.1)

def show_loading(message, duration=3):
    """লোডিং অ্যানিমেশন দেখান"""
    spinner_text = [
        '⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'
    ]
    
    start_time = time.time()
    spinner_index = 0
    
    while time.time() - start_time < duration:
        spinner = spinner_text[spinner_index % len(spinner_text)]
        print(f"\r{Fore.YELLOW}{spinner} {message}...{Style.RESET_ALL}", end='', flush=True)
        spinner_index += 1
        time.sleep(0.1)
    
    print("\r" + " " * 50 + "\r", end='', flush=True)

def show_success(message):
    """সফল বার্তা দেখান (সবুজ রং)"""
    success_animations = [
        "✓", "✔"
    ]
    
    # অ্যানিমেটেড টিক চিহ্ন
    for anim in success_animations * 2:
        print(f"\r{Fore.GREEN}{anim} {message}{Style.RESET_ALL}", end='', flush=True)
        time.sleep(0.1)
    
    print(f"\r{Fore.GREEN}✅ {message}{Style.RESET_ALL}")
    time.sleep(0.5)

def show_error(message):
    """ত্রুটি বার্তা দেখান (লাল রং)"""
    error_animations = [
        "✗", "✘"
    ]
    
    # অ্যানিমেটেড X চিহ্ন
    for anim in error_animations * 2:
        print(f"\r{Fore.RED}{anim} {message}{Style.RESET_ALL}", end='', flush=True)
        time.sleep(0.1)
    
    print(f"\r{Fore.RED}❌ {message}{Style.RESET_ALL}")
    time.sleep(0.5)

def show_progress(current, total, message="ডাউনলোড হচ্ছে"):
    """প্রগতি বার দেখান"""
    bar_length = 30
    filled = int(bar_length * current / total)
    bar = '█' * filled + '░' * (bar_length - filled)
    percentage = (current / total) * 100
    
    print(f"\r{Fore.CYAN}[{bar}] {percentage:.1f}% {message}{Style.RESET_ALL}", end='', flush=True)
    
    if current == total:
        print()  # নতুন লাইন

def show_info(message):
    """তথ্য বার্তা দেখান (নীল রং)"""
    print(f"{Fore.BLUE}ℹ️  {message}{Style.RESET_ALL}")

def show_warning(message):
    """সতর্কতা বার্তা দেখান (হলুদ রং)"""
    print(f"{Fore.YELLOW}⚠️  {message}{Style.RESET_ALL}")

def animated_text(text, color=Fore.GREEN, delay=0.05):
    """পাঠ্য অ্যানিমেশন - ওয়ার্ড বাই ওয়ার্ড"""
    for word in text.split():
        print(f"{color}{word}{Style.RESET_ALL}", end=' ', flush=True)
        time.sleep(delay)
    print()
