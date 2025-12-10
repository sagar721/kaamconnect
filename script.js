// Stats animation on scroll
const stats = document.querySelectorAll('.stat');
window.addEventListener('scroll', () => {
  stats.forEach(stat => {
    const rect = stat.getBoundingClientRect();
    if (rect.top < window.innerHeight - 100) {
      stat.classList.add('visible');
    }
  });
});

// Initialize stats animation on page load
document.addEventListener('DOMContentLoaded', () => {
  // Check if stats are already in view
  stats.forEach(stat => {
    const rect = stat.getBoundingClientRect();
    if (rect.top < window.innerHeight - 100) {
      stat.classList.add('visible');
    }
  });

  // Form validation
  const forms = document.querySelectorAll('form');
  forms.forEach(form => {
    form.addEventListener('submit', (e) => {
      const password = form.querySelector('input[name="password"]');
      const confirmPassword = form.querySelector('input[name="confirm_password"]');
      
      if (password && confirmPassword) {
        if (password.value !== confirmPassword.value) {
          e.preventDefault();
          alert('Passwords do not match!');
          return false;
        }
        
        if (password.value.length < 6) {
          e.preventDefault();
          alert('Password must be at least 6 characters long!');
          return false;
        }
      }
      
      // Phone number validation
      const phoneInput = form.querySelector('input[type="tel"]');
      if (phoneInput) {
        const phonePattern = /^[0-9]{10}$/;
        if (!phonePattern.test(phoneInput.value.replace(/\D/g, ''))) {
          e.preventDefault();
          alert('Please enter a valid 10-digit phone number!');
          return false;
        }
      }
      
      // Email validation (if email field exists)
      const emailInput = form.querySelector('input[type="email"]');
      if (emailInput && emailInput.value) {
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailPattern.test(emailInput.value)) {
          e.preventDefault();
          alert('Please enter a valid email address!');
          return false;
        }
      }
      
      return true;
    });
  });

  // Auto-hide flash messages after 5 seconds
  const flashMessages = document.querySelectorAll('.flash');
  flashMessages.forEach(flash => {
    setTimeout(() => {
      flash.style.opacity = '0';
      flash.style.transition = 'opacity 0.5s ease';
      setTimeout(() => {
        flash.remove();
      }, 500);
    }, 5000);
  });

  // Phone number formatting
  const phoneInputs = document.querySelectorAll('input[type="tel"]');
  phoneInputs.forEach(input => {
    input.addEventListener('input', (e) => {
      let value = e.target.value.replace(/\D/g, '');
      if (value.length > 10) value = value.substring(0, 10);
      e.target.value = value;
    });
  });
});