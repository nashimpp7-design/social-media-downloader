#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import zipfile
import shutil
from pathlib import Path
from animations import show_welcome, show_loading, show_success, show_error
from downloader import download_video, download_audio, detect_platform

def setup_download_folder():
    """ডাউনলোড ফোল্ডার তৈরি করুন"""
    download_dir = Path.home() / 'Downloads' / 'SocialMediaDownloads'
    download_dir.mkdir(parents=True, exist_ok=True)
    return str(download_dir)

def create_zip_archive(folder_path, zip_name=None):
    """ডাউনলোড ফোল্ডারকে ZIP ফাইলে কম্প্রেস করুন"""
    try:
        if zip_name is None:
            import time
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            zip_name = f"SocialMediaDownloads_{timestamp}.zip"
        
        zip_path = os.path.join(Path.home(), 'Downloads', zip_name)
        
        show_loading("ফাইল কম্প্রেস করছে", 2)
        
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, folder_path)
                    zipf.write(file_path, arcname)
        
        file_size = os.path.getsize(zip_path) / (1024 * 1024)  # MB এ
        show_success(f"✅ ZIP ফাইল তৈরি হয়েছে!")
        print(f"📁 অবস্থান: {zip_path}")
        print(f📐 ফাইল সাইজ: {file_size:.2f} MB")
        return zip_path
    
    except Exception as e:
        show_error(f"❌ ZIP ফাইল তৈরি করতে ত্রুটি: {str(e)}")
        return None

def main():
    os.system('clear' if os.name == 'posix' else 'cls')
    
    # স্বাগত অ্যানিমেশন দেখান
    show_welcome()
    
    # ডাউনলোড ফোল্ডার সেটআপ
    download_folder = setup_download_folder()
    
    print("\n")
    print("📱 সোশ্যাল মিডিয়া ডাউনলোডার - Termux সংস্করণ")
    print("=" * 50)
    print("\nসমর্থিত প্ল্যাটফর্ম:")
    print("  🎥 YouTube")
    print("  📷 Instagram")
    print("  🎬 TikTok")
    print("  👍 Facebook")
    print("  🐦 Twitter/X")
    print("  🎵 SoundCloud")
    print("\n" + "=" * 50)
    
    while True:
        print("\n\n🗑️  বিকল্প:")
        print("  1️⃣  লিংক গত ডাউনলোড")
        print("  2️⃣  ZIP ফাইল তৈরি করুন")
        print("  3️⃣  বের হন্")
        
        choice = input("\nপছন্দ (1, 2, 3): ").strip()
        
        if choice == '1':
            print("\nলিংক পেস্ট করুন (বা 'exit' টাইপ করে বের হন):")
            url = input(">>> ").strip()
            
            if url.lower() == 'exit':
                continue
            
            if not url:
                show_error("❌ লিংক খালি! আবার চেষ্টা করুন।")
                continue
            
            print("\nডাউনলোড টাইপ বেছে নিন:")
            print("  1️⃣  ভিডিও ডাউনলোড করুন")
            print("  2️⃣  অডিও/মিউজিক ডাউনলোড করুন")
            
            download_choice = input("\nপছন্দ (1 বা 2): ").strip()
            
            if download_choice == '1':
                show_loading("ভিডিও ডাউনলোড হচ্ছে", 3)
                download_video(url, download_folder)
            elif download_choice == '2':
                show_loading("অডিও ডাউনলোড হচ্ছে", 3)
                download_audio(url, download_folder)
            else:
                show_error("❌ অবৈধ পছন্দ!")
        
        elif choice == '2':
            if os.listdir(download_folder):
                create_zip_archive(download_folder)
            else:
                show_error("❌ ফোল্ডারে কোনো ফাইল নেই!")
        
        elif choice == '3':
            show_success("ধন্যবাদ! বাই বাই!")
            break
        
        else:
            show_error("❌ অবৈধ পছন্দ!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        show_error("\n\n❌ প্রোগ্রাম বন্ধ করা হয়েছে (Ctrl+C)")
        sys.exit(0)
    except Exception as e:
        show_error(f"\n❌ একটি ত্রুটি ঘটেছে: {str(e)}")
        sys.exit(1)
