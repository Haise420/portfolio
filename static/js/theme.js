function setTheme(theme) {
    document.body.className = theme;
    localStorage.setItem('theme', theme);
    applyThemeToDivs(theme);
}

function applyThemeToDivs(theme) {
    const mainDivs = document.querySelectorAll('.main-div');
    mainDivs.forEach(div => {
        div.className = `main-div ${theme}`;
    });
}

document.addEventListener('DOMContentLoaded', (event) => {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        document.body.className = savedTheme;
        applyThemeToDivs(savedTheme);
    }
});
