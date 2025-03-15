// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Navbar background change on scroll
window.addEventListener('scroll', function() {
    if (window.scrollY > 50) {
        document.querySelector('.navbar').classList.add('bg-dark');
    } else {
        document.querySelector('.navbar').classList.remove('bg-dark');
    }
});

document.addEventListener('DOMContentLoaded', function() {
    let lastScroll = 0;
    const navbar = document.querySelector('.navbar');

    window.addEventListener('scroll', function() {
        const currentScroll = window.pageYOffset;

        // Scroll aşağı
        if (currentScroll > lastScroll && currentScroll > 100) {
            navbar.style.transform = 'translateY(-100%)';
        }
        // Scroll yukarı
        else {
            navbar.style.transform = 'translateY(0)';
            if (currentScroll > 100) {
                navbar.classList.add('shadow-nav');
            } else {
                navbar.classList.remove('shadow-nav');
            }
        }
        lastScroll = currentScroll;
    });
});

// Contact form submission
document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.querySelector('#contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            try {
                const response = await fetch('/contact/', {
                    method: 'POST',
                    body: new FormData(this),
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest',
                    }
                });
                
                const data = await response.json();
                showAlert(data.message, data.status);
                
                if (data.status === 'success') {
                    this.reset();
                }
            } catch (error) {
                showAlert('Bir hata oluştu. Lütfen tekrar deneyin.', 'error');
            }
        });
    }
});

function showAlert(message, type) {
    const alertDiv = document.getElementById('alertPopup');
    alertDiv.innerHTML = `
        <div class="alert alert-${type === 'success' ? 'success' : 'danger'} alert-dismissible fade show">
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
    `;
    alertDiv.style.display = 'block';
    
    setTimeout(() => {
        const alert = alertDiv.querySelector('.alert');
        if (alert) {
            alert.classList.remove('show');
        }
    }, 3000);
}