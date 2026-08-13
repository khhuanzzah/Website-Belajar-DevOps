from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'kunci-rahasia-anda'  # Penting untuk flash message

# Data pengguna dummy untuk validasi
USERS = {
    'admin': 'password123',
    'user': 'password456'
}

@app.route('/')
def home():
    """Mengalihkan pengguna ke halaman login."""
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Menangani tampilan halaman login dan validasi form.
    
    Metode GET: Menampilkan form login.
    Metode POST: Menerima data dari form dan memvalidasinya.
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Cek apakah username ada di database dummy
        if username in USERS:
            # Cek apakah password cocok
            if USERS[username] == password:
                # Login berhasil
                flash('Login berhasil!', 'success')
                # Arahkan ke halaman dashboard
                return redirect(url_for('dashboard')) 
            else:
                # Password salah
                flash('Password salah. Silakan coba lagi.', 'error')
        else:
            # Username tidak ditemukan
            flash('Username tidak ditemukan. Silakan periksa kembali.', 'error')
            
    # Jika metode GET atau validasi gagal, tampilkan kembali halaman login
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    """Halaman Dashboard (dengan file HTML)."""
    return render_template('dashboard.html')

# Tambahkan kode baru di sini
@app.route('/add_item')
def add_item():
    """Halaman untuk menambah/melihat daftar barang."""
    return render_template('forms/add_item.html')

# Tambahkan kode baru di sini
@app.route('/laporan')
def laporan():
    """Halaman untuk menambah/melihat laporan."""
    return render_template('laporan.html')

# Tambahkan kode baru di sini
@app.route('/add_transaksi')
def add_transaksi():
    """Halaman untuk menambah/melihat transaksi."""
    return render_template('transactions/add_transaksi.html')

@app.route('/validasi')
def validasi_form():
    """Endpoint untuk menampilkan halaman validasi formulir."""
    return render_template('validasi_form.html')

# ... (kode aplikasi Flask Anda yang sudah ada) ...

@app.route('/proses_validasi', methods=['POST'])
def proses_validasi():
    if request.method == 'POST':
        email = request.form['email']
        phone = request.form['phone']

        # Logika validasi
        # Anda bisa menyalin regex dari kode JS Anda ke sini
        email_valid = "@" in email and "." in email
        phone_valid = phone.isdigit() and (phone.startswith('08') or phone.startswith('+62'))

        if email_valid and phone_valid:
            # Jika validasi berhasil, arahkan ke dashboard dan berikan pesan sukses
            flash('Validasi berhasil! Selamat datang kembali.', 'success')
            return redirect(url_for('dashboard'))
        else:
            # Jika validasi gagal, kembalikan ke formulir validasi dengan pesan error
            flash('Validasi gagal. Mohon periksa kembali data Anda.', 'error')
            return redirect(url_for('validasi_form'))

    # Mengalihkan kembali jika ada yang mengakses URL ini selain dengan metode POST
    return redirect(url_for('validasi_form'))


if __name__ == '__main__':
    app.run(debug=True)