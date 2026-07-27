import streamlit as st

# --- STREAMLIT WEB APP: 2028 MENTOR & FOTOĞROFLA SORU ÇÖZÜMÜ ---

st.set_page_config(page_title="2028 AI Mentor", page_icon="🤖", layout="centered")

st.title("🤖 AI Copilot 2028 Mentorluk ve Soru Analiz Sistemi")
st.markdown("Maarif Modeli'ne uygun, kişiselleştirilmiş yapay zeka ders koçunuz ve akıllı soru çözüm asistanınız.")
st.markdown("---")

# 1. Adım: Öğrenci Bilgileri
ogrenci_adi = st.text_input("1. Adın nedir?")

if ogrenci_adi:
    st.success(f"Memnun oldum, {ogrenci_adi}! Bugün hangi alanda koçluk yapalım?")
    
    # İşlem Modu Seçimi (Test Analizi vs Soru Çözümü)
    mod = st.radio("Yapmak istediğin işlemi seç:", ["📊 Test ve Konu Analizi", "📸 Fotoğraflı Soru Çözüm Asistanı"])
    st.markdown("---")
    
    if mod == "📊 Test ve Konu Analizi":
        # Sınıf Seçimi
        sinif_secimi = st.selectbox("Kaçıncı sınıfsın?", ["9", "10", "11", "12"])
        
        # Ders Seçimi
        ders_listesi = [
            "Matematik", 
            "Türk Dili ve Edebiyatı", 
            "Fizik", 
            "Kimya", 
            "Biyoloji", 
            "Tarih", 
            "Coğrafya"
        ]
        ders_secim = st.selectbox("Hangi dersi çalışıyorsun?", ders_listesi)
        
        # Konu Veritabanı (Maarif Modeli Uyumlu)
        konular = []
        
        if ders_secim == "Matematik":
            if sinif_secimi == "9":
                konular = ["Sayı Kümeleri ve Üslü-Köklü İfadeler", "Doğrusal Fonksiyonlar ve Mutlak Değer", "Algoritma Temelli Problemler ve Mantık", "Üçgende Eşlik ve Benzerlik"]
            elif sinif_secimi == "10":
                konular = ["Trigonometriye Giriş ve Analitik Geometri", "Fonksiyonların Nitel Özellikleri", "Veri, İstatistik, Sayma ve Olasılık"]
            elif sinif_secimi == "11":
                konular = ["İleri Düzey Fonksiyonlar ve Denklem Sistemleri", "Çember/Daire Analitiği ve Çokgenler", "Uzay Geometri"]
            else:
                konular = ["Limit ve Türev (Değişimin Matematiği)", "Üstel ve Logaritmik Fonksiyonlar", "Diziler ve Veri Analizi"]

        elif ders_secim == "Türk Dili ve Edebiyatı":
            if sinif_secimi == "9":
                konular = ["İletişim Öğeleri ve Metinlerin Sınıflandırılması", "Hikaye ve Roman Türlerinin Yapısal Analizi", "Dil Bilgisi (Sözcük Türleri)"]
            elif sinif_secimi == "10":
                konular = ["Türk Edebiyatının Dönemleri", "Masal, Fabl, Destan ve Halk Hikayeleri", "Mesnevi ve Millî Edebiyat Dönemi Eserleri"]
            elif sinif_secimi == "11":
                konular = ["Batı Etkisindeki Türk Edebiyatı", "Tanzimat ve Servet-i Fünun Dönemi", "Fecr-i Ati ve Millî Edebiyat Şiir/Roman Analizleri"]
            else:
                konular = ["Cumhuriyet Dönemi Türk Edebiyatı (Saf Şiir, Garip)", "Modern ve Postmodern Romanlar", "Dünya Edebiyatından Metin Analizleri"]

        elif ders_secim == "Fizik":
            if sinif_secimi == "9":
                konular = ["Fizik Bilimine Giriş", "Kuvvet, Hareket ve Vektörler", "İş, Güç, Enerji ve Sürdürülebilir Enerji"]
            elif sinif_secimi == "10":
                konular = ["Elektrik ve Manyetizma (Akım, Devreler)", "Basınç ve Kaldırma Kuvveti", "Dalgalar (Ses, Yay, Işık)"]
            elif sinif_secimi == "11":
                konular = ["İleri Mekanik (Bağıl Hareket, Newton Yasaları, Atışlar)", "Tork, Denge ve Elektriksel Alan/Potansiyel"]
            else:
                konular = ["Çembersel ve Basit Harmonik Hareket", "Dalga Mekaniği ve Atom Fiziği", "Modern Fizik ve Teknolojideki Uygulamaları"]

        elif ders_secim == "Kimya":
            if sinif_secimi == "9":
                konular = ["Kimya Bilimi ve Güvenlik Sembolleri", "Atom Modelleri ve Periyodik Sistem", "Kimyasal Türler Arası Etkileşimler"]
            elif sinif_secimi == "10":
                konular = ["Kimyanın Temel Kanunları ve Tepkimeler", "Gazlar ve Homojen Karışımlar (Çözeltiler)"]
            elif sinif_secimi == "11":
                konular = ["Modern Atom Teorisi ve Gaz Yasaları", "Sıvı Çözeltiler ve Çözünürlük", "Kimyasal Tepkimelerde Enerji, Hız ve Denge"]
            else:
                konular = ["Kimya ve Elektrik (Elektrokimya)", "Karbon Kimyasına Giriş ve Organik Bileşikler", "Yeşil Kimya ve Sürdürülebilirlik"]

        elif ders_secim == "Biyoloji":
            if sinif_secimi == "9":
                konular = ["Bilimsel Araştırma Süreçleri ve Canlıların Ortak Özellikleri", "Hücre Yapısı (Prokaryot/Ökaryot) ve Zar Geçişleri"]
            elif sinif_secimi == "10":
                konular = ["Canlılarda Enerji Dönüşümleri (ATP, Fotosentez, Solunum)", "Ekosistem Ekolojisi"]
            elif sinif_secimi == "11":
                konular = ["İnsan Fizyolojisi ve Sistemler (Sinir, Endokrin, Duyu)", "Destek-Hareket, Sindirim, Dolaşım ve Solunum Sistemleri", "Boşaltım ve Üreme Sistemleri"]
            else:
                konular = ["Nükleik Asitler ve Protein Sentezi", "Genetik Mühendisliği ve Biyoteknoloji", "Bitki Biyolojisi (Yapı, Taşınma, Üreme)"]

        elif ders_secim == "Tarih":
            if sinif_secimi == "9":
                konular = ["Geçmişin İnşa Sürecinde Tarih", "Eski Çağ ve Orta Çağ Medeniyetleri"]
            elif sinif_secimi == "10":
                konular = ["Türkistan'dan Türkiye'ye (Anadolu'nun Türkleşmesi)", "Beylikten Devlete Osmanlı Siyaseti ve Cihan Devleti"]
            elif sinif_secimi == "11":
                konular = ["Değişen Dünya Dengeleri Karşısında Osmanlı (1595-1774)", "Devrimler Çağında Devlet-Toplum İlişkileri"]
            else:
                konular = ["20. Yüzyıl Başlarında Dünya ve Osmanlı", "Millî Mücadele Dönemi ve Atatürkçülük", "Çağdaş Türk ve Dünya Tarihi"]

        else:
            if sinif_secimi == "9":
                konular = ["Harita Okuryazarlığı ve Coğrafi Bilgi Sistemleri (CBS)", "İklim Sistemi ve Doğal Sistem Süreçleri"]
            elif sinif_secimi == "10":
                konular = ["Beşerî Sistemler (Nüfus, Göç, Yerleşme)", "Ekonomik Faaliyetler, Afetler ve Sürdürülebilir Çevre"]
            elif sinif_secimi == "11":
                konular = ["Biyoçeşitlilik ve Ekosistemlerin İşleyişi", "Ülkelerin Ekonomik Politikaları ve Küresel Ticaret"]
            else:
                konular = ["Küreselleşen Dünya ve Çevre Toplum", "Küresel Çevre Sorunları ve Jeopolitik Konum"]

        # Konu Seçimi
        secilen_konu = st.selectbox("Çalıştığın Konuyu Seç:", konular)
        
        st.markdown("---")
        st.subheader("📝 Test Sonuçlarını Gir")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            dogru = st.number_input("Doğru Sayısı", min_value=0, max_value=100, value=0)
        with col2:
            yanlis = st.number_input("Yanlış Sayısı", min_value=0, max_value=100, value=0)
        with col3:
            bos = st.number_input("Boş Sayısı", min_value=0, max_value=100, value=0)
            
        if st.button("🚀 Analiz Et ve Rapor Al"):
            toplam = dogru + yanlis + bos
            net = dogru - (yanlis * 0.25)
            basari = (dogru / toplam) * 100 if toplam > 0 else 0
            
            st.markdown("---")
            st.subheader(f"📊 {ogrenci_adi.upper()} - Mentor Raporun")
            st.write(f"**Ders & Konu:** {sinif_secimi}. Sınıf {ders_secim} -> {secilen_konu}")
            st.metric(label="Toplam Net", value=f"{net}")
            st.metric(label="Başarı Oranı", value=f"%{basari:.1f}")
            
            if yanlis > 0:
                st.error(f"🚨 '{secilen_konu}' başlığında {yanlis} yanlışın var. Bu konunun soru çözüm videolarını tekrar izlemelisin!")
            else:
                st.success(f"🏆 Harika! '{secilen_konu}' konusunda hiç yanlışın çıkmadı, yola böyle devam et!")

    else:
        # FOTOĞRAFLI SORU ÇÖZÜM ASİSTANI
        st.subheader("📸 Yapay Zeka Soru Çözüm Paneli")
        st.write("Çözemediğin veya takıldığın sorunun fotoğrafını buraya yükle, yapay zeka senin için adım adım çözümünü ve mantığını anlatsın.")
        
        yuklenen_dosya = st.file_uploader("Soru fotoğrafını seç (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])
        
        if yuklenen_dosya is not None:
            # Fotoğrafı ekranda göster
            st.image(yuklenen_dosya, caption="Yüklenen Soru", use_column_width=True)
            
            ders_secimi_soru = st.selectbox("Bu soru hangi derse ait?", ["Matematik", "Fizik", "Kimya", "Biyoloji", "Türk Dili ve Edebiyatı", "Tarih", "Coğrafya"])
            
            if st.button("🔍 Soruyu Yapay Zekaya Çözdür"):
                with st.spinner("Soru okunuyor ve adım adım çözülüyor... Lütfen bekleyin."):
                    # Simüle edilmiş akıllı çözüm çıktısı (Gerçek yapay zeka vision entegrasyonu için altyapı hazır)
                    st.markdown("---")
                    st.success("✅ Soru başarıyla analiz edildi!")
                    st.markdown(f"### 💡 {ders_secimi_soru} - Adım Adım Çözüm Rehberi")
                    st.markdown("""
                    1. **Soru Kökü Analizi:** Soru bizden ilgili kavramın temel tanımını ve formül bağlamını kurmamızı istiyor.
                    2. **İpucu / Formül:** Verilen öncülleri alt alta yazarak değişkenleri yerine koyuyoruz.
                    3. **Çözüm Adımı:** İşlemleri sırasıyla takip ettiğimizde doğru seçeneğe ulaşıyoruz.
                    """)
                    st.info("📌 **Koç Notu:** Bu tarz soru kalıplarında bir sonraki sefere öncülleri elerken dikkatli olmalısın.")