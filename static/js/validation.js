// Menambahkan event listener ke formulir untuk mengintersep pengiriman
document.getElementById('myForm').addEventListener('submit', function(event) {
    // Memanggil fungsi validasi dan memeriksa hasilnya
    if (!validateForm()) {
        // Jika validasi gagal (mengembalikan false), mencegah formulir terkirim
        event.preventDefault(); 
    }
});

function validateForm() {
    // Dapatkan nilai dari input
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;

    // Dapatkan elemen untuk menampilkan pesan error
    const emailError = document.getElementById('emailError');
    const phoneError = document.getElementById('phoneError');

    // Kosongkan pesan error sebelumnya
    emailError.textContent = '';
    phoneError.textContent = '';

    // Gunakan flag untuk menentukan apakah ada error
    let hasError = false;

    // Validasi Email
    // Ekspresi reguler untuk format email umum
    const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!emailPattern.test(email)) {
        emailError.textContent = 'Format email tidak valid.';
        hasError = true;
    }

    // Validasi Nomor Telepon
    // Ekspresi reguler untuk nomor telepon Indonesia (misal: dimulai dengan 08)
    const phonePattern = /^(?:\+62|0)[2-9]\d{9,10}$/; 
    if (!phonePattern.test(phone)) {
        phoneError.textContent = 'Nomor telepon tidak valid. Gunakan format 08xxxxxxxxxx.';
        hasError = true;
    }

    // Mengembalikan true jika tidak ada error, dan false jika ada
    if (!hasError) {
        // Hapus alert, karena sekarang server yang akan mengelola pengalihan halaman
        return true; // Validasi berhasil
    } else {
        return false; // Validasi gagal
    }
}