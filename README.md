
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

