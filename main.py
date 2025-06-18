#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SAM PRO - نظام إدارة المبيعات والمخزون
Desktop Application Main Entry Point
"""

import os
import sys
import threading
import webbrowser
import time
import socket
from contextlib import closing
import tkinter as tk
from tkinter import messagebox, ttk
import subprocess

# إضافة المجلد الحالي إلى مسار Python
if hasattr(sys, '_MEIPASS'):
    # عند التشغيل من ملف exe
    base_path = sys._MEIPASS
else:
    # عند التشغيل من المصدر
    base_path = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, base_path)

# استيراد التطبيق
try:
    from app import create_app
    from models import db
except ImportError as e:
    print(f"خطأ في استيراد التطبيق: {e}")
    sys.exit(1)

class SAMProDesktopApp:
    def __init__(self):
        self.app = None
        self.server_thread = None
        self.port = self.find_free_port()
        self.host = '127.0.0.1'
        self.url = f'http://{self.host}:{self.port}'
        
        # إنشاء واجهة المستخدم
        self.create_gui()
        
    def find_free_port(self):
        """البحث عن منفذ متاح"""
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
            s.bind(('', 0))
            s.listen(1)
            port = s.getsockname()[1]
        return port
    
    def create_gui(self):
        """إنشاء واجهة المستخدم الرسومية"""
        self.root = tk.Tk()
        self.root.title("SAM PRO - نظام إدارة المبيعات والمخزون")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        
        # تعيين أيقونة التطبيق (إذا كانت متوفرة)
        try:
            if os.path.exists('icon.ico'):
                self.root.iconbitmap('icon.ico')
        except:
            pass
        
        # إنشاء الإطار الرئيسي
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # العنوان
        title_label = ttk.Label(main_frame, text="SAM PRO", font=("Arial", 24, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))
        
        subtitle_label = ttk.Label(main_frame, text="نظام إدارة المبيعات والمخزون", font=("Arial", 14))
        subtitle_label.grid(row=1, column=0, columnspan=2, pady=(0, 20))
        
        # معلومات الخادم
        server_frame = ttk.LabelFrame(main_frame, text="معلومات الخادم", padding="10")
        server_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))
        
        ttk.Label(server_frame, text="العنوان:").grid(row=0, column=0, sticky=tk.W)
        self.url_label = ttk.Label(server_frame, text=self.url, foreground="blue")
        self.url_label.grid(row=0, column=1, sticky=tk.W, padx=(10, 0))
        
        ttk.Label(server_frame, text="الحالة:").grid(row=1, column=0, sticky=tk.W)
        self.status_label = ttk.Label(server_frame, text="متوقف", foreground="red")
        self.status_label.grid(row=1, column=1, sticky=tk.W, padx=(10, 0))
        
        # أزرار التحكم
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=(0, 20))
        
        self.start_button = ttk.Button(button_frame, text="تشغيل الخادم", command=self.start_server)
        self.start_button.grid(row=0, column=0, padx=(0, 10))
        
        self.stop_button = ttk.Button(button_frame, text="إيقاف الخادم", command=self.stop_server, state=tk.DISABLED)
        self.stop_button.grid(row=0, column=1, padx=(0, 10))
        
        self.open_button = ttk.Button(button_frame, text="فتح التطبيق", command=self.open_browser, state=tk.DISABLED)
        self.open_button.grid(row=0, column=2)
        
        # شريط التقدم
        self.progress = ttk.Progressbar(main_frame, mode='indeterminate')
        self.progress.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # منطقة الرسائل
        message_frame = ttk.LabelFrame(main_frame, text="الرسائل", padding="10")
        message_frame.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.message_text = tk.Text(message_frame, height=8, width=60, wrap=tk.WORD)
        scrollbar = ttk.Scrollbar(message_frame, orient=tk.VERTICAL, command=self.message_text.yview)
        self.message_text.configure(yscrollcommand=scrollbar.set)
        
        self.message_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # تكوين الشبكة
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(5, weight=1)
        message_frame.columnconfigure(0, weight=1)
        message_frame.rowconfigure(0, weight=1)
        
        # إضافة رسالة ترحيب
        self.add_message("مرحباً بك في SAM PRO - نظام إدارة المبيعات والمخزون")
        self.add_message(f"سيتم تشغيل الخادم على العنوان: {self.url}")
        
        # معالج إغلاق النافذة
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def add_message(self, message):
        """إضافة رسالة إلى منطقة الرسائل"""
        timestamp = time.strftime("%H:%M:%S")
        self.message_text.insert(tk.END, f"[{timestamp}] {message}\n")
        self.message_text.see(tk.END)
        self.root.update_idletasks()
    
    def start_server(self):
        """تشغيل خادم Flask"""
        try:
            self.add_message("جاري تشغيل الخادم...")
            self.progress.start()
            
            # إنشاء التطبيق
            self.app = create_app()
            
            # تشغيل الخادم في خيط منفصل
            self.server_thread = threading.Thread(
                target=self.run_server,
                daemon=True
            )
            self.server_thread.start()
            
            # انتظار قصير للتأكد من تشغيل الخادم
            time.sleep(2)
            
            # تحديث واجهة المستخدم
            self.status_label.config(text="يعمل", foreground="green")
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.open_button.config(state=tk.NORMAL)
            self.progress.stop()
            
            self.add_message("تم تشغيل الخادم بنجاح!")
            self.add_message(f"يمكنك الآن الوصول للتطبيق عبر: {self.url}")
            
        except Exception as e:
            self.progress.stop()
            self.add_message(f"خطأ في تشغيل الخادم: {str(e)}")
            messagebox.showerror("خطأ", f"فشل في تشغيل الخادم:\n{str(e)}")
    
    def run_server(self):
        """تشغيل خادم Flask"""
        try:
            with self.app.app_context():
                db.create_all()
            
            self.app.run(
                host=self.host,
                port=self.port,
                debug=False,
                use_reloader=False,
                threaded=True
            )
        except Exception as e:
            self.add_message(f"خطأ في الخادم: {str(e)}")
    
    def stop_server(self):
        """إيقاف الخادم"""
        try:
            self.add_message("جاري إيقاف الخادم...")
            
            # تحديث واجهة المستخدم
            self.status_label.config(text="متوقف", foreground="red")
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.open_button.config(state=tk.DISABLED)
            
            self.add_message("تم إيقاف الخادم")
            
        except Exception as e:
            self.add_message(f"خطأ في إيقاف الخادم: {str(e)}")
    
    def open_browser(self):
        """فتح المتصفح"""
        try:
            webbrowser.open(self.url)
            self.add_message("تم فتح التطبيق في المتصفح")
        except Exception as e:
            self.add_message(f"خطأ في فتح المتصفح: {str(e)}")
            messagebox.showerror("خطأ", f"فشل في فتح المتصفح:\n{str(e)}")
    
    def on_closing(self):
        """معالج إغلاق التطبيق"""
        if messagebox.askokcancel("إغلاق", "هل تريد إغلاق التطبيق؟"):
            self.stop_server()
            self.root.destroy()
            sys.exit(0)
    
    def run(self):
        """تشغيل التطبيق"""
        self.root.mainloop()

def main():
    """النقطة الرئيسية لتشغيل التطبيق"""
    try:
        app = SAMProDesktopApp()
        app.run()
    except Exception as e:
        print(f"خطأ في تشغيل التطبيق: {e}")
        messagebox.showerror("خطأ", f"فشل في تشغيل التطبيق:\n{str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
