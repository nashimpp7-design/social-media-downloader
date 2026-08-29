#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
from pathlib import Path
from animations import show_success, show_error, show_info, show_progress, show_loading

def detect_platform(url):
    """URL থেকে প্ল্যাটফর্ম শনাক্ত করুন"""
    url_lower = url.lower()
    
    platforms = {
        'youtube': ['youtube.com', 'youtu.be', 'yt.be'],
        'instagram': ['instagram.com', 'ig.me'],
        'tiktok': ['tiktok.com', 'vm.tiktok.com', 'vt.tiktok.com'],
        'facebook': ['facebook.com', 'fb.watch'],
        'twitter': ['twitter.com', 'x.com', 'tweet'],
        'soundcloud': ['soundcloud.com']
    }
    
    for platform, keywords in platforms.items():
        for keyword in keywords:
            if keyword in url_lower:
                return platform
    
    return 'unknown'

def download_video(url, output_folder):
    """ভিডিও ডাউনলোড করুন"""
    try:
        platform = detect_platform(url)
        show_info(f"🔍 প্ল্যাটফর্ম শনাক্ত করা হয়েছে: {platform.upper()}")
        
        output_path = os.path.join(output_folder, f"video_%(title)s.%(ext)s")
        
        command = [
            'yt-dlp',
            '-f', 'best[ext=mp4]',
            '-o', output_path,
            url
        ]
        
        show_loading("ভিডিও ডাউনলোড হচ্ছে", 2)
        
        result = subprocess.run(command, capture_output=True, text=True)
        
        if result.returncode == 0:
            show_success(f"✅ ভিডিও সফলভাবে ডাউনলোড হয়েছে!")
            show_info(f"📁 অবস্থান: {output_folder}")
        else:
            show_error(f"❌ ডাউনলোড ব্যর্থ: {result.stderr}")
    
    except Exception as e:
        show_error(f"❌ ত্রুটি: {str(e)}")

def download_audio(url, output_folder):
    """অডিও/মিউজিক ডাউনলোড করুন"""
    try:
        platform = detect_platform(url)
        show_info(f"🔍 প্ল্যাটফর্ম শনাক্ত করা হয়েছে: {platform.upper()}")
        
        output_path = os.path.join(output_folder, f"audio_%(title)s.%(ext)s")
        
        command = [
            'yt-dlp',
            '-x',
            '--audio-format', 'mp3',
            '--audio-quality', '0',
            '-o', output_path,
            url
        ]
        
        show_loading("অডিও ডাউনলোড হচ্ছে", 2)
        
        result = subprocess.run(command, capture_output=True, text=True)
        
        if result.returncode == 0:
            show_success(f"✅ অডিও সফলভাবে ডাউনলোড হয়েছে!")
            show_info(f"📁 অবস্থান: {output_folder}")
        else:
            show_error(f"❌ ডাউনলোড ব্যর্থ: {result.stderr}")
    
    except Exception as e:
        show_error(f"❌ ত্রুটি: {str(e)}")

def check_dependencies():
    """প্রয়োজনীয় টুলস চেক করুন"""
    required_tools = ['yt-dlp', 'ffmpeg']
    missing_tools = []
    
    for tool in required_tools:
        try:
            subprocess.run([tool, '--version'], capture_output=True, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            missing_tools.append(tool)
    
    if missing_tools:
        show_error(f"❌ নিম্নলিখিত টুলস ইনস্টল করা প্রয়োজন: {', '.join(missing_tools)}")
        show_info("📱 Termux-এ ইনস্টল করতে: pkg install ffmpeg yt-dlp")
        return False
    
    return True
