document.addEventListener('DOMContentLoaded', function() {
    console.log("Page fully loaded and parsed");

    // 示例：你可以在这里添加事件监听器或其他逻辑
    const navLinks = document.querySelectorAll('nav a');
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            alert("Navigating to " + this.textContent);
        });
    });
});
