document.addEventListener('DOMContentLoaded', function() {
    function changeFontSize(size) {
        document.body.style.fontSize = size === 'small' ? '14px' : size === 'medium' ? '16px' : '20px';
    }

    function toggleDarkMode() {
        document.body.classList.toggle('dark-mode');
        const isDarkMode = document.body.classList.contains('dark-mode');
        localStorage.setItem('dark-mode', isDarkMode);
    }

    if (localStorage.getItem('dark-mode') === 'true') {
        document.body.classList.add('dark-mode');
    }

    function resetAccessibility() {
        document.body.style.fontSize = '';
        document.body.classList.remove('dark-mode');
    }
    
    var logo = document.getElementById('logo-asuan');

    function toggleDarkMode() {
        document.body.classList.toggle('dark-mode');
        const isDarkMode = document.body.classList.contains('dark-mode');
        localStorage.setItem('dark-mode', isDarkMode);

        if (isDarkMode) {
            logo.src = 'static/img/logo_asuanFW.png';
        } else {
            logo.src = 'static/img/logo_asuanF.png';
        }
    }

    window.changeFontSize = changeFontSize;
    window.toggleDarkMode = toggleDarkMode;
    window.resetAccessibility = resetAccessibility;
});