# تعليمات إنشاء Repository على GitHub ونشر التطبيق

## 📋 الخطوات المطلوبة

### 1. إنشاء Repository جديد على GitHub

1. **اذهب إلى GitHub**:
   - افتح https://github.com
   - سجل الدخول بحسابك

2. **إنشاء Repository جديد**:
   - انقر على زر "+" في الأعلى
   - اختر "New repository"
   - املأ البيانات التالية:
     - **Repository name**: `sam-pro-desktop`
     - **Description**: `SAM PRO - نظام إدارة المبيعات والمخزون - إصدار سطح المكتب`
     - **Public** (عام) أو **Private** (خاص) حسب رغبتك
     - ✅ **Add a README file**
     - ✅ **Add .gitignore** → اختر **Python**
     - ✅ **Choose a license** → اختر **MIT License**

3. **انقر "Create repository"**

### 2. رفع الملفات إلى GitHub

#### الطريقة الأولى: استخدام GitHub Web Interface
1. **في صفحة Repository الجديد**:
   - انقر "uploading an existing file"
   - اسحب وأفلت جميع ملفات المشروع
   - أو انقر "choose your files" واختر الملفات

2. **الملفات المطلوبة**:
   ```
   ✅ main.py
   ✅ app.py
   ✅ config.py
   ✅ models.py
   ✅ requirements.txt
   ✅ sam_pro.spec
   ✅ version_info.txt
   ✅ build.bat
   ✅ LICENSE
   ✅ .gitignore
   ✅ README_DESKTOP.md
   ✅ BUILD_README.md
   ✅ دليل_الاستخدام_السريع.md
   ✅ .github/workflows/build-release.yml
   ✅ .github/workflows/test-build.yml
   ✅ templates/ (المجلد كاملاً)
   ✅ static/ (المجلد كاملاً)
   ```

3. **كتابة رسالة Commit**:
   - **Commit message**: `Initial commit - SAM PRO Desktop v1.0.0`
   - انقر "Commit changes"

#### الطريقة الثانية: استخدام Git Command Line
```bash
# في مجلد المشروع
git init
git add .
git commit -m "Initial commit - SAM PRO Desktop v1.0.0"
git branch -M main
git remote add origin https://github.com/mohazard555/sam-pro-desktop.git
git push -u origin main
```

### 3. إنشاء أول إصدار (Release)

1. **في صفحة Repository**:
   - انقر على "Releases" (في الجانب الأيمن)
   - انقر "Create a new release"

2. **إعداد الإصدار**:
   - **Tag version**: `v1.0.0`
   - **Release title**: `SAM PRO Desktop v1.0.0 - الإصدار الأول`
   - **Description**:
     ```markdown
     # SAM PRO Desktop - الإصدار الأول 🎉
     
     ## ما الجديد
     - ✅ تطبيق سطح مكتب كامل الميزات
     - ✅ واجهة مستخدم سهلة الاستخدام
     - ✅ لا حاجة لتثبيت Python
     - ✅ يعمل بدون اتصال بالإنترنت
     
     ## كيفية الاستخدام
     1. حمل ملف `SAM_PRO_Desktop_v1.0.0.zip`
     2. استخرج الملفات
     3. شغل `SAM_PRO.exe`
     4. اتبع التعليمات في التطبيق
     
     ## متطلبات النظام
     - Windows 10 أو أحدث
     - 4 جيجابايت رام (الحد الأدنى)
     - 500 ميجابايت مساحة فارغة
     ```

3. **انقر "Publish release"**

### 4. تفعيل GitHub Actions للبناء التلقائي

1. **التحقق من Actions**:
   - اذهب إلى تبويب "Actions" في Repository
   - ستجد workflows جاهزة للتشغيل

2. **تشغيل أول بناء**:
   - انقر على "Build and Release SAM PRO Desktop"
   - انقر "Run workflow"
   - أدخل `v1.0.0` في حقل Version
   - انقر "Run workflow"

3. **مراقبة عملية البناء**:
   - ستستغرق العملية 10-15 دقيقة
   - يمكنك مراقبة التقدم في تبويب Actions

### 5. الحصول على رابط التحميل

بعد اكتمال البناء:

1. **اذهب إلى Releases**:
   - ستجد إصدار جديد مع الملفات المبنية

2. **رابط التحميل المباشر**:
   ```
   https://github.com/mohazard555/sam-pro-desktop/releases/latest
   ```

3. **مشاركة الرابط**:
   - يمكنك مشاركة هذا الرابط مع المستخدمين
   - سيحصلون دائماً على أحدث إصدار

## 🔄 إنشاء إصدارات جديدة

### عند إضافة ميزات جديدة:

1. **تحديث الكود**:
   - عدل الملفات المطلوبة
   - ارفعها إلى GitHub

2. **إنشاء Tag جديد**:
   ```bash
   git tag v1.1.0
   git push origin v1.1.0
   ```

3. **البناء التلقائي**:
   - سيتم بناء الإصدار الجديد تلقائياً
   - سيظهر في Releases

## 🛠️ إعدادات إضافية

### تخصيص Repository:

1. **إضافة وصف**:
   - في صفحة Repository الرئيسية
   - انقر على ⚙️ بجانب "About"
   - أضف وصف ومواضيع (topics)

2. **إضافة Website**:
   - في نفس القسم
   - أضف رابط الإصدارات:
     ```
     https://github.com/mohazard555/sam-pro-desktop/releases
     ```

3. **تفعيل Issues**:
   - اذهب إلى Settings
   - تأكد من تفعيل Issues للدعم الفني

## 📊 مراقبة الإحصائيات

يمكنك مراقبة:
- عدد التحميلات
- عدد النجوم (Stars)
- عدد المشاهدات
- Issues والمشاكل المبلغ عنها

## 🎯 النتيجة النهائية

بعد اتباع هذه الخطوات، ستحصل على:

✅ **Repository عام على GitHub**
✅ **بناء تلقائي للتطبيق**
✅ **إصدارات منتظمة**
✅ **رابط تحميل مباشر**
✅ **دعم فني عبر Issues**

**رابط التحميل النهائي**:
```
https://github.com/mohazard555/sam-pro-desktop/releases/latest
```

---

**ملاحظة**: تأكد من استبدال `mohazard555` باسم المستخدم الخاص بك على GitHub.
