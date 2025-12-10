// Dashboard JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Mobile menu toggle
    const menuToggle = document.getElementById('menuToggle');
    const sidebar = document.querySelector('.sidebar');
    
    if (menuToggle && sidebar) {
        menuToggle.addEventListener('click', function() {
            sidebar.classList.toggle('active');
        });
    }
    
    // Close sidebar when clicking outside on mobile
    document.addEventListener('click', function(event) {
        if (window.innerWidth <= 1200) {
            if (!sidebar.contains(event.target) && !menuToggle.contains(event.target)) {
                sidebar.classList.remove('active');
            }
        }
    });
    
    // Close flash messages
    const closeFlashButtons = document.querySelectorAll('.close-flash');
    closeFlashButtons.forEach(button => {
        button.addEventListener('click', function() {
            const flashMessage = this.closest('.flash-message');
            if (flashMessage) {
                flashMessage.style.animation = 'slideOut 0.3s ease';
                setTimeout(() => {
                    flashMessage.remove();
                }, 300);
            }
        });
    });
    
    // Auto-close flash messages after 5 seconds
    setTimeout(() => {
        const flashMessages = document.querySelectorAll('.flash-message');
        flashMessages.forEach(message => {
            message.style.animation = 'slideOut 0.3s ease';
            setTimeout(() => {
                message.remove();
            }, 300);
        });
    }, 5000);
    
    // Add slideOut animation
    const style = document.createElement('style');
    style.textContent = `
        @keyframes slideOut {
            from {
                transform: translateX(0);
                opacity: 1;
            }
            to {
                transform: translateX(100%);
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(style);
    
    // Progress bars animation
    const progressBars = document.querySelectorAll('.progress-fill');
    progressBars.forEach(bar => {
        const width = bar.style.width;
        bar.style.width = '0';
        setTimeout(() => {
            bar.style.transition = 'width 1s ease';
            bar.style.width = width;
        }, 100);
    });
    
    // Apply button functionality
    const applyButtons = document.querySelectorAll('.apply-btn');
    applyButtons.forEach(button => {
        button.addEventListener('click', function() {
            const jobTitle = this.closest('.job-item').querySelector('h4').textContent;
            this.innerHTML = '<i class="fas fa-check"></i> Applied';
            this.classList.add('applied');
            this.disabled = true;
            
            // Show success message
            showNotification(`Successfully applied for "${jobTitle}"`, 'success');
        });
    });
    
    // Verify user functionality
    const verifyButtons = document.querySelectorAll('.verify-btn');
    verifyButtons.forEach(button => {
        button.addEventListener('click', function() {
            const userName = this.closest('.registration-item').querySelector('h4').textContent;
            this.innerHTML = '<i class="fas fa-check"></i> Verified';
            this.classList.remove('verify-btn');
            this.classList.add('verified-btn');
            this.disabled = true;
            
            // Update status
            const statusElement = this.closest('.registration-item').querySelector('.user-status');
            if (statusElement) {
                statusElement.textContent = 'Verified';
                statusElement.classList.remove('pending');
                statusElement.classList.add('verified');
            }
            
            showNotification(`Successfully verified user "${userName}"`, 'success');
        });
    });
    
    // Resolve issue functionality
    const resolveButtons = document.querySelectorAll('.resolve-btn');
    resolveButtons.forEach(button => {
        button.addEventListener('click', function() {
            const issueTitle = this.closest('.issue-item').querySelector('h4').textContent;
            const issueItem = this.closest('.issue-item');
            
            // Remove from DOM with animation
            issueItem.style.animation = 'fadeOut 0.3s ease';
            setTimeout(() => {
                issueItem.remove();
                updateIssueStats();
            }, 300);
            
            showNotification(`Issue "${issueTitle}" resolved`, 'success');
        });
    });
    
    // Update issue statistics
    function updateIssueStats() {
        const issueStats = {
            high: document.querySelectorAll('.issue-item.high').length,
            medium: document.querySelectorAll('.issue-item.medium').length,
            low: document.querySelectorAll('.issue-item.low').length
        };
        
        // Update stats display
        document.querySelectorAll('.issue-stat').forEach(stat => {
            const label = stat.querySelector('span:first-child').textContent.trim();
            const valueSpan = stat.querySelector('span:last-child');
            
            if (label === 'High Priority') {
                valueSpan.textContent = issueStats.high;
            } else if (label === 'Medium') {
                valueSpan.textContent = issueStats.medium;
            } else if (label === 'Low') {
                valueSpan.textContent = issueStats.low;
            }
        });
    }
    
    // Notification function
    function showNotification(message, type = 'info') {
        const container = document.querySelector('.flash-container') || createFlashContainer();
        
        const notification = document.createElement('div');
        notification.className = `flash-message ${type}`;
        notification.innerHTML = `
            <span>${message}</span>
            <button class="close-flash"><i class="fas fa-times"></i></button>
        `;
        
        container.appendChild(notification);
        
        // Add close functionality
        notification.querySelector('.close-flash').addEventListener('click', function() {
            notification.style.animation = 'slideOut 0.3s ease';
            setTimeout(() => {
                notification.remove();
            }, 300);
        });
        
        // Auto-remove after 5 seconds
        setTimeout(() => {
            if (notification.parentNode) {
                notification.style.animation = 'slideOut 0.3s ease';
                setTimeout(() => {
                    notification.remove();
                }, 300);
            }
        }, 5000);
    }
    
    // Create flash container if it doesn't exist
    function createFlashContainer() {
        const container = document.createElement('div');
        container.className = 'flash-container';
        document.body.appendChild(container);
        return container;
    }
    
    // Add fadeOut animation
    const fadeOutStyle = document.createElement('style');
    fadeOutStyle.textContent = `
        @keyframes fadeOut {
            from {
                opacity: 1;
                transform: scale(1);
            }
            to {
                opacity: 0;
                transform: scale(0.95);
            }
        }
    `;
    document.head.appendChild(fadeOutStyle);
    
    // Search functionality
    const searchInput = document.querySelector('.search-box input');
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const searchTerm = this.value.toLowerCase();
            
            // Search in project items
            document.querySelectorAll('.project-item, .job-item, .worker-card').forEach(item => {
                const text = item.textContent.toLowerCase();
                if (text.includes(searchTerm)) {
                    item.style.display = 'flex';
                } else {
                    item.style.display = 'none';
                }
            });
        });
    }
    
    // Notification bell click
    const notificationBell = document.querySelector('.notification-btn');
    if (notificationBell) {
        notificationBell.addEventListener('click', function() {
            showNotification('Notifications feature coming soon!', 'info');
        });
    }
    
    // Logout functionality
    const logoutButtons = document.querySelectorAll('.logout, .logout-link');
    logoutButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            if (confirm('Are you sure you want to logout?')) {
                showNotification('Logged out successfully', 'success');
                setTimeout(() => {
                    window.location.href = '/';
                }, 1500);
            }
        });
    });
    
    // Home link
    const homeLinks = document.querySelectorAll('.home-link');
    homeLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            window.location.href = '/';
        });
    });
    
    // Quick action buttons
    const quickActionButtons = document.querySelectorAll('.action-btn');
    quickActionButtons.forEach(button => {
        button.addEventListener('click', function() {
            const actionText = this.querySelector('span').textContent;
            showNotification(`${actionText} feature coming soon!`, 'info');
        });
    });
    
    // View all links
    const viewAllLinks = document.querySelectorAll('.view-all');
    viewAllLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            showNotification('Detailed view feature coming soon!', 'info');
        });
    });
    
    // System action buttons
    const systemButtons = document.querySelectorAll('.system-actions .btn');
    systemButtons.forEach(button => {
        button.addEventListener('click', function() {
            const buttonText = this.textContent.trim();
            showNotification(`${buttonText} action initiated`, 'success');
        });
    });
    
    // Initialize tooltips for buttons
    initializeTooltips();
});

// Initialize tooltips
function initializeTooltips() {
    const tooltipElements = document.querySelectorAll('[title]');
    tooltipElements.forEach(element => {
        element.addEventListener('mouseenter', showTooltip);
        element.addEventListener('mouseleave', hideTooltip);
    });
}

function showTooltip(e) {
    const tooltip = document.createElement('div');
    tooltip.className = 'tooltip';
    tooltip.textContent = this.title;
    document.body.appendChild(tooltip);
    
    const rect = this.getBoundingClientRect();
    tooltip.style.top = `${rect.top - tooltip.offsetHeight - 10}px`;
    tooltip.style.left = `${rect.left + rect.width / 2 - tooltip.offsetWidth / 2}px`;
    
    this._tooltip = tooltip;
}

function hideTooltip() {
    if (this._tooltip) {
        this._tooltip.remove();
        this._tooltip = null;
    }
}

// Add tooltip styles
const tooltipStyle = document.createElement('style');
tooltipStyle.textContent = `
    .tooltip {
        position: fixed;
        background: rgba(0, 0, 0, 0.8);
        color: white;
        padding: 5px 10px;
        border-radius: 4px;
        font-size: 12px;
        z-index: 9999;
        pointer-events: none;
        white-space: nowrap;
    }
    
    .tooltip::after {
        content: '';
        position: absolute;
        top: 100%;
        left: 50%;
        transform: translateX(-50%);
        border: 5px solid transparent;
        border-top-color: rgba(0, 0, 0, 0.8);
    }
