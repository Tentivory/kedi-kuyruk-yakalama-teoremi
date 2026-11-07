#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kedi Kuyruk Yakalama Teoremi
===========================
Bu algoritma, bir kedinin kendi kuyruğunu yakalamaya çalışmasının
matematiksel olarak neden imkansız olduğunu kanıtlar.

Sonuç: Her zaman sonsuz döngüye girer. Bilim kazanır.
"""

import time
import random

def kedi_kuyruk_yakalama_girisimi(kedi_adi="Boncuk"):
    print(f"{kedi_adi} kuyruğunu yakalamaya karar verdi...")
    print("Fizik kanunları devreye giriyor...")
    
    deneme = 0
    while True:
        deneme += 1
        mesafe = random.uniform(0.1, 5.0)
        print(f"Deneme {deneme}: Kuyruk {mesafe:.2f} cm uzaklıkta...")
        
        # Kedi döner, kuyruk da döner
        time.sleep(0.5)
        print(f"  -> {kedi_adi} döndü, kuyruk kaçtı!")
        
        if deneme > 10:
            print("\n⚠️  UYARI: Bu işlem sonsuza kadar sürebilir.")
            print("Teorem kanıtlandı: Kedi kuyruğunu ASLA yakalayamaz.")
            print("Matematik > Kedi")
            break
        
        if random.random() < 0.05:  # %5 şansla mucize
            print("\n🎉 MUCİZE! Kedi kuyruğunu yakaladı... ama bu sadece rüya.")
            print("Uyanın, gerçek dünyada imkansız.")
            break

if __name__ == "__main__":
    print("=" * 50)
    print("KEDİ KUYRUK YAKALAMA TEOREMİ v1.0")
    print("Bilimsel olarak kanıtlanmış absürtlük")
    print("=" * 50)
    kedi_kuyruk_yakalama_girisimi()
    print("\nSonuç: Evren hala ayakta. Kedi hala dönüyor.")
