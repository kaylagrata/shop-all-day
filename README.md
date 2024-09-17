
Link PWS: http://kayla-agrata-shopallday.pbp.cs.ui.ac.id
# 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Hal pertama yang harus dilakukan adalah membuat sebuah direktori utama yang diberi nama shop-all-day. Kemudian, langkah selanjutnya adalah mengaktifkan virtual environment. Setelah itu, saya membuat file requirements.txt yang diisi dengan beberapa dependencies dan melakukan instalasi terhadap dependencies tersebut.

1) Setup Proyek Django
Melakukan instalasi django dan membuat project shop_all_day dengan perintah 'django-admin startproject shop_all_day'. 
2) Menambahkan Berkas .gitignore
Membuat berkas .gitignore yang digunakan sebagai konfigurasi pada repositori git untuk memilah berkas apa saja yang perlu diabaikan seperti env dan db.sqlite3.
3) Setting Github bernama shop-all-day
Menginisiasi direktori lokal shop-all-day sebagai repositori git. Setelah itu melakukan add, commit, dan push dari direktori lokal
4) Membuat Aplikasi Django
Membuat aplikasi baru dengan nama 'main' dan mendaftarkan aplikasi di 'settings.py' agar Django dapat mengenali aplikasi tersebut.
5) Membuat berkas template html
Membuat direktori baru bernama template lalu mengisinya dengan berkas 'main.html'.
6) Membuat Model
Mengubah berkas 'models.py' sesuai dengan ketentuan soal. Setelah itu, melakukan migrasi model agar perubahan model yang terjadi dapat diketahui oleh server.
7) Membuat views
Melakukan integrasi model, views, dan template pada berkas 'views.py'. Fungsinya untuk mengatur http agar dapat mengembalikan tampilan yang sesuai. Lalu melakukan modifikasi pada template agar dapat menampilkan data.
8) Melakukan routing URL
Menambahkan 'urls.py' pada direktori main agar dapat mengambil modul main views sebagai tampilan ketika mengakses url. 


# 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Link bagan : https://drive.google.com/file/d/1-mmPskH5lrDAkIWCBSBKqGPpG39R2JCW/view?usp=sharing
Bagan tersebut menggambarkan konsep Django yaitu MVT (Model-Views-Template)
Model berfungsi untuk mengelola data dan berinteraksi dengan database. Isi dari model biasanya class yang berhubungan dengan aplikasi tersebut. Views berfungsi untuk mengambil data yang diperlukan dari model, mengirimkan data tersebut ke template, dan mengelola data apa yang dapat ditampilkan ke user. Template sebagai tampilan data yang diberikan oleh views pada user dengan format yang ditentukan.


# 3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
1) Untuk berkolaborasi
Git memungkinkan para pengembang untuk bekerja sama dengan pengembang  atau tim lain dalam satu repositori utama. Git akan menyimpan setiap perubahan yang dilakukan dan dapat melakukan sinkronisasi dengan repositori lainnya. Adanya branch pada git memungkinkan para pengembang untuk mengerjakan fitur-fitur yang berbeda secara terpisah.  Sumber : domainesia.com
2) Melacak Perubahan
Setiap perubahan yang dilakukan pada kode tercatat, hal ini dapat memudahkan para pengembang untuk mempercepat proses debugging. Sumber : revou.co
3) Menjadi backup
Kode tersimpan dalam repositori remote di Github sehingga terdapat backup apabila terjadi sesuatu yang tidak diinginkan. Sumber : dte.telkomuniversity.ac.id


# 4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django menggunakan bahasa python yang mudah dimengerti oleh para pemula dalam pemrograman. Django juga memiliki dokumentasi yang lengkap sehingga mempermudah proses pembelajaran. Django juga memiliki komunitas yang banyak sehingga pemula dalam pemrograman dapat mendapatkan bantuan. Django juga membantu pemula untuk memahami struktur aplikasi dengan baik karena adanya pola Model-View-Template.

# 5. Mengapa model pada Django disebut sebagai ORM?
ORM adalah singkatan dari Object-Relational-Mapping. Model pada Django disebut sebagai ORM karena Django ORM memiliki tugas untuk memetakan objek ke struktur basis data relasional dan mendefinisikan model python dalam tabel. Tabel ini dapat berinteraksi dengan data menggunakan operasi objek python tanpa adanya keterlibatan SQL. Sumber : rumahcoding.co.id

# Tugas 3 : Implementasi Form dan Data Delivery pada Django
### 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery memiliki peran yang penting dalam implementasi sebuah platform. Beberapa alasannya adalah sebagai berikut:
1. User experience yang responsif dan akurat
Data delivery diperlukan karena data perlu dikirimkan secara efisien agar user dapat mengakses informasi dengan cepat dan akurat. Data delivery membuat interaksi user dengan platform menjadi baik.
2. Real-time data delivery
Beberapa platform memerlukan pengiriman data secara real-time untuk menyesuaikan dengan input pengguna. Data delivery secara real-time memastikan bahwa pengguna dapat selalu melihat pembaruan data atau konten terbaru.
3. Integrasi
Data delivery yang efektif memastikan bahwa komunikasi antara platform dengan sistem lain misalnya sistem pembayaran eksternal berjalan dengan lancar.
4. Security
Data delivery yang dikontrol dengan baik membantu memastikan bahwa data yang dikirimkan aman.

### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya, JSON lebih baik dari XML. Dalam pengembangan web, umumnya JSON dianggap lebih baik, itulah alasan mengapa JSON lebih populer dibandingkan XML. Berikut adalah beberapa alasan mengapa JSON lebih populer dan sering digunakan:
1. Format dan Syntax Lebih Ringkas dan Simpel
JSON memiliki struktur yang lebih ringkas daripada XML. JSON menggunakan pasangan key dan value untuk membuat struktur. 'Key' adalah string, yang akan mengidentifikasi pasangan tersebut. Value adalah informasi yang diberikan pada key tersebut. Misalnya, “NumberProperty”: 10. Dalam hal ini, “NumberProperty” adalah key, dan 10 adalah value. Struktur ini mudah dibaca oleh programmer maupun orang awam.
2. Kemudahan dalam Parsing
Melakukan parsing XML harus dengan parser XML. Hal ini sering memperlambat dan mempersulit prosesnya.
Sementara itu, JSON dapat dilakukan parsing menggunakan fungsi JavaScript standar. Hal ini membuat JSON lebih mudah diakses. Karena perbedaan sintaks dan ukuran file, JSON juga dapat diparsing lebih cepat daripada XML.
Sumber : https://aws.amazon.com/compare/the-difference-between-json-xml/

### 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() digunakan untuk melakukan validasi pada setiap field dalam form, dan didefinisikan dalam kelas Form Django. Method ini memerika apakah semua field dalam form sudah terisi dengan benar (misal apakah field name sudah diisi). Method ini mengembalikan True jika data valid dan menempatkan semua data ke dalam atribut cleaned_data. Alasan is_valid() dibutuhkan adalah agar kita tidak perlu memeriksa validitas input satu per satu secara manual. Selain itu, method ini juga dapat membantu kita untuk memastikan bahwa data tersebut valid sebelum disimpan ke database.
Sumber : https://www.javatpoint.com/django-form-validation

### 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Dalam Django, kita membutuhkan csrf_token untuk melindungi user dari serangan yang dikenal sebagai Cross-Site-Request-Forgery(CSRF). Jika kita tidak menambahkan csrf_token, attacker dapat memanfaatkan misalnya sesi login user untuk mengirimkan permintaan yang berbahaya tanpa kesadaran user. Pada serangan CSRF, attacker mengirimkan email atau sms yang mengandung link untuk mengelabui user yang sudah authenticated pada website untuk melakukan tindakan yang tidak diinginkan seperti transfer dana atau penggantiam email tanpa sepengetahuan user. Tanpa validasi csrf_token, aplikasi Django tidak bisa membedakan antara permintaan dari pengguna dan permintaan berbahaya dari pihak ketiga.
Sumber : https://www.geeksforgeeks.org/csrf-token-in-django/

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Membuat forms.py
Membuat file forms.py pada direktori main, file diisi dengan model yang sudah dibuat sebelumnya yaitu product.
2. Implementasi fungsi create product pada views.py untuk dan menampilkannya di template HTML
Melakukan import forms yang baru dibuat dan menambahkan import redirect. Lalu membuat fungsi baru yaitu create_product agar dapat melakukan validasi input form dan menambahkan data yang disubmit secara otomatis. Selanjutnya, pada fungsi `show_main`, ditambahkan kode `Product.objects.all()` untuk mengambil semua objek dari model Product yang ada di database. Nilai yang diambil dari `Product.objects.all()` disimpan dalam variabel `products` dan dimasukkan ke dalam context, kemudian dikirim ke template HTML agar dapat ditampilkan.
3. Melakukan routing URL
Melakukan import fungsi `create_product` pada urls.py dan tambahkan path untuk mengakses fungsi `create_product`.
4. Menampilkan pada template HTML
Membuat file HTML baru dengan nama create_product.html pada direktori main/templates dengan `<form method="POST>` untuk menandakan block untuk form yang menggunakan metode POST, `{% csrf_token %}` yang berfungsi untuk mencegah serangan CSRF, dan button untuk submit form.
5. Membuat fungsi untuk mengembalikan data dalam bentuk XML dan JSON
Masuk ke file views.py dan membuat 4 fungsi untuk melihat data JSON dan XML yaitu `show_xml`, `show_json`, `show_xml_by_id`, dan `show_json_by_id`.
6. Melakukan routing URL 
Menambahkan path untuk menampilkan page yang dapat melihat database yang ditampilkan dalam bentuk JSON maupun XML
7. Melakukan push ke pws dan github

### Postman Documentation
`show_xml`
<img src="./images/show_xml.png" width="1802" height="330">

`show_json`
<img src="./images/show_json.png" width="1802" height="330">

`show_xml_by_id`
<img src="./images/show_xml_by_id.png" width="1802" height="330">

`show_json_by_id`
<img src="./images/show_json_by_id.png" width="1802" height="330">