`;
document.head.appendChild(tooltipStyle);

// Simulate real-time updates
setInterval(() => {
    // Update notification count randomly
    const notificationCount = document.querySelector('.notification-count');
    if (notificationCount) {
        const currentCount = parseInt(notificationCount.textContent);
        const newCount = Math.max(0, currentCount + (Math.random() > 0.7 ? 1 : -1));
        if (newCount !== currentCount) {
            notificationCount.textContent = newCount;
            notificationCount.style.animation = 'bounce 0.3s';
            setTimeout(() => {
                notificationCount.style.animation = '';
            }, 300);
        }
    }
    
    // Update some stats randomly
    const statNumbers = document.querySelectorAll('.stat-number');
    statNumbers.forEach(stat => {
        if (Math.random() > 0.8) {
            const current = parseInt(stat.textContent.replace(/[^0-9]/g, ''));
            const change = Math.floor(Math.random() * 10) - 2;
            const newValue = Math.max(0, current + change);
            stat.textContent = stat.textContent.replace(current, newValue);
            
            // Add visual feedback
            stat.style.color = change > 0 ? '#43a047' : change < 0 ? '#f44336' : '#263238';
            setTimeout(() => {
                stat.style.color = '';
            }, 1000);
        }
    });
}, 5000);

// Add bounce animation
const bounceStyle = document.createElement('style');
bounceStyle.textContent = `
    @keyframes bounce {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.2); }
    }
`;
document.head.appendChild(bounceStyle);